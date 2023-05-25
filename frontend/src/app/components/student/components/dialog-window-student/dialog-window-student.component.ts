import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";
import {GroupService} from "../../../../servicies/group.service";

@Component({
  selector: 'app-dialog-window-student',
  templateUrl: './dialog-window-student.component.html',
  styleUrls: ['./dialog-window-student.component.css']
})
export class DialogWindowStudentComponent implements OnInit{
  error ='';
  @Output() protected isOpen: EventEmitter<boolean> = new EventEmitter<boolean>();
  protected formCreateGroup!: FormGroup;

  constructor(private groupService: GroupService) {  }

  ngOnInit() {
    this.formCreateGroup = new FormGroup({
      login: new FormControl('', [Validators.required]),
      password: new FormControl('', [Validators.required]),
    })
  }

  protected manageDialog() {
    this.isOpen.emit(false);
  }

  submit(){
    this.createGroup();
  }

  createGroup(): void {
    const form = this.formCreateGroup?.value;
    console.log(form)
    this.groupService.joinGroup(
      form.login,
      form.password).subscribe(
      data => {
        console.log(data);
          this.manageDialog();
    },
      error => {
        this.error = 'Данной группы не существует';
        console.log(this.error);
      });
  }
}
