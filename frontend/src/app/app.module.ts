import { NgDompurifySanitizer } from "@tinkoff/ng-dompurify";
import {TuiRootModule, TuiDialogModule, TuiAlertModule, TUI_SANITIZER, TuiButtonModule} from "@taiga-ui/core";
import { BrowserAnimationsModule } from "@angular/platform-browser/animations";
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import {RouterLink, RouterOutlet} from "@angular/router";
import { TasksComponent } from './components/tasks/tasks.component';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import { HttpClientModule } from "@angular/common/http";
import { StudentComponent } from './components/student/student.component';
import { TeacherComponent } from './components/teacher/teacher.component';
import { AccountComponent } from './components/account/account.component';
import { RegistrationComponent } from './components/registration/registration.component';
import { LoginComponent } from './components/login/login.component';
import { MainComponent } from './components/main/main.component';
import { AppRoutingModule } from "./app-routing.module";
import { NavigationBarComponent } from './components/navigation-bar/navigation-bar.component';
import { HeaderComponent } from './components/header/header.component';
import { ProfileComponent } from './components/profile/profile.component';
import { GroupsComponent } from './components/groups/groups.component';
import { ConstructorComponent } from './components/constructor/constructor.component';

@NgModule({
  declarations: [
    AppComponent,
    TasksComponent,
    StudentComponent,
    TeacherComponent,
    AccountComponent,
    RegistrationComponent,
    LoginComponent,
    MainComponent,
    NavigationBarComponent,
    HeaderComponent,
    ProfileComponent,
    GroupsComponent,
    ConstructorComponent,
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
  ],
  providers: [{provide: TUI_SANITIZER, useClass: NgDompurifySanitizer}],
  bootstrap: [AppComponent]
})
export class AppModule { }
