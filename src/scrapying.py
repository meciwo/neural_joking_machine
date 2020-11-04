import requests
from bs4 import BeautifulSoup
import os
import pandas as pd



LOAD_URL = "https://bokete.jp/odai/"
main_df = pd.DataFrame([])

# Webページを取得して解析する
#4.4MB 
for page in range(100):
    batch_df = pd.DataFrame([])
    page_url = LOAD_URL + "55316" + str(page).zfill(2)
    html = requests.get(page_url)
    soup = BeautifulSoup(html.content, "html.parser")
    texts = []
    img=soup.find("div", class_ = "photo-content").find("img").get("src")

    for text in soup.find_all("a", class_ = "boke-text"):
        texts.append(text.get_text().strip())
    re = requests.get("https:"+img)
    with open("data/"+img.split("/")[-1], 'wb') as f:
        f.write(re.content)

    batch_df["image"] = [img.split("/")[-1]]*len(texts)
    batch_df["text"] = texts
    main_df = pd.concat([main_df, batch_df], axis = 0)
#print(main_df)
main_df.to_csv("relation.csv", index=False)