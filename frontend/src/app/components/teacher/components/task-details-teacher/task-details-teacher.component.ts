import {Component, OnInit} from '@angular/core';
import {ITest} from "../../../../interfaces/interface.test";
import {TaskService} from "../../../../servicies/task.service";
import {IGroup} from "../../../../interfaces/interface.group";
import {Subscription} from "rxjs";
import {ActivatedRoute} from "@angular/router";
import {GroupService} from "../../../../servicies/group.service";
import {QuestionService} from "../../../../servicies/question.service";

@Component({
  selector: 'app-task-details-teacher',
  templateUrl: './task-details-teacher.component.html',
  styleUrls: ['./task-details-teacher.component.css']
})
export class TaskDetailsTeacherComponent implements OnInit {
  protected test: ITest = {} as ITest;
  protected questions: any = [];
  private idTest: number = 0;
  private routeSubscription: Subscription;
  constructor(private route: ActivatedRoute, private taskService: TaskService, private questionService: QuestionService ) {
    this.routeSubscription = route.params.subscribe(params => {
      this.idTest = params['id'];
    });
  }

  ngOnInit() {
    console.log(this.idTest);
    this.test = this.taskService.getTask(this.idTest).subscribe(
      (data: any) => {
        console.log(data)
    });
    this.questions = this.questionService.getQuestions(this.idTest).subscribe(
      (data: any) => {
        console.log(data)
    });
  }
}
