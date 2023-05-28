import {ChangeDetectorRef, Component, OnInit} from '@angular/core';
import {IGroup} from "../../../../interfaces/interface.group";
import {GroupService} from "../../../../servicies/group.service";
import {Router} from "@angular/router";
import {StudentService} from "../../../../servicies/student.service";

@Component({
  selector: 'app-statistics-teacher',
  templateUrl: './statistics-teacher.component.html',
  styleUrls: ['./statistics-teacher.component.css']
})
export class StatisticsTeacherComponent implements OnInit{
  protected groups: IGroup[] = [];
  protected testRecord: any = {};
  constructor(private groupService: GroupService, private router: Router,
              private cdr: ChangeDetectorRef, private studentService: StudentService) {  }

  ngOnInit() {
    this.getGroups();
    this.getTestRecord();
    this.cdr.detectChanges();
  }

  getGroups(): void {
    this.groupService.getGroups().subscribe(
      groups => {
        console.log(groups)
        this.groups = groups;
    });
  }

  getTestRecord(): void {
    this.studentService.getTestRecord().subscribe(
      (data: any) => {
        this.testRecord = data;
        console.log(data);
      }
    )
  }
}
