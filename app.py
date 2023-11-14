from flask import Flask, request, jsonify

# フィボナッチ数列の関数
def fibonacci(n):
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for i in range(2, n):
        a, b = b, a + b
    return b

# Flaskアプリケーション
app = Flask(__name__)

@app.route('/fib', methods=['GET'])
def get_fibonacci():
    try:
        n_str = request.args.get('n')
        if n_str is None or not n_str.isdigit():
            raise ValueError("n must be a positive integer")

        n = int(n_str)
        result = fibonacci(n)
        return jsonify({"result": result}), 200
    except ValueError as e:
        return jsonify({"status": 400, "message": str(e)}), 400

# アプリケーションの実行
if __name__ == '__main__':
    app.run(debug=True)
