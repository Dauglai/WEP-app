import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {TaskService} from "./task.service";
import {Observable} from "rxjs";
import {IGroup} from "../interfaces/interface.group";

@Injectable({
  providedIn: 'root'
})
export class BossService {

  constructor(private http: HttpClient) { }

  private apiGetBoss = 'http://localhost:8000/api/teacher/boss/';
  private apiHeroes = 'http://localhost:8000/api/student/hero/';
  private apiAccountStatistics = 'http://localhost:8000/api/student/account_statistics/';
  private apiProtagonist = 'http://localhost:8000/api/student/protagonist/';

  private headers = new HttpHeaders(
      {'Content-Type': 'application/json',
        Authorization: 'Token ' + localStorage.getItem('my-token')}
    );

  getBosses(): Observable<any> {
    return this.http.get<any>(this.apiGetBoss,{headers: this.headers });
  }

  getHeroes(): Observable<any> {
    return this.http.get<any>(this.apiHeroes);
  }

  getAccountStatistics(id: number): any {
    return this.http.get<any>(this.apiAccountStatistics + id);
  }

  getProtagonist(id: number): any {
    return this.http.get<any>(this.apiProtagonist + id);
  }

  createProtagonist(): any {
    const data = {}
    return this.http.post<any>(this.apiProtagonist, data, {headers: this.headers });
  }

  createAccountStatistics(): any {
    const data = {}
    return this.http.post<any>(this.apiAccountStatistics, data, {headers: this.headers });
  }
}
