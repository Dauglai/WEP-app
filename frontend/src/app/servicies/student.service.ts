import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class StudentService {

  constructor(private http: HttpClient) { }

  // private apiGetBoss = 'http://localhost:8000/api/teacher/boss/';
  // private apiHeroes = 'http://localhost:8000/api/student/hero/';
  // private apiAccountStatistics = 'http://localhost:8000/api/student/account_statistics/';
  // private apiAllAccountStatistics = 'http://localhost:8000/api/student/all_account_statistics/';
  // private apiProtagonist = 'http://localhost:8000/api/student/protagonist/';
  //
  // private apiChoice = 'http://localhost:8000/api/student/choice/';
  // private apiTestRecord = 'http://localhost:8000/api/student/test_record/';
  // private apiTestRecordList = 'http://localhost:8000/api/student/test_record_list/';
  // private apiReward = 'http://localhost:8000/api/student/reward/';

  private apiGetBoss = 'http://danilsvp.beget.tech/api/teacher/boss/';
  private apiHeroes = 'http://danilsvp.beget.tech/api/student/hero/';
  private apiAccountStatistics = 'http://danilsvp.beget.tech/api/student/account_statistics/';
  private apiAllAccountStatistics = 'http://danilsvp.beget.tech/api/student/all_account_statistics/';
  private apiProtagonist = 'http://danilsvp.beget.tech/api/student/protagonist/';

  private apiChoice = 'http://danilsvp.beget.tech/api/student/choice/';
  private apiTestRecord = 'http://danilsvp.beget.tech/api/student/test_record/';
  private apiTestRecordList = 'http://danilsvp.beget.tech/api/student/test_record_list/';
  private apiReward = 'http://danilsvp.beget.tech/api/student/reward/';

  // private apiGetBoss = 'http://danilsvp.beget.tech/api/teacher/boss/';
  // private apiHeroes = 'http://danilsvp.beget.tech/api/student/hero/';
  // private apiAccountStatistics = 'http://danilsvp.beget.tech/api/student/account_statistics/';
  // private apiAllAccountStatistics = 'http://danilsvp.beget.tech/api/student/all_account_statistics/';
  // private apiProtagonist = 'http://danilsvp.beget.tech/api/student/protagonist/';
  //
  // private apiChoice = 'http://danilsvp.beget.tech/api/student/choice/';
  // private apiTestRecord = 'http://danilsvp.beget.tech/api/student/test_record/';
  // private apiTestRecordList = 'http://danilsvp.beget.tech/api/student/test_record_list/';




  // private apiGetBoss = 'http://DenisGM.pythonanywhere.com/api/teacher/boss/';
  // private apiHeroes = 'http://DenisGM.pythonanywhere.com/api/student/hero/';
  // private apiAccountStatistics = 'http://DenisGM.pythonanywhere.com/api/student/account_statistics/';
  // private apiAllAccountStatistics = 'http://DenisGM.pythonanywhere.com/api/student/all_account_statistics/';
  // private apiProtagonist = 'http://DenisGM.pythonanywhere.com/api/student/protagonist/';
  //
  // private apiChoice = 'http://DenisGM.pythonanywhere.com/api/student/choice/';
  // private apiTestRecord = 'http://DenisGM.pythonanywhere.com/api/student/test_record/';
  // private apiTestRecordList = 'http://DenisGM.pythonanywhere.com/api/student/test_record_list/';


  private headers = new HttpHeaders(
      {'Content-Type': 'application/json',
        Authorization: 'Token ' + localStorage.getItem('my-token')}
    );

  postChoice(question: number, number_answer: number): any {
    const data = {question: question, number_answer: number_answer};
    return this.http.post(this.apiChoice, data, {headers: this.headers })
  }

  postTestRecord(test: number,test_name: string, count_correct: number, grades: number, count_points: number): any {
    const data = {test: test, test_name: test_name, count_correct: count_correct, grades: grades,
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

  postAccountStatistics(i: number): any {
    const data: any = {i: i};
    return this.http.post(this.apiAccountStatistics, data, {headers: this.headers });
  }

  getAllAccountStatistics(): any {
    return this.http.get<any>(this.apiAllAccountStatistics, {headers: this.headers });
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

  rewardStudent(exp: number, score: number): any {
    const data = {exp: exp, score: score}
    return this.http.post<any>(this.apiReward, data, {headers: this.headers });
  }
}
