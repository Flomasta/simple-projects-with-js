const search_button = document.getElementById('search-button')
const search_container = document.getElementById('search_container')
const input = document.querySelector('.input')
search_button.addEventListener('click', () => {
    search_container.classList.toggle('active')
    input.focus()
})
