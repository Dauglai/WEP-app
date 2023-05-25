import { Component } from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";

@Component({
  selector: 'app-task-constructor',
  templateUrl: './task-constructor.component.html',
  styleUrls: ['./task-constructor.component.css']
})
export class TaskConstructorComponent {
  error ='';
  nextPage: boolean = false;
  userEmail = localStorage.getItem('user-email');
  userName = localStorage.getItem('user-full-name');
  testFrom = new FormGroup({
    title: new FormControl('', [Validators.required]),
    subject: new FormControl('', [Validators.required]),
    group: new FormControl('', [Validators.required]),
    text: new FormControl('', [Validators.required]),

    difficulty: new FormControl('', [Validators.required]),
    time: new FormControl('00:15', [Validators.required]),
    time_deadline: new FormControl('', [Validators.required]),
    date_deadline: new FormControl('', [Validators.required]),

    five: new FormControl('', [Validators.required]),
    four: new FormControl('', [Validators.required]),
    three: new FormControl('', [Validators.required]),
    two: new FormControl('', [Validators.required]),
  })

  saveTest(): void {
    this.nextPage = true;
    console.log(this.testFrom.value);
  }

  returnTest(): void {
    this.nextPage = false;
  }

  convertDate(date: string): string {
    // год, месяц, день
    const dateArr = date.split('-');
    return `${dateArr[2]}.${dateArr[1]}.${dateArr[0]}`;
  }

  submit() {
    console.log(this.testFrom.value)
    console.log(this.userEmail);
    console.log(this.userName);
  }
}
