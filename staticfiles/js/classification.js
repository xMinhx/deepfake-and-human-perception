document.getElementById("display").style.visibility = "hidden";

function reload_video() {
	document.getElementById("video").load()
}

function call_display() {
	document.getElementById("display").style.visibility = "visible";
}
setTimeout(call_display, 2500);
var progress_value = parseInt(parseInt(progress) / 25 * 100) + "%";
document.getElementById("progress_bar").style.width = progress_value;
document.getElementById("display").innerHTML = progress_value;

var correct_screen = document.getElementById("feedback_background_correct");
var wrong_screen = document.getElementById("feedback_background_wrong");

correct_screen.style.visibility = "hidden";
wrong_screen.style.visibility = "hidden";

const video = document.getElementById("video");
var toggle_counter = 0;
var toggle_play = false;

function togglePlay() {
	toggle_play ? video.pause() : video.play();
	toggle_play = !toggle_play;
	toggle_counter++;
}

var fullscreen_counter = 0

function openFullscreen() {
	fullscreen_counter++;
	if (video.requestFullscreen) {
		video.requestFullscreen();
	} else if (video.webkitRequestFullscreen) { /* Safari */
		video.webkitRequestFullscreen();
	} else if (video.msRequestFullscreen) { /* IE11 */
		video.msRequestFullscreen();
	}
}
var replay_counter = 0;

function replay() {
	replay_counter++;
	video.currentTime = '0';
	video.play();
	toggle_play = true;
}
var playback_counter = 0;

var playback_index = 0;

function playback() {
	playback_index++;
	if (playback_index > 4) {
		playback_index = 0;
	}
	var playback_array = [1, 1.5, 2, 0.1, 0.5];
	video.playbackRate = playback_array[playback_index];
	document.getElementById("playbackspeed").innerHTML = "Playbackspeed: " + playback_array[playback_index] + "x";
	playback_counter++;
}

var duration_in_sec = 0;

function second_counter() {
	duration_in_sec += 1;
}
setInterval(second_counter, 1000)

window.onload = function () {
	var loader = document.getElementById("loader_screen");
	loader.style.display = "none";
}
var difficulty = "0";
var category = "0";

function set_difficulty(diffi) {
	difficulty = diffi;
}

function set_category(cate) {
	category = cate;
}

document.getElementById("submit_button").onmouseover = function () {
	var color = "rgb(191,0,0)"
	if (difficulty !== "0" && category !== "0") {
		color = "rgb(4,164,0, 1)";
	}
	this.style.backgroundColor = color;
};

document.getElementById("submit_button").onmouseout = function () {
	this.style.backgroundColor = "rgba(220, 160, 140, 0)";
};

function check_values() {
	document.getElementById("display").style.visibility = "hidden";
	if (["1", "2", "3"].includes(difficulty) && ["1", "2"].includes(category)) {
		video.pause();
		if ((category === i) && (j === "1")) {
			correct_screen.style.visibility = "visible";
		} else if ((category !== i) && (j === "1")) {
			wrong_screen.style.visibility = "visible";
		} else {
			document.getElementById("loader_screen").style.display = "unset";
		}
		setTimeout(submit_data, 1000);
	} else {
		alert("Please enter a correct difficulty or category value.");
	}
}

function submit_data() {
	document.getElementById('play_count').value = toggle_counter;
	document.getElementById('fullscreen_count').value = fullscreen_counter;
	document.getElementById('replay_count').value = replay_counter;
	document.getElementById("playback_count").value = playback_counter;
	document.getElementById("duration").value = duration_in_sec;
	document.getElementById("textarea_submit").value = document.getElementById("text_field").value;
	document.getElementById("difficulty_submit").value = difficulty;
	document.getElementById("category_submit").value = category;

	document.getElementById("submit_form").submit();
}