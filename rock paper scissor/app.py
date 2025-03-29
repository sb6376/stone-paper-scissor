from flask import Flask, render_template, request, session, redirect, url_for
import random
app = Flask(__name__)
app.secret_key = "your_secret_key"  
choices = ["rock", "paper", "scissors"]
def get_winner(player, computer):
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        session['player_score'] += 1  
        return "You win!"
    else:
        session['computer_score'] += 1 
        return "You lose!"
@app.route("/", methods=["GET", "POST"])
def index():
    if 'player_score' not in session:
        session['player_score'] = 0
    if 'computer_score' not in session:
        session['computer_score'] = 0
    user_choice = None
    computer_choice = None
    result = None
    if request.method == "POST":
        user_choice = request.form["choice"]
        computer_choice = random.choice(choices)
        result = get_winner(user_choice, computer_choice)
    return render_template("index.html", user_choice=user_choice, computer_choice=computer_choice, result=result, player_score=session['player_score'], computer_score=session['computer_score'])
@app.route("/reset")
def reset():
    session['player_score'] = 0
    session['computer_score'] = 0
    return redirect(url_for("index"))  
@app.route("/remove")
def remove():
    session.pop('player_score', None)
    session.pop('computer_score', None)
    return redirect(url_for("index"))  
if __name__ == "__main__":
    app.run(debug=True)
