import config.hardwarePins as hw

class Movement:
  '''
  Read motor encoder sensor data
  '''

  def __init__(self, pinouts=hw.MOTOR_PINOUT):
    self.pinouts = pinouts
    return

  def getMotorReadings(motor):
    # TODO: Implement fetching of motor encoder readings for the selected motor
    # Selected motor corresponds to index of the wheel pinout array inputted in init
    return 0