let referrer = document.referrer;

const btnMain = document.querySelector('#btn-back');
btnMain.addEventListener('click', (el)=> {
    window.history.go(-1);
});