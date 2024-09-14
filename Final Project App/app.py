from flask import Flask
from flask import Flask, render_template, request, redirect, flash, session, url_for
from query5 import query_5

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        t1 = request.form["t1"]
        t2 = request.form["t2"]
        # t3 = request.form["t3"]

        print(t1,t2)
        data=query_5(t1, t2)
        print(data)
        # data=temp2(sample)
        return render_template("result5.html",data=data)
    return render_template("option5.html")


@app.route("/option5", methods=["GET", "POST"])
def option5():
    if request.method == "POST":
        t1 = request.form["t1"]
        t2 = request.form["t2"]
        # t3 = request.form["t3"]

        print(t1,t2)
        data=query_5(t1, t2)
        print(data)
        # data=temp2(sample)
        return render_template("result5.html",data=data)
    return render_template("option5.html")


@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        text = request.form["r1"]
        print(text)
        # input =text.split(',')
        data=query1(text, opt)
        return render_template("result.html",data=data)
    return render_template("result.html")
    



if __name__ == "__main__":

    app.run(debug=True)