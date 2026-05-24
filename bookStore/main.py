def main():
    # Print a welcome message
    print("Hello world")

    # Try to read existing book data from a file
    try:
        booksList = []  # This list will store all books

        # Open the file in read mode
        inFile = open("theBooksList.txt", "r")

        # Read the first line of the file
        line = inFile.readline()

        # Loop until there are no more lines
        while line:
            # Remove newline character and split data by comma
            booksList.append(line.rstrip("\n").split(","))

            # Read the next line
            line = inFile.readline()

        # Close the file after reading
        inFile.close()

    # If the file does not exist, handle the error
    except FileNotFoundError:
        print("The booksList.txt file is not found")
        print("Starting a new book list")
        booksList = []

    choice = 0

    # Menu loop runs until user chooses option 4
    while choice != 4:
        print("\n")
        print("*** Books Manager ***")
        print("1) Add a book")
        print("2) Lookup a book")
        print("3) Display all books")
        print("4) Quit\n")

        # Take user input
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Add a new book
            print("Adding a book")
            nBook = input("Enter the name of the book: ")
            mAuthor = input("Enter the name of the author: ")
            nPages = input("Enter number of pages: ")

            # Store book as a list
            booksList.append([nBook, mAuthor, nPages])

        elif choice == 2:
            # Search for a book
            print("Looking for a book...")
            keyword = input("Enter search term: ")

            for book in booksList:
                if keyword in book:
                    print(book)

        elif choice == 3:
            # Display all books
            print("Displaying all books")
            for book in booksList:
                print(book)

        elif choice == 4:
            # Exit the program
            print("Quitting program")

        else:
            print("Choose the correct option between 1 and 4")

    print("Program terminated!")

    # Save books back to the file
    outFile = open("theBooksList.txt", "w")

    for book in booksList:
        # Join book details with commas and write to file
        outFile.write(",".join(book) + "\n")

    # Close the file after writing
    outFile.close()


# Program starts here
if __name__ == "__main__":
    main()
