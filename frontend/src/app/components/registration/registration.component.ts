import { Component } from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";
import {AccountService} from "../../servicies/account.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent {
  isTeacher: boolean = false;
  nextPage = false;

  constructor(private accountService: AccountService, private router: Router) { }

  formRegister = new FormGroup({
    email: new FormControl('', Validators.required),
    password: new FormControl('', Validators.required),
    password2: new FormControl('', Validators.required),
  })

  registration(): void {
    const form = this.formRegister.value;
    console.log(this.isTeacher);
    console.log(form)
    this.createAccount(form.email!, form.password!, form.password2!);
  }

  chooseRoleTeacher(): void {
    this.isTeacher = true;
    this.nextPage = true;
  }

  chooseRoleStudent(): void {
    this.isTeacher = false;
    this.nextPage = true;
  }

  previousPage(): void {
    this.nextPage = false;
  }

  createAccount(email: string, password: string, password2: string ) {
    this.accountService.createAccount(email, password, password2).subscribe(
      data => {
      this.router.navigate(['/login']);
    },
      error => {
        console.log(error);
      })

  }
}
