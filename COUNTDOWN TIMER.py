import time
from tkinter import *
from tkinter import messagebox

clockWindow = Tk()
clockWindow.geometry("500x500")
clockWindow.title("Countdown Timer")
clockWindow.configure(background='orange')

# Declare Variables
hourString = StringVar()
minuteString = StringVar()
secondString = StringVar()

# Set strings to default values
hourString.set("00")
minuteString.set("00")
secondString.set("00")

# Get User Input
hourEntry = Entry(clockWindow, width=3, font=(
    "Calibri", 20, ""), textvariable=hourString)
minuteEntry = Entry(clockWindow, width=3, font=(
    "Calibri", 20, ""), textvariable=minuteString)
secondEntry = Entry(clockWindow, width=3, font=(
    "Calibri", 20, ""), textvariable=secondString)

# Center Textboxes
hourEntry.place(x=170, y=180)
minuteEntry.place(x=220, y=180)
secondEntry.place(x=270, y=180)


def runTimer():
    try:
        # clockTime is raw time computation from converting the specified time all to seconds
        clockTime = int(hourString.get()) * 3600 + \
            int(minuteString.get()) * 60 + int(secondString.get())

    except:
        print("Incorrect Values")

    while clockTime > - 1:

        # This function takes 2 parameters, a numerator and denominator and returns a tuple of numbers (x,y), where x is the quotient and y is the remainder. So, this will tell us the amount of minutes and seconds in the clockTime by dividing the raw clockTime by 60
        totalMinutes, totalSeconds = divmod(clockTime, 60)

        totalHours = 0

        if totalMinutes > 60:
            totalHours, totalMinutes = divmod(
                totalMinutes, 60)  # Same thing to get our hours

        hourString.set("{0:2d}".format(totalHours))
        minuteString.set("{0:2d}".format(totalMinutes))
        secondString.set("{0:2d}".format(totalSeconds))

        clockWindow.update()
        time.sleep(1)

        # Let User know when time elapses
        if (clockTime == 0):
            messagebox.showinfo("", "Your time has expired")

        clockTime -= 1


setTimeButton = Button(clockWindow, text="Set Time", bd="5", command=runTimer)
setTimeButton.place(relx=0.5, rely=0.5, anchor=CENTER)

clockWindow.mainloop()
