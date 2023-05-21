import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainComponent } from "./components/main/main.component";
import {TasksComponent} from "./components/tasks/tasks.component";
import {CommonModule} from "@angular/common";
import {StudentComponent} from "./components/student/student.component";
import {RegistrationComponent} from "./components/registration/registration.component";
import {LoginComponent} from "./components/login/login.component";
import {TeacherComponent} from "./components/teacher/teacher.component";
import {ProfileComponent} from "./components/profile/profile.component";
import {GroupsComponent} from "./components/groups/groups.component";
import {ConstructorComponent} from "./components/constructor/constructor.component";


const routes: Routes = [
  { path: '', redirectTo: 'main', pathMatch: 'full' },
  { path: 'main', component: MainComponent },
  { path: 'student', component: StudentComponent },
  // { path: 'teacher', component: TeacherComponent },
  { path: 'teacher', component: GroupsComponent },
  { path: 'groups', component: GroupsComponent },
  { path: 'profile', component: ProfileComponent },
  { path: 'constructor', component: ConstructorComponent },
  { path: 'login', component: LoginComponent },
  { path: 'registration', component: RegistrationComponent },
  { path: 'tasks', component: TasksComponent},
  { path: '**', redirectTo: 'main'},
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes),
    CommonModule
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
