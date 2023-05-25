import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams} from "@angular/common/http";
import {forkJoin, Observable} from "rxjs";
import {IGroup} from "../interfaces/interface.group";
import {TaskService} from "./task.service";

@Injectable({
  providedIn: 'root'
})
export class GroupService {
constructor(private http: HttpClient, private taskService: TaskService) { }
  private apiUrl = 'http://localhost:8000/api/groups/';
  private apigetGroupsStudent = 'http://localhost:8000/api/student/groups/';
  private apiGroupCreate = 'http://localhost:8000/api/teacher/create_group/';
  private apiGetGroup = 'http://localhost:8000/api/teacher/get_group/';
  private apiGetParticipants= 'http://localhost:8000/api/teacher/get_participants/';
  private apiGetAccounts = 'http://localhost:8000/api/teacher/get_accounts/';

  private headers = new HttpHeaders(
      {'Content-Type': 'application/json',
        Authorization: 'Token ' + localStorage.getItem('my-token')}
    );

  getGroups(): Observable<IGroup[]> {
    const body = {}
    return this.http.get<IGroup[]>(this.apiUrl,{headers:
        {Authorization: 'Token ' + localStorage.getItem('my-token')}
    });
  }

  getGroupsStudent(): Observable<IGroup[]> {
    const body = {}
    return this.http.get<IGroup[]>(this.apigetGroupsStudent,{headers:
        {Authorization: 'Token ' + localStorage.getItem('my-token')}
    });
  }

  getGroup(id: number): any {
    let params = new HttpParams().set("id", id)
     return forkJoin({
      group: this.http.get<any>(this.apiGetGroup + id, {
        headers: {Authorization: 'Token ' + localStorage.getItem('my-token')},
        params: params
      }),
      participants: this.http.get<any>(this.apiGetParticipants + id, {
        headers: {Authorization: 'Token ' + localStorage.getItem('my-token')},
        params: params
      }),
      accounts: this.http.get<any>(this.apiGetAccounts + id, {
        headers: {Authorization: 'Token ' + localStorage.getItem('my-token')},
        params: params
      }),
       tests: this.taskService.getTestsByGroup()
    })
  }


  createGroup(nameGroup: string, login: string, password: string): Observable<any> {
    const group = {group_name:  nameGroup, login: login, password: password};
    return this.http.post(this.apiGroupCreate, group, {headers: this.headers});
  }

  joinGroup(nameGroup: string, login: string, password: string): Observable<any> {
    const group = {group_name:  nameGroup, login: login, password: password};
    return this.http.post(this.apiGroupCreate, group, {headers: this.headers});
  }
}
