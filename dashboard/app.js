
console.log("Smart Home Dashboard Loaded");

// --------------------
// FETCH LIVE STATE
// --------------------
async function fetchData() {
    try {
        const res = await fetch("http://127.0.0.1:5000/latest");
        const data = await res.json();

        document.getElementById("livingLight").innerText =
            "Status: " + (data.light ? "ON" : "OFF");

        document.getElementById("livingFan").innerText =
            "Speed: " + data.fan + "%";

        document.getElementById("bedAC").innerText =
            "Temp: " + data.ac + "°C";

        document.getElementById("kitchenLight").innerText =
            "Status: " + (data.kitchen ?? 0 ? "ON" : "OFF");

        document.getElementById("bathFan").innerText =
            "Status: " + (data.bath ?? 0 ? "ON" : "OFF");

        document.getElementById("tv").innerText =
            "Status: " + (data.tv ?? 0 ? "ON" : "OFF");

        document.getElementById("garage").innerText =
            "Status: " + (data.garage ?? 0 ? "OPEN" : "CLOSED");

    } catch (err) {
        console.log("Fetch error:", err);
    }
}

// --------------------
// SEND COMMANDS
// --------------------
async function send(payload) {
    await fetch("http://127.0.0.1:5000/control", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });
}

// --------------------
// CONTROLS
// --------------------
function setLight(v) { send({ light: v }); }
function setFan(v) { send({ fan: Number(v) }); }
function setAC(v) { send({ ac: Number(v) }); }

function setKitchen(v) { send({ kitchen: v }); }
function setBath(v) { send({ bath: v }); }
function setTV(v) { send({ tv: v }); }
function setGarage(v) { send({ garage: v }); }

// --------------------
// LOOP
// --------------------
setInterval(fetchData, 1000);
fetchData();