import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router"

import { AuthService } from "../../services/auth.service"
import { Token } from "../../interfaces/token"
import { Validateduser } from "../../interfaces/validateduser"

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['../../layouts/dashboardlayout/dashboardlayout.component.css']
})
export class SidebarComponent implements OnInit {
  constructor(private auth: AuthService, private router: Router) { }

  ngOnInit(): void {
    if(sessionStorage.getItem("token")){
      var token: Token = {
        token: sessionStorage.getItem("token")
      }

      this.auth.userValidate(token).subscribe({
        next: data => {
          this.userInfo = data;
        }
      });
    }
  }

  public userInfo: Validateduser;

  logout(){
    sessionStorage.removeItem("token");

    this.router.navigate(["/login"]);
  }
}
