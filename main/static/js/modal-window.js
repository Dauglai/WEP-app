addEventBtnSubmit();

function addEventBtnSubmit() {
    let btnSubmit = document.querySelector('.add-new-group');
    let modalWindow = document.querySelector('.modal-window');
    let overlay = document.querySelector('.modal-overlay');
    let closeButton = document.querySelector('.close-modal-window');

    btnSubmit.addEventListener('click', ()=> {
        console.log(1)
        let display = modalWindow.style.display;
        modalWindow.style.display = 'block';

        // Пока отключил overlay
        overlay.style.display = 'block';

        document.body.style.overflowY = 'hidden';
        console.log(getScrollBarWidth());
        document.body.style.paddingRight = `${getScrollBarWidth()}px`;
    });

    closeButton.addEventListener('click', ()=> {
        console.log(2)
        modalWindow.style.display = 'none';
        overlay.style.display = 'none';
        document.body.style.overflow = 'visible';
        document.body.style.paddingRight = '0';
    })
}

function getScrollBarWidth () {
    var inner = document.createElement('p');
    inner.style.width = "100%";
    inner.style.height = "200px";
  
    var outer = document.createElement('div');
    outer.style.position = "absolute";
    outer.style.top = "0px";
    outer.style.left = "0px";
    outer.style.visibility = "hidden";
    outer.style.width = "200px";
    outer.style.height = "150px";
    outer.style.overflow = "hidden";
    outer.appendChild (inner);
  
    document.body.appendChild (outer);
    var w1 = inner.offsetWidth;
    outer.style.overflow = 'scroll';
    var w2 = inner.offsetWidth;
    if (w1 == w2) w2 = outer.clientWidth;
  
    document.body.removeChild (outer);
  
    return (w1 - w2);
  };