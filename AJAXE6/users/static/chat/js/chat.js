let chat_id = JSON.parse(document.getElementById('room-id').textContent)

let socket = new WebSocket(`ws://${window.location.host}/ws/chat/${chat_id}/`)

let message_button = document.getElementById('message_button')

let message_div = document.getElementById('all_message_div')



socket.onopen = function(e){
    console.log('Соединение установлено')
    socket.send(JSON.stringify({
        'command': 'load',
        'chat_id': chat_id,
    }))
}


socket.onmessage = function(e){
    data = JSON.parse(e.data)
    console.log(`Получены данные с сервера ${data.message}`);
    for(let item of data.message){
        let html_item = `
        
    <div class="${item.by_request_user ? 'div_message_user' : 'div_message'}">

        <div class="div_message_text">
            ${item.message}
        </div>

        <div class="div_image">
            <img src='${item.image}'>
        </div>

    </div>
        `

        message_div.innerHTML += html_item
    }
}


let sendMessage = function(e){
    let text_message = document.getElementById('message_input').value
    let message = {
        'command': 'send',
        'chat_id': chat_id,
        'message': text_message
    }

    socket.send(JSON.stringify(message))
}

message_button.addEventListener('click', sendMessage)

