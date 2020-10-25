import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LoginlayoutComponent } from "./layouts/loginlayout/loginlayout.component"
import { LoginComponent } from "./login/login.component"

const routes: Routes = [
  {
    path: "",
    component: LoginlayoutComponent, // this is the component with the <router-outlet> in the template
    children: [
      {
        path: "login", // child route path
        component: LoginComponent, // child route component that the router renders
      }
    ],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
