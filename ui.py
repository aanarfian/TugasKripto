from flask import Flask,jsonify, render_template, request, redirect, send_from_directory
import dec_shitt
import enc_shitt
import enc_substitution
import dec_substitution
import convertThings as con


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/", methods=['GET'])
def home():
    return render_template("index.html", is_home= 'yes')

@app.route("/Shift-Cipher-standard", methods=['POST', 'GET'])
def shittChipher():
    enk_shitt = ""
    dek_shitt = ""
    if request.method == "POST":
        key_enk = con.conint(request.form.get("key_enc"))
        key_dek = con.conint(request.form.get("key_dec"))
        text_enk = request.form.get("text_enc")
        text_dek = request.form.get("text_dec")
        if key_enk != -1:
            enk_shitt = enc_shitt.encrypt_shitt(text_enk, key_enk)
        if key_dek != -1:
            dek_shitt = dec_shitt.decrypt_shitt(text_dek, key_dek)
        return render_template("ShittCipherstandard.html", content=[enk_shitt, dek_shitt] , is_shift = 'yes')
    else:
        return render_template("ShittCipherstandard.html", content=[enk_shitt, dek_shitt], is_shift = 'yes')

@app.route("/Subtitution-Cipher-standard", methods=['POST', 'GET'])
def subsitution():
    enk_subsitution = ""
    dek_subsitution = ""
    if request.method == "POST":
        key_enk = con.constring(request.form.get("key_enc"))
        key_dek = con.constring(request.form.get("key_dec"))
        text_enk = request.form.get("text_enc")
        text_dek = request.form.get("text_dec")
        if key_enk != -1:
            enk_subsitution = enc_substitution.encrypt_subsitution(text_enk, key_enk)
        if key_dek != -1:
            dek_subsitution = dec_substitution.decrypt_subsitution(text_dek, key_dek)
        return render_template("Subtitutioncipherstandard.html", content=[enk_subsitution, dek_subsitution], is_substitution = 'yes')
    else:
        return render_template("Subtitutioncipherstandard.html", content=[enk_subsitution, dek_subsitution], is_substitution = 'yes')

if __name__ == "__name_-":
    app.run()
