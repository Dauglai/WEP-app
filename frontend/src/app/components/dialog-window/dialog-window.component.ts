import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";
import {GroupService} from "../../servicies/group.service";

@Component({
  selector: 'app-dialog-window',
  templateUrl: './dialog-window.component.html',
  styleUrls: ['./dialog-window.component.css']
})
export class DialogWindowComponent implements OnInit{
  error ='';
  @Output() protected isOpen: EventEmitter<boolean> = new EventEmitter<boolean>();
  protected formCreateGroup!: FormGroup;

  constructor(private groupService: GroupService) {  }

  ngOnInit() {
    this.formCreateGroup = new FormGroup({
      nameGroup: new FormControl('', [Validators.required]),
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
    this.groupService.createGroup(
      form.nameGroup,
      form.login,
      form.password).subscribe(
      data => {
        console.log(data);
        console.log('create_group');
          this.manageDialog();
    },
      error => {
        console.log(error);
        this.error = 'Группа с данным login уже существует';
        console.log(this.error);
      });
  }
}
