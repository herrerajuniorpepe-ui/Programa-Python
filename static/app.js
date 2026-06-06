document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('calcForm');
  const resultEl = document.getElementById('result');
  const resultJson = document.getElementById('resultJson');

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const i = document.getElementById('iInput').value;
    const j = document.getElementById('jInput').value;

    // POST JSON to /add
    try {
      const resp = await fetch('/add', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ i: Number(i), j: Number(j) })
      });

      const data = await resp.json();

      const payload = {
        status: resp.status,
        ok: resp.ok,
        body: data
      };

      resultJson.textContent = JSON.stringify(payload, null, 2);
      resultEl.classList.remove('hidden');
    } catch (err) {
      resultJson.textContent = JSON.stringify({ error: String(err) }, null, 2);
      resultEl.classList.remove('hidden');
    }
  });
});
