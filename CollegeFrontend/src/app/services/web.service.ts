import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Router} from "@angular/router"

import { Registerinfo } from "../interfaces/registerinfo"


@Injectable({
  providedIn: 'root'
})
export class WebService {

  constructor(private http: HttpClient, private router: Router) { }
  
  addStudent(userInfo: Registerinfo){
    return this.http.post("http://localhost:5000/students/", userInfo);
  }
}
