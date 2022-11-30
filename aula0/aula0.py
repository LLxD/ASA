from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def my_microservice():
    return jsonify({"message": "Hello World!"})


@app.route("/api", methods=["GET", "POST"])
def api():
    if request.method == "POST":
        person_data = request.get_json()
        if person_data:
            return jsonify({"message": "POST", "data": person_data})
        return jsonify({"message": "POST", "data": None})
    else:
        return jsonify({"message": "Hello API!", "method": "GET", "status": 200})


@app.route("/api/<person_id>", methods=["POST"])
def person_api(person_id):
    name = request.args.get("name")
    return jsonify({"user_code": person_id, "name": name})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
