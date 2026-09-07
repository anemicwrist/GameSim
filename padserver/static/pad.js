/* Touch controller. Bit positions mirror BUTTON_BITS in padserver/protocol.py. */
"use strict";

const BITS = { LP: 0, HP: 1, LK: 2, HK: 3, A1: 4, A2: 5, START: 6, SELECT: 7 };
const DEADZONE = 0.28;   // fraction of the d-pad radius that counts as neutral
const RECONNECT_MIN = 250;
const RECONNECT_MAX = 4000;

const els = {
  player: document.getElementById("player"),
  ping: document.getElementById("ping"),
  overlay: document.getElementById("overlay"),
  overlayText: document.getElementById("overlay-text"),
  go: document.getElementById("go"),
  dpad: document.getElementById("dpad"),
  dot: document.getElementById("dpad-dot"),
};

const targets = [];          // {name, kind, el, rect}
let dpadRect = null;
let ws = null;
let reconnectDelay = RECONNECT_MIN;
let sent = { b: -1, x: 9, y: 9 };
let state = { b: 0, x: 0, y: 0 };
let started = false;
let wakeLock = null;

/* ---------- identity ---------- */

function token() {
  let t = null;
  try { t = localStorage.getItem("padserver-token"); } catch (e) { /* private mode */ }
  if (!t) {
    t = (crypto.randomUUID && crypto.randomUUID()) ||
        (Date.now().toString(36) + Math.random().toString(36).slice(2));
    try { localStorage.setItem("padserver-token", t); } catch (e) { /* ignore */ }
  }
  return t;
}

/* ---------- geometry ---------- */

function measure() {
  targets.length = 0;
  document.querySelectorAll("[data-btn]").forEach((el) => {
    targets.push({ name: el.dataset.btn, el: el, rect: el.getBoundingClientRect() });
  });
  dpadRect = els.dpad.getBoundingClientRect();
}

function hit(rect, x, y) {
  return x >= rect.left && x <= rect.right && y >= rect.top && y <= rect.bottom;
}

/* Direction from the d-pad centre, snapped to 8 ways. */
function direction(x, y) {
  const cx = dpadRect.left + dpadRect.width / 2;
  const cy = dpadRect.top + dpadRect.height / 2;
  const radius = Math.min(dpadRect.width, dpadRect.height) / 2;
  const dx = (x - cx) / radius;
  const dy = (y - cy) / radius;
  if (Math.hypot(dx, dy) < DEADZONE) return { x: 0, y: 0 };
  // 8 sectors of 45 degrees, offset by half a sector so cardinals are centred.
  const sector = Math.round((Math.atan2(dy, dx) * 4) / Math.PI) & 7;
  const table = [
    { x: 1, y: 0 }, { x: 1, y: 1 }, { x: 0, y: 1 }, { x: -1, y: 1 },
    { x: -1, y: 0 }, { x: -1, y: -1 }, { x: 0, y: -1 }, { x: 1, y: -1 },
  ];
  return table[sector];
}

/* ---------- input ---------- */

function recompute(touches) {
  let b = 0;
  let dir = { x: 0, y: 0 };
  for (let i = 0; i < touches.length; i++) {
    const t = touches[i];
    if (dpadRect && hit(dpadRect, t.clientX, t.clientY)) {
      dir = direction(t.clientX, t.clientY);
      continue;
    }
    for (const target of targets) {
      if (hit(target.rect, t.clientX, t.clientY)) {
        b |= 1 << BITS[target.name];
        break;
      }
    }
  }
  state = { b: b, x: dir.x, y: dir.y };
  render();
  send();
}

function render() {
  for (const target of targets) {
    const on = (state.b & (1 << BITS[target.name])) !== 0;
    target.el.classList.toggle("on", on);
  }
  const moving = state.x !== 0 || state.y !== 0;
  els.dot.classList.toggle("on", moving);
  els.dot.style.transform = moving
    ? "translate(" + state.x * 30 + "%, " + state.y * 30 + "%)"
    : "";
}

function send() {
  if (state.b === sent.b && state.x === sent.x && state.y === sent.y) return;
  if (!ws || ws.readyState !== WebSocket.OPEN) return;
  ws.send(JSON.stringify({ t: "in", b: state.b, x: state.x, y: state.y }));
  if (state.b > sent.b && navigator.vibrate) navigator.vibrate(8);
  sent = { b: state.b, x: state.x, y: state.y };
}

function onTouch(ev) {
  ev.preventDefault();
  if (!started) return;
  recompute(ev.touches);
}

/* ---------- connection ---------- */

function wsUrl() {
  const proto = location.protocol === "https:" ? "wss:" : "ws:";
  return proto + "//" + location.host + "/ws" + location.search;
}

function setBadge(text, cls) {
  els.player.textContent = text;
  els.player.className = "badge" + (cls ? " " + cls : "");
}

function connect() {
  setBadge("connecting");
  ws = new WebSocket(wsUrl());

  ws.onopen = () => {
    reconnectDelay = RECONNECT_MIN;
    ws.send(JSON.stringify({ t: "hello", token: token(), name: navigator.platform || "phone" }));
    sent = { b: -1, x: 9, y: 9 };
    send();
  };

  ws.onmessage = (ev) => {
    let msg;
    try { msg = JSON.parse(ev.data); } catch (e) { return; }
    if (msg.t === "slot") {
      setBadge("PLAYER " + msg.player, "live");
    } else if (msg.t === "full") {
      setBadge("game full", "dead");
      els.overlayText.textContent =
        "Both player slots are taken. Close the other phone's tab and reload.";
      els.overlay.classList.remove("hidden");
    } else if (msg.t === "pong") {
      els.ping.textContent = Math.round(performance.now() - msg.ts) + " ms";
    }
  };

  ws.onclose = () => {
    setBadge("reconnecting", "dead");
    els.ping.textContent = "-- ms";
    setTimeout(connect, reconnectDelay);
    reconnectDelay = Math.min(reconnectDelay * 2, RECONNECT_MAX);
  };

  ws.onerror = () => { try { ws.close(); } catch (e) { /* ignore */ } };
}

setInterval(() => {
  if (ws && ws.readyState === WebSocket.OPEN) {
    ws.send(JSON.stringify({ t: "ping", ts: performance.now() }));
  }
}, 1000);

/* ---------- start ---------- */

async function start() {
  started = true;
  els.overlay.classList.add("hidden");
  try {
    if (document.documentElement.requestFullscreen) {
      await document.documentElement.requestFullscreen({ navigationUI: "hide" });
    }
  } catch (e) { /* fullscreen is a nicety, not a requirement */ }
  try {
    if (screen.orientation && screen.orientation.lock) await screen.orientation.lock("landscape");
  } catch (e) { /* ignore */ }
  try {
    if (navigator.wakeLock) wakeLock = await navigator.wakeLock.request("screen");
  } catch (e) { /* ignore */ }
  measure();
}

document.addEventListener("visibilitychange", async () => {
  if (document.visibilityState === "visible" && started) {
    measure();
    try {
      if (navigator.wakeLock && (!wakeLock || wakeLock.released)) {
        wakeLock = await navigator.wakeLock.request("screen");
      }
    } catch (e) { /* ignore */ }
  } else {
    state = { b: 0, x: 0, y: 0 };
    render();
    send();
  }
});

els.go.addEventListener("click", start);
window.addEventListener("resize", measure);
window.addEventListener("orientationchange", () => setTimeout(measure, 200));
for (const type of ["touchstart", "touchmove", "touchend", "touchcancel"]) {
  document.addEventListener(type, onTouch, { passive: false });
}
document.addEventListener("contextmenu", (e) => e.preventDefault());
document.addEventListener("gesturestart", (e) => e.preventDefault());

measure();
connect();
