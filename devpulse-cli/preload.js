// preload.js
const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('devpulseAPI', {
  getWeather: (city) => ipcRenderer.invoke('python-weather', city),
  selectFile: () => ipcRenderer.invoke('select-file'),
  getFileStats: (filePath) => ipcRenderer.invoke('python-stats', filePath)
});