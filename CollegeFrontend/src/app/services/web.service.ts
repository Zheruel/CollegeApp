import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import {Router} from "@angular/router"

import { Registerinfo } from "../interfaces/registerinfo"
import { Major } from "../interfaces/major"


@Injectable({
  providedIn: 'root'
})
export class WebService {
  
  constructor(private http: HttpClient, private router: Router) { }
  
  addStudent(userInfo: Registerinfo){
    return this.http.post("http://localhost:5000/students/", userInfo);
  }

  getMajors(){
    return this.http.get<Major[]>("http://localhost:5000/majors", 
    {
      headers: new HttpHeaders().set("Authorization", sessionStorage.getItem("token")),
    });
  }
}
