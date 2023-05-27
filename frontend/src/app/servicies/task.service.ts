import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
import {ITest} from "../interfaces/interface.test";

@Injectable({
  providedIn: 'root'
})
export class TaskService {
  constructor(private http: HttpClient) { }
  private apiUrl = 'http://127.0.0.1:8000/api/tests/';
  private apiDeleteTest = 'http://localhost:8000/api/teacher/delete_test/';
  private apiGetTestsByGroup = 'http://localhost:8000/api/student/tests-by-group/';

  private headers = new HttpHeaders(
      {'Content-Type': 'application/json',
        Authorization: 'Token ' + localStorage.getItem('my-token')}
    );

  getTasks(): Observable<ITest[]> {
      return this.http.get<ITest[]>(this.apiUrl, {headers: this.headers });
  }

  getTask(id: number): any {
      return this.http.get<ITest[]>(this.apiUrl + id, {headers: this.headers });
  }

  getTasksByGroup(): any {
    const tests = this.http.get<any>(this.apiGetTestsByGroup, { headers: this.headers })
    return tests;
  }

  deleteTask(id: number): any {
    return this.http.get(this.apiDeleteTest + id, {headers: this.headers});
  }

  createTask(newTask: any) {
      this.http.post(this.apiUrl, newTask);
  }
}
