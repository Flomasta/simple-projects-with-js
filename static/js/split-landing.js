const left = document.querySelector('.left')
const right = document.querySelector('.right')
const landing_container = document.querySelector('.container--split-landing')

left.addEventListener('mouseenter', () => landing_container.classList.add('hover-left')
)
left.addEventListener('mouseleave', () => landing_container.classList.remove('hover-left')
)


right.addEventListener('mouseenter', () => landing_container.classList.add('hover-right')
)
right.addEventListener('mouseleave', () => landing_container.classList.remove('hover-right')
)
