from flask import Flask, request, jsonify

# フィボナッチ数列の関数
def fibonacci(n):
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for i in range(2, n):
            a, b = b, a + b
        return b

# Flaskアプリケーション
app = Flask(__name__)

@app.route('/fib', methods=['GET'])
def get_fibonacci():
    try:
        n = int(request.args.get('n'))
        result = fibonacci(n)
        return jsonify({"result": result}), 200
    except ValueError as e:
        return jsonify({"status": 400, "message": str(e)}), 400

# アプリケーションの実行
if __name__ == '__main__':
    app.run(debug=True)
