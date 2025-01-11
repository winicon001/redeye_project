import encoders
import move
import time
import RPi.GPIO as GPIO
import arduinosensorsdata

speed = 50
init_yaw = 0

move.setup()
arduinosensorsdata.reading.checkdata()
print("Setting up sensors feed...Please wait")
time.sleep(5)


while True:
    # Encoders Readings

    arduino_read_values = arduinosensorsdata.reading.checkdata()
    dist = arduino_read_values[0]
    yaw = float(arduino_read_values[1])
    pitch = float(arduino_read_values[2])
    row = float(arduino_read_values[3])

      


    enc1 = encoders.enc()[0]       # Left Encoder instantaneous 
    enc1Total = encoders.enc()[1]  # Left Encoder total ticks coutns
    Rev_L = encoders.enc()[2]      # Number of Revolutions for Left wheel
    dist_L = encoders.enc()[3]     # Total distance travelled for Left Wheel
    enc2 = encoders.enc()[4]       # Right Encoder instantaneous counts
    enc2Total = encoders.enc()[5]  # Right Encoder total ticks count
    Rev_R = encoders.enc()[6]      # Number of Revolutions for Right wheel
    dist_R = encoders.enc()[7]     # Total distance travelled for Right Wheel

    # Sensors Data Processing
    abs_yaw = abs(yaw)
    
    if (dist_L == 0.0 and dist_R == 0.0):
        init_yaw = abs_yaw
    true_yaw = round((abs(init_yaw - abs_yaw)), 2)

    # Remove String character from Sensor readings from ESP32
    numeric_part = ''.join(char for char in dist if char.isdigit() or char == '.')

    # Remove white space from Sensor readings from ESP32
    clean_part = numeric_part.strip().replace(' ', '')

    # Convert Sensor readings from ESP32 to float data type
    obstacle_dist = float(clean_part)

    def data():
        print('obstacle at: ', obstacle_dist, '|', end = ' ')
        print('Yaw:', yaw, '| ', end = ' ')
        print('abs_Yaw:', abs_yaw, '| ', end = ' ')
        print('true_Yaw:', true_yaw, '| ', end = ' ')
        print('Pitch: ', pitch, '| ', end = '')
        print('Row: ', row, '| ', end = '')
        print('enc1_', enc1,'| ', end= '')
        print('enc1Total', enc1Total,'|', end= '')
        print('Rev_L', Rev_L,'| ', end= '')
        print('dist_L', dist_L,'| ', end= '')
        print('enc2', enc2,'| ', end= '')
        print('enc2Total', enc2Total,'| ', end= '')
        print('Rev_R', Rev_R,'| ', end= '')
        print('dist_R', dist_R)


    # Change obstacle distance based on environmental features
    if (obstacle_dist <=20.0):
        while true_yaw < 90:
            move.move(speed, direction = "backward", turn = "left")
            data()

    else:
        # move.move(speed, direction = "forward", turn = "")
        init_yaw = true_yaw
        move.move(speed, direction = "forward", turn = "")
        data()
        
