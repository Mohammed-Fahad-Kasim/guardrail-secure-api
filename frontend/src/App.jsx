import Sidebar from "./components/Sidebar";
import Dashboard from "./pages/Dashboard";

export default function App() {
  return (
    <div className="min-h-screen bg-black text-white">
      {/* Sidebar */}
      <Sidebar />

      {/* Main Content Area */}
      <div className="ml-64 min-h-screen overflow-x-hidden">
        <Dashboard />
      </div>
    </div>
  );
}
