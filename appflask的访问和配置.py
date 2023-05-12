from flask import Flask

app = Flask(__name__)


@app.route('/tt')  #指定路由路由
def index():   #视图函数

    return 'hello word'


if __name__=="__main__":
    app.run(host='0.0.0.0')





