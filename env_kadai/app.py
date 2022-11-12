import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
# def hello():
#     mes = "Hello World"
#     return mes
def index():
    todayNumber = random.randint(1,100)
    list = [1,2,3,4,5,6,7,8,9]
    dictionary = {"color":"オレンジ","food":"焼肉","sport":"卓球"}
    return render_template("index.html",list =list,dictionary=dictionary,todayNumber=todayNumber)



if __name__ == "__main__":
    app.run(port=8080)
