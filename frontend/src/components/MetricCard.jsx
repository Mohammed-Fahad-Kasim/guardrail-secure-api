export default function MetricCard({ title, value, color }) {
  return (
    <div className="glass hover-lift rounded-2xl p-6">
      <p className="text-gray-400 text-sm">{title}</p>
      <p className={`text-4xl font-bold mt-3 ${color}`}>{value}</p>
    </div>
  );
}
