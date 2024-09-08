import encoders
import move
import time
import RPi.GPIO as GPIO
# from ultra_2 import reading
import ultra_2

speed = 80

move.setup()

while True:

    arduino_read_value = ultra_2.reading.checkdist()

    # Remove String character from Sensor readings from ESP32
    numeric_part = ''.join(char for char in arduino_read_value if char.isdigit() or char == '.')

    # Remove white space from Sensor readings from ESP32
    clean_part = numeric_part.strip().replace(' ', '')

    # Convert Sensor readings from ESP32 to float data type
    obstacle_dist = float(clean_part)

    # print("Message is :  ", arduino_read_value)
    # print("Message is :  ", obstacle_dist, end = " ")
    







    # y = float(obstacle_dist) #+ 10.5
    # print(obstacle_dist, y)
    # encoders.enc()
    # move.move(speed+10, direction = "forward", turn = "")

    
    if (obstacle_dist <= 10.0):
        move.move(speed, direction = "backward", turn = "left")
        # ultra_2.reading.checkdist()
        print('obstacle at: ', obstacle_dist, '|', end = ' ')
        encoders.enc()
        

    
    else:
        move.move(speed+10, direction = "forward", turn = "")
        # ultra_2.reading.checkdist()
        print('obstacle at: ', obstacle_dist, '|', end = ' ')
        encoders.enc()

    
