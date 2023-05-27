import {Component, OnInit} from '@angular/core';
import {ITest} from "../../../../interfaces/interface.test";
import {TaskService} from "../../../../servicies/task.service";
import {IGroup} from "../../../../interfaces/interface.group";
import {Subscription} from "rxjs";
import {ActivatedRoute} from "@angular/router";
import {GroupService} from "../../../../servicies/group.service";
import {QuestionService} from "../../../../servicies/question.service";
import {Location} from '@angular/common';

@Component({
  selector: 'app-task-details-teacher',
  templateUrl: './task-details-teacher.component.html',
  styleUrls: ['./task-details-teacher.component.css']
})
export class TaskDetailsTeacherComponent implements OnInit{
  protected taskId: number = 0;
  protected task: any = {};
  protected questions: any = [];
  protected serialNumberQuestion: number = 0;
  private routeSubscription: Subscription;

  constructor(private route: ActivatedRoute, private taskService: TaskService,
              private questionService: QuestionService, private _location: Location) {
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

  returnBack() {
    this._location.back();
  }
}
