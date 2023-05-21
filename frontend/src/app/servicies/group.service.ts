import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
import {Group} from "../interfaces/interface.group";
import {AccountService} from "./account.service";

@Injectable({
  providedIn: 'root'
})
export class GroupService {
constructor(private http: HttpClient) { }
  private apiUrl = 'http://localhost:8000/api/groups/';
  private apiGroupCreate = 'http://localhost:8000/api/teacher/create_group/';
  private headers = new HttpHeaders(
      {'Content-Type': 'application/json',
        Authorization: 'Token ' + localStorage.getItem('my-token')}
    );

  getGroups(): Observable<Group[]> {
    const body = {}
    return this.http.get<Group[]>(this.apiUrl,{headers:
        {Authorization: 'Token ' + localStorage.getItem('my-token')}
    });
  }

  createGroup(nameGroup: string, login: string, password: string): Observable<any> {
    const group = {group_name:  nameGroup, login: login, password: password};
    return this.http.post(this.apiGroupCreate, group, {headers: this.headers});
  }
}
