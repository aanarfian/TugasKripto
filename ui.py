import array
import json

from flask import Flask, render_template, request, redirect

import convertThings as con
import encryption.shift as shift
import encryption.substitution as substitution

from encryption.affine import Affine
from encryption.vigenere_ext import VigenereExt


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
            enk_shitt = shift.encrypt_shitt(text_enk, key_enk)
        if key_dek != -1:
            dek_shitt = shift.decrypt_shitt(text_dek, key_dek)
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
            enk_subsitution = substitution.encrypt_subsitution(text_enk, key_enk)
        if key_dek != -1:
            dek_subsitution = substitution.decrypt_subsitution(text_dek, key_dek)
        return render_template("Subtitutioncipherstandard.html", content=[enk_subsitution, dek_subsitution], is_substitution = 'yes')
    else:
        return render_template("Subtitutioncipherstandard.html", content=[enk_subsitution, dek_subsitution], is_substitution = 'yes')


@app.route("/Affine-Cipher-standard", methods=['POST', 'GET'])
def affine():
    enk_affine = ""
    dek_affine = ""
    if request.method == "POST":
        key_enk_a = con.conint(request.form.get("key_enc_a"))
        key_enk_b = con.conint(request.form.get("key_enc_b"))
        key_dek_a = con.conint(request.form.get("key_dec_a"))
        key_dek_b = con.conint(request.form.get("key_dec_b"))
        text_enk = request.form.get("text_enc")
        text_dek = request.form.get("text_dec")
        if key_enk_a != -1 and key_enk_b != -1:
            enk_affine = Affine.encrypt(text_enk, key_enk_a, key_enk_b)
        if key_dek_a != -1 and key_dek_b != -1:
            dek_affine = Affine.decrypt(text_dek, key_dek_a, key_dek_b)
        return render_template("affinechipherstandard.html", content=[enk_affine, dek_affine], is_affine = 'yes')
    else:
        return render_template("affinechipherstandard.html", content=[enk_affine, dek_affine], is_affine = 'yes')


@app.route("/vigenere-ext-cipher", methods=['POST', 'GET'])
def vigenere_ext():
    output = {}

    if request.method == "POST":
        data = request.form.get("data")
        key = request.form.get("key")
        is_encryption = request.args.get("type") == "enc"

        if is_encryption:
            bin_data = array.array("B", bytearray(data, "ASCII"))
            output["type"] = "enc"
            output["result"] = VigenereExt.encrypt(bin_data, key)
            output["as_str"] = ''.join([chr(i) for i in output["result"]])

    return render_template('vigenere_ext_cipher.html', output=json.dumps(output))


if __name__ == "__name_-":
    app.run()
