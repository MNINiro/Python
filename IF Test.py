Number1 = int(input("Enter number:"))
Number2 = int(input("Enter number:"))
Number3 = int(input("Enter number:"))

if Number1 < Number2 and Number1 < Number3:
    prod = Number2 * Number3
    print(prod)

if Number2 < Number1 and Number2 < Number3:
    prod = Number1 * Number3
    print(prod)

if Number3 < Number1 and Number3 < Number2:
    prod = Number1*Number2
    print(prod)



 SEND "Enter the second number:" TO DISPLAY
        INPUT Number2 FROM (INTEGER)KEYBOARD
        IF Number2 < Smallest
              SET Smallest TO Number2
              BREAK
        ELSE IF Number2 = Number1
                       SEND "You cannot enter the same number" TO DISPLAY
                       CONTINUE
WHILE True
         SEND "Enter the third number:" TO DISPLAY
         INPUT Number3 FROM (INTEGER)KEYBOARD
         IF (Number3 = Number1) OR (Number3 = Number2)
                SEND "You cannot enter the same number twice" TO DISPLAY
                Continue
        ELSE IF Number3 < Smallest
                SET Smallest TO Number3
Answer = (Number1  Number2  Number3)/Smallest