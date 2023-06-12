import {ChangeDetectorRef, Component, OnInit} from '@angular/core';
import {TaskService} from "../../../../servicies/task.service";
import {QuestionService} from "../../../../servicies/question.service";
import {ActivatedRoute, Router} from "@angular/router";
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

  protected countCorrect: number = 0;
  protected countPoints: number = 0;

  protected serialNumberQuestion: number = 0;
  private routeSubscription: Subscription;

  constructor(private route: ActivatedRoute, private router1: Router, private taskService: TaskService,
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
    this.studentService.postChoice(this.questions[this.serialNumberQuestion].id, this.formChoice).subscribe(
      (data: any) => {
        console.log(data);
      }
    )
    const question = this.questions[this.serialNumberQuestion];

    const hero = this.protagonist;
    const boss = this.boss;
    // console.log(question.number_correct_answer, this.formChoice);
    if(question.number_correct_answer == this.formChoice) {
      this.countCorrect += 1;
      this.countPoints += question.reward;
      // console.log(hero.power + hero.endurance * 0.5);
      this.bossHP -=
        Math.round((this.protagonist.health / this.questions.length) + hero.power * hero.endurance - boss.resistance);
      // console.log(this.bossHP);
    }
    else {
      this.heroHP -= Math.round((this.boss.health / this.questions.length) + (boss.power + boss.resistance) * question.reward);
      // console.log(this.heroHP);
    }
    this.serialNumberQuestion += 1;
  }

  getTask(id: number) {
    this.taskService.getTask(id).subscribe(
      (data: any) => {
        // console.log(data)
        this.task = data;
        this.getBoss(data.boss);
        // console.log(data.id)
      }
    )
  }

  getQuestions(id: number) {
    this.questionService.getQuestions(id).subscribe(
      (data: any) => {
        // console.log(data)
        this.questions = data;
      }
    )
  }

  getAccountStatistics(): void {
    this.studentService.getAccountStatistics().subscribe(
      (data: any) => {
        // console.log(data);
        this.statistic = data;
      }
    )
  }

  getProtagonist(): void {
    this.studentService.getProtagonist().subscribe(
      (data: any) => {
        // console.log(data);
        this.protagonist = data;
        this.getHero(data.hero);
        this.heroHP = data.health;
      }
    )
  }

  getHero(id: number): void {
    this.studentService.getHero(id).subscribe(
      (data: any) => {
        // console.log(data);
        this.hero = data;
      }
    )
  }

  getBoss(id: number) {
    this.studentService.getBoss(id).subscribe(
      (data: any) => {
        // console.log(data);
        this.boss = data;
        this.bossHP = data.health;
      }
    )
  }

  completeTask() {
    let grades = 0;
    let reward = 0;
    if (this.countCorrect >= this.task.five) {
      grades = 5;
      reward += 5;
    }
    else if (this.countCorrect >= this.task.four && this.countCorrect < this.task.five) {
      grades = 4;
      reward += 2;
    }
    else if (this.countCorrect >= this.task.three && this.countCorrect < this.task.four) {
      grades = 3;
      reward += 1;
    }
    else if (this.countCorrect >= this.task.two && this.countCorrect < this.task.three) {
      grades = 2;
    }
    if (this.bossHP <= 0){
      console.log('Победа!');
      console.log(reward + 10);
      this.studentService.rewardStudent(reward + 10, 0).subscribe(
        (data: any) => {
          console.log(data);
        },
        (error: any) => {
          console.log(error)
        }
      )
    }
    this.createTestRecord(this.task.id, this.task.title, this.countCorrect, grades, this.countPoints);
    this.postAccountStatistics();
    this.router1.navigate(['/student/main']);
  }

  postAccountStatistics(): void {
    this.studentService.postAccountStatistics(1).subscribe(
      (data: any) => {
        console.log(data);
      }
    )
  }

  createTestRecord(test: number, test_name: string, count_correct: number, grades: number, count_points: number) {
    this.studentService.postTestRecord(test,test_name, count_correct, grades, count_points).subscribe(
      (data: any) => {
        console.log(data);
      }
    )
  }
}
