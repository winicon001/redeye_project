/* 
 * This Arduino Nano ESP32 code was developed by newbiely.com
 * 
 * For comprehensive instructions and wiring diagrams, please visit:
 * [Arduino Nano ESP32 Ultrasonic Sensor Tutorial](https://newbiely.com/tutorials/arduino-nano-esp32/arduino-nano-esp32-ultrasonic-sensor)
 */

int TRIG_PIN = 5; // The Arduino Nano ESP32 pin connected to the Ultrasonic Sensor's TRIG pin
int  ECHO_PIN = 18; // The Arduino Nano ESP32 pin connected to the Ultrasonic Sensor's ECHO pin

float duration_us, distance_cm;

void setup() {
    // Begin serial communication
    Serial.begin(115200);

    // Configure the trigger pin to output mode
    pinMode(TRIG_PIN, OUTPUT);

    // Configure the echo pin to input mode
    pinMode(ECHO_PIN, INPUT);
}

void loop() {
    // Produce a 10-microsecond pulse to the TRIG pin
    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG_PIN, LOW);

    // Measure the pulse duration from the ECHO pin
    duration_us = pulseIn(ECHO_PIN, HIGH);

    // Calculate the distance
    distance_cm = 0.017 * duration_us;

    // Print the value to the Serial Monitor
    Serial.println(distance_cm);
  

    delay(10);
}
