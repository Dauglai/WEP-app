import {Component, OnInit} from '@angular/core';
import {AccountService} from "../../servicies/account.service";

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit{
  user: any;

  constructor(private accountService: AccountService) {  }
  ngOnInit() {
    this.getUserWithToken(localStorage.getItem('my-token'));
  }

  getUserWithToken(MyToken: any): void {
    this.accountService.getAccountWhithToken(MyToken).subscribe(
      data => {
        this.user = data;
        console.log(this.user);
      },
      error => {
        // console.log(error);
      }
    )
  }
}
