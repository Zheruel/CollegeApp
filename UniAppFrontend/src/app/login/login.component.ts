import { Component, OnInit } from '@angular/core';
import { AuthService } from "../services/auth.service"
import { FormControl } from '@angular/forms';
import { UserLogin } from '../interfaces/user-login';
import { Token } from '../interfaces/token';
import {Router} from "@angular/router"

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  constructor(private authService: AuthService, private router: Router) { }

  ngOnInit(): void {
    var token: Token = {
      token: sessionStorage.getItem("token"),
    }
    
    if(token.token != null){
      this.authService.verifyToken(token).subscribe({
        next: data => {
          this.router.navigate([""]);
        },
        error: error => {
          this.authService.refreshToken(token).subscribe({
            next: data => {
              sessionStorage.setItem("token", data);

              this.router.navigate([""]);
            },
            error: error => {
              console.log(error);
              sessionStorage.removeItem("token");
            }
          });
        }
      });
    }
  }
  
  email = new FormControl("");
  password = new FormControl("");

  login(){
    var loginInfo: UserLogin = {
      email: this.email.value,
      password: this.password.value
    }

    this.authService.login(loginInfo).subscribe({
      next: data => {
        sessionStorage.setItem("token", data);

        this.router.navigate([""]);
      },
      error: error => {
        console.log(error);
      }
    });
  }
}
