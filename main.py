from flask import Flask, render_template, request, jsonify
from moduls.slay import solve_slae 
from moduls.log import solve_log
from moduls.moreChlenov import solve_polynomial_gcd
from moduls.gcd import solve_gcd

app = Flask(__name__)

@app.route("/", methods=['GET'])
def start():
    return render_template("index.html")

@app.route("/slay", methods=['GET'])
def slay():
    return render_template("slay.html")

@app.route("/log", methods=['GET'])
def log():
    return render_template("log.html")

@app.route("/polynomial", methods=['GET'])
def polynomial():
    return render_template("polynomial.html")

@app.route("/calculate", methods=['GET'])
def gcd():
    return render_template("gcd.html")


@app.route("/calculate", methods=["POST"])
def gcd_post():
    data = request.get_json()

    a = int(data["a"])
    b = int(data["b"])

    if a < 0 or b < 0:
        a = abs(a)
        b = abs(b)

    if a == 0 and b == 0:
        return jsonify({
            "error": "Оба числа не могут быть равны нулю одновременно."
        }), 400

    result = solve_gcd(a, b)

    return jsonify({
        "result": result
    })

@app.route("/polynomial", methods=["POST"])
def polynomial_post():
    data = request.get_json()

    a = data["dividend"].strip()
    b = data["divisor"].strip()

    if (
        not a
        or not b
        or set(a) - {"0", "1"}
        or set(b) - {"0", "1"}
    ):
        return jsonify({
            "error": (
                "Входные данные должны быть "
                "непустыми двоичными строками "
                "(только 0 и 1)."
            )
        }), 400

    result = solve_polynomial_gcd(a, b)

    return jsonify({
        "result": result
    })

@app.route("/log", methods=["POST"]) 
def log_post(): 
    data = request.get_json() 
    p = int(data["p"]) 
    y = int(data["y"]) 
    result = solve_log(p, y) 
    return jsonify({ "result": result })

@app.route("/slay", methods=['POST'])
def slay_post():

    data = request.get_json()

    matrix = data["matrix"]
    field = data["field"]

    result = solve_slae(matrix, field)

    return jsonify({
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)