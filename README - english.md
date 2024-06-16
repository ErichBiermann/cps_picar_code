# cps_picar_code
** Just a little showcase of we were doing at the DAA lately **

The code has two parts: The Pathfinder-class itself and a file to instantiate it.

It uses built-in functions of the manufacturer's PiCar library, available at  https://github.com/sunfounder/picar-4wd, and will not run on its own.

The code implements a rather simple 'gap-follow-algorithm' that maneuvers a PiCar through a labyrinth or parcours by measuring distances to obstacles with an ulatrasonic sensor that is mounted on a servo-motor at the front. It can be turned 180° left to right and back.

This is shown in a video in the Video folder (testdrive-demo.mp4)!
And there's also one from the final challenge at the DAA meeting in Bielefeld (Challenge.mp4), that went a little sideways, but in a good way, at the end :D. 

By instantiating the Pathfinder class, the angle range to scan by the ultrasonic sensor is set via the max_angle and min_angle attributes, which are set to 90° and -90° by default (front is 0°). Furthermore, a constant step size STEP can be set, which corresponds to the angular distances at which measurements will be taken. A smaller step size will take more measurements at smaller angular distances.

In the 'scan_step_cps' method the measurements (taken with the built-in distance_at-function) at the specific angles are stored in a dictionary as key-value pairs (e.g. -90: 34.43) so that they can be referred to as a particular angle by the other methods or the user, instantiating a class or altering the code.

If the PiCar faces an obstacle at a distance less than 10 cm, it will back off and measure again. The same behavior is coded for an obstacle to the side at less than 5 cm, to cope with situations where the picar is stuck at corners.

The code is simple but robust and even enables the car to maneuver itself out of dead ends.
