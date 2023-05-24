import {Component, OnInit} from '@angular/core';
import {AccountService} from "../../servicies/account.service";

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})
export class MainComponent implements OnInit{
  user: string = '';
  isTeacher: boolean = false;
  isAuthentication: boolean = false;

  constructor(private accountService: AccountService) { }
  ngOnInit() {
    this.getUserWithToken(localStorage.getItem('my-token'));
    console.log(localStorage.getItem('my-token'));
  }
  getUserWithToken(MyToken: any): void {
    this.accountService.getAccountWhithToken(MyToken).subscribe(
      (data: any) => {
        console.log(data)
        this.user = `${data.last_name} ${data.first_name} ${data.patronymic}`;
        this.isAuthentication = true;
      },
      error => {
        console.log(error);
        this.isAuthentication = false;
      }
    )
  }

  logout(): void {
    this.accountService.logout().subscribe(
      (data: any) => {
        console.log(data)
        this.isAuthentication = false;
        localStorage.clear();
      },
      error => {
        console.log(error);
      }
    )
  }
}
