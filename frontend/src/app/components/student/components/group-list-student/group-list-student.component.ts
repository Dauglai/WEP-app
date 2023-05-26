import {ChangeDetectionStrategy, Component, OnInit} from '@angular/core';
import {IGroup} from "../../../../interfaces/interface.group";
import {GroupService} from "../../../../servicies/group.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-group-list-student',
  templateUrl: './group-list-student.component.html',
  styleUrls: ['./group-list-student.component.css'],
  changeDetection: ChangeDetectionStrategy.Default,
})
export class GroupListStudentComponent implements OnInit{
  protected groups: IGroup[] = [];
  constructor(private groupService: GroupService, private router: Router) {  }

  ngOnInit() {
    this.getGroups();
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
    this.groupService.getGroupsStudent().subscribe(
      (groups: any) => {
        console.log(groups);
        this.groups = groups;
      }
    )
  }

  getRandomColor(): string {
    // return 'rgba(123,37,70, 0.34 )'
    return "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + ","
      + Math.floor(Math.random() * 255) + ", 0.34 )";
  }
}
