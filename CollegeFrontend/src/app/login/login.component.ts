import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import {Router} from "@angular/router"

import { Logininfo } from "../interfaces/logininfo"
import { AuthService } from "../services/auth.service"

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  public loginFailed = false;

  constructor(private auth: AuthService, private router: Router) { }

  ngOnInit(): void {
    if(sessionStorage.getItem("token")){
      this.router.navigate(["/dashboard"])
    }
  }

  email = new FormControl('');
  password = new FormControl('');

  login(){
    var loginInfo: Logininfo = {
      email: this.email.value,
      password: this.password.value
    }

    this.auth.login(loginInfo).subscribe({
      next: data => {
        sessionStorage.setItem("token", String(data));
        
        this.router.navigate(["/dashboard"])
      },

      error: error => {
        this.loginFailed = true;
      }
    });
  }
}
