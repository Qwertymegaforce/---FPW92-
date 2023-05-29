
let button = document.getElementById('sub_button')


button.addEventListener('click', (ev) => {

    ev.preventDefault()

    let first_name = document.getElementById('name').value
    let last_name = document.getElementById('surname').value

    let url = `http://127.0.0.1:8000/api/get_users/${first_name}/${last_name}`

    fetch(url)
        .then((resp) => resp.json())
        .then(function(data){buildUserlist(data)})

})


let buildUserlist = function(data){
    let wrapper = document.getElementById('container')

    wrapper.innerHTML = ''

    for(let i in data){
        let single_user = 
        `<div id="single_user_${i}" class="single_user">
        <img src="${data[i].avatar}" class="picture">
        <span class="name_surname"> ${data[i].first_name} ${data[i].last_name} </span>
        <button id="start_button_${i}"> В избранное </button>
        </div>` 

        wrapper.innerHTML += single_user
    }

    for(let i in data){
        let start_button = document.getElementById(`start_button_${i}`)

        start_button.addEventListener('click', (smth)=>{
            let url = `http://127.0.0.1:8000/api/to_friend_list/${data[i].id}`
            fetch(url)
            .then((resp) => {
                start_button.innerHTML = 'В списке'
                start_button.className = 'added'
                start_button.disabled = true
            })
        })

    }
}