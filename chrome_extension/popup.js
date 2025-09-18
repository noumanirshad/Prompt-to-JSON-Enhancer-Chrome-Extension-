// Popup logic for Prompt-to-JSON Enhancer
// - Captures prompt, calls backend, renders JSON, copy + reinsert helpers

const els = {
  backendUrl: document.getElementById('backendUrl'),
  saveSettings: document.getElementById('saveSettings'),
  promptInput: document.getElementById('promptInput'),
  enhanceBtn: document.getElementById('enhanceBtn'),
  captureBtn: document.getElementById('captureBtn'),
  jsonOutput: document.getElementById('jsonOutput'),
  copyBtn: document.getElementById('copyBtn'),
  reinjectBtn: document.getElementById('reinjectBtn')
};

// Load stored backend URL or default
chrome.storage.sync.get({ backendUrl: 'https://prompt-to-json-enhancer.onrender.com' }, (cfg) => {
  els.backendUrl.value = cfg.backendUrl;
});

els.saveSettings.addEventListener('click', () => {
  chrome.storage.sync.set({ backendUrl: els.backendUrl.value.trim() || 'http://localhost:8000' }, () => {
    toast('Settings saved');
  });
});

els.captureBtn.addEventListener('click', async () => {
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  const resp = await chrome.tabs.sendMessage(tab.id, { type: 'CAPTURE_PROMPT' }).catch(() => null);
  if (resp && resp.prompt) {
    els.promptInput.value = resp.prompt;
    toast('Captured from page');
  } else {
    toast('Nothing captured');
  }
});

els.enhanceBtn.addEventListener('click', async () => {
  const prompt = els.promptInput.value.trim();
  if (!prompt) return toast('Enter a prompt');

  els.enhanceBtn.disabled = true;
  els.enhanceBtn.textContent = 'Enhancing...';

  const backendUrl = els.backendUrl.value.trim() || 'http://localhost:8000';
  try {
    const res = await fetch(`${backendUrl}/enhance`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt })
    });
    if (!res.ok) throw new Error('Backend error');
    const data = await res.json();
    els.jsonOutput.value = JSON.stringify(data.enhanced_prompt, null, 2);
    toast('Enhanced');
  } catch (e) {
    console.error(e);
    toast('Failed to enhance');
  } finally {
    els.enhanceBtn.disabled = false;
    els.enhanceBtn.textContent = 'Enhance';
  }
});

els.copyBtn.addEventListener('click', async () => {
  try {
    await navigator.clipboard.writeText(els.jsonOutput.value || '');
    toast('Copied');
  } catch {
    toast('Copy failed');
  }
});

els.reinjectBtn.addEventListener('click', async () => {
  const jsonText = els.jsonOutput.value.trim();
  if (!jsonText) return toast('Nothing to insert');
  let parsed;
  try { parsed = JSON.parse(jsonText); } catch { return toast('Invalid JSON'); }
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  await chrome.tabs.sendMessage(tab.id, { type: 'REINJECT_JSON', json: parsed }).catch(() => null);
  toast('Reinserted');
});

function toast(msg) {
  // Simple inline toast
  const el = document.createElement('div');
  el.textContent = msg;
  el.style.cssText = 'position:fixed;bottom:10px;left:10px;background:#111;color:#fff;padding:6px 8px;border-radius:6px;font-size:12px;opacity:0.95;z-index:9999';
  document.body.appendChild(el);
  setTimeout(() => el.remove(), 1500);
}


