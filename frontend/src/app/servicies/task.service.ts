import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {ITest} from "../interfaces/interface.test";

@Injectable({
  providedIn: 'root'
})
export class TaskService {
  constructor(private http: HttpClient) { }
  private apiUrl = 'http://127.0.0.1:8000/api/tests/';

  getTasks(): Observable<ITest[]> {
      return this.http.get<ITest[]>(this.apiUrl, {headers:
        {Authorization: 'Token ' + localStorage.getItem('my-token')}
    });
  }

  getTask(id: number): any {
      return this.http.get<ITest[]>(this.apiUrl + id, {headers:
        {Authorization: 'Token ' + localStorage.getItem('my-token')}
    });
  }

  createTask(newTask: any) {
      this.http.post(this.apiUrl, newTask);
  }
}
