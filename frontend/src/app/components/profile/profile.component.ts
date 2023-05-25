import {Component, OnInit} from '@angular/core';
import {AccountService} from "../../servicies/account.service";

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit{
  user: any;
  userRole: string = '';

  constructor(private accountService: AccountService) {  }
  ngOnInit() {
    this.getUserWithToken(localStorage.getItem('my-token'));
  }

  getUserWithToken(MyToken: any): void {
    this.accountService.getAccountWhithToken(MyToken).subscribe(
      (data: any) => {
        switch (data.is_teacher){
          case 'True':
            this.userRole = 'Учитель';
            break;
          case 'False':
            this.userRole = 'Ученик';
            break;
          default:
            this.userRole = 'Нет информации'
            break;
        }
        this.user = data;
        console.log(this.user);
      },
      error => {
        // console.log(error);
      }
    )
  }
}
