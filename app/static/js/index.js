/* 

*/

var case_lab = 'get_bit';
var path = '';
var radio_mode = 'enc';
var des_mode = 'ecb';

// отправка на сервер
function communicate(lab, values_list) {
    // console.log(lab)
    // console.log(values_list)
    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/proc_lab1");
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
        values_list.push(document.forms.lab_form.third_data.value)
    }
    communicate(case_lab, values_list)
}

// Функция для обработки шифра Вернама
function submit_vernam_click() {
    console.log('submit vernam')

    var form = new FormData(document.forms.lab_form);

    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/vernam");
    xhr.send(form)

    var answer = document.getElementById("answer");
    answer.innerHTML = 'Wait...';

    xhr.onload = function () {
        console.log(xhr.response);
        var ans = JSON.parse(xhr.response)
        if (ans.err != undefined) {
            answer.innerHTML = ans.err
        }
        else {
            delete_answer()
            path = ans.res;
            down_btn_ctr = document.getElementById('download_btn');
            down_btn_ctr.setAttribute("class", "btn")
            down_btn_ctr.hidden = false;
        }
    }
}

function submit_rc4_click() {
    console.log('submit rc4')

    var form = new FormData(document.forms.lab_form);

    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/rc4");
    xhr.send(form)

    var answer = document.getElementById("answer");
    answer.innerHTML = 'Wait...';

    xhr.onload = function () {
        console.log(xhr.response);
        var ans = JSON.parse(xhr.response)
        if (ans.err != undefined) {
            answer.innerHTML = ans.err
        }
        else {
            delete_answer()
            path = ans.res;
            down_btn_ctr = document.getElementById('download_btn');
            down_btn_ctr.setAttribute("class", "btn")
            down_btn_ctr.hidden = false;
        }
    }
}

function submit_des_click() {
    console.log('submit des')

    console.log('des_mode ' + des_mode);
    console.log('radio_mode ' + radio_mode);

    var form = new FormData(document.forms.lab_form);
    form.append('enc_dec_mode', des_mode);
    form.append('check_enc_dec', radio_mode);

    // убираю кнопку скачать
    down_btn_ctr = document.getElementById('download_btn');
    down_btn_ctr.setAttribute("class", "btn download_btn")

    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/des");
    xhr.send(form)

    var answer = document.getElementById("answer");
    answer.innerHTML = 'Wait...';

    xhr.onload = function () {
        console.log(xhr.response);
        var ans = JSON.parse(xhr.response)
        if (ans.err != undefined) {
            answer.innerHTML = ans.err
        }
        else {
            delete_answer()
            path = ans.res;
            down_btn_ctr = document.getElementById('download_btn');
            down_btn_ctr.setAttribute("class", "btn")
            down_btn_ctr.hidden = false;
        }
    }
}

function des_modes_click(mode) {
    des_mode = mode;
    console.log('des_mode ' + des_mode);
}

function des_radio_click(mode) {
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

// получить k-ый бит
function get_bit() {
    // выбираю лабу
    case_lab = 'get_bit'
    // Делаю пункт меню актывным
    set_active('get_bit')
    // меняю форму
    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">Number (base 2)</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="second_data" placeholder=" ">
            <label class="form__label">Bit number</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}
// установить/снять k-ый бит
function change_bit() {
    // выбираю лабу
    case_lab = 'change_bit'
    // Делаю пункт меню актывным
    set_active('change_bit')
    // меняю форму
    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">Number (base 2)</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="second_data" placeholder=" ">
            <label class="form__label">Bit number</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}

// поменять местами i и j биты
function swap_bits() {
    // выбираю лабу
    case_lab = 'swap_bits'
    // Делаю пункт меню актывным
    set_active('swap_bits')
    // меняю форму
    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">Number (base 2)</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="second_data" placeholder=" ">
            <label class="form__label">Bit number i</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="third_data" placeholder=" ">
            <label class="form__label">Bit number j</label>
        </div>
        <div onclick="submit_click()" type="submit" class="btn">SEND</div>
    </form>`;
}
// обнулить младшие m бит
function zero_bits() {
    // выбираю лабу
    case_lab = 'zero_bits'
    // Делаю пункт меню актывным
    set_active('zero_bits')
    // меняю форму
    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">Number (base 2)</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="second_data" placeholder=" ">
            <label class="form__label">Bit count</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}
// «Склеить» первые 𝑖 битов с последними 𝑖 битами из 
// целого числа длиной 𝑙𝑒𝑛 битов
function splice_bits() {
    // выбираю лабу
    case_lab = 'splice_bits'
    // Делаю пункт меню актывным
    set_active('splice_bits')
    // меняю форму
    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">Number (base 2)</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="second_data" placeholder=" ">
            <label class="form__label">i bits</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}
// Получить биты из целого числа длиной 𝑙𝑒𝑛 битов, 
// находящиеся между первыми 𝑖 битами и последними 𝑖 битами
function middle_bits() {
    // выбираю лабу
    case_lab = 'middle_bits'
    // Делаю пункт меню актывным
    set_active('middle_bits')
    // меняю форму
    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">Number (base 2)</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="second_data" placeholder=" ">
            <label class="form__label">i bits</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}
// поменять байты местами с заданной перестановкой
function change_bytes() {
    // выбираю лабу
    case_lab = 'change_bytes'
    // Делаю пункт меню актывным
    set_active('change_bytes')
    // меняю форму
    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">Number (base 2)</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="second_data" placeholder=" ">
            <label class="form__label">Rearranging</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}

// Максимальная степень двойки
function max_pow() {
    // выбираю лабу
    case_lab = 'max_pow'
    // Делаю пункт меню актывным
    set_active('max_pow')
    // меняю форму
    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">Number (base 10)</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}
// 
function within_range() {
    // выбираю лабу
    case_lab = 'within_range'
    // Делаю пункт меню актывным
    set_active('within_range')
    // меняю форму
    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">Number (base 10)</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}

function xor_all_bits() {
    // выбираю лабу
    case_lab = 'xor_all_bits'
    // Делаю пункт меню актывным
    set_active('xor_all_bits')
    // меняю форму
    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">Number (base 2)</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}

function change_bits() {
    // выбираю лабу
    case_lab = 'change_bits'
    // Делаю пункт меню актывным
    set_active('change_bits')
    // меняю форму
    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">Number (base 2)</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="second_data" placeholder=" ">
            <label class="form__label">Rearranging</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}

function cycle_shift_left() {
    // выбираю лабу
    case_lab = 'cycle_shift_left'
    // Делаю пункт меню актывным
    set_active('cycle_shift_left')
    // меняю форму
    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">Number (base 2)</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="second_data" placeholder=" ">
            <label class="form__label">n</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="third_data" placeholder=" ">
            <label class="form__label">p</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}

function cycle_shift_right() {
    // выбираю лабу
    case_lab = 'cycle_shift_right'
    // Делаю пункт меню актывным
    set_active('cycle_shift_right')
    // меняю форму
    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">Number (base 2)</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="second_data" placeholder=" ">
            <label class="form__label">n</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="third_data" placeholder=" ">
            <label class="form__label">p</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}

function load_add_form() {

    let inputs = document.querySelectorAll('.input__file');
    Array.prototype.forEach.call(inputs, function (input) {
        let label = input.nextElementSibling;
        let labelVal = label.querySelector('.input__file-button-text').innerText;

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

function vernam() {
    case_lab = 'vernam'
    // Делаю пункт меню актывным
    set_active('vernam');
    // меняю форму
    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div style="padding: 0px 0px 20px 0px;">
            <div style="padding: 10px 0px;">
                <div class="name__field">
                    data
                </div>
                <div class="input__wrapper">
                    <input name="datafile" id="input_data_file" type="file" class="input input__file">
                    <label for="input_data_file" class="input__file-button">
                        <span class="input__file-icon-wrapper"><img class="input__file-icon" src= "static/img/add.svg" alt="Выбрать файл" width="25"></span>
                        <span class="input__file-button-text" id="data_label">Выберите файл</span>
                    </label>
                </div>
            </div>
            <div style="padding: 10px 0px;">
                <div class="name__field">
                    key
                </div>
                <div class="input__wrapper">
                    <input name="keyfile" id="input_key_file" type="file" class="input input__file">
                    <label for="input_key_file" class="input__file-button">
                        <span class="input__file-icon-wrapper"><img class="input__file-icon" src= "static/img/add.svg" alt="Выбрать файл" width="25"></span>
                        <span class="input__file-button-text" id="key_label">Выберите файл</span>
                    </label>
                </div>
            </div>
        </div>
        <div onclick="submit_vernam_click()" class="btn">Send</div>
        <div onclick="download()" id="download_btn" class="btn download_btn">Download</div>
    </form>`;
    load_add_form();
}


function des() {
    case_lab = 'des';
    // Делаю пункт меню актывным
    set_active('des');
    // меняю форму
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
                <span class="input__file-icon-wrapper"><img class="input__file-icon" src= "static/img/add.svg" alt="Выбрать файл" width="25"></span>
                <span class="input__file-button-text" id="data_label">Выберите файл</span>
            </label>
        </div>

        <p>
        <input type="radio" name="enc_dec_modes" onclick="des_modes_click('ecb')" checked>ECB
        <input type="radio" name="enc_dec_modes" onclick="des_modes_click('cbc')">CBC
        <input type="radio" name="enc_dec_modes" onclick="des_modes_click('cfb')">CFB
        <input type="radio" name="enc_dec_modes" onclick="des_modes_click('ofb')">OFB
        </p>

        <p>
        <input type="radio" name="enc_dec" onclick="des_radio_click('enc')" id="radio_enc" checked>ENC 
        <input type="radio" name="enc_dec" onclick="des_radio_click('dec')" id="radio_dec">DEC
        </p>

        <div onclick="submit_des_click()" class="btn">Send</div>
        <div onclick="download()" id="download_btn" class="btn download_btn">Download</div>
    </form>`;
    load_add_form();
}

function rc4() {
    case_lab = 'rc4';
    // Делаю пункт меню актывным
    set_active('rc4');
    // меняю форму
    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div style="padding: 0px 0px 20px 0px;">
            <div style="padding: 10px 0px;">
                <div class="name__field">
                    data
                </div>
                <div class="input__wrapper">
                    <input name="datafile" id="input_data_file" type="file" class="input input__file">
                    <label for="input_data_file" class="input__file-button">
                        <span class="input__file-icon-wrapper"><img class="input__file-icon" src= "static/img/add.svg" alt="Выбрать файл" width="25"></span>
                        <span class="input__file-button-text" id="data_label">Выберите файл</span>
                    </label>
                </div>
            </div>
            <div style="padding: 10px 0px;">
                <div class="name__field">
                    key
                </div>
                <div class="input__wrapper">
                    <input name="keyfile" id="input_key_file" type="file" class="input input__file">
                    <label for="input_key_file" class="input__file-button">
                        <span class="input__file-icon-wrapper"><img class="input__file-icon" src= "static/img/add.svg" alt="Выбрать файл" width="25"></span>
                        <span class="input__file-button-text" id="key_label">Выберите файл</span>
                    </label>
                </div>
            </div>
        </div>
        <div onclick="submit_rc4_click()" class="btn">SEND</div>
        <div onclick="download()" id="download_btn" class="btn download_btn">Download</div>
    </form>`;
    load_add_form();
}