import {Component, OnInit} from '@angular/core';
import {ITest} from "../../../../interfaces/interface.test";
import {TaskService} from "../../../../servicies/task.service";

@Component({
  selector: 'app-task-list-student',
  templateUrl: './task-list-student.component.html',
  styleUrls: ['./task-list-student.component.css']
})
export class TaskListStudentComponent implements OnInit {
  protected tasks?: ITest[];
  protected completedTests?: ITest[];

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
