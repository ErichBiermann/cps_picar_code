# this class uses built-in functions of the manufacturer's picar-library
# available at  https://github.com/sunfounder/picar-4wd

import picar_4wd as fc   
import time


class Pathfinder():
    def __init__(self, min_angle = -90, max_angle = 90, STEP = 18, TURN_FACTOR = 0.008) -> None:
        self.min_angle = min_angle    
        self.max_angle = max_angle
        self.current_angle = min_angle
        self.STEP = STEP
        self.us_step = STEP
        self.scan_dict = {}
        self.speed = 1
        self.TURN_SPEED = 30
        self.TURN_FACTOR = TURN_FACTOR
        
    # the scan_step_cps method iterates through all
    # the angles from the minimum angle to the maximum
    # angle with an angular distance given by STEP
    # and stores angle and distance as key-value
    # pairs on scan_dict like e.g (-72: 45.39)
        
    def scan_step_cps(self):
        angle_count = int((abs(self.max_angle - self.min_angle)/self.us_step) + 1)
        self.current_angle += self.us_step
        if self.current_angle >= self.max_angle:
            self.current_angle = self.max_angle
            self.us_step = -self.STEP
        elif self.current_angle <= self.min_angle:
            self.current_angle = self.min_angle
            self.us_step = self.STEP
        distance = fc.get_distance_at(self.current_angle)

        self.scan_dict[self.current_angle] = distance
        if len(self.scan_dict) == angle_count:
            for key, value in self.scan_dict.items():    # -2 is the time-out-value given back by the 
                if value == -2:                          # ultrasonic sensor class, if echoes do not 
                    self.scan_dict[key] = 200            # return (Which is here intrepreted as 2 m 
            tmp = self.scan_dict.copy()                  # distance without obstacle)
            self.scan_dict = {}
            return tmp
        else:
            return False
        
    # maneuvers, using picar-library functions to 
    # start and stop PiCar motors on all four wheels

    def backoff(self):
        fc.stop
        fc.backward(self.speed)
        time.sleep(0.5)
        fc.stop
        
    def right_turn(self, angle):
        fc.turn_right(self.TURN_SPEED)                    
        time.sleep(abs(angle) * self.TURN_FACTOR)
        fc.stop
        time.sleep(0.1)
        
    def left_turn(self, angle):
        fc.turn_left(self.TURN_SPEED)                    
        time.sleep(abs(angle) * self.TURN_FACTOR)
        fc.stop
        time.sleep(0.1)
        
    # the main method, in which measurement results 
    # of the ultrasonic sensor are subjected to the control flow
        
    def steer(self):
        fc.servo.set_angle(0)

        while(True):
            fc.stop()
            distance = self.scan_step_cps()
            if not distance:
                continue
            time.sleep(0.5)
            max_winkel = max(distance, key=distance.get)
            max_distance = distance[max_winkel]
            time.sleep(0.5)
            
            if max_distance > 0:
                
                if distance[0] < 10 or distance[self.STEP] < 10 or distance[-self.STEP] < 10:
                    self.backoff()
                    
                if distance[self.max_angle] < 5:  
                    self.backoff() 
                    self.right_turn(max_winkel)
                
                if distance[self.min_angle] < 5:
                    self.backoff() 
                    self.left_turn(max_winkel)
                    
                if max_winkel < 0:
                        self.right_turn(max_winkel)

                if max_winkel > 0:
                        self.left_turn(max_winkel)
            
            fc.forward(self.speed/2)
            time.sleep(0.55)
                    
                