// Скрыть/показать пароль в форме ввода
function showPassword() {
    let el = document.getElementById("input-password");
    if (el.type === "text")
        el.type = "password";
    else if (el.type === "password")
        el.type = "text";
};


let countQuestions = 1;
let deadСountQuestions = 1;
let countAnswer = 1;
let deadСountAnswer = 1;

let btnAddAnswer = document.getElementsByClassName('add-answer');
let btnAddQuestion = document.querySelector('.add-question');

let question = document.querySelector('.question');
let quest = question.cloneNode(true);
let answers = document.getElementsByClassName('answer');

let seqNum = document.getElementsByClassName('sequence-number');

initializeBtnAnswer();
addQuestion();

function initializeBtnAnswer() {
    btnAddAnswer.item(btnAddAnswer.length - 1).addEventListener('click', (el)=> {
        let curEl = el.target; 
        let answerClone = answers.item(0).cloneNode(true);

        let textarea = curEl.parentNode.querySelector('textarea');
        let inputs = curEl.parentNode.querySelectorAll('input');
        let inputInAnswer = answerClone.querySelector('input');
        
        inputInAnswer.setAttribute('name', `${textarea.getAttribute('name')}_${inputs.length + 1}`);
        console.log(inputs)
        console.log(inputs[inputs.length - 1].getAttribute('name'));

        // console.log(answerClone);
        curEl.insertAdjacentElement('beforebegin', answerClone);
    });
}

function addQuestion() {
    btnAddQuestion.addEventListener('click', (el)=> {
        countQuestions ++;
        // deadСountQuestions ++;

        let curEl = el.target;
        let questionClone = createClone(quest);
        curEl.insertAdjacentElement('beforebegin', questionClone);
        initializeBtnAnswer();
        updateSeqNum();
    });
}

function createClone(el) {
    // let elClone = el.item(0).cloneNode(true);
    let elClone = el.cloneNode(true);
    let textarea = elClone.querySelector('textarea');
    textarea.setAttribute('name', countQuestions);
    console.log(textarea.getAttribute('name'));
    
    let input = elClone.querySelector('input');
    input.setAttribute('name', `${textarea.getAttribute('name')}_${1}`);
    // renumberAttribute(selecters);

    return elClone;
}

function updateSeqNum() {
    let len = seqNum.length;
    for(let i = 0; i < len; i++){
        seqNum[i].innerHTML = i + 1;
        // console.log(countBeverageы);
    }
}
