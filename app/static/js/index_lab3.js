/* 

*/

var case_lab = 'pol_form'
var path = ''
var radio_mode = 'enc';
var des_mode = 'ecb';
var block_len = '16';

// отправка на сервер
function communicate(lab, values_list) {
    // console.log(lab)
    // console.log(values_list)
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/proc_lab3");
    let serverData = {
        lab: lab,
        values_list: values_list
    };
    // convert to json
    xhrMessage = JSON.stringify(serverData);
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(xhrMessage);
    xhr.onload = function () {
        //
        console.log(xhr.response);
        // convert ot object
        var res = JSON.parse(xhr.response)
        var answer = document.getElementById("answer");
        answer.innerHTML = 'Answer: ' + res.result;
    }
}

// Собирает информцию с формы и готовит 
// к отправке на сервер
function submit_click() {
    var values_list = []

    values_list.push(document.forms.lab_form.first_data.value);

    if (document.forms.lab_form.second_data != undefined) {
        values_list.push(document.forms.lab_form.second_data.value);
    }
    if (document.forms.lab_form.third_data != undefined) {
        values_list.push(document.forms.lab_form.third_data.value);
    }
    communicate(case_lab, values_list);
}

function submit_rijndael_click() {
    console.log('submit rijndael');

    delete_answer();

    console.log('des_mode ' + des_mode);
    console.log('radio_mode ' + radio_mode);
    console.log('block_len ' + block_len);

    down_btn_ctr = document.getElementById('download_btn');
    down_btn_ctr.setAttribute("class", "btn download_btn")

    var form = new FormData(document.forms.lab_form);
    form.append('enc_dec_mode', des_mode);
    form.append('check_enc_dec', radio_mode);
    form.append('len', block_len);

    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/rijndael");
    xhr.send(form)

    xhr.onload = function () {
        console.log(xhr.response);

        var ans = JSON.parse(xhr.response)
        if (ans.err != undefined) {
            answer.innerHTML = ans.err
        }
        else {
            path = ans.res;
            down_btn_ctr = document.getElementById('download_btn');
            down_btn_ctr.setAttribute("class", "btn")
        }
    }
}

function block_len_click(len) {
    block_len = len;
    console.log('block_len ' + block_len);
}

function rij_modes_click(mode) {
    des_mode = mode;
    console.log('des_mode ' + des_mode);
}

function rij_radio_click(mode) {
    radio_mode = mode;
    console.log('radio_mode ' + radio_mode);
}

// функция для закачки файла
function download() {
    document.location.href = 'http://127.0.0.1:5000/' + path;
}

// Чтобы убрать class "active"
function delete_active() {
    var elements = document.getElementsByClassName("nav__element")
    for (var i = 0; i < elements.length; ++i) {
        elements[i].classList.remove('active');
    }
}

// убрать ответ с сервера
function delete_answer() {
    answer = document.getElementById('answer')
    answer.innerHTML = ''
}

// Делает пункт меню активным
function set_active(id_str) {
    console.log(id_str);
    // set active
    delete_active();
    var ref_element = document.getElementById(id_str);
    ref_element.setAttribute('class', 'nav__element active');
    // delete answer
    delete_answer()
}

// -----Labs

// представляет элемент из gf 256 в полиномиальной форме
function pol_form() {
    case_lab = 'pol_form'
    set_active('pol_form')

    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">Number (base 2 GF256)</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}

// умножает два двоичных многочлена
function bin_pol_form() {
    case_lab = 'bin_pol_form'
    set_active('bin_pol_form')

    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">Number (base 2 GF256)</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="second_data" placeholder=" ">
            <label class="form__label">Number (base 2 GF256)</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}

// поиск мультипликативного обратного для элемента из gf 256
function mult_inverse() {
    case_lab = 'mult_inverse'
    set_active('mult_inverse')

    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">Number (base 2 GF256)</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}

function load_add_form() {

    let inputs = document.querySelectorAll('.input__file');
    Array.prototype.forEach.call(inputs, function (input) {
        let label = input.nextElementSibling;
        let labelVal = label.querySelector('.input__file-button-text').innerText;

        // console.log(labelVal.innerText)

        input.addEventListener('change', function (e) {
            let countFiles = '';
            if (this.files && this.files.length >= 1)
                countFiles = this.files.length;

            if (countFiles)
                label.querySelector('.input__file-button-text').innerText = this.files[0].name;
            else
                label.querySelector('.input__file-button-text').innerText = labelVal;
        });
    });
}

// алгоритм шифрования rijndael
function rijndael() {
    case_lab = 'rijndael'
    set_active('rijndael')

    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">KEY</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="second_data" placeholder=" ">
            <label class="form__label">C0</label>
        </div>
        <div class="input__wrapper">
            <input name="datafile" id="input_data_file" type="file" class="input input__file">
            <label for="input_data_file" class="input__file-button">
                <span class="input__file-icon-wrapper"><img class="input__file-icon"
                        src="static/img/add.svg" alt="Выбрать файл" width="25"></span>
                <span class="input__file-button-text" id="data_label">Выберите файл</span>
            </label>
        </div>
        <p>
            <input type="radio" name="block_len" onclick="block_len_click('16')" checked>16
            <input type="radio" name="block_len" onclick="block_len_click('24')">24
            <input type="radio" name="block_len" onclick="block_len_click('32')">32
        </p>
        <p>
            <input type="radio" name="enc_dec_modes" onclick="rij_modes_click('ecb')" checked>ECB
            <input type="radio" name="enc_dec_modes" onclick="rij_modes_click('cbc')">CBC
            <input type="radio" name="enc_dec_modes" onclick="rij_modes_click('cfb')">CFB
            <input type="radio" name="enc_dec_modes" onclick="rij_modes_click('ofb')">OFB
        </p>
        <p>
            <input type="radio" name="enc_dec" onclick="rij_radio_click('enc')" id="radio_enc" checked>ENC
            <input type="radio" name="enc_dec" onclick="rij_radio_click('dec')" id="radio_dec">DEC
        </p>

        <div onclick="submit_rijndael_click()" class="btn">Send</div>
        <div onclick="download()" id="download_btn" class="btn download_btn">Download</div>
    </form>`;
    load_add_form();
}