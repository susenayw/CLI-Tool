// main.js
const { app, BrowserWindow, ipcMain, dialog } = require('electron');
const { exec } = require('child_process');
const path = require('path');

function createWindow() {
  const win = new BrowserWindow({
    width: 720,
    height: 540,
    resizable: false,
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

// Helper function to execute Python CLI and parse JSON output
function runPythonCommand(commandArgs) {
  return new Promise((resolve, reject) => {
    const command = `python -m devpulse.main ${commandArgs}`;
    
    exec(command, { cwd: __dirname }, (error, stdout, stderr) => {
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
  return await runPythonCommand(`weather "${city}" --json`);
});

ipcMain.handle('select-file', async () => {
  const { canceled, filePaths } = await dialog.showOpenDialog({ properties: ['openFile'] });
  return canceled ? null : filePaths[0];
});

ipcMain.handle('python-stats', async (event, filePath) => {
  return await runPythonCommand(`stats "${filePath}" --json`);
});