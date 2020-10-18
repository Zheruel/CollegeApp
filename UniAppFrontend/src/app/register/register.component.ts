import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import { UserRegister } from "../interfaces/user-register"
import { WebService } from "../services/webservice.service"
import { Token } from "../interfaces/token"
import {Router} from "@angular/router"

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  constructor(private webService: WebService, private router: Router) { }

  ngOnInit(): void {
    var token: Token = {
      token: sessionStorage.getItem("token"),
    }

    if(token.token != null){
      this.router.navigate([""]);
    }
  }

  firstName = new FormControl("");
  lastName = new FormControl("");
  email = new FormControl("");
  password = new FormControl("");

  register(){
    var student: UserRegister = {
      firstName: this.firstName.value,
      lastName: this.lastName.value,
      email: this.email.value,
      password: this.password.value
    }

    this.webService.registerStudent(student).subscribe({
      next: data => {
        console.log(data)
      },
      error: error => {
        console.log(error);
      }
    });
  }
}
