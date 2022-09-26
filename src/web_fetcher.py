from bs4 import BeautifulSoup
import requests

HEADER={'User-Agent': 'Mozilla/5.0'}

#Fetches data from op.gg
def get_stats(name=None, region=None):
    try:
        url = f"https://{region}.op.gg/summoners/{region}/{name}"
        response = requests.get(url=url, headers=HEADER)
        doc = BeautifulSoup(response.text, "html.parser")

        rank_element = doc.find("div", {"class": "tier"})
        level_element = doc.find("span", {"class": "level"})
        winrate_element = doc.find("div", {"class": "ratio"})

        winrate_text = winrate_element.getText().split()[2]
        rank_text = rank_element.getText().capitalize()
        level_text = level_element.getText()

    except Exception:
        return "Could not find account"

    else:
        return {
                "rank": rank_text, 
                "level": level_text,
                "winrate": winrate_text,
               }

#account = get_stats('War', 'euw')
#print(account)