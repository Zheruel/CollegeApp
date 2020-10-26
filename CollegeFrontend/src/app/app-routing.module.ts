import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LoginlayoutComponent } from "./layouts/loginlayout/loginlayout.component"
import { LoginComponent } from "./login/login.component"
import { RegisterComponent } from "./register/register.component"
import { DashboardlayoutComponent } from "./layouts/dashboardlayout/dashboardlayout.component"

const routes: Routes = [
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
  },
  {path: "dashboard", component: DashboardlayoutComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
