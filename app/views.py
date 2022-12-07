from app import app
from flask import (
    request,
    render_template,
    make_response,
    redirect,
    url_for,
    send_from_directory,
)
from flask import Response
from werkzeug.utils import secure_filename
import json
from processing import proc_data_lab1, proc_data_lab2
from laba1 import des
import processing
import os
import time
import random
import os

UPLOAD_FOLDER = f"{os.getcwd()}/Downloads"
ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif"])

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/lab1")
def lab1():
    return render_template("firstlab.html")


@app.route("/lab2")
def lab2():
    return render_template("secondlab.html")


@app.route("/lab3")
def lab3():
    return render_template("thirdlab.html")


@app.route("/project")
def project():
    return render_template("project.html")


@app.route("/echo-json", methods=["POST"])
def json_query():
    jsdata = request.get_json()
    print(jsdata)
    return jsdata


@app.route("/echo-progress")
def progress_query():
    processing.progress = 0

    def generate():

        while processing.progress < 100:
            yield "data:" + str(processing.progress) + "\n\n"
            # progress += 10
            time.sleep(0.5)
        # return 100 progress
        yield "data:" + str(processing.progress) + "\n\n"

    return Response(generate(), mimetype="text/event-stream")


# lab processing
# =====================


@app.route("/proc_lab1", methods=["POST"])
def proc_lab1():
    jsdata = request.get_json()
    lab = jsdata["lab"]
    res = ""

    if lab == "get_bit":
        res = proc_data_lab1.get_bit_proc(jsdata)

    elif lab == "change_bit":
        res = proc_data_lab1.change_bit_proc(jsdata)

    elif lab == "swap_bits":
        res = proc_data_lab1.swap_bits_proc(jsdata)

    elif lab == "zero_bits":
        res = proc_data_lab1.zero_bits_proc(jsdata)

    elif lab == "splice_bits":
        res = proc_data_lab1.splice_bits_proc(jsdata)

    elif lab == "middle_bits":
        res = proc_data_lab1.middle_bits_proc(jsdata)

    elif lab == "xor_all_bits":
        res = proc_data_lab1.xor_all_bits_proc(jsdata)

    elif lab == "within_range":
        res = proc_data_lab1.within_range_proc(jsdata)

    elif lab == "change_bits":
        res = proc_data_lab1.change_bits_proc(jsdata)

    elif lab == "cycle_shift_left":
        res = proc_data_lab1.cycle_shift_left_proc(jsdata)

    elif lab == "cycle_shift_right":
        res = proc_data_lab1.cycle_shift_right_proc(jsdata)

    return json.dumps({"result": res})


@app.route("/proc_lab2", methods=["POST"])
def proc_lab2():
    jsdata = request.get_json()
    lab = jsdata["lab"]
    res = ""

    if lab == "simple_numbers":
        res = proc_data_lab2.simple_numbers_proc(jsdata)

    elif lab == "ded_system":
        res = proc_data_lab2.ded_system_proc(jsdata)

    elif lab == "euler_function":
        res = proc_data_lab2.euler_function_proc(jsdata)

    elif lab == "decomposition":
        res = proc_data_lab2.decomposition_proc(jsdata)

    elif lab == "fast_pow_mod":
        res = proc_data_lab2.fast_pow_mod_proc(jsdata)

    elif lab == "euclid_alg":
        res = proc_data_lab2.euclid_alg_proc(jsdata)

    elif lab == "bin_euclid_alg":
        res = proc_data_lab2.bin_euclid_alg_proc(jsdata)

    return json.dumps({"result": res})


@app.route("/proc_lab3", methods=["POST"])
def proc_lab3():
    jsdata = request.get_json()
    lab = jsdata["lab"]

    res = ""
    if lab == "pol_form":
        res = proc_data_lab3.pol_form_proc(jsdata)

    elif lab == "bin_pol_form":
        res = proc_data_lab3.bin_pol_form_proc(jsdata)

    elif lab == "mult_inverse":
        res = proc_data_lab3.mult_inverse_proc(jsdata)

    return json.dumps({"result": res})


# Complex lab process
# =====================

# Check correct file


def get_extension(filename: str):
    #
    return os.path.splitext(filename)[1]


def create_uniqu_file_name():
    #
    filename = str(random.randint(0, 999999))
    while is_file_alive(filename):
        filename = str(random.randint(0, 999999))

    return filename


def is_file_alive(file_name):
    #
    path = app.config["UPLOAD_FOLDER"]
    # collect filename without extensions
    onlyfiles = [
        os.path.splitext(f)[0]
        for f in os.listdir(path)
        if os.path.isfile(os.path.join(path, f))
    ]

    if file_name in onlyfiles:
        return True
    return False


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in ALLOWED_EXTENSIONS


# Return file from server to client
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(
        app.config["UPLOAD_FOLDER"], filename, as_attachment=True
    )


def check_key(key: bytes):
    #
    if len(key) > 8:
        key = key[:8]
    elif len(key) < 8:
        key += bytes(8 - len(key))
    return key


@app.route("/des", methods=["POST"])
def des_proc():
    #
    mode = request.form.get("enc_dec_mode")
    check_ed = request.form.get("check_enc_dec")

    print("check_enc_dec", check_ed)
    print("enc_dec_mode", mode)

    key = request.form.get("first_data")
    c0 = request.form.get("second_data")

    if len(key) == 0:
        return json.dumps({"err": "Error: enter key!"})

    if len(c0) == 0 and mode != "ecb":
        return json.dumps({"err": "Error: enter c0!"})

    key = check_key(key)
    c0 = check_key(c0)

    datafile = request.files["datafile"]

    if not datafile:
        return json.dumps({"err": "Choose file"})

    if allowed_file(datafile.filename):
        filename = secure_filename(datafile.filename)
        data = datafile.read()
        des_ = des.DES(des.Mode._bytes_to_block(key.encode("utf-8")))

        if mode == "ecb":
            alg = des.ECB(des_)
        elif mode == "cbc":
            alg = des.CBC(des_, des.Mode._bytes_to_block(c0.encode("utf-8")))
        elif mode == "ofb":
            alg = des.OFB(des_, des.Mode._bytes_to_block(c0.encode("utf-8")))
        elif mode == "cfb":
            alg = des.CFB(des_, des.Mode._bytes_to_block(c0.encode("utf-8")))

        if check_ed == "dec":
            res = alg.decode(data)
            while res[-1] == 0:
                res = res[:-1]
        else:
            res = alg.encode(data)

        res_file_name = os.path.join(
            app.config["UPLOAD_FOLDER"], check_ed + "_" + filename
        )

        with open(res_file_name, "wb") as f:
            f.write(res)

        return json.dumps({"res": "/uploads/" + check_ed + "_" + filename})

    else:
        return json.dumps({"err": "Incorrect data file type"})


@app.route("/rsa", methods=["POST"])
def rsa():
    #
    # если нужно зашифровать
    if request.form.get("check_enc_dec") == "enc":
        datafile = request.files["datafile"]

        # если файл не выбран
        if not datafile:
            return json.dumps({"err": "Choose file"})

        # провека на корректное имя
        if allowed_file(datafile.filename):
            data_filename = secure_filename(datafile.filename)
            datafile.save(os.path.join(app.config["UPLOAD_FOLDER"], data_filename))
        else:
            return json.dumps({"err": "Incorrect data file type"})

        res_filename = "data_" + create_uniqu_file_name() + get_extension(data_filename)
        res_keyname = "rsa_key_" + create_uniqu_file_name() + ".txt"

        # выполняется шифрование
        path = app.config["UPLOAD_FOLDER"]
        proc_data_lab2.rsa_proc(
            os.path.join(path, data_filename),
            os.path.join(path, res_keyname),
            os.path.join(path, res_filename),
            "enc",
        )

        # пользователю вернется зашифрованный файл и ключ
        return json.dumps(
            {"res": ["/uploads/" + res_filename, "/uploads/" + res_keyname]}
        )

    # если нужно дешифровать
    else:
        datafile = request.files["datafile"]
        keyfile = request.files["keyfile"]

        if not datafile or not keyfile:
            return json.dumps({"err": "Choose file"})

        if allowed_file(datafile.filename):
            data_filename = secure_filename(datafile.filename)
            datafile.save(os.path.join(app.config["UPLOAD_FOLDER"], data_filename))
        else:
            return json.dumps({"err": "Incorrect data file type"})

        if allowed_file(keyfile.filename):
            key_filename = secure_filename(keyfile.filename)
            keyfile.save(os.path.join(app.config["UPLOAD_FOLDER"], key_filename))

        # дешефруется
        path = app.config["UPLOAD_FOLDER"]
        proc_data_lab2.rsa_proc(
            os.path.join(path, data_filename),
            os.path.join(path, key_filename),
            os.path.join(path, "dec_" + data_filename),
            "dec",
        )

        # пользователю вернется дешифрованный файл
        return json.dumps({"res": ["/uploads/" + "dec_" + data_filename]})
