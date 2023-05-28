import {Component, OnInit} from '@angular/core';
import {ITest} from "../../../../interfaces/interface.test";
import {TaskService} from "../../../../servicies/task.service";
import {StudentService} from "../../../../servicies/student.service";

@Component({
  selector: 'app-task-list-student',
  templateUrl: './task-list-student.component.html',
  styleUrls: ['./task-list-student.component.css']
})
export class TaskListStudentComponent implements OnInit {
  protected tasks?: ITest[];
  protected completedTests?: ITest[];
  protected testRecord: any = {};

  constructor(private taskService: TaskService, private studentService: StudentService) {
  }

  ngOnInit() {
    this.getTasks();
    this.getTestRecord();
  }

  getTasks(): void {
    this.taskService.getTasksByGroup().subscribe(
      (tests: any) => {
        console.log(tests);
        this.tasks = tests;
      }
    )
  }

  getTestRecord(): void {
    this.studentService.getTestRecordList().subscribe(
      (data: any) => {
        this.testRecord = data;
      }
    )
  }
}
