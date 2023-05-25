import {Component, OnInit} from '@angular/core';
import {ITest} from "../../../../interfaces/interface.test";
import {TaskService} from "../../../../servicies/task.service";
import {IGroup} from "../../../../interfaces/interface.group";
import {GroupService} from "../../../../servicies/group.service";
import {forkJoin, from, of, pipe, switchMap} from "rxjs";
import {group} from "@angular/animations";

@Component({
  selector: 'app-student-main',
  templateUrl: './student-main.component.html',
  styleUrls: ['./student-main.component.css']
})
export class StudentMainComponent implements OnInit {
  protected tasks?: ITest[];
  protected groups: IGroup[] = [];
  protected completedTests?: ITest[];

  constructor(private taskService: TaskService, private groupService: GroupService) {
  }

  ngOnInit() {
    this.getGroups();
    this.getTasks();
  }

  public isOpen = false;

  public showDialog() {
    this.isOpen = true;
  }

  protected manageDialog(isOpen: boolean) {
    this.isOpen = false;
    this.getGroups();
  }

  getTasks(): void {
    this.taskService.getTestsByGroup().subscribe(
      (tests: any) => {
        console.log(tests);
        this.tasks = tests;
      }
    )
  }

  getGroups(): void {
    this.groupService.getGroupsStudent().subscribe(
      (groups: any) => {
        console.log(groups);
        this.groups = groups;
      }
    )
  }

}
