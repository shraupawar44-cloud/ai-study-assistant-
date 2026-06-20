from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""

    if request.method == "POST":

        question = request.form["question"].lower()

        if "html" in question:
            answer = "HTML is used to create web pages."

        elif "css" in question:
            answer = "CSS is used for styling web pages."

        elif "javascript" in question:
            answer = "JavaScript makes web pages interactive."

        elif "python" in question:
            answer = "Python is a powerful programming language."

        else:
            answer = "Sorry, I don't know this answer yet."

    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(debug=True)