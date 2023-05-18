import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Group} from "../interfaces/interface.group";

@Injectable({
  providedIn: 'root'
})
export class GroupService {
constructor(private http: HttpClient) { }
  private apiUrl = 'http://localhost:8000/api/groups/';

  getGroups(): Observable<Group[]> {
    const body = {}
    return this.http.get<Group[]>(this.apiUrl,{headers:
        {Authorization: 'Token ' + localStorage.getItem('my-token')}
    });
  }
}
