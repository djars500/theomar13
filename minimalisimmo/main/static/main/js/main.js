
const btn = document.querySelector('#btnSCheme');
const theme = document.querySelector('.gg');

const logo = document.querySelectorAll('.logo');
const logoCircle = document.querySelectorAll('.logo__circle');
const logoH = document.querySelectorAll('.logo__h');



if (!localStorage.theme) localStorage.theme = "";
if(!localStorage.color) localStorage.color = '';

theme.className = localStorage.theme;
logo.forEach((item) => {
    item.style.fill = localStorage.color;
});
logoH.forEach((item) => {
    item.style.fill = localStorage.color;
});
logoH.forEach((item) => {
    item.style.stroke = localStorage.color;
});
logoCircle.forEach((item) => {
    item.style.stroke = localStorage.color;
});

//logoH.style.fill = localStorage.color;
//logoH.style.stroke = localStorage.color;
//logoCircle.style.stroke = localStorage.color;


btn.addEventListener('click', () =>{
    if(theme.classList.contains('light-theme') & theme.classList.contains('gg') ){
        theme.className = 'dark-theme';
        logo.forEach(item =>{
            item.style.fill = 'white';
        });
        logoH.forEach((item) => {
            item.style.fill = 'white';
        });
        logoH.forEach((item) => {
            item.style.stroke = 'white';
        });
        logoCircle.forEach((item) => {
            item.style.stroke = 'white';
        });
//        logoH.style.fill = 'white';
//        logoCircle.style.stroke = 'white';
        localStorage.color = 'white';
        localStorage.theme = theme.className;
        claudio.play();
    }
    else{
        theme.className = 'light-theme';
         logo.forEach(item =>{
            item.style.fill = 'black';
        });
        logoH.forEach((item) => {
            item.style.fill = 'black';
        });
        logoH.forEach((item) => {
            item.style.stroke = 'black';
        });
        logoCircle.forEach((item) => {
            item.style.stroke = 'black';
        });
//        logoH.style.fill = 'black';
//        logoCircle.style.stroke = 'black';
        localStorage.color = 'black';
        localStorage.theme = theme.className;
        claudio.play();
    }
});