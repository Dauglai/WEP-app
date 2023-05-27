import {Component, EventEmitter, Input, Output} from '@angular/core';
import {FormControl, FormGroup, Validators} from "@angular/forms";
import {GroupService} from "../../../../servicies/group.service";

@Component({
  selector: 'app-dialog-window-test-start',
  templateUrl: './dialog-window-test-start.component.html',
  styleUrls: ['./dialog-window-test-start.component.css']
})
export class DialogWindowTestStartComponent {
  @Input() curTest: any = {};
  @Output() protected isOpen: EventEmitter<boolean> = new EventEmitter<boolean>();

  protected manageDialog() {
    this.isOpen.emit(false);
  }

}
