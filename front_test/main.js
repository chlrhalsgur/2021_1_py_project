const toggleBtn = document.querySelector('.navbar__toogleBtn')
const menu = document.querySelector('.navbar__menu')
const icons = document.querySelector('.navbar__icons')

//버튼이 클릭될 때마다 함수 호출
toggleBtn.addEventListener('click', () => {
    //active class를 토글링 한다.
    //active가 없다면 해주고 있다면 빼준다.
    menu.classList.toggle('active')
    icons.classList.toggle('active')
});

