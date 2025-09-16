// Content script: capture prompt from common AI site inputs and allow reinsertion

function getActiveInput() {
  // Try common selectors for ChatGPT, Claude, Gemini
  const selectors = [
    'textarea',
    'textarea[placeholder*="message" i]',
    'textarea[placeholder*="prompt" i]',
    'div[contenteditable="true"]'
  ];
  for (const sel of selectors) {
    const el = document.querySelector(sel);
    if (el) return el;
  }
  return null;
}

function getTextFromElement(el) {
  if (!el) return '';
  if (el.tagName === 'TEXTAREA' || el.tagName === 'INPUT') return el.value || '';
  if (el.getAttribute('contenteditable') === 'true') return el.textContent || '';
  return '';
}

function setTextToElement(el, text) {
  if (!el) return;
  if (el.tagName === 'TEXTAREA' || el.tagName === 'INPUT') el.value = text;
  else if (el.getAttribute('contenteditable') === 'true') el.textContent = text;
}

chrome.runtime.onMessage.addListener((msg, _sender, sendResponse) => {
  if (msg?.type === 'CAPTURE_PROMPT') {
    const el = getActiveInput();
    const prompt = getTextFromElement(el);
    sendResponse({ prompt });
    return true;
  }
  if (msg?.type === 'REINJECT_JSON') {
    const el = getActiveInput();
    const pretty = JSON.stringify(msg.json, null, 2);
    setTextToElement(el, pretty);
    sendResponse({ ok: true });
    return true;
  }
});


