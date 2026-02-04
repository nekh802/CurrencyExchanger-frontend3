const API_BASE =
  import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

export async function convert(from, to, amount) {
  const params = new URLSearchParams({
    from_currency: from,
    to_currency: to,
    amount: String(amount),
  });

  const url = `${API_BASE.replace(/\/$/, "")}/convert?${params}`;

  const res = await fetch(url);
  const text = await res.text();

  if (!res.ok) throw new Error(text);

  return JSON.parse(text);
}