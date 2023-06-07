import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {ITest} from "../interfaces/interface.test";

@Injectable({
  providedIn: 'root'
})
export class QuestionService {
constructor(private http: HttpClient) { }
  private apiUrl = 'http://127.0.0.1:8000/api/questions/';

  // private apiUrl = 'http://DenisGM.pythonanywhere.com/api/questions/';

  getQuestions(idTest: number): Observable<any> {
      return this.http.get<any>(this.apiUrl + idTest, {headers:
        {Authorization: 'Token ' + localStorage.getItem('my-token')}
    });
  }

  createQuestion(newQuestion: any) {
      this.http.post(this.apiUrl, newQuestion);
  }
}
