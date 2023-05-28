import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {TaskService} from "./task.service";
import {Observable} from "rxjs";
import {IGroup} from "../interfaces/interface.group";

@Injectable({
  providedIn: 'root'
})
export class StudentService {

  constructor(private http: HttpClient) { }

  private apiGetBoss = 'http://localhost:8000/api/teacher/boss/';
  private apiHeroes = 'http://localhost:8000/api/student/hero/';
  private apiAccountStatistics = 'http://localhost:8000/api/student/account_statistics/';
  private apiProtagonist = 'http://localhost:8000/api/student/protagonist/';

  private apiChoice = 'http://localhost:8000/api/student/choice/';
  private apiTestRecord = 'http://localhost:8000/api/student/test_record/';
  private apiTestRecordList = 'http://localhost:8000/api/student/test_record_list/';

  private headers = new HttpHeaders(
      {'Content-Type': 'application/json',
        Authorization: 'Token ' + localStorage.getItem('my-token')}
    );

  postChoice(question: number, number_answer: number): any {
    const data = {question: question, number_answer: number_answer};
    return this.http.post(this.apiChoice, data, {headers: this.headers })
  }

  postTestRecord(test: number, count_correct: number, grades: number, count_points: number): any {
    const data = {test: test, count_correct: count_correct, grades: grades,
      count_points: count_points};
    return this.http.post(this.apiTestRecord, data, {headers: this.headers })
  }

  getTestRecordList(): any {
    return this.http.get<any>(this.apiTestRecordList, {headers: this.headers })
  }

  getTestRecord(): any {
    return this.http.get<any>(this.apiTestRecord, {headers: this.headers })
  }

  getBosses(): Observable<any> {
    return this.http.get<any>(this.apiGetBoss,{headers: this.headers });
  }

  getBoss(id: number): any {
    return this.http.get<any>(this.apiGetBoss + id,{headers: this.headers });
  }

  getHeroes(): Observable<any> {
    return this.http.get<any>(this.apiHeroes);
  }

  getHero(id: number): any {
    return this.http.get<any>(this.apiHeroes + id);
  }

  getAccountStatistics(): any {
    return this.http.get<any>(this.apiAccountStatistics, {headers: this.headers });
  }

  getProtagonist(): any {
    return this.http.get<any>(this.apiProtagonist, {headers: this.headers });
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
