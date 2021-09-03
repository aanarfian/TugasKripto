from flask import Flask,jsonify, render_template, request, redirect, send_from_directory
import dec_shitt
import enc_shitt

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/", methods=['POST', 'GET'])
def home():
	enk_shitt = ""
	dek_shitt = ""
	if request.method == "POST":
		key = int(request.form["key"])
		print(type(key))
		print(key)
		plaintext = request.form["plaintext"]
		enk_shitt = enc_shitt.encrypt_shitt(plaintext, key)
		dek_shitt = dec_shitt.decrypt_shitt(enk_shitt, key)

	return render_template("index.html", content=[enk_shitt, dek_shitt])

if __name__ == "__name_-":
	app.run()
