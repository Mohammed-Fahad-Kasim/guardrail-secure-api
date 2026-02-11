import { useState } from "react";

export default function ThreatPanel() {
  const [threatScore, setThreatScore] = useState(84);
  const [events, setEvents] = useState([
    { time: "12:01:02", text: "High request burst detected" },
    { time: "12:01:04", text: "Threat score crossed threshold" },
    { time: "12:01:05", text: "Client blocked automatically" },
  ]);

  const simulateBotAttack = () => {
    setThreatScore((p) => Math.min(p + 5, 100));
    setEvents((e) => [
      { time: new Date().toLocaleTimeString(), text: "Bot behavior detected" },
      ...e,
    ]);
  };

  return (
    <div className="relative rounded-2xl border border-red-500/40 bg-black/40 p-6 shadow-[0_0_60px_rgba(255,0,0,0.15)]">
      <h3 className="text-sm text-gray-400">Threat Level</h3>

      <div className="mt-2 flex items-center gap-3">
        <span className="text-4xl font-bold text-red-500">HIGH</span>
        <span className="rounded-full bg-red-500 px-3 py-1 text-xs font-semibold text-black">
          ALERT
        </span>
      </div>

      <div className="mt-4 text-5xl font-extrabold text-white">
        {threatScore}
      </div>
      <p className="text-xs text-gray-400">Threat Score</p>

      <div className="mt-6 space-y-2 text-sm">
        <p className="text-red-400">• Rate limit exceeded: +39</p>
        <p className="text-orange-400">• Behavior anomaly: +30</p>
        <p className="text-yellow-400">• Fingerprint mismatch: +15</p>
      </div>

      <button
        onClick={simulateBotAttack}
        className="mt-6 w-full rounded-lg bg-red-500 px-4 py-2 font-semibold text-black hover:bg-red-400 transition"
      >
        Simulate Bot Attack
      </button>

      <div className="mt-6 border-t border-white/10 pt-4">
        <h4 className="mb-2 text-sm font-semibold text-white">Live Events</h4>
        <div className="space-y-2 max-h-32 overflow-y-auto pr-2">
          {events.map((e, i) => (
            <div
              key={i}
              className="flex justify-between rounded-md bg-white/5 px-3 py-2 text-xs text-gray-300"
            >
              <span>{e.text}</span>
              <span className="text-gray-500">{e.time}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
