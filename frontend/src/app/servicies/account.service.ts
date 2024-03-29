import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class AccountService {

  constructor(private http: HttpClient) { }
  private apiUrl = 'http://127.0.0.1:8000/api/account/registr/';
  private apiUrl2 = 'http://127.0.0.1:8000/api/account/create-statistics/';
  private apiGetToken = 'http://127.0.0.1:8000/auth-token/token/login/';
  private apiGetAccount = 'http://127.0.0.1:8000/api/account/user/by/token/';
  private apiLogoutAccount = 'http://127.0.0.1:8000/auth-token/token/logout/';

  // private apiUrl = 'http://DenisGM.pythonanywhere.com/api/account/registr/';
  // private apiUrl2 = 'http://DenisGM.pythonanywhere.com/api/account/create-statistics/';
  // private apiGetToken = 'http://DenisGM.pythonanywhere.com/auth-token/token/login/';
  // private apiGetAccount = 'http://DenisGM.pythonanywhere.com/api/account/user/by/token/';
  // private apiLogoutAccount = 'http://DenisGM.pythonanywhere.com/auth-token/token/logout/';



  createAccount(last_name: string, first_name: string, patronymic: string, location: string,
                school_number: number, email: string, password: string, password2: string,
                is_teacher: boolean, gender: string): Observable<any> {
    const account = { last_name: last_name, first_name: first_name, patronymic: patronymic,
      location: location, school_number: school_number, email: email, password: password,
      password2: password2, is_teacher: is_teacher, gender: gender};
    return this.http.post(this.apiUrl, account);
  }

  createStatistics(Token: any): Observable<any> {
    const myHeaders = new HttpHeaders(
      {'Content-Type': 'application/json', Authorization: 'Token ' + Token}
    );
    const statistics = { };
    return this.http.post(this.apiUrl2, statistics, {headers: myHeaders});
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

  logout() {
    const myHeaders = new HttpHeaders(
      {'Content-Type': 'application/json', Authorization: 'Token ' + localStorage.getItem('my-token')}
    );
    const body = {}
    return this.http.post(this.apiLogoutAccount, body,
      {headers: myHeaders})
  }
}
