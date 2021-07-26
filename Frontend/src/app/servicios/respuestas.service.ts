import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http'
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RespuestasService {

  private BASE_URL = 'http://localhost:5000'
  constructor(private http:HttpClient) { }

  getAnsweres():Observable<any>{
    return this.http.get(`${this.BASE_URL}/get-Is-Answered-get`)
  }
}
