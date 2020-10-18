import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { UserLogin } from '../interfaces/user-login';
import { Token } from "../interfaces/token"

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  constructor(private http: HttpClient) { }

  login(user: UserLogin){
    return this.http.post<string>("http://localhost:5000/login", user);
  }

  refreshToken(token: Token){
    return this.http.post<string>("http://localhost:5000/token/refresh", token);
  }

  verifyToken(token: Token){
    return this.http.post<string>("http://localhost:5000/token/validate", token);
  }
}
