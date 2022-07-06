from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/add_two_nums', methods=['POST'])  # POST 데이터를 추가.
def add_two_nums():
    data = request.get_json()  # 클라이언트로부터 json형식으로 데이터를 받는다.
    return data

if __name__ == "__main__":   # flask 마지막에 들어가는 기본
    app.run()
