 if (user_id in dictionary) {
        document.getElementById("p1").innerHTML = "You are: " + dictionary[user_id]["username"] + "<br>"
            + "Your score: " + dictionary[user_id]["user_score"]+ "/2500" + " points (" + parseInt(dictionary[user_id]["correct"] / 25 * 100) + "%)";
    }else{
        document.getElementById("p1").innerHTML = "You are: User not found."
    }
    function scrollen()
    {
        document.getElementById('you').scrollIntoView({
  behavior: 'smooth'
});
    }