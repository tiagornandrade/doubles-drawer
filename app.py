from flask import Flask, render_template, request, redirect, url_for
import random
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

people = []
rounds = []
drawn_pairs = set()

@app.route("/")
def index():
    return render_template("index.html", people=people)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        if name and name not in people:
            people.append(name)
        return redirect(url_for("index"))
    return render_template("register.html")

@app.route("/edit/<string:name>", methods=["GET", "POST"])
def edit(name):
    if request.method == "POST":
        new_name = request.form["new_name"]
        if new_name and new_name not in people:
            people[people.index(name)] = new_name
        return redirect(url_for("index"))
    return render_template("edit.html", name=name)

@app.route("/delete/<string:name>", methods=["POST"])
def delete(name):
    if name in people:
        people.remove(name)
    return redirect(url_for("index"))

@app.route("/reset", methods=["POST"])
def reset():
    global people, rounds, drawn_pairs
    people = []
    rounds = []
    drawn_pairs = set()
    return redirect(url_for("index"))

@app.route("/draw", methods=["GET", "POST"])
def draw():
    global drawn_pairs

    if request.method == "POST":
        if len(people) < 2:
            return redirect(url_for("index"))

        combinations = [(p1, p2) for i, p1 in enumerate(people) for p2 in people[i + 1:]]
        
        valid_combinations = [
            pair for pair in combinations if pair not in drawn_pairs
        ]

        if not valid_combinations:
            return render_template("draw.html", message="All combinations have been used!")

        random.shuffle(valid_combinations)

        current_round = []
        remaining_people = set(people)

        for pair in valid_combinations:
            if pair[0] in remaining_people and pair[1] in remaining_people:
                current_round.append(pair)
                remaining_people -= set(pair)

            if not remaining_people:
                break

        for pair in current_round:
            drawn_pairs.add(pair)

        rounds.append(current_round)

        excluded = None
        if len(people) % 2 != 0:
            excluded = list(remaining_people)[0] if remaining_people else None

        return render_template(
            "draw.html",
            round=current_round,
            excluded=excluded,
            drawn_pairs=drawn_pairs
        )

    return render_template("draw.html", drawn_pairs=drawn_pairs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
