import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';
import {Router} from "@angular/router"

import { WebService } from "../services/web.service"
import { Registerinfo } from "../interfaces/registerinfo"

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {
  constructor(private webService: WebService, private router: Router) { }

  ngOnInit(): void {
  }

  public registerFailed = false;

  firstName = new FormControl('');
  lastName = new FormControl('');
  email = new FormControl('');
  password = new FormControl('');

  register(){
    var studentInfo: Registerinfo = {
      firstName: this.firstName.value,
      lastName: this.lastName.value,
      email: this.email.value,
      password: this.password.value,
    }

    this.webService.addStudent(studentInfo).subscribe({
      next: data => {
        console.log(data);

        this.router.navigate(["/login"])
      },

      error: error => {
        this.registerFailed = true;
      }
    });
  }
}
