//Hide display element (progress)
document.getElementById("display").style.visibility = "hidden";

//Reload video
function reload_video() {
	document.getElementById("video").load()
}

//Show display element (progress)
function call_display() {
	document.getElementById("display").style.visibility = "visible";
}
//Show progress bar after 2.5 sec
setTimeout(call_display, 2500);
var progress_value = parseInt(parseInt(progress) / 25 * 100) + "%";
document.getElementById("progress_bar").style.width = progress_value;
document.getElementById("display").innerHTML = progress_value;

//Define variable for feedback
var correct_screen = document.getElementById("feedback_background_correct");
var wrong_screen = document.getElementById("feedback_background_wrong");

//Hide both feedback at the beginning
correct_screen.style.visibility = "hidden";
wrong_screen.style.visibility = "hidden";

const video = document.getElementById("video");
var toggle_counter = 0;
var toggle_play = false;

//Function for play/pause button
function togglePlay() {
	if (toggle_play) {
		video.pause();
		document.getElementById("play_button").innerHTML = "Play";
	} else {
		video.play();
		document.getElementById("play_button").innerHTML = "Pause";
	}
	toggle_play = !toggle_play;
	toggle_counter++;
}

//Function for fullscreen button
function toggleFullscreen() {
	if (document.fullscreenElement || document.webkitFullscreenElement ||
		document.mozFullScreenElement) {
		if (document.exitFullscreen) {
			document.exitFullscreen();
		} else if (document.webkitExitFullscreen) { /* Safari */
			document.webkitExitFullscreen();
		} else if (document.msExitFullscreen) { /* IE11 */
			document.msExitFullscreen();
		}
	} else {
		if (video_margin.requestFullscreen) {
			video_margin.requestFullscreen();
		} else if (video_margin.webkitRequestFullscreen) { /* Safari */
			video_margin.webkitRequestFullscreen();
		} else if (video_margin.msRequestFullscreen) { /* IE11 */
			video_margin.msRequestFullscreen();
		}
	}
}

var fullscreen_counter = 0;
var video_margin = document.getElementById("video-margin");

//Define event listener for fullscreen integrity, calls check_screen method on fullscreen change
document.addEventListener("fullscreenchange", check_screen);

//Keeps integrity of fullscreen even after "Esc" has been pressed
function check_screen() {
	fullscreen_counter++;
	if (!(document.fullscreenElement || document.webkitFullscreenElement ||
			document.mozFullScreenElement)) {
		video.height = "480";
		video.width = "720";
	} else {
		video.height = "4096";
		video.width = "3072";
	}
}


var replay_counter = 0;

//Function for replay button
function replay() {
	replay_counter++;
	video.currentTime = '0';
	video.play();
	toggle_play = true;
	document.getElementById("play_button").innerHTML = "Pause";
}
var playback_counter = 0;

var playback_index = 0;

//Function for playback button
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
//Counts duration spent on website per video
function second_counter() {
	duration_in_sec += 1;
}
//Calls the second_counter function every second
setInterval(second_counter, 1000)

//If window finished loading hide loading screen
window.onload = function () {
	var loader = document.getElementById("loader_screen");
	loader.style.display = "none";
}
var difficulty = "0";
var category = "0";

//Submission difficulty of participant
function set_difficulty(diffi) {
	difficulty = diffi;
}

//Submission category of participant
function set_category(cate) {
	category = cate;
}

//Color change of submit button on mouse hover
document.getElementById("submit_button").onmouseover = function () {
	var color = "rgb(191,0,0)"
	if (difficulty !== "0" && category !== "0") {
		color = "rgb(4,164,0, 1)";
	}
	this.style.backgroundColor = color;
};

//Color change of submit button on mouse remove
document.getElementById("submit_button").onmouseout = function () {
	this.style.backgroundColor = "rgba(220, 160, 140, 0)";
};

//Is called if pressed on the submit button, checks integrity of submission and the feedback group
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

//Submits the data to the server
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
