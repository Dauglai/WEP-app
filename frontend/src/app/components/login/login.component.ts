import {Component, OnInit} from '@angular/core';
import {AccountService} from "../../servicies/account.service";
import {Router} from "@angular/router";
import {FormControl, FormGroup, Validators} from "@angular/forms";

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit{
  errorLogin: string ='';
  constructor(private accountService: AccountService, private router: Router) { }

  ngOnInit() {
    // this.getUserWithToken(localStorage.getItem('my-token'));
  }

  formLogin = new FormGroup({
    email: new FormControl('', [Validators.required]),
    password: new FormControl('', [Validators.required]),
  })

  login(): void {
    const form = this.formLogin.value;
    console.log(form)
    // this.createAccount(form.email!, form.password!, form.password2!);
    this.getToken(form.email!, form.password!);
  }

  getToken(email: string, password: string): void {
    this.accountService.getToken(email, password).subscribe(
      data => {
        console.log(data);
        localStorage.setItem('my-token', data.auth_token);
        this.router.navigate(['/main']);
      },
      error => {
        console.log(error);
        this.errorLogin = 'Вы ввели неверные данные';
      }
    )
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
