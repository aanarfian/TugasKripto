import array
import json
import math

from flask import Flask, render_template, request, redirect

from numpy.core.fromnumeric import reshape

import convertThings as con
import encryption.shift as shift
import encryption.substitution as substitution

from encryption.affine import Affine
from encryption.vigenere_ext import VigenereExt
import encryption.playfair as pf
import encryption.vigenere as vig
import encryption.hill as hillcipher


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

        bin_data = array.array("B", bytearray(data, "ASCII"))

        if is_encryption:
            output["type"] = "enc"
            output["result"] = VigenereExt.encrypt(bin_data, key)
        else:
            output["type"] = "dec"
            output["result"] = VigenereExt.decrypt(bin_data, key)

        output["as_str"] = ''.join([chr(i) for i in output["result"]])

    return render_template('vigenere_ext_cipher.html', output=json.dumps(output), is_ext_vignere = True)


@app.route("/Playfair-Cipher-standard", methods=['POST', 'GET'])
def playfair():
    enk_playfair = ""
    dek_playfair = ""
    if request.method == "POST":
        key_enk = con.constring(request.form.get("key_enc"))
        key_dek = con.constring(request.form.get("key_dec"))
        text_enk = request.form.get("text_enc")
        text_dek = request.form.get("text_dec")
        if key_enk != -1:
            enk_playfair = pf.encrypt_playfair(text_enk, key_enk)
        if key_dek != -1:
            dek_playfair = pf.decrypt_playfair(text_dek, key_dek)
        return render_template("Playfaircipherstandard.html", content=[enk_playfair, dek_playfair], is_playfair = 'yes')
    else:
        return render_template("Playfaircipherstandard.html", content=[enk_playfair, dek_playfair], is_playfair = 'yes')


@app.route("/Vignere-Cipher-standard", methods=['POST', 'GET'])
def vignere():
    enk_vignere = ""
    dek_vignere = ""
    if request.method == "POST":
        key_enk = con.constring(request.form.get("key_enc"))
        key_dek = con.constring(request.form.get("key_dec"))
        text_enk = request.form.get("text_enc")
        text_dek = request.form.get("text_dec")
        if key_enk != -1:
            enk_vignere = vig.encrypt_vigenere(text_enk, key_enk)
        if key_dek != -1:
            dek_vignere = vig.decrypt_vigenere(text_dek, key_dek)
        return render_template("Vignerecipherstandard.html", content=[enk_vignere, dek_vignere], is_vignere = 'yes')
    else:
        return render_template("Vignerecipherstandard.html", content=[enk_vignere, dek_vignere], is_vignere = 'yes')


@app.route("/Hill-Cipher-standard", methods=['POST', 'GET'])
def hill():
    enk_hill = ""
    dek_hill = ""
    if request.method == "POST":
        text_enk = request.form.get("text_enc")
        text_dek = request.form.get("text_dec")
        key_enk = con.constring(request.form.get("key_enc"))
        key_dek = con.constring(request.form.get("key_dec"))
        if key_enk != -1:
            arr = list(map(int, key_enk.split()))
            sqrt = math.sqrt(len(arr))
            arr2 = reshape(arr, (int(sqrt), int(sqrt)))
            enk_hill = hillcipher.encrypt_hill(text_enk, arr2)
        if key_dek != -1:
            arr0 = list(map(int, key_dek.split()))
            sqrt = math.sqrt(len(arr0))
            arr3 = reshape(arr0, (int(sqrt), int(sqrt)))
            dek_hill = hillcipher.decrypt_hill(text_dek, arr3)
        return render_template("Hillcipherstandard.html", content=[enk_hill, dek_hill], is_hill = 'yes')
    else:
        return render_template("Hillcipherstandard.html", content=[enk_hill, dek_hill], is_hill = 'yes')


if __name__ == "__name_-":
    app.run()
