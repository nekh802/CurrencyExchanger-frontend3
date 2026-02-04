import { useState } from "react";
import { convert } from "./api";

const CURRENCIES = ["USD", "KRW", "JPY", "EUR", "BTC"];

export default function App() {
  const [from, setFrom] = useState("USD");
  const [to, setTo] = useState("KRW");
  const [amount, setAmount] = useState(1);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function onConvert() {
    try {
      setLoading(true);
      setError("");
      const data = await convert(from, to, amount);
      setResult(data);
    } catch (e) {
      setError(String(e));
    } finally {
      setLoading(false);
    }
  }

  function onSwap() {
    setFrom(to);
    setTo(from);
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50 p-6">
      <div className="w-full max-w-sm rounded-2xl bg-white p-6 shadow-sm ring-1 ring-black/5">
        <h2 className="text-xl font-bold">환율 계산기</h2>
        <p className="mt-1 text-sm text-gray-500">
          From/To 통화와 금액을 입력하세요.
        </p>

        <div className="mt-6 space-y-4">
          <label className="block">
            <span className="text-sm font-medium text-gray-700">From</span>
            <select
              value={from}
              onChange={(e) => setFrom(e.target.value)}
              className="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2
                        focus:border-gray-400 focus:ring-2 focus:ring-gray-200"
            >
              {CURRENCIES.map((cur) => (
                <option key={cur} value={cur}>
                  {cur}
                </option>
              ))}
            </select>
          </label>

          <label className="block">
            <span className="text-sm font-medium text-gray-700">To</span>
            <select
              value={to}
              onChange={(e) => setTo(e.target.value)}
              className="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2
                        focus:border-gray-400 focus:ring-2 focus:ring-gray-200"
            >
              {CURRENCIES.map((cur) => (
                <option key={cur} value={cur}>
                  {cur}
                </option>
              ))}
            </select>
          </label>

          <label className="block">
            <span className="text-sm font-medium text-gray-700">Amount</span>
            <input
              className="mt-1 w-full rounded-lg border border-gray-300 px-3 py-2 outline-none focus:border-gray-400 focus:ring-2 focus:ring-gray-200"
              type="number"
              inputMode="decimal"
              value={amount}
              onChange={(e) => setAmount(Number(e.target.value))}
              min="0"
              step="any"
            />
          </label>

          <button
            type="button"
            onClick={onSwap}
            className="mx-auto mt-2 flex items-center gap-1 text-sm text-gray-500 hover:text-black"
          >
            ↔ swap
          </button>

          <button
            onClick={onConvert}
            disabled={loading}
            className="mt-2 w-full rounded-lg bg-black px-4 py-2.5 text-white font-medium disabled:opacity-60"
          >
            {loading ? "계산 중..." : "변환"}
          </button>

          {error && <p className="text-sm text-red-600">{error}</p>}

          {result && (
            <div className="mt-4 rounded-lg bg-gray-50 p-4">
              <div className="text-sm text-gray-500">결과</div>

              <div className="mt-1 text-xl font-bold">
                {result.amount} {result.from} = {result.result} {result.to}
              </div>

              <div className="mt-2 text-xs text-gray-500">
                base: {result.base} · updated_at:{" "}
                {new Date(result.updated_at * 1000).toLocaleString()}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}