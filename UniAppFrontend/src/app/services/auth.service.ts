import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { UserLogin } from '../interfaces/user-login';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  constructor(private http: HttpClient) { }

  login(user: UserLogin){
    return this.http.post<string>("http://localhost:5000/login", user);
  }

  verifyToken(token: string){
    return this.http.post<boolean>("http://localhost:5000/token/validate", token);
  }

  refreshToken(token: string){
    return this.http.post<string>("http://localhost:63402/token/refresh", token);
  }
}
