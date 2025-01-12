import serial

class reading:
    def checkdist():
        arduino_port = '/dev/ttyUSB0'  # Adjust this based on your actual port
        baud_rate = '115200'
        with serial.Serial(arduino_port, baud_rate) as ser:
            user_input = "1" # Start Data Reading from MPU6050
            ser.write(user_input.encode())
            data = ser.readline().decode().strip()
            print("Distance =  ", data)
            return data

if __name__ == '__main__':
    while True:
        reading.checkdist()
