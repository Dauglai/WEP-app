import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {TaskService} from "../../servicies/task.service";
// import { Task } from './task';

export interface Task {
    id: number;
    name: string;
    description: string;
    created_at: string;
}

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.css']
})
export class TaskListComponent implements OnInit{
  protected tasks?: Task[];
  newTask: Task = { id: 1, name: '', description: '', created_at: '' };

  constructor(private taskService: TaskService) {
  }

  ngOnInit() {
    this.taskService.getTasks().subscribe(
      tasks => {
        console.log(tasks)
        this.tasks = tasks;
    });
  }

  // createTask(): void {
  //   this.taskService.createTask().
  // }
  // .subscribe(() => {
  //         // code to refresh the task list goes here
  //     });
}
