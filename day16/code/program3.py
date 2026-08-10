import datetime

def function1():
    # constants
    print(f"minimum year = {datetime.MINYEAR}")
    print(f"maximum year = {datetime.MAXYEAR}")

# function1() 

def function2():
    # get the current local time
    print(f"local time = {datetime.datetime.today()}")
    print(f"local time = {datetime.datetime.now()}")

    # get the current local time in required format
    # %Y = year
    # %m = month
    # %d = day
    # %h = hour
    # %M = minute
    # %s = second
    print(f"local day  = {datetime.datetime.now().strftime('%d-%m-%Y')}")
    print(f"local time = {datetime.datetime.now().strftime('%H:%M')}")

    # get the current date (not the time)
    print(f"local day  = {datetime.date.today()}")
    
# function2()

def function3():
    # get the time delta
    delta = datetime.timedelta(days=2)
    print(f"delta = {delta}")

# function3()

def function4():
    # create a datetime object using user defined components
    print(f"datetime using (2026, 8, 10) = {datetime.datetime(2026, 8, 10)}")

    # create a datetime using user input
    year = int(input("year: "))
    month = int(input("month: "))
    day = int(input("day: "))
    hour = int(input("hour: "))
    miniutes = int(input("minutes: "))
    seconds = int(input("seconds: "))
    print(f"datetime using user input    = {datetime.datetime(year, month, day, hour, miniutes, seconds)}")


function4()