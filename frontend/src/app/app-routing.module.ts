import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainComponent } from "./components/main/main.component";
import {CommonModule} from "@angular/common";
import {StudentComponent} from "./components/student/student.component";
import {RegistrationComponent} from "./components/registration/registration.component";
import {LoginComponent} from "./components/login/login.component";
import {ProfileComponent} from "./components/profile/profile.component";
import {GroupTeacherComponent} from "./components/teacher/components/group-teacher/group-teacher.component";
import {ConstructorComponent} from "./components/teacher/components/constructor/constructor.component";
import {GroupDetailedTeacherComponent} from "./components/teacher/components/group-detailed-teacher/group-detailed-teacher.component";
import {GroupListTeacherComponent} from "./components/teacher/components/group-list-teacher/group-list-teacher.component";
import {TeacherComponent} from "./components/teacher/teacher.component";
import {TasksStudentComponent} from "./components/student/components/tasks-student/tasks-student.component";
import {StudentMainComponent} from "./components/student/components/student-main/student-main.component";
import {GroupStudentComponent} from "./components/student/components/group-student/group-student.component";
import {
  GroupListStudentComponent
} from "./components/student/components/group-list-student/group-list-student.component";
import {
  GroupDetailedStudentComponent
} from "./components/student/components/group-detailed-student/group-detailed-student.component";
import {TaskConstructorComponent} from "./components/teacher/components/task-constructor/task-constructor.component";
import {
  QuestionsConstructorComponent
} from "./components/teacher/components/questions-constructor/questions-constructor.component";
import {TasksTeacherComponent} from "./components/teacher/components/tasks/tasks-teacher.component";
import {TaskListTeacherComponent} from "./components/teacher/components/task-list-teacher/task-list-teacher.component";
import {TaskListStudentComponent} from "./components/student/components/task-list-student/task-list-student.component";
import {
  TaskDetailsStudentComponent
} from "./components/student/components/task-details-student/task-details-student.component";
import {
  TaskDetailsTeacherComponent
} from "./components/teacher/components/task-details-teacher/task-details-teacher.component";
import {StatisticsComponent} from "./components/statistics/statistics.component";


const routesGroupTeacher: any =
  { path: 'group', component: GroupTeacherComponent, children: [
    { path: 'list', component: GroupListTeacherComponent},
    { path: 'details/:id', component: GroupDetailedTeacherComponent},
    ]
  };

const routesGroupStudent: any =
  { path: 'group', component: GroupStudentComponent, children: [
    { path: 'list', component: GroupListStudentComponent},
    { path: 'details/:id', component: GroupDetailedStudentComponent},
    ]
  };

const routesTaskTeacher: any =
  { path: 'task', component: TasksTeacherComponent, children: [
    { path: 'list', component: TaskListTeacherComponent},
    { path: 'details/:id', component: TaskDetailsTeacherComponent},
    ]
  };

const routesTaskStudent: any =
  { path: 'task', component: TasksStudentComponent, children: [
    { path: 'list', component: TaskListStudentComponent},
    // { path: 'details/:id', component: TaskDetailsStudentComponent},
    ]
  };

const routesConstructor: any =
  { path: 'constructor', component: ConstructorComponent, children: [
      { path: 'task-constructor', component: TaskConstructorComponent},
      { path: 'questions-constructor', component: QuestionsConstructorComponent},
    ]
  };

const routes: Routes = [
  { path: '', redirectTo: 'main', pathMatch: 'full' },
  { path: 'main', component: MainComponent },
  { path: 'student', component: StudentComponent, children: [
      { path: 'main', component: StudentMainComponent },
      { path: 'profile', component: ProfileComponent },
      { path: 'statistics', component: StatisticsComponent },
      routesGroupStudent, routesTaskStudent
    ]},
  { path: 'teacher', component: TeacherComponent, children: [
      { path: 'profile', component: ProfileComponent },
      { path: 'statistics', component: StatisticsComponent },
      routesConstructor, routesGroupTeacher, routesTaskTeacher
    ]
  },
  { path: 'task', component: TasksStudentComponent, children: [
    { path: 'details/:id', component: TaskDetailsStudentComponent},
    ]},
  { path: 'login', component: LoginComponent },
  { path: 'registration', component: RegistrationComponent },
  // { path: '**', redirectTo: 'main'},
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
    CommonModule
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
