import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";
import {GroupService} from "../../../../servicies/group.service";
import {IGroup} from "../../../../interfaces/interface.group";

@Component({
  selector: 'app-dialog-window-teacher',
  templateUrl: './dialog-window-teacher.component.html',
  styleUrls: ['./dialog-window-teacher.component.css']
})
export class DialogWindowTeacherComponent implements OnInit{
  error ='';
  @Input() curGroup: any= {};
  @Output() protected isOpen: EventEmitter<boolean> = new EventEmitter<boolean>();
  protected formEditGroup!: FormGroup;

  constructor(private groupService: GroupService) {  }

  ngOnInit() {
    this.formEditGroup = new FormGroup({
      nameGroup: new FormControl(`${this.curGroup.group_name}`, [Validators.required]),
      login: new FormControl(`${this.curGroup.login}`, [Validators.required]),
      password: new FormControl(`${this.curGroup.password}`, [Validators.required]),
    })
  }

  protected manageDialog() {
    this.isOpen.emit(false);
  }

  submit(){
    this.editeGroup();
  }

  editeGroup(): void {
    const form = this.formEditGroup?.value;
    console.log(form);
    this.groupService.editGroup(this.curGroup.id, form.nameGroup, form.login, form.password).subscribe(
      (data: any) => {
        console.log(data);
        console.log('create_group');
          this.manageDialog();
    },
      (error: any) => {
        console.log(error);
        // this.error = 'Группа с данным login уже существует';
        // console.log(this.error);
      });
  }
}
