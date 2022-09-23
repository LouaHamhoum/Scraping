#pip install facebook-scraperf
import uvicorn
from facebook_scraper import get_group_info, get_posts, set_noscript
from fastapi import FastAPI
import pandas as pd
import sqlite3


app = FastAPI()


def scrap_page(page_name):
    post_list=[] 
    for post in get_posts(page_name, pages=3, options={"comments": True, "reactors": True}):
        post_str={k:[str(item)] for k,item in post.items()}
        df=pd.DataFrame.from_dict(post_str)
        post_list.append(df)
    df_all=pd.concat(post_list,ignore_index=True)
    return df_all

def saveTodatabase(df_all):  
    conn = sqlite3.connect('./local_db/scrapingFacebbok_database')
    c = conn.cursor()
    columns=df_all.columns.to_list

    c.execute('CREATE TABLE IF NOT EXISTS posts (columns)')
    conn.commit()
    df_all.to_sql('posts', conn, if_exists='replace', index = False)
    
def scrap_fill_database( pageName):
    df=scrap_page(pageName)
    saveTodatabase(df)
    return 'Success'
  


#POST Method
@app.post("/scraping")
async def scraping_fct(pageName:str):
    return scrap_fill_database( pageName)

    
#Web server port 8080
if __name__ == "__main__":
     uvicorn.run(app, port=8080 )
