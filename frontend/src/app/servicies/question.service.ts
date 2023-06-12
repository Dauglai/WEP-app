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
  private apiCreateQuestion = 'http://localhost:8000/api/teacher/create_question/';
  private apiDeleteQuestion = 'http://localhost:8000/api/teacher/delete_question/';

  // private apiUrl = 'http://danilsvp.beget.tech/api/questions/';
  // private apiCreateQuestion = 'http://danilsvp.beget.tech/api/teacher/create_question/';
  // private apiDeleteQuestion = 'http://danilsvp.beget.tech/api/teacher/delete_question/';


  getQuestions(idTest: number): Observable<any> {
      return this.http.get<any>(this.apiUrl + idTest, {headers:
        {Authorization: 'Token ' + localStorage.getItem('my-token')}
    });
  }

  createQuestion(newQuestion: any) {
      return this.http.post(this.apiCreateQuestion, newQuestion);
  }

  deleteQuestion(data: any) {
      return this.http.post(this.apiDeleteQuestion, data);
  }
}
