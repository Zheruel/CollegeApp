import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Router} from "@angular/router"

import { Logininfo } from "../interfaces/logininfo"
import { Token } from "../interfaces/token"
import { Validateduser } from "../interfaces/validateduser"

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient, private router: Router) { }

  login(loginInfo: Logininfo){
    return this.http.post("http://localhost:5000/login", loginInfo);
  }

  validateToken(token: Token){
    return this.http.post("http://localhost:5000/token/validate", token);
  }

  refreshToken(token: Token){
    return this.http.post("http://localhost:5000/token/refresh", token);
  }

  userValidate(token: Token){
    return this.http.post<Validateduser>("http://localhost:5000/user/validate", token);
  }

  confirmSession(){
    if(sessionStorage.getItem("token")){
      var token: Token = {
        token: sessionStorage.getItem("token")
      }

      this.validateToken(token).subscribe({
        next: data =>{},

        error: error => {
          this.refreshToken(token).subscribe({
            next: data => {
              sessionStorage.setItem("token", String(data));
            },

            error: error => {
              sessionStorage.removeItem("token");
              
              this.router.navigate(["/login"]);
            }
          });
        }
      });
    }

    else{
      this.router.navigate(["/login"]);
    }
  }
}
 