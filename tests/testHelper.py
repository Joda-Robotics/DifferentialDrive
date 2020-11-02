from inspect import currentframe, getframeinfo

# Returns file name and line number from location this was called
def getLineDetails():
  frameInfo = getframeinfo(currentframe().f_back)
  return [frameInfo.filename, frameInfo.lineno]

# Prints error message including line details as fetched from getLineDetails()
def printError(message, lineDetails):
  print('{} [{}: line {}]'.format(message, lineDetails[0], lineDetails[1]))