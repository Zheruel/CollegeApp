import { Component, OnInit } from '@angular/core';
import {Router} from "@angular/router"
import { AuthService } from "../services/auth.service"
import { Token } from "../interfaces/token"

@Component({
  selector: 'app-main-portal',
  templateUrl: './main-portal.component.html',
  styleUrls: ['./main-portal.component.css']
})
export class MainPortalComponent implements OnInit {

  constructor(private router: Router, private authService: AuthService) { }

  ngOnInit(): void {
    var token: Token = {
      token: sessionStorage.getItem("token"),
    }

    if(token.token == null){
      this.router.navigate(["login"]);
    }
  }
}
