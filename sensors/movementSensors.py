import config.hardwarePins as hw

class Movement:
  '''
  Read gyro/accel/compass sensor data
  '''

  def __init__(self, pinouts=hw.GYRO_PINOUT):
    self.pinouts = pinouts
    return

  def getGyro():
    # TODO: Implement fetching of gyro reading (deg/second)
    return 0

  def getAcceleration():
    # TODO: Implement fetching of acceleration (in Gs)
    return 0

  def getCompass():
    # TODO: Implement fetching of acceleration (in gauss)
    return 0