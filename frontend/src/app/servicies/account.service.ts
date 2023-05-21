import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class AccountService {

  constructor(private http: HttpClient) { }
  private apiUrl = 'http://127.0.0.1:8000/api/account/registr/';
  private apiGetToken = 'http://127.0.0.1:8000/auth-token/token/login/';
  private apiGetAccount = 'http://127.0.0.1:8000/api/account/user/by/token/';

  createAccount(last_name: string, first_name: string, patronymic: string, location: string,
                school_number: number, email: string, password: string, password2: string,
                is_teacher: boolean, gender: string): Observable<any> {
    // const account = { email: email, password: password, password2: password2 };
    const account = { last_name: last_name, first_name: first_name, patronymic: patronymic,
      location: location, school_number: school_number, email: email, password: password,
      password2: password2, is_teacher: is_teacher, gender: gender};
    return this.http.post(this.apiUrl, account);
  }

  getToken(email: string, password: string):Observable<any> {
    const account = { email: email, password: password};
    return this.http.post(this.apiGetToken, account)
  }

  getAccountWhithToken(Token: any) {
    const myHeaders = new HttpHeaders(
      {'Content-Type': 'application/json', Authorization: 'Token ' + Token}
    );
    const body = {}
    return this.http.post(this.apiGetAccount, body,
      {headers: {'Content-Type': 'application/json', Authorization: 'Token ' + Token}})
  }
}
