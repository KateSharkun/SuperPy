import pandas as pd
from pandas.core.frame import DataFrame
import datenow
import datetime
from datetime import date
from rich import print
from rich.console import Console
from rich.table import Table
from rich.pretty import pprint



def add_item(item):
    item.pop('func') #removing info on sub-command function
    df = pd.DataFrame([item]) #creating a row for a dataframe with all the command-line data, stored in dict where keys are arguments and values are command-line passed values 
    df.to_csv('bought.csv', mode='a', index=False, header=False) #appending a row to our csv file 
    pprint('OK')

def sell_item(item):
    #removing a function information from a namespace
    item.pop('func') 
    #getting Dataframe of a table with bougth items
    df = pd.read_csv('bought.csv')
    df.index = [x for x in range(1, len(df.values)+1)] #setting index to start from 1
    df.index.name = 'id' #setting index column name
    
    #getting Dataframe of a table with sold items
    ds = pd.read_csv('sold.csv')    
    ds.index = [x for x in range(1, len(ds.values)+1)]
    ds.index.name = 'id'
    #print(tabulate(ds, headers="keys", tablefmt = "psql"))
    
    
    #getting list of all bought_id`s - id of an item in a bought.id table
    
    bought_ids = ds['bought_id'].to_list()
    sold_item = None
    #print(bought_ids, ' is list of all the ids of bought items in sold.csv table')
    #getting a list of all bought items that has sold item name
    sell_item_id = df.index[df['product_name'] == item['product_name']].to_list()  
    #print(sell_item_id, ' all item in bought.csv that equal to item we want to sell')
    for i in bought_ids:    #checking if the products we found in bought items are not sold
            if i in sell_item_id:
                sell_item_id.remove(i)
    if len(sell_item_id) == 0:
        pprint('Product out of stock')
    else:
        #print(df.iloc[sell_item_id[0]], ' is row of product we need') 
        
        for i in sell_item_id:
            #checking if the item we want to sell is not expired
            if datetime.datetime.strptime(df.loc[sell_item_id[0]]['expiration_date'],'%Y-%m-%d').date() > date.today():
                sold_item = dict(df.loc[sell_item_id[0]]) #creating a dict from a desired row in bought.csv
                sold_item['sell_price'] = item['price']   #adding column`s values
                sold_item['sell_date'] = datenow.today()
                sold_item['bought_id'] = sell_item_id[0] 
                #creating a dataframe to add a dict with element we want to sell as a dict 
                #print(sold_item, 'this is a sold item')
                df_new_row = pd.DataFrame([sold_item])
                #appending to our file our sold item`s dictionary
                df_new_row.to_csv('sold.csv', mode='a', index=False, header=False)
                pprint('OK')
            else:
                sell_item_id.remove(i)
                continue
            if len(sell_item_id) == 0:
                pprint('Product out of stock')


def report_inventory(time): 
    df = pd.read_csv('bought.csv') #creating dataframes for both "sold" and "bought" tables
    ds = pd.read_csv('sold.csv')
    
    df.index = [x for x in range(1, len(df.values)+1)]
    df.index.name = 'id'
    #formatting indexing to start from 1 and not from 0
    ds.index = [x for x in range(1, len(ds.values)+1)]
    ds.index.name = 'id'
    
    bought_ids = ds['bought_id'].to_list()   #creating a list of id`s of all bought products

   
    if time['now'] == True:  
        dt = df[~df.index.isin(bought_ids)].reset_index(drop=True)  #removing all items that have been sold from bought dataframe
        dt.index += 1
        if dt.empty:
            pprint('The stock is empty')
        else:

            table = Table("Report: present in stock now", style='black')
            table.add_row(dt.to_string(float_format=lambda _: '{:.4f}'.format(_)))
            console = Console()
            console.log(table, style="green")

    else:
        df['buy_date'] = df[['buy_date']].apply(pd.to_datetime)  #changin string representation of date to datetime format to be able to compare it
        dt = df.loc[df['buy_date'] <= time['on_date']]      #creating filtered dataframe where date <= requested date
        filtered = dt[~dt.index.isin(bought_ids)].reset_index(drop=True)  #final dataframe without sold products
        
        if filtered.empty == True: #in case there were no products available till/on that date
            table_2 = Table(f"Report: present in stock on {time['on_date']}", style='black')
            table_2.add_row('No items were available on that day')
            console = Console()
            console.log(table_2, style="green")
        else:
            table_2 = Table(f"Report: present in stock on {time['on_date']}", style='black')
            table_2.add_row(filtered.to_string(float_format=lambda _: '{:.4f}'.format(_)))
            console = Console()
            console.log(table_2, style="green")
        
       
        
def report_revenue(time): 
    df = pd.read_csv('sold.csv')   #creating dataframe with all sold items
    if time['now'] == True:
        revenue = df['sell_price'].sum()    #summing revenue
 
        table = Table("Report: general revenue")
        table.add_row(str(f'{revenue:.2f}'))
        console = Console()
        console.log(table, style="green")
    else:
        df['sell_date'] = df[['sell_date']].apply(pd.to_datetime) #changin string representation of date to datetime format to be able to compare it
        dt = df.loc[df['sell_date'] <= time['on_date']]       #creating filtered dataframe where date <= requested date
        revenue = dt['sell_price'].sum()                     #summing 

        table = Table(f"Report: revenue on {time['on_date']}", style='black')
        table.add_row(str(f'{revenue:.2f}'))
        console = Console()
        console.log(table, style="green")
        
    
def report_profit(time):
    df = pd.read_csv('sold.csv')
    if time['now'] == True:
        revenue = df['sell_price'].sum()
        cost = df['buy_price'].sum()
        profit = revenue-cost

        table = Table("Report: general profit", style='black')
        table.add_row(str(f'{profit:.2f}'))
        console = Console()
        console.log(table, style="green")

    else:
        df['sell_date'] = df[['sell_date']].apply(pd.to_datetime)
        dt = df.loc[df['sell_date'] == time['on_date']]
        revenue = dt['sell_price'].sum()
        cost = dt['buy_price'].sum()
        profit = revenue-cost
        
        table = Table(f"Report: profit on {time['on_date']}", style='black')  
        table.add_row(str(f'{profit:.2f}'))
        console = Console()
        console.log(table, style="green")

