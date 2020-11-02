from tests.testHelper import *

from sensors.ultraSonicSensors import UltraSonic
import config.hardwarePins as hw

# Test 1 - Checks pinout was initialised to defaults
def ultraSonic_1():
  testSuccess = True
  usSensor = UltraSonic()
  try: 
    usSensor.pinouts[0].tx
    usSensor.pinouts[0].rx
  except: 
    printError('UltraSonic pinout not initialised by default', getLineDetails())
    testSuccess = False
  return testSuccess

# Test 2 - Checks pinout was initialised to inputted values
def ultraSonic_2():
  testSuccess = True
  pinouts = [hw.UltrasonicPinOut(1,2)]
  usSensor = UltraSonic(pinouts)
  try: 
    if usSensor.pinouts[0].tx != 1 or usSensor.pinouts[0].rx != 2:
      printError('UltraSonic pinout not set to inputted values', getLineDetails())
      testSuccess = False
  except:
    printError('UltraSonic pinout undefined', getLineDetails())
    testSuccess = False
  return testSuccess

# Contains a list of tests to run
TEST_LIST = [
  ultraSonic_1,
  ultraSonic_2
]

# Main test function, runs all tests in TEST_LIST
def test():
  testSuccess = True
  numTests = 0
  numSuccesses = 0

  for testFunction in TEST_LIST:
    numTests = numTests + 1
    if testFunction():
      numSuccesses = numSuccesses + 1

  return [numTests, numSuccesses]