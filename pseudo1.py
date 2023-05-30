import machine
import time

# Define GPIO pins
TRIGGER_PIN = 0
ECHO_PIN = 1

# Set up ultrasonic sensor
trigger = machine.Pin(TRIGGER_PIN, machine.Pin.OUT)
echo = machine.Pin(ECHO_PIN, machine.Pin.IN)

# Function to measure distance using the GY-53 sensor
def measure_distance():
    # Generate trigger pulse
    trigger.high()
    time.sleep_us(10)
    trigger.low()
    
    # Measure echo pulse duration
    while echo.value() == 0:
        pulse_start = time.ticks_us()
    while echo.value() == 1:
        pulse_end = time.ticks_us()
    
    # Calculate distance based on pulse duration
    """
    In the given code, the line distance = pulse_duration * 0.0343 / 2 calculates the distance based on the duration of the pulse received from the ultrasonic sensor.

The number 0.0343 is a conversion factor used to convert the pulse duration into distance. This factor is derived from the speed of sound in air and the time it takes for the sound wave to travel a distance of 1 centimeter. It represents the time it takes for sound to travel 1 centimeter in microseconds.

The division by 2 is because the pulse duration measured by the ultrasonic sensor represents the round-trip time for the sound wave. To obtain the one-way distance from the sensor to the target, we divide the pulse duration by 2.

By multiplying the pulse duration by 0.0343 and dividing by 2, we can obtain the distance in centimeters. This calculation assumes that the speed of sound in the medium (usually air) remains constant.
    """
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 0.0343 / 2  # Divide by 2 for one-way distance
    
    return distance

# Main loop
while True:
    # Measure distance
    distance = measure_distance()
    print("Distance: %.2f cm" % distance)
    
    # Check if elevator needs to be called
    if distance < 50:  # Adjust this threshold according to your needs
        print("Elevator called!")
        # Add your elevator control logic here
        # For example, you can send a signal to move the elevator up or down
        
    time.sleep(0.1)  # Delay between measurements
