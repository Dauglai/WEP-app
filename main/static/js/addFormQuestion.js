let questionForm = document.getElementsByClassName("question-form");
let container = document.querySelector("#form-container");
let addButton = document.querySelector(".add-question");
let totalForms = document.querySelector("#id_form-TOTAL_FORMS");

let formNum = questionForm.length-1;
addButton.addEventListener('click', addForm);
initializeDeleteButtons();

function initializeDeleteButtons() {
    let deleteButtons = document.querySelectorAll('.del-question');
    deleteButtons.forEach( btn => {
        btn.addEventListener('click', deleteQuestion)
    });
}

function addForm() {
    let newForm = questionForm[0].cloneNode(true);
    let formRegex = RegExp(`form-(\\d){1}-`,'g');

    formNum++;
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`);
    newForm.querySelector('.question-number').innerHTML = formNum + 1;
    // recalculateQuestions();
    questionForm[questionForm.length - 1].after(newForm);
    totalForms.setAttribute('value', `${formNum+1}`);
    initializeDeleteButtons();
    recalculateQuestions();
};

function deleteQuestion() {
    this.parentNode.remove();
    recalculateQuestions();
}

function recalculateQuestions() {
    let questionNumberField = document.querySelectorAll(".question-number");
    let len = questionNumberField.length;
    console.log(len)
    for(let i=0; i < len + 1; i++) {
        questionNumberField[i].innerHTML = i + 1;
    }
}