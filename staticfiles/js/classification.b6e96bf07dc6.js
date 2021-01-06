document.getElementById("display").style.visibility = "hidden";

function call_display() {
	document.getElementById("display").style.visibility = "visible";
}
setTimeout(call_display, 2100);
var progress_value = parseInt(parseInt(videoleft) / 25 * 100) + "%";
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
}
var playback_counter = 0;

function playback() {
	video.playbackRate = document.getElementById("playspeed_id").value;
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

function check_values() {
	document.getElementById("display").style.visibility = "hidden";
	var difficulty = document.getElementById("difficulty").value;
	var category = document.getElementById("category").value;
	if (["1", "2", "3"].includes(difficulty) && ["1", "2"].includes(category)) {
		video.pause();
		if (category === video_label_id && test_id === "1") {
			correct_screen.style.visibility = "visible";
		} else if (category !== video_label_id && test_id === "1") {
			wrong_screen.style.visibility = "visible";
		} else {
			document.getElementById("loader_screen").style.display = "unset";
		}
		setTimeout(submit_data, 1500);
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
	document.getElementById("difficulty_submit").value = document.getElementById("difficulty").value;
	document.getElementById("category_submit").value = document.getElementById("category").value;

	document.getElementById("submit_form").submit();
}