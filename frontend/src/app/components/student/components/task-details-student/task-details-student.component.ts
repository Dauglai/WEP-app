import {ChangeDetectorRef, Component, OnInit} from '@angular/core';
import {TaskService} from "../../../../servicies/task.service";
import {QuestionService} from "../../../../servicies/question.service";
import {ActivatedRoute} from "@angular/router";
import {Subscription} from "rxjs";
import {GroupService} from "../../../../servicies/group.service";
import {StudentService} from "../../../../servicies/student.service";
import {FormControl, FormGroup, Validators} from "@angular/forms";

@Component({
  selector: 'app-task-details-student',
  templateUrl: './task-details-student.component.html',
  styleUrls: ['./task-details-student.component.css']
})
export class TaskDetailsStudentComponent implements OnInit{
  protected taskId: number = 0;
  protected task: any = {};
  protected questions: any = [];
  protected statistic: any = {};
  protected protagonist: any = {};
  protected hero: any = {};
  protected boss: any = {};

  public heroHP: number = 0;
  public bossHP: number = 0;

  protected serialNumberQuestion: number = 0;
  private routeSubscription: Subscription;

  constructor(private route: ActivatedRoute, private taskService: TaskService,
              private questionService: QuestionService, private groupService: GroupService,
              private studentService: StudentService) {
     this.routeSubscription = route.params.subscribe(params => {
      this.taskId = params['id'];
    });
  }
  ngOnInit() {
    this.getTask(this.taskId);
    this.getQuestions(this.taskId);
    this.getAccountStatistics();
    this.getProtagonist();
    console.log(this.hero)
  }

  public formChoice: number = 0;
  // protected myForm = new FormGroup({
  //   'formChoice': new FormControl(),
  // });

  sendAnswer(){
    console.log(this.questions[this.serialNumberQuestion].id);
    this.studentService.postChoice(this.questions[this.serialNumberQuestion].id, this.formChoice).subscribe(
      (data: any) => {
        console.log(data);
      }
    )
    console.log(this.questions[this.serialNumberQuestion].id, this.formChoice)
    this.serialNumberQuestion += 1;
  }

  getTask(id: number) {
    this.taskService.getTask(id).subscribe(
      (data: any) => {
        console.log(data)
        this.task = data;
        this.getBoss(data.boss);
      }
    )
  }

  getQuestions(id: number) {
    this.questionService.getQuestions(id).subscribe(
      (data: any) => {
        console.log(data)
        this.questions = data;
      }
    )
  }

  getAccountStatistics(): void {
    this.studentService.getAccountStatistics().subscribe(
      (data: any) => {
        console.log(data);
        this.statistic = data;
      }
    )
  }

  getProtagonist(): void {
    this.studentService.getProtagonist().subscribe(
      (data: any) => {
        console.log(data);
        this.protagonist = data;
        this.getHero(data.hero);
        this.heroHP = data.health;
      }
    )
  }

  getHero(id: number): void {
    this.studentService.getHero(id).subscribe(
      (data: any) => {
        console.log(data);
        this.hero = data;
      }
    )
  }

  getBoss(id: number) {
    this.studentService.getBoss(id).subscribe(
      (data: any) => {
        console.log(data);
        this.boss = data;
        this.bossHP = data.health;
      }
    )
  }
}
