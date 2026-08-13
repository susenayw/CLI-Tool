// main.js
const { app, BrowserWindow, ipcMain, dialog } = require('electron');
const { execFile } = require('child_process');
const path = require('path');

function createWindow() {
  const win = new BrowserWindow({
    width: 720,
    height: 540,
    resizable: false,
    icon: path.join(__dirname, 'build', 'icon.ico'),
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false
    }
  });

  win.loadFile('src/index.html');
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});

// Resolve binary path depending on dev mode vs packaged build
function getEnginePath() {
  const isPackaged = app.isPackaged;
  return isPackaged
    ? path.join(process.resourcesPath, 'bin', 'devpulse-engine.exe')
    : path.join(__dirname, 'bin', 'devpulse-engine.exe');
}

// Execute Python binary
function runPythonCommand(commandArgs) {
  return new Promise((resolve, reject) => {
    const enginePath = getEnginePath();
    
    execFile(enginePath, commandArgs, (error, stdout, stderr) => {
      if (error) {
        reject(stderr || error.message);
        return;
      }
      try {
        resolve(JSON.parse(stdout.trim()));
      } catch (e) {
        resolve({ rawOutput: stdout.trim() });
      }
    });
  });
}

// --- IPC Handlers ---
ipcMain.handle('python-weather', async (event, city) => {
  return await runPythonCommand(['weather', city, '--json']);
});

ipcMain.handle('select-file', async () => {
  const { canceled, filePaths } = await dialog.showOpenDialog({ properties: ['openFile'] });
  return canceled ? null : filePaths[0];
});

ipcMain.handle('python-stats', async (event, filePath) => {
  return await runPythonCommand(['stats', filePath, '--json']);
});