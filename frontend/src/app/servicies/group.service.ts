import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders, HttpParams} from "@angular/common/http";
import {forkJoin, Observable} from "rxjs";
import {IGroup} from "../interfaces/interface.group";
import {AccountService} from "./account.service";

@Injectable({
  providedIn: 'root'
})
export class GroupService {
constructor(private http: HttpClient) { }
  private apiUrl = 'http://localhost:8000/api/groups/';
  private apiGroupCreate = 'http://localhost:8000/api/teacher/create_group/';
  private apiGetGroup = 'http://localhost:8000/api/teacher/get_group/';
  private apiGetParticipants= 'http://localhost:8000/api/teacher/get_participants/';
  private apiGetAccounts = 'http://localhost:8000/api/teacher/get_accounts/';
  private apiGetTestsByGroup = 'http://localhost:8000/api/teacher/get_tests_by_group/';

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
       tests: this.http.get<any>(this.apiGetTestsByGroup + id, {
        headers: {Authorization: 'Token ' + localStorage.getItem('my-token')},
        params: params
      }),
    })
  }

  createGroup(nameGroup: string, login: string, password: string): Observable<any> {
    const group = {group_name:  nameGroup, login: login, password: password};
    return this.http.post(this.apiGroupCreate, group, {headers: this.headers});
  }
}
