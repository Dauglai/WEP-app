import { Component } from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";
import {AccountService} from "../../servicies/account.service";
import {Router} from "@angular/router";

export interface IError {
  last_name: string,
  first_name: string,
  patronymic: string,
  location: string,
  school_number: number,
  email: string,
  password: string,
  password2: string,
  is_teacher: boolean,
  gender: string
}

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent {
  isTeacher: boolean = false;
  nextPage = false;
  errors: IError = {} as IError;
  errorPassword = '';

  constructor(private accountService: AccountService, private router: Router) { }

  formRegister = new FormGroup({
    email: new FormControl('', [Validators.required]),
    password: new FormControl('', [Validators.required]),
    password2: new FormControl('', [Validators.required]),

    last_name: new FormControl('', [Validators.required]),
    first_name: new FormControl('', [Validators.required]),
    patronymic: new FormControl('', [Validators.required]),

    location: new FormControl('', [Validators.required]),
    school_number: new FormControl(null, [Validators.required, Validators.min(0)]),

    gender: new FormControl('', [Validators.required]),
    is_teacher: new FormControl(this.isTeacher),
  })

  registration(): void {
    const form = this.formRegister.value;
    form.is_teacher = this.isTeacher;
    console.log(form)
    this.createAccount(form.last_name!, form.first_name!, form.patronymic!, form.location!,
      form.school_number!,
      form.email!, form.password!, form.password2!, form.is_teacher!, form.gender!);
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

  createAccount(last_name: string, first_name: string, patronymic: string, location: string,
                school_number: number, email: string, password: string, password2: string,
                is_teacher: boolean, gender: string) {
    this.accountService.createAccount(last_name, first_name, patronymic, location, school_number,
      email, password, password2, is_teacher, gender).subscribe(
      data => {
        console.log(data);
        this.errors = data;
        if(data.response) {
          if (!this.isTeacher) {
            this.accountService.getToken(email, password).subscribe(
            data => {
              console.log(data);
              this.accountService.createStatistics(data).subscribe(
                data =>
                console.log(data)
              );
              this.router.navigate(['/login']);
            },
              error => {
              console.log(error);
            })
          }
        }
    },
      error => {
        console.log(error);
        this.errorPassword = error.error.qw12er34;
        // this.errorPassword = error.error();
      })
  }
}
