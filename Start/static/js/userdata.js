const times = [];
let fps;

function refreshLoop() {
    window.requestAnimationFrame(() => {
        const now = performance.now();
        while (times.length > 0 && times[0] <= now - 1000) {
            times.shift();
        }
        times.push(now);
        fps = times.length;
        refreshLoop();
    });
}
refreshLoop();

function get_device_data() {
    document.getElementById('height').value = window.innerHeight;
    document.getElementById('width').value = window.innerWidth;
    document.getElementById('fps').value = fps;
    var age = parseInt(document.getElementById("age").value)
    if (["1", "2", "3"].includes(document.getElementById('gender').value) && (age >= 8 && age <= 122)) {
        document.getElementById("mainform").submit();
    } else {
        alert("Please enter a correct difficulty or category value.")
    }
}