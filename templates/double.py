<!DOCTYPE html>
<html>
<head>
    <title>Simple Flask Form (Compute the double)</title>
</head>
<body>

    <h2>Input a number</h2>

    <form action="/predict" method="post">
        <input type="number" name="x" required>
        <button type="submit">Submit</button>
    </form>

    {% if result is not none %}
        <h3>Double Result: {{ result }}</h3>
    {% endif %}

</body>
</html>

from flask import Flask, render_template, request

app = Flask(__name__)


# 路由 1：顯示首頁輸入畫面
@app.route("/")
def index():
    return render_template("index.html")


# 路由 2：處理表單送出的資料
@app.route("/predict", methods=["POST"])
def predict():
    # 從前端表單抓取 name="x" 的輸入值，並轉換成整數
    x = int(request.form["x"])

    # 將數字乘以 2
    result = x * 2

    # 將計算結果回傳給 index.html 顯示
    return render_template("index.html", result=result)


if __name__ == "__main__":
    # 講義截圖中的執行方式
    app.run(debug=True)
