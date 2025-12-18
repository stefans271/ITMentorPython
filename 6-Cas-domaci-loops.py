
shops={
    "Maxi":{
        "hleb":80,
        "novine":50
    },
    "Idea":{
        "hleb":95,
        "novine":62
    },
    "Market":{
        "hleb":100,
        "novine":60
    },
    "Roda":{
        "novine":60
    }
}
max_price=0
max_price_shop=""
for i,items in shops.items():
    if "hleb" in items:
        if max_price<items["hleb"]:
            max_price = items["hleb"]
            max_price_shop = i
print(max_price, max_price_shop)
