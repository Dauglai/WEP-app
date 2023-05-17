import {Component, OnInit} from '@angular/core';
import {AccountService} from "../../servicies/account.service";

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit{

  constructor(private accountService: AccountService) { }
  ngOnInit() {
    // this.getUserWithToken(localStorage.getItem('my-token'));
    console.log(localStorage.getItem('my-token'));
  }
  getUserWithToken(MyToken: any): void {
    this.accountService.getAccountWhithToken(MyToken).subscribe(
      data => {
        console.log(data);
      },
      error => {
        console.log(error);
      }
    )
  }
}
