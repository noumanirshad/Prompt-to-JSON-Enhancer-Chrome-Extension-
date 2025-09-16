// Background service worker (MV3)
// Currently not required for simple popup->content messaging and direct fetch to backend.
// Placeholder for future features: context menu, keyboard shortcuts, auto-capture, etc.

chrome.runtime.onInstalled.addListener(() => {
  // Initialize defaults
  chrome.storage.sync.set({ backendUrl: 'http://localhost:8000' });
});


