from datetime import datetime
import random

database = []

class ElectricBill:
    def __init__(self, billOwner, usedUnits=0, monthlyUnits=150):
        self.billOwner = billOwner
        self.usedUnits = usedUnits
        self.monthlyUnits = monthlyUnits

    def showRemainingUnits(self):
        remainingUnits = self.monthlyUnits - self.usedUnits
        print(f"The remaining units are {remainingUnits}")

    def showUsedUnits(self):
        print(f"The used units are {self.usedUnits}")
        if self.usedUnits > self.monthlyUnits:
            self.showOverUsedUnits()
        else:
            self.showRemainingUnits()

    def showOverUsedUnits(self):
        overUsedUnits = self.usedUnits - self.monthlyUnits
        feeToPay = overUsedUnits * 1.4

        database.append({
            "moneyDue": feeToPay
        })

        print(f"You exceeded by {overUsedUnits} units")
        print(f"You have to pay ${feeToPay}")

    def generateRandomUsage(self):
        randomUnits = random.randint(30, 200)
        self.usedUnits += randomUnits
        print(f"{randomUnits} kWh consumed this month")

    def checkMonthlyReset(self, lastReset):
        currentDate = datetime.now()

        if (currentDate.month != lastReset.month or
            currentDate.year != lastReset.year):

            print("New month detected. Resetting units...")
            self.usedUnits = 0
            return True

        return False


class Security:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def registerNewUser(self):
        for user in database:
            if user.get("name") == self.name:
                print("User already exists")
                return

        database.append({
            "name": self.name,
            "password": self.password,
            "usedUnits": 0,
            "monthlyLimit": 150,
            "lastReset": datetime.now()
        })

        print("User registered successfully")

    def loginUser(self):
        for user in database:
            if (user["name"] == self.name and
                user["password"] == self.password):

                print("Login successful\n")

                bill = ElectricBill(
                    billOwner=user["name"],
                    usedUnits=user["usedUnits"],
                    monthlyUnits=user["monthlyLimit"]
                )

                bill.generateRandomUsage()

                if bill.checkMonthlyReset(user["lastReset"]):
                    user["usedUnits"] = 0
                    user["lastReset"] = datetime.now()

                user["usedUnits"] = bill.usedUnits
                bill.showUsedUnits()
                return

        print("Invalid credentials")


def main():
    print("""====================================
        ELECTRIC SAVING SYSTEM
====================================""")
    while True:
        print("\n")
        print("1) Register as New User")
        print("2) Login as Existing User")
        print("3) Exit System")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Enter a valid number")
            continue

        if choice == 1:
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            security = Security(name, password)
            security.registerNewUser()

        elif choice == 2:
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            security = Security(name, password)
            security.loginUser()

        elif choice == 3:
            print("Exiting System")
            break

        else:
            print("Enter valid choice")

#=======  Main Function =======
if __name__ == "__main__":
    main()