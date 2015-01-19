# Destinaty
This is a code repository for our group's work during the 3rd ever HWeekend event.
This event took place at Oregon State University on January 17-18, 2015 and was sponsored by Micron. HWeekend (short for Hardware Weekend) is a 30 hour engineering event for OSU Engineering students of all levels.

This project took the form of a small car with two fixed, individually motored wheels in the front and a caster wheel in the back. It uses two ultrasonic sensors (HC-SR04) to judge distances to obstructions and turn to avoid them. The body casing is laser cut acryllic cut acryllic and some internal parts were printed with 3D printers. Inside, the car runs on a Raspberry Pi with the Raspbian OS and has one motor controller as well as a switch to toggle the program.

All programming for this project was done in python.
* stop-motors.py is a simple script that stops all the motors in case they were running.
* destinaty.py is the original code to run the car.
* destianty_switch.py contains improvements to destinaty.py as well as implementation of a switch to start and stop the car.
* destinaty_switch_bluetooth.py contains basic bluetooth implementation for starting and stopping the program as well.
