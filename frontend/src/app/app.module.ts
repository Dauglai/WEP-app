import { NgDompurifySanitizer } from "@tinkoff/ng-dompurify";
import {TuiRootModule, TuiDialogModule, TuiAlertModule, TUI_SANITIZER, TuiButtonModule} from "@taiga-ui/core";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import {RouterLink, RouterOutlet} from "@angular/router";
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import { HttpClientModule } from "@angular/common/http";
import { StudentComponent } from './components/student/student.component';
import { TeacherComponent } from './components/teacher/teacher.component';
import { AccountComponent } from './components/account/account.component';
import { RegistrationComponent } from './components/registration/registration.component';
import { LoginComponent } from './components/login/login.component';
import { MainComponent } from './components/main/main.component';
import { AppRoutingModule } from "./app-routing.module";
import { HeaderComponent } from './components/header/header.component';
import { ProfileComponent } from './components/profile/profile.component';
import { GroupTeacherComponent } from './components/teacher/components/group-teacher/group-teacher.component';
import { ConstructorComponent } from './components/teacher/components/constructor/constructor.component';
import {DialogWindowComponent} from "./components/dialog-window/dialog-window.component";
import { GroupDetailedTeacherComponent } from './components/teacher/components/group-detailed-teacher/group-detailed-teacher.component';
import {TuiAccordionModule} from "@taiga-ui/kit";
import {NavigationBarStudentComponent} from "./components/student/components/navigation-bar-student/navigation-bar-student.component";
import {NavigationBarTeacherComponent} from "./components/teacher/components/navigation-bar-teacher/navigation-bar-teacher.component";
import { GroupListTeacherComponent } from './components/teacher/components/group-list-teacher/group-list-teacher.component';
import { StudentMainComponent } from './components/student/components/student-main/student-main.component';
import {TasksTeacherComponent} from "./components/teacher/components/tasks/tasks-teacher.component";
import {TasksStudentComponent} from "./components/student/components/tasks-student/tasks-student.component";
import {
  GroupDetailedStudentComponent
} from "./components/student/components/group-detailed-student/group-detailed-student.component";
import {
  GroupListStudentComponent
} from "./components/student/components/group-list-student/group-list-student.component";
import {GroupStudentComponent} from "./components/student/components/group-student/group-student.component";
import { TaskConstructorComponent } from './components/teacher/components/task-constructor/task-constructor.component';
import { QuestionsConstructorComponent } from './components/teacher/components/questions-constructor/questions-constructor.component';
import { TaskListTeacherComponent } from './components/teacher/components/task-list-teacher/task-list-teacher.component';
import { TaskListStudentComponent } from './components/student/components/task-list-student/task-list-student.component';
import { TaskDetailsStudentComponent } from './components/student/components/task-details-student/task-details-student.component';
import { TaskDetailsTeacherComponent } from './components/teacher/components/task-details-teacher/task-details-teacher.component';
import {
  DialogWindowStudentComponent
} from "./components/student/components/dialog-window-student/dialog-window-student.component";
import { StatisticsComponent } from './components/statistics/statistics.component';
import {
  DialogWindowTeacherComponent
} from "./components/teacher/components/dialog-window-teacher/dialog-window-teacher.component";
import { DialogWindowTestStartComponent } from './components/student/components/dialog-window-test-start/dialog-window-test-start.component';


@NgModule({
  declarations: [
    AppComponent,
    StudentComponent,
    TeacherComponent,
    AccountComponent,
    RegistrationComponent,
    LoginComponent,
    MainComponent,
    NavigationBarTeacherComponent,
    HeaderComponent,
    ProfileComponent,
    GroupTeacherComponent,
    ConstructorComponent,
    DialogWindowComponent,
    GroupDetailedTeacherComponent,
    NavigationBarStudentComponent,
    GroupListTeacherComponent,
    StudentMainComponent,
    TasksTeacherComponent,
    TasksStudentComponent,
    GroupStudentComponent,
    GroupDetailedStudentComponent,
    GroupListStudentComponent,
    TaskConstructorComponent,
    QuestionsConstructorComponent,
    TaskListTeacherComponent,
    TaskListStudentComponent,
    TaskDetailsStudentComponent,
    TaskDetailsTeacherComponent,
    DialogWindowStudentComponent,
    StatisticsComponent,
    DialogWindowTeacherComponent,
    DialogWindowTestStartComponent,
  ],
    imports: [
        TuiButtonModule,
        BrowserModule,
        AppRoutingModule,
        HttpClientModule,
        RouterOutlet,
        FormsModule,
        RouterLink,
        BrowserAnimationsModule,
        TuiRootModule,
        TuiDialogModule,
        TuiAlertModule,
        ReactiveFormsModule,
        TuiAccordionModule,
    ],
  providers: [{provide: TUI_SANITIZER, useClass: NgDompurifySanitizer}],
  bootstrap: [AppComponent]
})
export class AppModule { }
