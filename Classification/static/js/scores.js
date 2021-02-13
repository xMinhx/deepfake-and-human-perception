//Check if user is listed in the scoreboard, if yes show his performance, else display user not found
if (user_id in dictionary) {
        document.getElementById("p1").innerHTML = "You are: " + dictionary[user_id]["username"] + "<br>"
            + "Your score: " + dictionary[user_id]["user_score"]+ "/2500" + " points (" + parseInt(dictionary[user_id]["correct"] / 25 * 100) + "%)";
    }else{
        document.getElementById("p1").innerHTML = "You are: User not found."
    }
//Function of the Find Button, which searches the user in the scoreboard
    function scrollen()
    {
        document.getElementById('you').scrollIntoView({
  behavior: 'smooth'
});
    }
