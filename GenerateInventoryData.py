import BuffBot as buff


def parse_csgo_exchange_export(filepath):
    artifact_path = filepath[:-4]+".csv"
    artifact = open(artifact_path, "w", encoding="utf-8")
    artifact.write("#;Name;Steam Market Price (csgo.exchange - USD)\n")
    lines = open(filepath, "r", encoding="utf-8").readlines()
    for line in lines:
        artifact.write(
            line.strip().replace(" x ", ";").replace(" = ", ";") + "\n")
    return artifact_path


def append_buff_data_to_inventory_list(filepath):
    artifact_path = filepath[:-4]+"WithBuffData.csv"
    artifact = open(artifact_path, "w", encoding="utf-8")
    input = open(filepath, "r", encoding="utf-8")
    artifact.write(
        input.readline().strip() +
        ";Buff ID;Max Buy Price (RMB);Min Sell Price (RMB);"
        "Last 5 Sales Average Price (RMB);Steam Market Price (Buff - USD);"
        "Steam Market URL\n")
    for line in input.readlines():
        item_name = line.strip().split(";")[1]
        print(item_name)
        id = buff.get_id(item_name)
        max_buy_price = buff.get_buy_price(item_name)
        min_sell_price = buff.get_sell_price(item_name)
        last5_avg_price = buff.get_last_n_sales_avg_price(item_name, 5)
        steam_market_price = buff.get_steam_market_price(item_name)
        steam_market_url = buff.get_steam_market_url(item_name)
        artifact.write(
            line.strip() + ";" + str(id) + ";" + str(max_buy_price) + ";" +
            str(min_sell_price) + ";" + str(last5_avg_price) + ";" +
            str(steam_market_price) + ";" + str(steam_market_url) + "\n")
    return artifact_path


parsed = parse_csgo_exchange_export("./CSGOExchangeExport.txt")
append_buff_data_to_inventory_list(parsed)
