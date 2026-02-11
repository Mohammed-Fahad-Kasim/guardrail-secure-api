import React from "react";

const clients = [
  {
    id: "fp_92ac",
    reason: "Rate-limit bypass",
    score: 87,
    status: "Blocked",
  },
  {
    id: "fp_18bd",
    reason: "Bot behavior",
    score: 92,
    status: "Blocked",
  },
  {
    id: "fp_c369",
    reason: "Automated abuse",
    score: 84,
    status: "Blocked",
  },
];

export default function BlockedClientsTable() {
  return (
    <div className="mt-8 rounded-2xl border border-white/10 bg-gradient-to-br from-white/5 to-white/0 p-6 backdrop-blur-xl">
      <h2 className="mb-4 text-lg font-semibold text-white">
        Recently Blocked Clients
      </h2>

      <div className="overflow-x-auto">
        <table className="w-full border-collapse text-sm">
          <thead>
            <tr className="text-left text-white/60">
              <th className="pb-3">Client ID</th>
              <th className="pb-3">Reason</th>
              <th className="pb-3">Threat Score</th>
              <th className="pb-3">Status</th>
              <th className="pb-3 text-right">Action</th>
            </tr>
          </thead>

          <tbody>
            {clients.map((c, i) => (
              <tr
                key={i}
                className="border-t border-white/5 hover:bg-white/5 transition"
              >
                <td className="py-3 font-mono text-white">{c.id}</td>
                <td className="py-3 text-white/70">{c.reason}</td>
                <td className="py-3 text-white">{c.score}</td>

                <td className="py-3">
                  <span className="rounded-full bg-red-500/20 px-3 py-1 text-xs text-red-400">
                    {c.status}
                  </span>
                </td>

                <td className="py-3 text-right space-x-2">
                  <button className="rounded-lg bg-blue-500/20 px-3 py-1 text-xs text-blue-400 hover:bg-blue-500/30">
                    Unblock
                  </button>
                  <button className="rounded-lg bg-red-500/20 px-3 py-1 text-xs text-red-400 hover:bg-red-500/30">
                    Block
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
