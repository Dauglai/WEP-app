import {Component, OnInit} from '@angular/core';
import {TaskService} from "../../../../servicies/task.service";
import {QuestionService} from "../../../../servicies/question.service";
import {ActivatedRoute} from "@angular/router";
import {Subscription} from "rxjs";

@Component({
  selector: 'app-task-details-student',
  templateUrl: './task-details-student.component.html',
  styleUrls: ['./task-details-student.component.css']
})
export class TaskDetailsStudentComponent implements OnInit{
  protected taskId: number = 0;
  protected task: any = {};
  protected questions: any = [];
  protected serialNumberQuestion: number = 0;
  private routeSubscription: Subscription;

  constructor(private route: ActivatedRoute, private taskService: TaskService,
              private questionService: QuestionService) {
     this.routeSubscription = route.params.subscribe(params => {
      this.taskId = params['id'];
    });
  }
  ngOnInit() {
    this.getTask(this.taskId);
    this.getQuestions(this.taskId);
  }

  sendAnswer(){
    this.serialNumberQuestion += 1;
    console.log(this.serialNumberQuestion);
  }

  getTask(id: number) {
    this.taskService.getTask(id).subscribe(
      (data: any) => {
        console.log(data)
        this.task = data;
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
}
