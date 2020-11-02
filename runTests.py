from tests.testSensorInit import test as sensorTests

totalTests = 0
totalSuccesses = 0

print('Commencing tests\n')

# Call sensor tests
sensorResults = sensorTests()
totalTests += sensorResults[0]
totalSuccesses += sensorResults[1]
print('[sensorTests] {}/{} tests passed'.format(sensorResults[1], sensorResults[0]))

# Summarise results
print('\nTesting finished')
print('{}/{} tests succeeded'.format(totalSuccesses, totalTests))