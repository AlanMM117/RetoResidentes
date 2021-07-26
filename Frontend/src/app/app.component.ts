import { Component } from '@angular/core';
import { Respuestas } from './modelos/respuestas';
import { RespuestasService } from './servicios/respuestas.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  respuestaArray:Respuestas[] = [];
  constructor(private respuestasService:RespuestasService){

  }

  ngOnInit(): void {
    //Called after the constructor, initializing input properties, and the first call to ngOnChanges.
    //Add 'implements OnInit' to the class.
    this.respuestasService.getAnsweres()
    .subscribe(data=>{
      console.log(data)
      this.respuestaArray = data.data
    },
    error=>console.log(error)   );
  }
}
