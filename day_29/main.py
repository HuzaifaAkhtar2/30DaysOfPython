from flask import Flask, request, jsonify

app = Flask(__name__)

# sample in-memory "database"
countries = [
    {"id": 1, "name": "Finland", "capital": "Helsinki"},
    {"id": 2, "name": "Sweden", "capital": "Stockholm"},
    {"id": 3, "name": "Norway", "capital": "Oslo"}
]

# GET ALL
@app.route("/countries", methods=["GET"])
def get_countries():
    return jsonify(countries)

# GET ONE
@app.route("/countries/<int:id>", methods=["GET"])
def get_country(id):
    for c in countries:
        if c["id"] == id:
            return jsonify(c)
    return jsonify({"message": "Not found"}), 404

# CREATE
@app.route("/countries", methods=["POST"])
def add_country():
    data = request.get_json()
    countries.append(data)
    return jsonify(data), 201

# UPDATE
@app.route("/countries/<int:id>", methods=["PUT"])
def update_country(id):
    data = request.get_json()
    for i, c in enumerate(countries):
        if c["id"] == id:
            countries[i] = data
            return jsonify(data)
    return jsonify({"message": "Not found"}), 404

# DELETE
@app.route("/countries/<int:id>", methods=["DELETE"])
def delete_country(id):
    for i, c in enumerate(countries):
        if c["id"] == id:
            deleted = countries.pop(i)
            return jsonify(deleted)
    return jsonify({"message": "Not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
