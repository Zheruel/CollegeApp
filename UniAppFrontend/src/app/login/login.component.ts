import { Component, OnInit } from '@angular/core';
import { AuthService } from "../services/auth.service"
import { FormControl } from '@angular/forms';
import { UserLogin } from '../interfaces/user-login';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  constructor(private authService: AuthService) { }

  ngOnInit(): void {
    if(sessionStorage.getItem("token") != null){
      console.log("Token is here");
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
        sessionStorage.setItem("token", data)
        console.log(sessionStorage.getItem("token"));
      },
      error: error => {
        console.log(error);
      }
    });
  }

}
