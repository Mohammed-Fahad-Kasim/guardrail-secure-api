export default function Sidebar() {
  return (
    <aside className="fixed left-0 top-0 h-screen w-64 bg-gradient-to-b from-[#050b18] to-black border-r border-white/10 px-6 py-6 z-50">
      
      <div className="flex items-center gap-2 mb-10 text-xl font-bold">
        🛡 GuardRail
      </div>

      <nav className="space-y-3">
        <div className="rounded-xl bg-white/10 px-4 py-3 cursor-pointer">
          📊 Dashboard
        </div>
        <div className="rounded-xl px-4 py-3 hover:bg-white/5 cursor-pointer">
          🚨 Threats
        </div>
        <div className="rounded-xl px-4 py-3 hover:bg-white/5 cursor-pointer">
          ⚙️ Settings
        </div>
      </nav>

      <div className="absolute bottom-6 left-6 text-xs text-green-400">
        System Health: Stable
      </div>
    </aside>
  );
}
