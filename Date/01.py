# You can use the datetime class from the datetime module 
# to get the current date and time.

from datetime import datetime

now = datetime.now()
print("Current Date and Time:", now)


from datetime import date

today = date.today()
print("Current Date:", today)


birthday = date(1995, 5, 15)
print("Birthday:", birthday)