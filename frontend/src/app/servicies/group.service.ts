import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Task} from "../components/task-list/task-list.component";
import {Group} from "../components/groups/groups.component";

@Injectable({
  providedIn: 'root'
})
export class GroupService {
constructor(private http: HttpClient) { }
  private apiUrl = 'http://localhost:8000/api/groups/';

  getGroups(): Observable<Group[]> {
      return this.http.get<Group[]>(this.apiUrl);
  }

  createTask(newTask: any) {
      this.http.post(this.apiUrl, newTask);
  }
}
