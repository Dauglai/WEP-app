import {Component, OnInit} from '@angular/core';
import {AccountService} from "./servicies/account.service";
import {Router} from "@angular/router";

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
  }
  getUserWithToken(MyToken: any): void {
    this.accountService.getAccountWhithToken(MyToken).subscribe(
      data => {
        console.log(data);
        this.user = data;
      },
      error => {
        console.log(error);
      }
    )
  }
}
