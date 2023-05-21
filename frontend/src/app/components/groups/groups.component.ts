import {Component, OnInit} from '@angular/core';
import {GroupService} from "../../servicies/group.service";
import {Group} from "../../interfaces/interface.group";


@Component({
  selector: 'app-groups',
  templateUrl: './groups.component.html',
  styleUrls: ['./groups.component.css']
})
export class GroupsComponent implements OnInit{
  protected groups: Group[] = [];
  constructor(private groupService: GroupService) {  }

  ngOnInit() {
    this.groupService.getGroups().subscribe(
      groups => {
        console.log(groups)
        this.groups = groups;
    });
  }

  public isOpen = false;

  public showDialog() {
    this.isOpen = true;
  }

  protected manageDialog(isOpen: boolean) {
    // if (isOpen)
    this.isOpen = false;
  }

  getRandomColor(): string {
    return 'rgba(123,37,70, 0.34 )'
    // return "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + ","
    //   + Math.floor(Math.random() * 255) + ", 0.34 )";
  }
}
