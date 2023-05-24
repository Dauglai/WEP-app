import {Component, OnInit, ViewChild} from '@angular/core';
import {AccountService} from "./servicies/account.service";
import {Router} from "@angular/router";
import {ProfileComponent} from "./components/profile/profile.component";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  constructor(private accountService: AccountService) {  }

  ngOnInit() {
    this.getUserWithToken(localStorage.getItem('my-token'));
  }
  getUserWithToken(MyToken: any): void {
    this.accountService.getAccountWhithToken(MyToken).subscribe(
      (data: any) => {
        console.log(data);
        localStorage.setItem('user-email', data.email);
        localStorage.setItem('user-full-name', `${data.last_name} ${data.first_name} ${data.patronymic}`);
        localStorage.setItem('is-teacher', data.is_teacher);
      },
      error => {
        console.log(error);
      }
    )
  }
}
