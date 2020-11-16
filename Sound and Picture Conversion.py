def sound(sampleRate, bit, duration, channel):
    seconds = duration * 60
    fSize = (sampleRate * bit * seconds * channel)/(8 * 1000 * 1000)
    return fSize

sampleRate = float(input("Enter sample rate :"))
bit = int(input("Enter bit rate :"))
duration = float(input("Enter duration :"))
channel = int(input("Enter number of channer :"))

print(sound(sampleRate, bit, duration, channel))
