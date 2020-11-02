import config.hardwarePins as hw

class UltraSonic:
  '''
  Read ultrasonic sensor data
  '''

  def __init__(self, pinouts=hw.ULTRASONIC_PINOUT):
    self.pinouts = pinouts

  def getDistance(sensor):
    # TODO: Implement fetching of distance for the selected sensor
    return 0