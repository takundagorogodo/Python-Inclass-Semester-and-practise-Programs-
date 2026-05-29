from datetime import datetime

# ---------------- STORAGE STRUCTURE ----------------
hostelRooms = [
    {
        "name": "",
        "roomNumber": room,
        "tenantId": "",
        "monthlyRent": 0,
        "dueRent": 0,
        "lastRentDate": None,
        "occupied": False
    }
    for room in range(100, 121)
]


# ---------------- HELPER FUNCTIONS ----------------

def findRoom(roomNumber):
    for room in hostelRooms:
        if room["roomNumber"] == roomNumber:
            return room
    return None


# Allocate Room
def allocateRoom():
    roomNo = int(input("Enter Room Number: "))
    room = findRoom(roomNo)

    if not room:
        print("Invalid room number.")
        return

    if room["occupied"]:
        print("Room already occupied.")
        return

    room["name"] = input("Enter Tenant Name: ")
    room["tenantId"] = input("Enter Tenant ID: ")
    room["monthlyRent"] = float(input("Enter Monthly Rent: "))
    room["lastRentDate"] = datetime.now()
    room["occupied"] = True

    print("Room allocated successfully.")


# Automatic Rent Generation
def autoGenerateRent():
    currentDate = datetime.now()

    for room in hostelRooms:
        if room["occupied"] and room["lastRentDate"]:

            lastDate = room["lastRentDate"]

            months_passed = (
                (currentDate.year - lastDate.year) * 12
                + (currentDate.month - lastDate.month)
            )

            if months_passed > 0:
                room["dueRent"] += months_passed * room["monthlyRent"]
                room["lastRentDate"] = currentDate
                print(f"Rent added for Room {room['roomNumber']}")


# Apply 10% Penalty
def applyPenalty():
    for room in hostelRooms:
        if room["dueRent"] > 0:
            penalty = room["dueRent"] * 0.10
            room["dueRent"] += penalty
            print(f"Penalty applied to Room {room['roomNumber']}")


# Pay Rent
def payRent():
    roomNo = int(input("Enter Room Number: "))
    room = findRoom(roomNo)

    if not room:
        print("Invalid room number.")
        return

    amount = float(input("Enter Amount to Pay: "))

    if amount > room["dueRent"]:
        print("Amount exceeds due rent.")
        return

    room["dueRent"] -= amount
    print(f"Payment successful. Remaining Due: {room['dueRent']}")


# Vacate Room
def vacateRoom():
    roomNo = int(input("Enter Room Number: "))
    room = findRoom(roomNo)

    if not room:
        print("Invalid room number.")
        return

    if room["dueRent"] > 0:
        print("Clear due rent before vacating.")
        return

    room["name"] = ""
    room["tenantId"] = ""
    room["monthlyRent"] = 0
    room["dueRent"] = 0
    room["lastRentDate"] = None
    room["occupied"] = False

    print("Room vacated successfully.")


# Display Rooms
def displayRooms():
    for room in hostelRooms:
        print(
            "Room:", room["roomNumber"],
            "| Occupied:", room["occupied"],
            "| Due:", room["dueRent"]
        )


# ---------------- MAIN FUNCTOON ----------------
def main():
        print("""========================+===============
        GODAZ APARTMENT
========================================""")
        while True:

                autoGenerateRent()   # Automatic monthly check

                print("\n1. Allocate Room")
                print("2. Pay Rent")
                print("3. Apply Late Penalty (10%)")
                print("4. Vacate Room")
                print("5. Display Rooms")
                print("6. Exit")

                choice = input("Enter choice: ")

                if choice == "1":
                        allocateRoom()

                elif choice == "2":
                        payRent()

                elif choice == "3":
                        applyPenalty()

                elif choice == "4":
                        vacateRoom()

                elif choice == "5":
                        displayRooms()

                elif choice == "6":
                        print("Exiting system...")
                        break

                else:
                        print("Invalid choice.")
#====== execution start here===
if __name__ == "__main__":
     main()