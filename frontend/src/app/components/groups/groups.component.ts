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

  getRandomColor(): string {
    return "rgba(" + Math.floor(Math.random() * 255) + "," + Math.floor(Math.random() * 255) + ","
      + Math.floor(Math.random() * 255) + ", 0.34 )";
  }
}
