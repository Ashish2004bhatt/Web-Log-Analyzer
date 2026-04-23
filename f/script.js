// 🌙 Dark Mode Toggle
function toggleDarkMode() {
  document.body.classList.toggle("dark-mode");
}

// 📊 Bar Chart (Blue theme)
const barCtx = document.getElementById('barChart');
new Chart(barCtx, {
  type: 'bar',
  data: {
    labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    datasets: [{
      label: 'Requests',
      data: [120, 190, 300, 500, 200, 300, 400],
      backgroundColor: '#0078ff'
    }]
  },
  options: {
    responsive: true,
    scales: { y: { beginAtZero: true } }
  }
});

// 🧩 Pie Chart (colorful)
const pieCtx = document.getElementById('pieChart');
new Chart(pieCtx, {
  type: 'pie',
  data: {
    labels: ['Success', 'Fail', 'Error'],
    datasets: [{
      data: [60, 25, 15],
      backgroundColor: ['#1abc9c', '#e74c3c', '#f39c12']
    }]
  }
});

// 🗺️ Leaflet Map
const map = L.map('map').setView([20.5937, 78.9629], 3);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap'
}).addTo(map);
L.marker([28.6139, 77.2090]).addTo(map).bindPopup("New Delhi: 150 Requests");
L.marker([37.7749, -122.4194]).addTo(map).bindPopup("San Francisco: 230 Requests");
L.marker([51.5074, -0.1278]).addTo(map).bindPopup("London: 180 Requests");

// 🧠 Security Threat Meter (animated gauge)
const threatCtx = document.getElementById('threatMeter').getContext('2d');
let threatLevel = 0;
const gauge = new Chart(threatCtx, {
  type: 'doughnut',
  data: {
    datasets: [{
      data: [threatLevel, 100 - threatLevel],
      backgroundColor: ['#e74c3c', '#ddd'],
      borderWidth: 0
    }]
  },
  options: { rotation: -90, circumference: 180, cutout: '70%' }
});

function animateThreat() {
  threatLevel = Math.floor(Math.random() * 100);
  gauge.data.datasets[0].data = [threatLevel, 100 - threatLevel];
  gauge.update();
}

setInterval(animateThreat, 2000); // updates every 2 seconds