##AlarmState = Boolean(True/False)
##SensorValue = float
##ThresholdValue = float
##Temperature = float


def SampleTemp(ThresholdValue, SensorValue):

##    print("The threshold value is :", ThresholdValue)
##    print("The sensor value is :", SensorValue)

    Temperature = SensorValue * 1.135
    print('Temperature :',Temperature)

    if Temperature < ThresholdValue:
            AlarmState = False
            print("Temperature OK")
    else:
            AlarmState = True
            print("Temperature Alarm")
       

tv = float(input('Enter Threshold value :'))
sv = int(input('Enter Sensor Value :'))

SampleTemp(tv, sv)

        
    
        
        
                                 
    
