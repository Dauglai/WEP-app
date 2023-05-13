import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Task} from "../components/task-list/task-list.component";

@Injectable({
  providedIn: 'root'
})
export class TaskService {
  constructor(private http: HttpClient) { }
  private apiUrl = 'http://localhost:8000/api/tasks/';

  getTasks(): Observable<Task[]> {
      return this.http.get<Task[]>(this.apiUrl);
  }

  createTask(newTask: any) {
      this.http.post(this.apiUrl, newTask);
  }
}
