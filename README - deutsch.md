# cps_picar_code
** Just a little showcase of we were doing at the DAA lately **

Der code besteht aus der Pathfinder-Klasse und dem Klassenaufruf. Er verwendet z.T. Standard-Funktionen aus den mitgelieferten Bibliotheken des Herstellers, die unter https://github.com/sunfounder/picar-4wd abrufbar sind. Der hier hochgeladene Code ist für sich allein nicht ausführbar.


Es handelt sich um einen einfachen 'gap-follow' - Algorithmus, bei dem sich das PiCar mithilfe des vorne montierten Ultraschallsensors seinen Weg durch ein Labyrinth oder einen geschlossenen Parcours sucht. Der Ultraschallsensor sitzt auf einem Sevormotor und kann in einem Bereich von 180° von links nach rechts und zurück gedreht werden. 

Dazu befindet sich ein Video von einer Testfahrt im Videoordner (testdrive-demo.mp4)! Und auch eins von der am Ende etwas holprigen, aber erfolgreichen Challenge auf der DAA-Tagung in Bielefeld (Challenge.mp4) :D! 

Beim Klassenaufruf wird über die Parameter min_angle und max_angle der abzutastende Bereich eingestellt. Als Default sind die vollen 180 ° gesetzt (-90° bis 90°, 0° ist "vorne"). Dazu kann eine Schrittweite (STEP) eingestellt werden, in welchem Winkelabstand jeweils der Abstand bis zu einem eventuellen Hindernis gemessen werden soll. 

Die Methode 'scan_step_cps' führt die eigentliche Messung aus. Dabei werden die Winkel mit den dazugehörigen, gemessenen Distanzen als Key-Value-Paare in ein Dictionary geschrieben, um für weitere Schritte mit diesen konkreten Winkelangaben ansprechbar zu sein.

In der Methode 'steer' wird die Fahrt gesteuert, indem aus diesen key-value-Paaren der Winkel mit der maximalen, messbaren Distanz ausgewählt wird. Das PiCar wird in Folge in die Richtung dieses Winkels gedreht (mit den Methoden right_turn und left_turn). Je größer die Differenz zum Winkel 0 ° (vorne), desto länger (über time.sleep).

Befindet sich das piCar weniger als 10 cm vor einem Hindernis, setzt es zurück und misst erneut. Dasselbe gilt für ein seitliches Hindernis in weniger als 5 cm, um zu verhindern, dass es sich verkeilt.

Der Code ist einfach aber robust und ermöglicht dem PiCar sich selbst aus Sackgassen wieder hinaus zu manövrieren.