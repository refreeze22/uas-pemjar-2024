from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/', methods=['GET'])

def sample():
	data = {
		"status": 200,
		"message": "success"
	}
	return jsonify(data)

if __name__ == "__main__":
	port = 8000
	app.run("0.0.0.0", port)