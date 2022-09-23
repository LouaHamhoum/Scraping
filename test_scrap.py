import pytest
import json
from fastapi.testclient import TestClient
from app.ScrapingFacebook import scrap_page,app,scraping_fct

#test scraping data from amazon facebook page and save it in dataframe to show if df empty or not
def test_df_Not_Empty():
    assert scrap_page('Amazon').empty == False


