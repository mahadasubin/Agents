const BASE = import.meta.env.VITE_API_BASE ?? 'http://localhost:4000';

export async function getHello() {
  const res = await fetch(`${BASE}/api/hello`);
  if (!res.ok) throw new Error('Network error');
  return res.json();
}

export async function echo(data) {
  const res = await fetch(`${BASE}/api/echo`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data)
  });
  return res.json();
}
