let referrer = document.referrer;

const btnMain = document.querySelector('#btn-main');
btnMain.addEventListener('click', (el)=> {
    window.history.go(-1);
});