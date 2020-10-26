import { Component, OnInit } from '@angular/core';
import { FormControl } from '@angular/forms';

import { Logininfo } from "../interfaces/logininfo"

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }

  email = new FormControl('');
  password = new FormControl('');

  login(){
    var loginInfo: Logininfo = {
      email: this.email.value,
      password: this.password.value
    }

    
  }
}
