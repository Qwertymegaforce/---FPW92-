let url = 'http://127.0.0.1:8000/api/get_friends'
let start_url = 'http://127.0.0.1:8000/'
let friends = new Array()
let create_url = 'http://127.0.0.1:8000/api/form_chat'
let send_data = new FormData()

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

fetch(url)
.then((resp) => resp.json())
.then(function(data){
    console.log(data);
    let wrapper = document.getElementById('container')



    wrapper.innerHTML = ''

    for(let i in data){
        let single_user = 
        `<div id="single_user" class="single_user">
        <img src="${data[i].avatar}" class="picture">
        <span class="name_surname"> ${data[i].first_name} ${data[i].last_name} </span>
        <button id="start_button_${i}"> В список </button>
        </div>` 

        wrapper.innerHTML += single_user
    }

for(let i in data){
    let start_button = document.getElementById(`start_button_${i}`)

    start_button.addEventListener('click', addButton)
    start_button.data = data
    start_button.i = i

}})

let addButton = function(event){
    console.log('click');
    this.innerHTML = 'В списке'
    this.className = 'added'
    user = event.currentTarget.data[event.currentTarget.i]
    friends.push(user)
    console.log(friends)
    this.removeEventListener('click', addButton)
    this.addEventListener('click', refreshButton)
    this.data = event.currentTarget.data
    this.i = event.currentTarget.i
}

let refreshButton = function(event){
    delete_item = friends.indexOf(event.currentTarget.data[event.currentTarget.i])
    friends.splice(delete_item, 1)
    console.log(friends);
    this.innerHTML = 'В список'
    this.className = null
    this.removeEventListener('click', refreshButton)
    this.addEventListener('click', addButton)
}


create_button = document.getElementById('create_button')


let sendList = function(){

    file = document.querySelector('#file_input')
    chat_name = document.getElementById('name_input').value
    
    send_data.append('name', chat_name)

    let image = file.files[0]
    
    if(image){
        send_data.append('image', image)
    }

    send_data.append('members', JSON.stringify(friends))

    for(var item of send_data.entries()){
        console.log(`${item[0]} ${item[1]}`);
    }
    
fetch(create_url, 
    {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
        body: send_data
    }
    ).then(window.location.href = start_url)
}

create_button.addEventListener('click', sendList)

