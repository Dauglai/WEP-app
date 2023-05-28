import {ChangeDetectionStrategy, ChangeDetectorRef, Component, OnInit} from '@angular/core';
import {IGroup} from "../../../../interfaces/interface.group";
import {GroupService} from "../../../../servicies/group.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-group-list-teacher',
  templateUrl: './group-list-teacher.component.html',
  styleUrls: ['./group-list-teacher.component.css'],
  changeDetection: ChangeDetectionStrategy.Default,
})
export class GroupListTeacherComponent implements OnInit{
  protected groups: IGroup[] = [];
  constructor(private groupService: GroupService, private router: Router,
              private cdr: ChangeDetectorRef) {  }

  ngOnInit() {
    this.getGroups();
    this.cdr.detectChanges();
  }

  public isOpen = false;

  public showDialog() {
    this.isOpen = true;
  }

  protected manageDialog(isOpen: boolean) {
    this.isOpen = false;
    this.getGroups();
  }

  getGroups(): void {
    this.groupService.getGroups().subscribe(
      groups => {
        console.log(groups)
        this.groups = groups;
    });
  }

  getRandomColor(): string {
    // return 'rgba(123,17,70, 0.34 )'
    return "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + ","
      + Math.floor(Math.random() * 255) + ", 0.34 )";
  }
}
