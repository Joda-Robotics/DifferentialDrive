class UltrasonicPinOut():
  def __init__(self, tx, rx):
    self.tx = tx
    self.rx = rx

class MotorPinOut():
  # TODO: These should be named appropriately
  def __init__(self, pin1, pin2, pin3, pin4, pin5, pin6):
    self.pin1 = pin1
    self.pin2 = pin2
    self.pin3 = pin3
    self.pin4 = pin4
    self.pin5 = pin5
    self.pin6 = pin6

# Pins for the ultrasonic sensor(s)
ULTRASONIC_PINOUT = [
  UltrasonicPinOut(14, 15)
]

# Pins for the motor sensor(s)
MOTOR_PINOUT = [
  MotorPinOut(16,17,18,19,20,21),
  MotorPinOut(22,23,24,25,26,27)
]

# Pins for the gyroscopic sensor/accelerometer/compass
GYRO_PINOUT = []