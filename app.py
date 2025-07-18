from flask import Flask, render_template, request, session, redirect, url_for
from flask_session import Session
from etterspor_data import skrap
import json

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["TEMPLATES_AUTO_RELOAD"] = True
Session(app)


@app.route('/')
def index():  # put application's code here
    return redirect(url_for("spill", merker='["nintendo"]', butikker='["Halden"]'))


@app.route("/spill")
def spill():
    #finne produkt
    merker = json.loads(
        request.args.get("merker", "[]")          #merker=[playstation, xbox, nintendo]           #merker=[playstation, nintendo]
    )

    if merker == []:
        merker = ["nintendo"]

    merke_verdier =  {
        "playstation": 8015,
        "xbox": 8023,
        "nintendo": 8027
    }

    merke_ider = []
    for merke in merker:
        merke_ider.append(merke_verdier[merke])


    #finne butikk
    butikker = json.loads(
        request.args.get("butikker", "[]")          #butikker=["halden", "fredrikstad", "sarpsborg"]
    )

    allle_power_butikker = {
        "Alnabru": 1120,
        "Alta": 1199,
        "Arendal": 1156,
        "Askim": 1139,
        "Askvoll": 1516,
        "Askøy": 1107,
        "Bergen Sentrum": 1106,
        "Bjørkelangen": 1635,
        "Bodø": 1190,
        "Brotorvet": 1679,
        "Brumunddal": 1181,
        "Brønnøysund": 1695,
        "Bø i Telemark": 1618,
        "City": 1130,
        "Drammen": 1124,
        "Egersund": 1693,
        "Eidsvoll": 1608,
        "Elverum": 1129,
        "Etne": 1347,
        "Evje": 1645,
        "Farsund": 1687,
        "Fauske": 1479,
        "Finnsnes": 1194,
        "Flekkefjord": 1455,
        "Florø": 1684,
        "Forus": 1110,
        "Fredrikstad": 1170,
        "Gjøvik": 1180,
        "Gran": 1137,
        "Grimstad": 1152,
        "Halden": 1132,
        "Hamar": 1126,
        "Hammerfest": 1682,
        "Harstad": 1195,
        "Haugesund": 1344,
        "Hemsedal": 1638,
        "Hitra": 1681,
        "Hokksund": 1459,
        "Horten": 1146,
        "Husnes": 1345,
        "Hønefoss": 1128,
        "Jessheim": 1117,
        "Jærhagen": 1691,
        "Jørpeland": 1641,
        "Knarvik": 1108,
        "Kongsberg": 1147,
        "Kongsvinger": 1177,
        "Kragerø": 1678,
        "Kristiansand Sentrum": 1688,
        "Kristiansund": 1164,
        "Lade": 1142,
        "Lagunen": 1103,
        "Larvik": 1677,
        "Leknes": 1683,
        "Leksvik": 1166,
        "Levanger": 1171,
        "Lille Grensen": 1121,
        "Lillehammer": 1184,
        "Lillesand": 1547,
        "Lyngdal": 1544,
        "Lørenskog": 1118,
        "Majorstuen": 1123,
        "Mandal": 1597,
        "Mariero": 1690,
        "Mjøndalen": 1188,
        "Moa": 1161,
        "Mo I Rana": 1192,
        "Molde": 1169,
        "Mosjøen": 1595,
        "Moss": 1127,
        "Namsos": 1174,
        "Narvik": 1198,
        "Nesbyen": 1660,
        "Nordfjord": 1659,
        "Notodden": 1148,
        "Nærbø": 1550,
        "Odda": 1620,
        "Oppdal": 1532,
        "Orkanger": 1326,
        "Porsanger": 1302,
        "Porsgrunn": 1676,
        "Revetal": 1493,
        "Rissa": 1542,
        "Risør": 1680,
        "Rosendal": 1464,
        "Rud": 1122,
        "Rørvik": 1685,
        "Sandefjord": 1149,
        "Sandnessjøen": 1652,
        "Sandnes (Amfi Vågen)": 1692,
        "Sarpsborg": 1173,
        "Seljord": 1427,
        "Ski": 1135,
        "Skien": 1155,
        "Skjåk": 1639,
        "Skullerud": 1116,
        "Skøyen": 1186,
        "Slependen": 1119,
        "Smøla": 1673,
        "Sogndal": 1666,
        "Stavanger Tvedt": 1112,
        "Steinkjer": 1172,
        "Stjørdal": 1168,
        "Stord": 1343,
        "Storo": 1115,
        "Stryn": 1656,
        "Strømmen": 1185,
        "Sunnfjord": 1674,
        "Surnadal": 1615,
        "Sykkylven": 1640,
        "Søgne": 1662,
        "Sørlandstunet": 1157,
        "Tiller": 1144,
        "Tromsø Jekta": 1193,
        "Tynset": 1533,
        "Tønsberg": 1145,
        "Vadsø": 1611,
        "Valdres": 1672,
        "Vestby": 1136,
        "Vestkanten": 1109,
        "Vestnes": 1494,
        "Vinstra": 1555,
        "Voss": 1104,
        "Vågå": 1643,
        "Øystese": 1356,
        "Ål": 1696,
        "Ålesund": 1160,
        "Åndalsnes": 1661,
        "Årnes": 1548,
        "Åsane": 1101
    }

    butikk_ider = []
    for butikk in butikker:
        butikk_ider.append(allle_power_butikker.get(butikk.title(), 0))

    if butikk_ider == [] or sum(butikk_ider) == 0:
        print("ingen butikk valgt")
        butikk_ider = [1132]
        print(butikk_ider)


    if merker == [] and butikk_ider != []:
        merke_ider = [8015, 8023, 8027]

    #skrap
    produkter = []
    for merke_id in merke_ider:
        produkter += skrap(cat=merke_id, butikker=butikk_ider)          #kombinere listene

    print(len(produkter))

    return render_template("produkter_grid.html", produkter=produkter, alle_butikker=allle_power_butikker.keys())

@app.route("/halden")
def halden():
    return render_template("produkter_grid.html", produkter=skrap(cat=8015, butikker=[1132]))

@app.route("/qrkode")
def qrkode():
    pass



if __name__ == '__main__':
    app.run(debug=True)


