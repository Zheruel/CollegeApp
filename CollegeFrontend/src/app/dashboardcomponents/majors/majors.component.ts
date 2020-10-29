import { Component, OnInit } from '@angular/core';
import { Major } from 'src/app/interfaces/major';

import { WebService } from "../../services/web.service"

@Component({
  selector: 'app-majors',
  templateUrl: './majors.component.html',
  styleUrls: ['./majors.component.css']
})
export class MajorsComponent implements OnInit {
  constructor(private webService: WebService) { }

  public majorList: Major[] = null;

  ngOnInit(): void {
    this.webService.getMajors().subscribe({
      next: data => {
        this.majorList = data;
        console.log(this.majorList)
      }
    });
  }

}
