from time import sleep
import requests as r


def get_buff_session():
    """
    Place your Buff.163 session cookie here to scrape Buff pricing data.

    You can obtain your cookie by logging in and inspecting the page.
    On Chrome it is found under the Application tab. In the "Storage" section
    select "Cookies > htps://buff163.com" and paste the data from the "Value"
    column matching the row named "session" below.
    """
    return {'session': '<INSERT SESSION COOKIE HERE>'}


games = {
    'csgo',
    'dota2',
    'rust',
    'h1z1',
    'tf2',
    'pubg',
    'pubg_recycle'
}
default_game = 'csgo'
api_url = "https://buff.163.com/api/market/"


def get_game(game):
    if game not in games:
        print("Invalid game: " + game +
              ", assuming you meant: " + default_game +
              ".  Valid games are: " + str(games))
        game = default_game
    return game


def get_suggestion_url(search_text, game):
    return (api_url + "search/suggest?text=" + search_text +
                      "&game=" + get_game(game))


def get_market_page_url(page_num, game):
    return (api_url + "goods?page_num=" + str(page_num) +
                      "&game=" + get_game(game))


def get_goods_search_url(search_text, page_num, game):
    return (api_url + "goods?search=" + search_text +
                      "&page_num=" + str(page_num) +
                      "&game=" + get_game(game))


def get_sell_order_url(id, game):
    return (api_url + "goods/sell_order?goods_id=" + str(id) +
                      "&game=" + get_game(game))


def get_buy_order_url(id, game):
    return (api_url + "goods/buy_order?goods_id=" + str(id) +
                      "&game=" + get_game(game))


def get_bill_order_url(id, game):
    return (api_url + "goods/bill_order?goods_id=" + str(id) +
                      "&game=" + get_game(game))


def get_suggestion_json(item_name, game=default_game):
    """ Makes a Buff API call to suggest a Buff ID for the given name text. """
    suggest_url = get_suggestion_url(item_name, game)
    sleep(5)
    return r.get(suggest_url, cookies=get_buff_session()).json()


def get_market_page_json(page_num=1, game=default_game):
    """ Executes a Buff API call to list the items on a given page #. """
    page_url = get_market_page_url(str(page_num), game)
    sleep(5)
    return r.get(page_url, cookies=get_buff_session()).json()


def get_goods_search_json(item_name, page_num=1, game=default_game):
    """ Executes a Buff API call to list the items matching a search term. """
    page_url = get_goods_search_url(item_name, str(page_num), game)
    sleep(5)
    return r.get(page_url, cookies=get_buff_session()).json()


def get_sell_order_json(buff_id, game=default_game):
    """ Calls Buff API to get the sell order data for a given item ID. """
    sell_order_url = get_sell_order_url(buff_id, game)
    sleep(5)
    return r.get(sell_order_url, cookies=get_buff_session()).json()


def get_buy_order_json(buff_id, game=default_game):
    """ Calls Buff API to get the buy order data for a given item ID. """
    buy_order_url = get_buy_order_url(buff_id, game)
    sleep(5)
    return r.get(buy_order_url, cookies=get_buff_session()).json()


def get_bill_order_json(buff_id, game=default_game):
    """ Calls Buff API to get the trade recodrs data for a given item ID. """
    bill_order_url = get_bill_order_url(buff_id, game)
    sleep(5)
    return r.get(bill_order_url, cookies=get_buff_session()).json()
