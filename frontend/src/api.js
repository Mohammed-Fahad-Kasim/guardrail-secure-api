// frontend/src/api.js

const BASE_URL = "http://127.0.0.1:8000/api";

export async function fetchMetrics() {
  const res = await fetch(`${BASE_URL}/metrics`);
  return res.json();
}

export async function fetchBlockedClients() {
  const res = await fetch(`${BASE_URL}/blocked-clients`);
  return res.json();
}

export async function simulateBotAttack() {
  const res = await fetch(`${BASE_URL}/simulate/bot`, {
    method: "POST",
  });
  return res.json();
}
