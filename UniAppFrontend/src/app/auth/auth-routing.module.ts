import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LayoutComponent } from "../auth/layout/layout.component"
import { LoginComponent } from "../auth/login/login.component"

const routes: Routes = [
  { 
    path: '', 
    component: LayoutComponent,
    children: [
      { path: "login", component: LoginComponent},
    ]
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AuthRoutingModule { }