import BuffAPISession as buff


def get_matching_item(item_name):
    """ Returns the goods search data for the given item, if a good with a
        matching name is found. """
    search_results = buff.get_goods_search_json(item_name)
    total_pages = search_results['data']['total_page']
    total_count = search_results['data']['total_count']
    page_size = search_results['data']['page_size']
    for page in range(total_pages):
        suggestions = buff.get_goods_search_json(item_name, page + 1)
        page_item_count = total_count if total_count < page_size else page_size
        for item in range(page_item_count):
            suggestion = suggestions['data']['items'][item]
            if suggestion['market_hash_name'] == item_name:
                return suggestion
        total_count - page_size
    print("No exact name match found, assuming the first result.")
    return search_results['data']['items'][0]


def get_id(item_name, surpress_print=True):
    """ Prints the Buff ID for the given item name. """
    item = get_matching_item(item_name)
    if not surpress_print:
        print(item['name'] + " Buff ID: " + str(item['id']))
    return item['id']


def get_sell_price(item_name, surpress_print=True):
    """ Prints the lowest sell price for the given item name. """
    item_id = get_id(item_name)
    sell_price = 0
    try:
        low_sell_order = buff.get_sell_order_json(item_id)["data"]['items'][0]
        sell_price = float(low_sell_order['price'])
    except IndexError:
        if not surpress_print:
            print("No active Sell Orders")
        sell_price = ""
    if not surpress_print:
        print(item_name + " Lowest Sell Order: ¥" + str(sell_price))
    return sell_price


def get_buy_price(item_name, surpress_print=True):
    """ Prints the highest buy price for the given item name. """
    item_id = get_id(item_name, True)
    buy_price = 0
    try:
        high_buy_order = buff.get_buy_order_json(item_id)["data"]['items'][0]
        buy_price = float(high_buy_order['price'])
    except IndexError:
        if not surpress_print:
            print("No active Buy Orders")
        buy_price = ""
    if not surpress_print:
        print(item_name + " Highest Buy Order: ¥" + str(buy_price))
    return buy_price


def get_last_n_sales_avg_price(item_name, n, surpress_print=True):
    """ Prints the average price for the last n sales of the given item. """
    item_id = get_id(item_name, True)
    sales = buff.get_bill_order_json(item_id)["data"]['items']
    average_price = 0
    for i in range(n):
        try:
            average_price += float(sales[i]['price'])
        except IndexError:
            if not surpress_print:
                print("Not enough Sales history, using " +
                      i-1 + " sales instead.")
            n = i-1
            break
    average_price /= n
    if not surpress_print:
        print(item_name + " Last " + str(n) + " Sales Avg: ¥" +
              str(average_price))
    return average_price


def get_steam_market_price(item_name, surpress_print=True):
    """ Prints the Steam Market price for the given item name. """
    item = get_matching_item(item_name)
    if not surpress_print:
        print(item['name'] + " Steam Market price: $" +
              str(item['goods_info']['steam_price']))
    return item['goods_info']['steam_price']


def get_steam_market_url(item_name, surpress_print=True):
    """ Prints the Steam Market url for the given item name. """
    item = get_matching_item(item_name)
    if not surpress_print:
        print(item['name'] + " Steam Market URL: " +
              str(item['steam_market_url']))
    return item['steam_market_url']


''' TODO: Add this as CLI
get_id("EMS Katowice 2014 Legends", False)
get_sell_price("EMS Katowice 2014 Legends", False)
get_buy_price("EMS Katowice 2014 Legends", False)
get_last_n_sales_avg_price("EMS Katowice 2014 Legends", 5, False)
get_steam_market_price("EMS Katowice 2014 Legends", False)
get_steam_market_url("EMS Katowice 2014 Legends", False)
'''
