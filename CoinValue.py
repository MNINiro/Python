def __init__(self):
    self.__amount = 0
    self.__state = "Idle"
    

def SetState(self, NewState):
    self.__State = NewState
    print(self.__State)


def ReturnCoins(self):
    print(self.__Amount)
    self.__Amount = 0


def __validCoin(self, s):
    coins = ['10','20','50','100']
    if s in coins:
        isValid = True
    else:
        isValid = False
    return(isValid)


def coinInserted(self, s):
    coinValue = int(s)
    self.__amount = self.__amount + coinValue


def stateChange(self):
    newInput = input("Insert coin: ")
    if newInput == "C":
        if self.__state == "Counting":
            self.setState("Cancelled")
            self.returnCoins()
        self.setState("Idle")
    elif newInput == "A":
            if self.__amount == 0:
                print("no coins inserted")
            else:
                self.setState("Accepted")
                self.__PrintTicket()
            self.setState("Idle")
    elif self.__validCoin(newInput):
            self.coinInserted(newInput)
            self.setState("Counting")
    else:
        print("Error - not a valid coin")


def main():
    ParkingMeter = TicketMachine()
    while True:
        ParkingMeter.stateChange()
        
            
        
