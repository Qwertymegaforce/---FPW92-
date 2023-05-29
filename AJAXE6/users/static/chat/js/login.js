let button = document.getElementById('button_sub')

button.addEventListener('click', (e) => {
    e.preventDefault()


let username = document.getElementById('username').value
let password = document.getElementById('password').value

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
};


const csrftoken = getCookie('csrftoken');

let url = '/api/login_user';

let data ={
    'username': username,
    'password': password,
}


console.log(data);

fetch(url, 
    {
        method: 'POST',
        headers: {
            'Content-type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify(data)
    }
    )
    .then(res => {
        if (res.status >= 200 && res.status < 300) {
            window.location.href = 'http://127.0.0.1:8000/'
        } else {
            let error = new Error(res.statusText);
            error.response = res;
            throw error
        }
    }).catch(err => {
        let username_field = document.getElementById('password')
        let p = document.createElement('p');
        p.className = "alert";
        p.innerHTML = "Нет пользователя с таким логином и паролем."
        username_field.insertAdjacentElement('afterend', p)
    })

})



