import {Component, OnInit} from '@angular/core';
import {ITest} from "../../../../interfaces/interface.test";
import {TaskService} from "../../../../servicies/task.service";

@Component({
  selector: 'app-task-list-teacher',
  templateUrl: './task-list-teacher.component.html',
  styleUrls: ['./task-list-teacher.component.css']
})
export class TaskListTeacherComponent implements OnInit {
  protected tasks?: ITest[];

  constructor(private taskService: TaskService) {
  }

  ngOnInit() {
    this.getTasks();
  }

  getTasks(): void {
    this.taskService.getTasks().subscribe(
      data => {
        console.log(data);
        this.tasks = data;
      },
      error => {
        console.log(error);
      }
    )
  }
}
