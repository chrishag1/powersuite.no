import requests

def skrap(cat=8015, butikker=None):

    if butikker is None or butikker == [0]:
        tilgjengli_i_butikk_tekst = ""

    else:
        tilgjengli_i_butikk_tekst = "BasicCnC>>1"
        for butikk_id in butikker:
            tilgjengli_i_butikk_tekst += f"<>{butikk_id}"

    url = "https://www.power.no/api/v2/productlists"
    params = {
        "cat": cat,
        "size": "36",
        "s": "5",
        "from": "0",
        "o": "false",
        "f": tilgjengli_i_butikk_tekst,
        #BasicCnC%3E%3E1%3C%3E1132%3C%3E1170%3C%3E1173
        #BasicCnC>>1<>1132<>1170<>1173

    }

    response = requests.get(url, params=params)
    #print(len(response.json()["products"]))
    params["size"] = f"{response.json()['totalProductCount']}"
    response = requests.get(url, params=params)

    spill = []

    for produkt in response.json()["products"]:
        if produkt["canAddToCart"]:
            spill.append(finne_info_om_produkt(produkt))
    spill.sort(key=lambda x: x["navn"])

    return spill


    """
    dict_keys(['categoryId', 'categoryName', 'clickNCollectStoreCount', 'energyTier', 
    'isLimitedQuantity', 'manufacturerName', 'manufacturerId', 'price', 'productId', 
    'salesArguments', 'shortDescription', 'stockCount', 'storesStockCount', 
    'stockDeliveryDate', 'stockDeliveryDateConfirmed', 'stockLimitedRemaining', 'title', 
    'url', 'advertisingCampaigns', 'breadcrumb', 'productReview', 'hasDescription', 
    'serviceCategoryId', 'vatPercent', 'modelType', 'priceType', 'barcode', 'eanGtin12', 
    'showSavingsAs', 'productImage', 'productManuals', 'campaignMediaUrl', 'webStatus', 
    'productManufactorIdentity', 'webStockStatus', 'webStockText', 'webStockTextShort', 
    'webStockMeta', 'cncStockStatus', 'cncStockText', 'canAddToCart', 'isOnDemand', 
    'elguideId', 'isRecurringPaymentProduct', 'releaseDate', 'depositPriceIncluded'])
    """

    #print(finne_info_om_produkt(spill))

def finne_info_om_produkt(produkt_json):

    print(produkt_json["url"])

    funnet_info = {}
    info_leter_etter = [
        "title",
        "price",
        "shortDescription",
        "salesArguments",
        "stockCount",
        "url"
    ]

    for info in info_leter_etter:
        try:
            funnet_info[info] = produkt_json[info]
        except KeyError:
            funnet_info[info] = None


    produkt: dict = {
        "navn": funnet_info["title"],
        "pris": funnet_info["price"],
        "beskrivelse": funnet_info["shortDescription"],
        "salgsargument": funnet_info["salesArguments"],
        "rating": int(produkt_json.get("productReview", {}).get("overallAverageRating", 0)),
        "bilde": f"https://media.power-cdn.net{produkt_json['productImage']['basePath']}/{produkt_json["productImage"]["variants"][0]["filename"].replace('1200', '600').replace("150", "600")}",
        "url": funnet_info["url"],
        "nettlager": funnet_info["stockCount"],
    }


    return produkt


"""def finne_epost_og_telefon():
    url = "https://www.power.no/api/v2/products/1013369/stores"
    params = {
        "postalCode": "1785",
        "amount": "1000",
    }

    response = requests.get(url, params=params)
    sortert = sorted(response.json(), key=lambda x: x["name"])

    for butikk in sortert:
        butikk_navn = butikk["name"].replace("Power ", "").replace("POWER ", "").replace("  ", " ")     #Den siste der kun for sandnes, fordi det er to mellomrom
        print(f'"{butikk_navn}": {butikk["storeId"]},')


    for butikk in response.json():
        print(f"butikk: {butikk['name']}, epost: {butikk['email']}, telefon: {butikk['phone']}")
    


    #produkt bilde = https://media.power-cdn.net/images/products/productId/productId_1_skjermstørrelse_w_g.webp

    spill_navn = []
    for product in response.json()["products"]:
        spill_navn.append(product["title"])
    print(len(spill_navn))"""

    #print(response.json()["totalProductCount"])
"""
data = response.json()

for product in data.get('products', []):
    print(f"Produktnavn: {product.get('name')}")
    print(f"Pris: {product.get('price', {}).get('current')}")
    print(f"Tilgjengelighet: {product.get('availability')}")
    print(f"Produktlenke: {product.get('url')}")
    print("-" * 40)"""
