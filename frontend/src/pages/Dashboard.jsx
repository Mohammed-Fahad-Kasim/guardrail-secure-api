import { useEffect, useState } from "react";
import Sidebar from "../components/Sidebar";
import MetricCard from "../components/MetricCard";
import ThreatPanel from "../components/ThreatPanel";
import BlockedClientsTable from "../components/BlockedClientsTable";
import {
  fetchMetrics,
  fetchBlockedClients,
  simulateBotAttack,
} from "../api";

export default function Dashboard() {
  const [metrics, setMetrics] = useState(null);
  const [blockedClients, setBlockedClients] = useState([]);

  async function loadData() {
    const metricsData = await fetchMetrics();
    const blockedData = await fetchBlockedClients();
    setMetrics(metricsData);
    setBlockedClients(blockedData);
  }

  async function handleSimulateBot() {
    await simulateBotAttack();
    await loadData(); // refresh after attack
  }

  useEffect(() => {
    loadData();
    const interval = setInterval(loadData, 3000); // live refresh
    return () => clearInterval(interval);
  }, []);

  if (!metrics) return null;

  return (
    <div className="flex">
      <Sidebar />

      <main className="flex-1 p-8 space-y-8">
        <header>
          <h1 className="text-3xl font-bold">
            🛡️ Secure API Abuse Detection
          </h1>
          <p className="text-gray-400">
            Real-time behavioral security monitoring
          </p>
        </header>

        <div className="grid grid-cols-3 gap-6">
          <MetricCard
            title="Total Requests"
            value={metrics.total_requests}
            color="blue"
          />

          <MetricCard
            title="Blocked Requests"
            value={metrics.blocked_requests}
            color="red"
          />

          <ThreatPanel
            threatLevel={metrics.threat_level}
            threatScore={metrics.threat_score}
            reasons={metrics.reasons}
            onSimulate={handleSimulateBot}
          />
        </div>

        <BlockedClientsTable clients={blockedClients} />
      </main>
    </div>
  );
}
