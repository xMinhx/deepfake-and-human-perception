document.getElementById("p1").innerText = "Your stats, " + dictionary["username"];
document.getElementById("p2").innerText = "Earned points: " + dictionary["user_score"];
document.getElementById("p3").innerText = "Correct answer : " + parseInt(dictionary["correct"]/50*100) + "%";