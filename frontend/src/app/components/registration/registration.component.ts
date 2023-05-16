import { Component } from '@angular/core';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent {
  isTeacher: boolean = false;
  nextPage = false;

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
}
