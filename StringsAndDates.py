# Darrell Lawson
# CIS261
# StringsAndDates

run = True


month = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}


while(run):

    date = input("Enter Date (Format : March 31, 2021 or (-1 to exit) : ")

    if (date == "-1"):
        run = False
        break
 
    try:
        # Split the input and set the date in required format
        list1 = date.split(" ")
        new_format = f"{month[list1[0]]}/{list1[1][:-1]}/{list1[2]}"
        print(new_format)

    except Exception as e:
        print("Invalid Input")
         