import random

class AtmAcct:
    def __init__(self, id, bal2 = 0, annualIntRate = 2.5):
        self.id = id
        self.bal2 = bal2
        self.getannualIntRate
    def getId(self):
        return self.id
    def withdraw(self, amt):
        self.bal2 += amt
    def deposit(self, amt):
        self.bal2 -= amt
    def getbal2(self):
        return self.bal2
    def getannualIntRate(self):
        return self.annualIntRate
    def getMonthlyIntRate(self):
        return self.annualIntRate/12
    def getMonthlyInt(self):
        return self.bal2 * self.getMonthlyIntRate()
    
def main():
    #Creating account
    accounts = []
    for i in range(1000, 9999):
        account = AtmAcct(i, 0)
        accounts.append(account)
    #ATM processes
    while True:
        #enter security pin
        id = int(input("\nEnter Account Pin:\n\n"))

        #Validate pin as 4 digit number
        while id < 1000 or id > 9999:
            id = int(input("\nInvalid pin, re-enter:\n\n"))

        while True:
            #Main menu
            print("\n[1] View Balance\n[2] Withdraw\n[3] Deposit\n[4] Exit\n")

            #Reading option
            option = int(input("\nEnter option:\n"))

            for acc in accounts:
                #comparing AtmAcc id
                if acc.getId() == id:
                    AtmAccObj = acc
                    break

            #View Balance
                if option == 1:
                    #Print Balance
                    print(AtmAccObj.getbal2())

                #Withdraw
                elif option == 2:
                    #Reading amt
                    amt = float(input("\nEnter amount to Withdraw:\n"))
                    withAns = input("Is the entry correct? Yes or No?\n" + str(amt) + " ")

                    if withAns == "Yes":
                        print("Verified withdraw")
                    else:
                        break

                    if amt < AtmAccObj.getbal2():
                        #Calling withdraw method
                        AtmAccObj.withdraw(amt)
                        #Printing updated balance
                        print("\nUpdated balance: " + str(AtmAccObj.getbal2()) + " n")
                    else:
                        print("\nYou have insufficient balance: " + str(AtmAccObj.getbal2()) + " n")
                        print("\nMae a deposit.");
    
                #Deposit
                elif option == 3:
                    #Reading amt
                    amt = float(input("\nEnter amount to deposit: \n"))
                    depoAns = input("Is the entry correct? Yes or No?" + str(amt) + " ")

                    if depoAns == "Yes":
                        #Calling deposit method
                        AtmAccObj.deposit(amt)
                        #   Printing updated balance
                        print("\nUpdate balance:\n" + str(AtmAccObj.getbal2()) + " n")
                    else:
                        break
                
                #Withdraw
                elif option == 4:
                    print("nTransaction successful.")
                    print("Transaction no.:", random.randint(10000, 1000000))
                    print("Current Interest Rate: ", AtmAccObj.annualIntRate)
                    print("Monthly Interest Rate: ", AtmAccObj.annualIntRate/12)
                    print("Thanks for your patronage!")
                    exit()
                

                #Withdraw
                else:
                    print("\nInvalid Option")

#Call main function
main()

