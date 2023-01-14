let questionForm = document.getElementsByClassName("question-form");
let container = document.querySelector("#form-container");
let questionNumberField = document.getElementsByClassName("question-number");
let addButton = document.querySelector(".add-question");
let totalForms = document.querySelector("#id_form-TOTAL_FORMS");

let formNum = questionForm.length-1;
addButton.addEventListener('click', addForm);

function addForm(e) {
    e.preventDefault();

    let newForm = questionForm[0].cloneNode(true);
    let formRegex = RegExp(`form-(\\d){1}-`,'g');

    formNum++;
    console.log(formNum);
    newForm.innerHTML = newForm.innerHTML.replace(formRegex, `form-${formNum}-`);
    newForm.querySelector('.question-number').innerHTML = formNum + 1;
    questionForm[questionForm.length - 1].after(newForm);
    totalForms.setAttribute('value', `${formNum+1}`);
};

function recalculateQuestions() {
    let len = questionNumberField.length;
    console.log(len)
    for(let i=0; i < len; i++) {
        questionNumberField[i].insertAdjacentText = i;
    }
}