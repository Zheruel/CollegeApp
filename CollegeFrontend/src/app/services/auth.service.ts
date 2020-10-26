import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import { Logininfo } from "../interfaces/logininfo"

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(private http: HttpClient) { }

  login(loginInfo: Logininfo){
    this.http.post("")
  }
}
 