// src/renderer.js

// Weather Query
document.getElementById('get-weather-btn').addEventListener('click', async () => {
  const city = document.getElementById('city-input').value.trim();
  const card = document.getElementById('weather-card');

  if (!city) return alert('Please enter a city name.');
  card.innerHTML = '⚡ Running Python backend...';

  try {
    const response = await window.devpulseAPI.getWeather(city);
    if (response.error) {
      card.innerHTML = `❌ ${response.error}`;
      return;
    }

    const data = response.data;
    card.innerHTML = `
      📍 ${data.city}, ${data.country}
      🌡️ Temp: ${data.temp}
      💧 Humidity: ${data.humidity}
      💨 Wind: ${data.wind}
    `;
  } catch (err) {
    card.innerHTML = `⚠️ Process Error: ${err}`;
  }
});

// File Stats
document.getElementById('select-stats-file').addEventListener('click', async () => {
  const filePath = await window.devpulseAPI.selectFile();
  if (!filePath) return;

  const card = document.getElementById('stats-card');
  card.innerText = '⚡ Processing file with Python...';

  const res = await window.devpulseAPI.getFileStats(filePath);
  if (res.error) {
    card.innerText = `Error: ${res.error}`;
    return;
  }

  card.innerHTML = `
    File: ${res.fileName}
    Lines: ${res.lines} | Words: ${res.words} | Chars: ${res.chars}
  `;
});