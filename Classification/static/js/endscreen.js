//Change the sentences at the beginning to the dictionary values provided by the server
document.getElementById("p1").innerText = "Your stats, " + dictionary["username"];
document.getElementById("p2").innerText = "Earned points: " + dictionary["user_score"] + "/2500";
document.getElementById("p3").innerText = "Correct answer : " + parseInt(dictionary["correct"]/25*100) + "%";
