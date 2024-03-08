from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user-recommendations/<user_id>")
def get_recommendations(user_id):
    return "hi"

if __name__ == "__main__":
    app.run(debug=True)