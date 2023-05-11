Superpy
=======

On creating a SuperPy command-line tool I found a few challenging moments that required time and thinking to find a good solution.


1.Setting and advancing the date, percieved by the application as 'today'. I created a module named datenow that has three methods:
-today() that extract the date, stored in a csv file
-change_date() allows to rewrite the date, stored in a file
-change_todays_date() creates the needed datetime object regarding to the called command, wether it is adding or subtracting a number of days or providing a new date in a string.

This implementation allows to store the date and change it continiously and it is not changing with every new call of the programm. 
When the current date is needed it is just taken from the file using today() function.


2. Second noticable thing is working with tables. 
The assignement,alghoug was not strick but reccomended to create two csv tables with connected id`s. 
The task required to create a model of relational database withing csv files and tat turen out to be tricky. 
I decided to use Pandas module - it allows to work with dataframes - abstration of data, instead of writing directly row by row into file.
It gives more possibilities to work with data and what is important with indexes and reduces mistaces.

First, when we buy a product it is just added to the bought.csv table where it is stored with the sell date and price. 
When we need to sell it, we create two dataframes for tables with bought and sold products, and if we find needed one in a bought.csv dataframe and at the same time it is not present in sold.csv table, the we add a new row in sold.scv.
To do that I create indexing for bought items and add index of a neede product to the sold.csv table as bought_id.

In detailes it is described in base.py in sell_item() with a commentaries.

 
3. The whole files organisation - I find it very comfortable to work with, because the program divided into structured block each responsible for a separate structure.
For example, parser.py contains only parsing functionality, datenow is a separate module for setting and advancing date and all the functions for parser`s arguments stored in base.py. 
It allows to allocate mistaces easily and change only required code instead of rewriting whole programm.










