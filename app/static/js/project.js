var path = '';
var radio_mode = 'enc';
var des_mode = 'ecb';

function submit_mag_click() {
    console.log('submit mag')

    console.log('des_mode ' + des_mode);
    console.log('radio_mode ' + radio_mode);

    down_btn_ctr = document.getElementById('download_btn');
    down_btn_ctr.setAttribute("class", "btn download_btn")

    var form = new FormData(document.forms.lab_form);
    form.append('enc_dec_mode', des_mode);
    form.append('check_enc_dec', radio_mode);

    const xhr = new XMLHttpRequest();
    xhr.open("POST", "http://127.0.0.1:5000/magenta");
    xhr.send(form)

    // progress
    add_progress_bar();
    //!!!
    var source = new EventSource("/echo-progress");
    do_progress(source);

    xhr.onload = function () {
        console.log(xhr.response);

        // end progress
        del_progress_bar();
        // end message exchange
        source.close()

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

function do_progress(source) {
    source.onmessage = function (event) {
        console.log(event.data);

        var elem = document.getElementById("myBar");
        if (elem != undefined) {
            elem.style.width = event.data + "%";
            elem.innerHTML = event.data + "%";
        }

        if (event.data == 100) {
            console.log("close");
            source.close();
        }
    }
}

function add_progress_bar() {
    var answer = document.getElementById("answer");
    answer.innerHTML = `
    <div id="myProgress">
        <div id="myBar">10%</div>
    </div>
    `;
}

function del_progress_bar() {
    var answer = document.getElementById("answer");
    answer.innerHTML = '';
}

// функция для закачки файла
function download() {
    document.location.href = 'http://127.0.0.1:5000/' + path;
}

// убрать ответ с сервера
function delete_answer() {
    answer = document.getElementById('answer')
    answer.innerHTML = ''
}

function mag_modes_click(mode) {
    des_mode = mode;
    console.log('des_mode ' + des_mode);
}

function mag_radio_click(mode) {
    radio_mode = mode;
    console.log('radio_mode ' + radio_mode);
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