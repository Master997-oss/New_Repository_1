const popup = document.querySelector('.popup-js')
const btn = document.querySelector('.btn-js')
const closeBtn = document.querySelector('.btn__close-js')
const input = document.querySelector('.contact__form-input-js')

btn.addEventListener('click', function() {
    popup.classList.add('open')
    input.focus()
})

closeBtn.addEventListener('click', function() {
    popup.classList.remove('open')
})
