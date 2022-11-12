from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index2():
    request_data= request.args.get("data")
    if request.method == "GET":
        print(request_data)
    return render_template("index2.html",request_data=request_data)

@app.route("/routing")
def routing():
    return render_template("routing.html")

@app.route("/get")
def get():
    request_data=request.args.get("getDATA")
    return render_template("get.html",request_data=request_data)

@app.route("/post",methods=["POST"])
def post():
    request_data=request.form["postDATA"]
    return render_template("post.html",request_data=request_data)


if __name__ == "__main__":
    app.run(port=8080)
