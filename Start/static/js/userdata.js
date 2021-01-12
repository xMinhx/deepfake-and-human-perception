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

//Code for user device detection from https://dev.to/itsabdessalam/detect-current-device-type-with-javascript-490j
function getDeviceType() {
  const ua = navigator.userAgent;
  if (/(tablet|ipad|playbook|silk)|(android(?!.*mobi))/i.test(ua)) {
    return "tablet";
  }
  if (
    /Mobile|iP(hone|od)|Android|BlackBerry|IEMobile|Kindle|Silk-Accelerated|(hpw|web)OS|Opera M(obi|ini)/.test(ua)
  ) {
    return "mobile";
  }
  return "desktop";
}

function get_device_data() {
    document.getElementById('height').value = window.innerHeight;
    document.getElementById('width').value = window.innerWidth;
    document.getElementById('fps').value = fps;
    document.getElementById('device').value = getDeviceType();
    alert(getDeviceType());
    var age = parseInt(document.getElementById("age").value)
    if (["1", "2", "3"].includes(document.getElementById('gender').value) && (age >= 8 && age <= 122)) {
        document.getElementById("mainform").submit();
    } else {
        alert("Please enter a correct value for gender and age.")
    }
}