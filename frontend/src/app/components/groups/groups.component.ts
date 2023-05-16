import {Component, OnInit} from '@angular/core';
import {GroupService} from "../../servicies/group.service";
import {Task} from "../task-list/task-list.component";

export interface Group {
    owner: number;
    owner_name: string;
    group_name: string;
    login: string;
    password: string;
}

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
}
