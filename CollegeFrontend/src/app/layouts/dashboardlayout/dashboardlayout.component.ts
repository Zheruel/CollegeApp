import { Component, OnInit } from '@angular/core';

import { AuthService } from "../../services/auth.service"

@Component({
  selector: 'app-dashboardlayout',
  templateUrl: './dashboardlayout.component.html',
  styleUrls: ['./dashboardlayout.component.css']
})
export class DashboardlayoutComponent implements OnInit {

  constructor(private auth: AuthService) { }

  ngOnInit(): void {
    this.auth.confirmSession();
  }

}
