import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router"

import { AuthService } from "../../services/auth.service"

@Component({
  selector: 'app-loginlayout',
  templateUrl: './loginlayout.component.html',
  styleUrls: ['./loginlayout.component.css']
})
export class LoginlayoutComponent implements OnInit {

  constructor(private auth: AuthService, private router: Router) { }

  ngOnInit(): void {
    if(sessionStorage.getItem("token")){
      this.router.navigate(["/dashboard"]);
    }

    if(this.router.url == "/"){
      this.router.navigate(["/login"]);
    }
  }

}
