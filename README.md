# SuperPy
A command-line tool for registering buying and selling products

Do operations with product stock: add and remove bought and sell products and get various
reports.
All the dates in all the arguments are added in format YYYY-MM-DD.


Tool suports next operations:

- `buy` - adds bought products to the stock table. 

Optional arguments: 
  
`--product-name -n`, string,indicate product's name
 
 `--date` - buy date, default - today's day
 
 `--price -p`
 
 `--expiration-date -e`, add expiration date in format YYYY-MM-DD


- `sell` command allows to sell any bought product and requires next arguments:
 `--product-name -n` 
  `--price -p`
  `--sell-date -s`


- `advance_time` changes date percieved by the app as "today". You can manually set the date that will be automatically used by app


 `-change --c`  requires number or full date in format YYYY-MM-DD. Argument either adds or subtracts given amount of days from the current date or replaces current day in the app by provided literal.                    
 
 `-reset --r` resets todays date to an actual date

- `report` with subcommands allow to generate various reports. You can get inventory, revenue or profit report.


Each of this commands supports two optional arguments: 

`--now`, that displays current inventory, revenue or profit

`-on_date -o`, that displays inventory, revenue or profit on particular date.

>Notice: `report profit -on_date` displays profit on that particular day while
>`report revenue -on_date` shows total revenue till provided date

# Exapmles of usage:


`python main.py report profit -h` displays help message for particular command

`python main.py buy -n watermelon -p 0.7 -e 2023-07-07` add to a database table row with a watermelon with price=0.7 and expiration date, defaul buy date is today

`python main.py sell -n watermelon -p 0.8` sells it for a price 0.8

`python main.py report profit -o 2023-05-06` reports profit on specified date

`python main.py report inventory --now` displays a table with all items available in stock


















