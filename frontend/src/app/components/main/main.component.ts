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
  isOneReload: boolean = false;

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
        this.isTeacher = data.is_teacher == 'False'? false: true;
        console.log(this.isTeacher);
        // if(!this.isOneReload) {
        //   window.location.reload();
        //   this.isOneReload = true;
        // }
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
        // this.isOneReload = false;
      },
      error => {
        console.log(error);
      }
    )
  }
}
