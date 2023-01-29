volume1 = 24.0
volume2 = 48.0

minVolume = volume1/2

width = float(input('Enter width:'))
height = float(input('Enter height:'))
length = float(input('Enter length:'))

reqVolume = width * length * height

if reqVolume < minVolume:
    print("Too small for cargo container")
elif reqVolume <= volume1:
    print("Require small container")
elif reqVolume <= volume2:
    print("Require large container")
else:
    print("Too large for cargo container")

