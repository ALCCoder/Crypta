/* 

*/

var case_lab = 'simple_numbers'
var path = ''

// отправка на сервер
function communicate(lab, values_list) {

    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/proc_lab2");
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


function submit_rsa_click() {
    console.log('submit rsa');

    var form = new FormData(document.forms.lab_form);
    form.append('check_enc_dec', get_radio_value());

    const xhr = new XMLHttpRequest();

    xhr.open("POST", "http://127.0.0.1:5000/rsa");
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
            console.log(path)

            down_btn_ctr = document.getElementById('download_btn');
            down_btn_ctr.setAttribute("class", "btn")
            down_btn_ctr.hidden = false;
        }
    }
}

function get_radio_value() {
    var radio_enc = document.getElementById("radio_enc");
    if (radio_enc.checked) {
        return 'enc';
    }
    return 'dec';
}

// при переключении между режимами шифрования и дешифрования
function rsa_radio_click() {
    if (get_radio_value() == 'enc') {
        key_field = document.getElementById("key_field");
        key_field.hidden = true;
    }
    else {
        key_field = document.getElementById("key_field");
        key_field.hidden = false;
    }
    down_btn_ctr = document.getElementById('download_btn');
    down_btn_ctr.setAttribute("class", "btn download_btn")
    down_btn_ctr.hidden = false;
}

// функция для закачки файла
function download_file(path) {
    document.location.href = 'http://127.0.0.1:5000/' + path;
}

// функция для закачки файла
function download() {
    download_file(path[0])
    if (path.length > 1) {
        setTimeout(() => { download_file(path[1]); }, 1000);
    }
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


// ------Labs


// все простые числа меньше m
function simple_numbers() {
    case_lab = 'simple_numbers'
    set_active('simple_numbers')

    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">m</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}

function ded_system() {
    case_lab = 'ded_system'
    set_active('ded_system')

    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">m</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}

function euler_function() {
    case_lab = 'euler_function'
    set_active('euler_function')

    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">m</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}

function decomposition() {
    case_lab = 'decomposition'
    set_active('decomposition')

    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">m</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}

function fast_pow_mod() {
    case_lab = 'fast_pow_mod'
    set_active('fast_pow_mod')

    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">a</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="second_data" placeholder=" ">
            <label class="form__label">b</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="third_data" placeholder=" ">
            <label class="form__label">m</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}

function euclid_alg() {
    case_lab = 'euclid_alg'
    set_active('euclid_alg')

    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">a</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="second_data" placeholder=" ">
            <label class="form__label">b</label>
        </div>
        <div onclick="submit_click()" class="btn">SEND</div>
    </form>`;
}

function bin_euclid_alg() {
    case_lab = 'bin_euclid_alg'
    set_active('bin_euclid_alg')

    var form = document.getElementById("form");
    form.innerHTML = `
    <form class="lab__form" name="lab_form">
        <div class="from__title">Enter data</div>
        <div class="form__group">
            <input class="form__input" name="first_data" placeholder=" ">
            <label class="form__label">a</label>
        </div>
        <div class="form__group">
            <input class="form__input" name="second_data" placeholder=" ">
            <label class="form__label">b</label>
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

function rsa() {
    case_lab = 'rsa'
    set_active('rsa')

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
            <div id="key_field" hidden="true" style="padding: 10px 0px;">
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
        <p><input type="radio" name="enc_dec" onclick="rsa_radio_click()" id="radio_enc" checked>ENC <input type="radio" name="enc_dec" onclick="rsa_radio_click()" id="radio_dec">DEC</p>
        <div onclick="submit_rsa_click()" class="btn">SEND</div>
        <div onclick="download()" id="download_btn" class="btn download_btn">Download</div>
    </form>`;
    load_add_form();
}
