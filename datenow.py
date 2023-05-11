from datetime import date, timedelta, datetime
import csv
import os

'''DateNow may be considered a module that allows to operate with current date by saving it in external file so the setting of day, percieved as today, will be saved for the next session.
It has three functions:
-today, that returns date, saved in file, to be percieved as 'today'
-change_todays_date - changes the value of a date which should be percieved as today. It covers all the variants of usage withing the application
-change_date - rewrites the file that contains current date 


'''

current_date = str(date.today())
def today():
    with open('today.csv', 'r+', newline='') as f:
        a = []
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            a.append(row)
        if len(a) == 0:
            writer = csv.writer(f)
            writer.writerow([current_date])
        date = a[0][0]
        return date


def change_date(date):
    with open('today.csv', 'w', newline='') as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerow([str(date)])

        
def change_todays_date(d='today'):
    date_today = ''
    if d == 'today'or d == None:

        date_today = today()

    elif type(d) == dict:
        
        if d['reset'] == True:
            change_date(date.today())

        elif d['change'] is not None:
            try:                
                d = int(d['change'])
                date_today += str(datetime.strptime(date_today,'%Y-%m-%d').date() + timedelta(days = d))
                change_date(date_today)
            except ValueError:
                try:
                    
                    new_date = datetime.strptime(d['change'],'%Y-%m-%d').date()
                    date_today = new_date
                    change_date(new_date)
           
                except ValueError:                
                    print('Enter correct date in format "YYYY-MM-DD" or an integer for the amount of days you would like to move from today')
   

    elif type(d) == str:
        try:
            date_n = datetime.strptime(d,'%Y-%m-%d').date()
               
           
            date_today = date_n
            change_date(date_n)
        except ValueError:
            print('Enter correct date')
    elif type(d) == int:       
        date_today = str(datetime.strptime(today(),'%Y-%m-%d').date() + timedelta(days = d))
        change_date(date_today)

    date_today = str(today())

    return date_today




