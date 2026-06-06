console.log("Dashboard JS Loaded");

async function fetchData() {
    try {
        const res = await fetch("http://127.0.0.1:5000/latest");
        const data = await res.json();

        console.log("DATA:", data);

        // Light
        document.getElementById("light").innerText =
            data.light ? "ON" : "OFF";

        // Fan
        document.getElementById("fan").innerText =
            data.fan + "%";

        // AC
        document.getElementById("ac").innerText =
            data.ac + "°C";

    } catch (err) {
        console.log("Fetch Error:", err);
    }
}

// auto refresh every 2 seconds
setInterval(fetchData, 2000);
fetchData();