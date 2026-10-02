from flask import Flask, render_template, request, jsonify
from moduls.slay import solve_slae 
from moduls.log import solve_log
from moduls.moreChlenov import solve_polynomial_gcd
from moduls.gcd import solve_gcd
from moduls.pod import solve_permutation_power
from moduls.pod_count import solve_permutation_count_by_order
from moduls.simple_pod import found
from moduls.sp_block import solve_reverse
from moduls.gefe import generate_fec_code

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

@app.route("/podstanovka", methods=['GET'])
def podstanovka():
    return render_template("podstanovka.html")

@app.route("/podstanovka_count", methods=['GET'])
def podstanovka_count():
    return render_template("pod_count.html")

@app.route("/podstanovka_simple", methods=['GET'])
def podstanovka_simple():
    return render_template("pod_simple.html")

@app.route("/sp_block", methods=['GET'])
def ps_block():
    return render_template("ps_block.html")

@app.route("/gefe", methods=['GET'])
def gefe():
    return render_template("gefe.html")

@app.route("/gefe", methods=['POST'])
def gefe_post():
    data = request.get_json()
    registers = data['registers']
    start_values = data['start_values']
    length = data['len']
    open_text = data['open_text']

    result = generate_fec_code(registers, start_values, length, open_text)

    return jsonify({
        "result": result
    })

@app.route("/sp_block", methods=['POST'])
def sp_block_post():
    data = request.get_json()
    s = data['s']
    result = solve_reverse(s)

    return jsonify({
        "result": result
    })

@app.route("/podstanovka_simple", methods=['POST'])
def podstanovka_simple_post():
    data = request.get_json()
    podsta = data['a']
    max_el = data['max_el']
    result = found(podsta, max_el)

    return jsonify({
        "result": result
    })

@app.route("/podstanovka_count", methods=['POST'])
def podstanovka_count_post():
    data = request.get_json()
    n = data["n"]
    k = data["k"]
    result = solve_permutation_count_by_order(n, k)

    return jsonify({
        "result": result
    })

@app.route("/podstanovka", methods=['POST'])
def podstanovka_post():
    data = request.get_json()
    podsta = data['permutation']
    step = data['power']
    result = solve_permutation_power(podsta, step)

    return jsonify({
        "result": result
    })

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
    app.run(
        host='0.0.0.0',
        port='5000'
    )