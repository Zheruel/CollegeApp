import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LoginlayoutComponent } from "./layouts/loginlayout/loginlayout.component"
import { LoginComponent } from "./login/login.component"
import { RegisterComponent } from "./register/register.component"
import { DashboardlayoutComponent } from "./layouts/dashboardlayout/dashboardlayout.component"
import { MajorsComponent } from "./dashboardcomponents/majors/majors.component"

const routes: Routes = [
  {
    path: "dashboard",
    component: DashboardlayoutComponent,
    children: [
      {
        path: "majors",
        component: MajorsComponent,
      }
    ],
  },
  {
    path: "",
    component: LoginlayoutComponent,
    children: [
      {
        path: "login",
        component: LoginComponent,
      },
      {
        path: "register",
        component: RegisterComponent,
      }
    ],
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
