import argparse
import base
from pathlib import Path
import datenow


parser = argparse.ArgumentParser(prog="SuperPy",description="Do operations with product stock: add and remove bought and sell products and get various reports.To see arguments for each command type: superpy {command name} -h",
    epilog="For more details see each operator`s options. Thanks for using %(prog)s! ")


subparsers = parser.add_subparsers(title='Operators to buy, sell products and get reports', help='operations in database')


buy_parser = subparsers.add_parser('buy', help='Add bought products to the stock list')
buy_parser.add_argument("--product-name", '-n', type=str,required=True, help='indicate product`s name')
buy_parser.add_argument('--date', default=datenow.today())
buy_parser.add_argument("--price", '-p', type=str,required=True)
buy_parser.add_argument("--expiration-date",'-e', required=True, metavar=("YYYY-MM-DD"),
    help="add expiration date in format %(metavar)s")

buy_parser.set_defaults(func=base.add_item)
buy_parser._positionals.title = 'Positional arguments'
buy_parser._optionals.title = 'Optional arguments'

sell_parser = subparsers.add_parser('sell', help='Remove sold products from database')
sell_parser.add_argument("--product-name", '-n', type=str,required=True)
sell_parser.add_argument("--price", '-p', type=float,required=True)
sell_parser.add_argument("--sell-date",'-s', default=datenow.today())
sell_parser.set_defaults(func=base.sell_item)



today_parser = subparsers.add_parser('advance_time', help='Change date percieved by the app as "today"')
today_parser.add_argument('-c', '--change', metavar=("number/YYYY-MM-DD"), help='change current date. You can provide the amount of days you would like to move from current date, percieved as today(+/- integer) or type an actual date in format"YYYY-MM-DD"', type=str)
today_parser.add_argument('-r', '--reset',help='reset todays date to actual todays date', action='store_true')

today_parser.set_defaults(func=datenow.change_todays_date)


report_parser = subparsers.add_parser('report', help ='Generate report')


option_report = report_parser.add_subparsers(title='stock', metavar='table')
report_inventory = option_report.add_parser('inventory', help = 'get inventory report')

time = report_inventory.add_mutually_exclusive_group(required=True)
time.add_argument("--now", action='store_true')
time.add_argument("--on-date", '-o', help='report on inventory on particular date in format YYYY-MM-DD')

report_inventory.set_defaults(func=base.report_inventory)


report_revenue = option_report.add_parser('revenue', help = 'get revenue report')

time = report_revenue.add_mutually_exclusive_group(required=True)
time.add_argument("--now", action='store_true')
time.add_argument("--on-date", '-o', help='shows general revenue till the indicated date in format YYYY-MM-DD')

report_revenue.set_defaults(func=base.report_revenue)



report_profit = option_report.add_parser('profit', help = 'get profit report')

time = report_profit.add_mutually_exclusive_group(required=True)
time.add_argument("--now", action='store_true')
time.add_argument("--on-date", '-o', help='generates report on a particular day')

report_profit.set_defaults(func=base.report_profit)
