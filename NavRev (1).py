# color_tracking_v1.py
# usb camera: Microsoft HD-3000 target: orange basketball
# This program was designed to have SCUTTLE following a basketball.
# The calibration was made in a brightly lit indoor environment.
# Video demo: https://youtu.be/9t1XHcomlIs
# color Tracking
import numpy as np      # Kernel
import time

import L1_lidar as lidar
import L2_vector as vector
import L1_motors as motors
import L1_ultrasonic as ultrasonic
import L1_servos as servos
import rcpy.sero as servo
import rcpy.clock as clock

print("loading rcpy.")
import rcpy                 # Import rcpy library
import rcpy.motor as motor  # Import rcpy motor module
print("finished loading libraries.")
import math

def main():
    candistance = ultrasonic.distanceMeasurement(ultrasonic.trig_pin,ultrasonic.echo_pin)
    if candistance < 5:
        print("ready")

        duty_l = 0 # initialize motor with zero duty cycle
        duty_r = 0 # initialize motor with zero duty cycle

        print("initializing rcpy...")
        rcpy.set_state(rcpy.RUNNING)        # initialize rcpy
        print("finished initializing rcpy.")

        try:

            while rcpy.get_state() != rcpy.EXITING:

                if rcpy.get_state() == rcpy.RUNNING:
                    x = 0
                    
                    motor_r = 2 	# Right Motor assigned to #2
                    motor_l = 1 	# Left Motor assigned to #1
                    
                    while x < 20
                    
                        clo = vector.getNearest()
                        
                            #Convert to angle and distance 
                        u = math.sin(clo[1])
                        dis = clo[0] * abs(u)
                        v = math.cos(clo[1])
                        dis2 = clo[0] * abs(v)
                        

                        dir = "driving"

                            
                        if clo[1] < 0 and clo[1] >= -75 and dis < 0.2 and dis2 < 0.2:
                            print(dis)
                            motor.set(motor_l, -0.6)
                            motor.set(motor_r, 0.62)
                            time.sleep(2.75)
                            motor.set(motor_l, 0)
                            motor.set(motor_r, 0)
                            time.sleep(0.5)
                            motor.set(motor_l, 0.97)
                            motor.set(motor_r, 1)
                            time.sleep(0.5)
                            motor.set(motor_l, 0)
                            motor.set(motor_r, 0)
                            time.sleep(0.5)
                            motor.set(motor_l, 0.6)
                            motor.set(motor_r, -0.62)
                            time.sleep(2.75)
                            motor.set(motor_l, 0)
                            motor.set(motor_r, 0)
                            time.sleep(0.5)
                            duty_r = 0
                            duty_l = 0
                            
                            #Case 2: obstruction the the right of the SCUTTLE
                        
                        elif clo[1] > 0 and clo[1] <= 75 and dis < 0.15 and dis2 < 0.15 :
                            print(dis)
                            motor.set(motor_l, 0.6)
                            motor.set(motor_r, -0.62)
                            time.sleep(2.75)
                            motor.set(motor_l, 0)
                            motor.set(motor_r, 0)
                            time.sleep(0.5)
                            motor.set(motor_l, 0.97)
                            motor.set(motor_r, 1)
                            time.sleep(0.5)
                            motor.set(motor_l, 0)
                            motor.set(motor_r, 0)
                            time.sleep(0.5)
                            motor.set(motor_l, -0.6)
                            motor.set(motor_r, 0.62)
                            time.sleep(2.75)
                            motor.set(motor_l, 0)
                            motor.set(motor_r, 0)
                            time.sleep(0.5)
                        else
                            motor.set(motor_l, 0.97)
                            motor.set(motor_r, 1)
                            time.sleep(0.5)
                            motor.set
                        x = x+1
            
                    # start clock
                    servos.clck.start()			# Starts PWM 1
                    servos.clck2.start()		# Starts PWM 2
                    # keep running
                    servos.srvo.set(servos.duty)	# Set motor 1 duty
                    servos.srvo2.set(servos.duty2)  #set motor 2 duty
                    while(x<5750):
                        x = x + 1
                        print(x)
                    print("out of loop")	
                    servos.srvo.set(servos.off)
                    servos.srvo2.set(servos.off)
                    print("off")
                                # stop clock
                    servos.clck.stop()
                    servos.clck2.stop()
		                        
                    rcpy.set_state(rcpy.EXITING)
                    pass
                elif rcpy.get_state() == rcpy.PAUSED:
                    pass

        except KeyboardInterrupt: # condition added to catch a "Ctrl-C" event and exit cleanly
            rcpy.set_state(rcpy.EXITING)
            pass

        finally:

    	    rcpy.set_state(rcpy.EXITING)
    	    print("Exiting Color Tracking.")

    # exiting program will automatically clean up cape
    elif candistance > 5:
	    print("Error: No can")
if __name__ == '__main__':
    main()