let submit_button = document.getElementById('btn')


submit_button.addEventListener('click', (event_click=> {

    event_click.preventDefault()
    
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
    
    let url = 'http://127.0.0.1:8000/api/update_profile'

    let first_name = document.getElementById('fn_input').value
    let last_name = document.getElementById('ln_input').value
    let file = document.querySelector('#file_input')

    let send_data = new FormData()
    
    if(first_name){
        send_data.append('first_name', first_name)
    }

    if(last_name){
        send_data.append('last_name', last_name)
    }
    let image = file.files[0]
    
    if(image){
        send_data.append('avatar', image)
    }


    fetch(url, 
        {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrftoken
            },
            body: send_data
        }
        ).then(console.log('ok'))
        
    }))