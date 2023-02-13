# Buff163 Bot

## A Python CLI that looks up [Buff.163](https://buff.163.com) prices for a given item name.
___
### Simply add your Buff Session Cookie to _BuffAPISession.py_'s `get_buff_session()` to use the scripts.
### This bot works for any game on the Buff market (CS:GO, DOTA2, TF2, Rust, H1Z1, and PUBG).  CS:GO is assumed by default, but you can specify which game to use in each API call or change the global `default_game` in _BuffAPISession.py_.
___
### The scripts included in this bot are detailed as follows:
* _BuffAPISession.py_ - handles your Buff Session and implements the available calls to the Buff API.
* _BuffBot.py_ - utilizes the API calls to do more make specific queries.  The current functionality includes:
    * `get_id(item_name)` - gets the Buff ID for the given item name.
    * `get_sell_price(item_name)` - gets the lowest sell price for the given item name.
    * `get_buy_price(item_name)` - gets the highest buy price for the given item name.
    * `get_last_n_sales_avg_price(item_name, n)` - gets the average price for the last n sales of the given item.
    * `get_steam_market_price(item_name)` - gets the reference Steam Market price for the given item name.  This is not always exact but usually close enough, though it can be wildly inaccurate for rare items.
    * `get_steam_market_url(item_name)` - gets the Steam Market URL for the given item name.
    * This is easily extensible to add whatever parsing you like of the _.json_ files returned by the various API calls.
* _BuffMarketScraper.py_ - creates a semi-colon seperated file (_BuffItemData.csv_) with all the listed items on buff, with key-pair `{id, name}` which could be used for future lookup, though I don't currently have that implemented.  It also scrapes current prices and a Steam Market link for each item.  This obviously takes many hours to run, especially given we can only increment on the market page, which is constantly changing.  It is important to use *;* because some CS:GO item names include commas.
* _GenerateInventoryData.py_ - appends Buff pricing data to a given (semi-colon seperated) list of items and their quantities.  There are some obvious possible improvements to speed up this script and reduce API calls, but I've left it simple.  You can create a list of the quantities and names of each item in your inventory using [csgo.exchange](https://csgo.exchange/)'s inventory export tool or compile this list another way.  I imported this data into a spreadsheet to do further processing to determine the total value of my inventory, the fair cash price of my high value items, and which market to sell them on.
___
This repository was originally forked from [André Vieira dos Santos](https://github.com/andrevsantos)' [buff163_bot](https://github.com/andrevsantos/buff163_bot) which had the basic session management, market page scraping, and sell order price lookup logic.  This foundation was immensely helpful when I was looking for a good tool to determine the value of my CS:GO inventory and how best to liquidate it.  Thank you André!
