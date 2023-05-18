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
  user: any;

  constructor(private accountService: AccountService) {  }

  ngOnInit() {
    this.getUserWithToken(localStorage.getItem('my-token'));
    localStorage.setItem('user', this.user);
  }
  getUserWithToken(MyToken: any): void {
    this.accountService.getAccountWhithToken(MyToken).subscribe(
      data => {
        console.log(data);
        // localStorage.setItem('user', data.toString());
      },
      error => {
        console.log(error);
      }
    )
  }
}
