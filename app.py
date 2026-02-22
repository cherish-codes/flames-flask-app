from flask import Flask, render_template, request

app = Flask(__name__)

def flames_result(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")

    for letter in name1[:]:
        if letter in name2:
            name1 = name1.replace(letter, "", 1)
            name2 = name2.replace(letter, "", 1)

    count = len(name1) + len(name2)

    flames = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

    while len(flames) > 1:
        split_index = (count % len(flames)) - 1

        if split_index >= 0:
            right = flames[split_index + 1:]
            left = flames[:split_index]
            flames = right + left
        else:
            flames.pop()

    return flames[0]


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        name1 = request.form["name1"]
        name2 = request.form["name2"]
        result = flames_result(name1, name2)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)