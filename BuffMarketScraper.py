from time import sleep
from BuffAPISession import get_market_page_json as get_market_page


market_page = get_market_page()

f = open("BuffItemData.csv", "w", encoding="utf-8")
f.write("Buff ID;Item Name;Max Buy Price (RMB);Min Sell Price (RMB);"
        "Quick Price (RMB);Reference Price (RMB);Steam Market Price (USD);"
        "Steam Market URL\n")

items = {}
total_item_count = market_page['data']['total_count']
total_page_count = market_page['data']['total_page']
times_through = 0

while len(items) < total_item_count and times_through < 5:
    for x in range(1, total_page_count+1):
        page = get_market_page(x)
        sleep(5)

        for item in page['data']['items']:
            id = str(item['id'])
            if id not in items:
                name = item['name']
                items[id] = name
                max_buy_price = str(item['buy_max_price'])
                min_sell_price = str(item['sell_min_price'])
                quick_price = str(item['quick_price'])
                reference_price = str(item['sell_reference_price'])
                steam_price = str(item['goods_info']['steam_price'])
                steam_market_url = item['steam_market_url']
                f.write(id + ";" +
                        name + ";" +
                        max_buy_price + ";" +
                        min_sell_price + ";" +
                        quick_price + ";" +
                        reference_price + ";" +
                        steam_price + ";" +
                        steam_market_url + "\n")

        # print(len(items), x)
        if len(items) == total_item_count:
            break
    times_through += 1

f.close()
