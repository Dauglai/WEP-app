import {Component, OnInit} from '@angular/core';
import {FormArray, FormBuilder, FormControl, FormGroup, Validators} from "@angular/forms";
import {StudentService} from "../../../../servicies/student.service";
import {GroupService} from "../../../../servicies/group.service";
import {TaskService} from "../../../../servicies/task.service";
import {QuestionService} from "../../../../servicies/question.service";
import {toNumbers} from "@angular/compiler-cli/src/version_helpers";
import {Router} from "@angular/router";

@Component({
  selector: 'app-task-constructor',
  templateUrl: './task-constructor.component.html',
  styleUrls: ['./task-constructor.component.css']
})
export class TaskConstructorComponent implements OnInit{
  protected bosses: any = [];
  private task: any = {};
  idTest: number = 0;
  lastQuestionId: number = 0;
  public groupSelect: FormControl = new FormControl();
  protected contactForm: FormGroup;
  protected groups: any = [];
  protected seqQuestions: number = 1;
  error ='';
  nextPage: boolean = false;
  userEmail = localStorage.getItem('user-email');
  userName = localStorage.getItem('user-full-name');

  constructor(private bossService: StudentService, private groupService: GroupService, private testService: TaskService,
              private _fb: FormBuilder,private questionService: QuestionService, private router: Router) {
    this.contactForm = this._fb.group({
      groupSelect: [null]
    });
  }

  ngOnInit() {
    this.getGroups();
    this.getBosses();
  }

  submitGroup() {
    console.log("Form Submitted")
    this.testFrom.value.group = this.contactForm.value.groupSelect;
    console.log(this.contactForm.value)
  }

  testFrom = new FormGroup({
    title: new FormControl('', [Validators.required]),
    subject: new FormControl('', [Validators.required]),
    group: new FormControl(null,  [Validators.required]),
    text: new FormControl('', [Validators.required]),

    difficulty: new FormControl('', [Validators.required]),
    boss: new FormControl(null,  [Validators.required]),
    time: new FormControl('00:15', [Validators.required]),
    time_deadline: new FormControl('', [Validators.required]),
    date_deadline: new FormControl('', [Validators.required]),

    number_attempts: new FormControl(1, [Validators.required]),
    five: new FormControl(null, [Validators.required]),
    four: new FormControl(null, [Validators.required]),
    three: new FormControl(null, [Validators.required]),
    two: new FormControl(null, [Validators.required]),
  })

  questionsForm = new FormGroup({
    question: new FormControl(''),
    first_answer: new FormControl(''),
    second_answer: new FormControl(''),
    third_answer: new FormControl(''),
    four_answer: new FormControl(''),
    reward: new FormControl(1),
    number_correct_answer: new FormControl(1),
    }
  )

  getGroups(): void {
    this.groupService.getGroups().subscribe(
      groups => {
        console.log(groups)
        this.groups = groups;
    });
  }

  getBosses() {
    this.bossService.getBosses().subscribe(
      (data: any) => {
        console.log(data);
        this.bosses = data;
      }
    )
  }

  saveTest(): void {
    this.task = this.testFrom.value;
    this.nextPage = true;
    console.log(this.groupSelect);
    const data = {
      group: this.contactForm.value.groupSelect,
      boss: this.task.boss,
      title: this.task.title,
      subject: this.task.subject,

      text: this.task.text,
      difficulty: this.task.difficulty,
      time: this.task.time,
      time_deadline: this.task.time_deadline,
      date_deadline: this.task.date_deadline,

      number_attempts: this.task.number_attempts,
      five: this.task.five,
      four: this.task.four,
      three: this.task.three,
      two: this.task.two
    }
    this.testService.createTask(data).subscribe(
      data => {
        console.log(data);
        this.idTest = data.id;
        console.log(this.idTest);
      },
      error => {
        console.log(error);
      }
    )
  }

  addQuestions() {
    this.questionsForm.reset();
    this.seqQuestions += 1;
  }

  deleteQuestions() {
    this.questionService.deleteQuestion({id: this.lastQuestionId }).subscribe(
      data => {
        console.log(data);
      },
      error => {
        console.log(error);
      }
    )
    if(this.seqQuestions > 1)
      this.seqQuestions -= 1;
  }

  saveQuestion() {
    const form = this.questionsForm.value;
    const data = {
      id: this.idTest,
      question: form.question,
      first_answer: form.first_answer,
      second_answer: form.second_answer,
      third_answer: form.third_answer,
      four_answer: form.four_answer,
      reward: form.reward,
      number_correct_answer: form.number_correct_answer,
    };
    this.questionService.createQuestion(data).subscribe(
      (data: any) => {
        console.log(data);
        this.lastQuestionId = + data.id;
        console.log(this.lastQuestionId);
      },
      error => {
        console.log(error);
      }
    )
  }

  returnTest(): void {
    // this.nextPage = false;
    // this.getGroups();
    // this.getBosses();
    this.router.navigate(['/teacher/task/list']);
  }

  convertDate(date: string): string {
    // год, месяц, день
    const dateArr = date.split('-');
    return `${dateArr[2]}.${dateArr[1]}.${dateArr[0]}`;
  }

  submit() {
    console.log(this.testFrom.value)
    console.log(this.userEmail);
    console.log(this.userName);
  }
}
