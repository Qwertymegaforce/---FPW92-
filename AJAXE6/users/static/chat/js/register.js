let button = document.getElementById('button_sub')

button.addEventListener('click', (e) => {
    e.preventDefault()


let username = document.getElementById('username').value
let first_name = document.getElementById('first_name').value
let last_name = document.getElementById('last_name').value
let first_avatar = document.querySelector('#avatar')
let password = document.getElementById('password').value
let password_confirm = document.getElementById('password2').value
let email = document.getElementById('email').value
div_form = document.getElementById('div_form')


if(!password){
    let password_field = document.getElementById('password')
        let p = document.createElement('p');
        p.className = "alert";
        p.id
        p.innerHTML = "Поле с паролем осталось пустым!"
        password_field.insertAdjacentElement('afterend', p)
}
else if(!password_confirm){
    let password_c_field = document.getElementById('password2')
        let p = document.createElement('p');
        p.className = "alert";
        p.innerHTML = "Вы не подтвердили пароль!"
        password_c_field.insertAdjacentElement('afterend', p)
}
else if(password_confirm != password){
    let password_c_field = document.getElementById('password2')
        let p = document.createElement('p');
        p.className = "alert";
        p.innerHTML = "Пароли не совпадают!"
        password_c_field.insertAdjacentElement('afterend', p)
}
else{


    function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


const csrftoken = getCookie('csrftoken');

let url = '/api/create_user'

let image = first_avatar.files[0]

let form_data = new FormData()
form_data.append('username', username)
form_data.append('first_name', first_name)
form_data.append('last_name', last_name)

if(image){
    form_data.append('avatar', image)
}

form_data.append('password', password)
form_data.append('email', email)


fetch(url, 
    {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
        body: form_data
    }
    ).then((res) => {
        if (res.status >= 200 && res.status < 300) {
            window.location.href = 'http://127.0.0.1:8000/'
        } else {
            let error = new Error(res.statusText);
            error.response = res;
            throw error
        }
    }).catch(err => {
        let username_field = document.getElementById('username')
        let p = document.createElement('p');
        p.className = "alert";
        p.innerHTML = "Пользователь с этим 'username' уже существует."
        username_field.insertAdjacentElement('afterend', p)
    })}

},

)
