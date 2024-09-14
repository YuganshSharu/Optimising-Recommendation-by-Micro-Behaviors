import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import googleapiclient.discovery
import requests
import pandas as pd
import pickle
from tabulate import tabulate
import pandas as pd
from IPython.display import HTML 


X_item_df = pd.DataFrame()
with open('X_item_model.pkl', 'rb') as f:
    X_item_df = pickle.load(f)

X_item_price_df = pd.DataFrame()
with open('X_item_price_model.pkl', 'rb') as f:
    X_item_price_df = pickle.load(f)

X_item_price_brand_df = pd.DataFrame()
with open('X_item_price_brand_model.pkl', 'rb') as f:
    X_item_price_brand_df = pickle.load(f)

X_item_price_brand_df.head()




def query_5(uid,cat):
        uid=int(uid)
        model1=top_5_recommendations(uid,cat,'item_based')
        model1=model1[['product_id','brand','price','predicted_interaction']]
        # model1=tabulate(model1, headers='keys', tablefmt='psql')
        model1=HTML(model1.to_html(index=True, header=True))
    
        model2=top_5_recommendations(uid,cat,'item_price_based')
        model2=model2[['product_id','brand','price','predicted_interaction']]
        model2=HTML(model2.to_html(index=True, header=True))
        # print(model2)

        model3=top_5_recommendations(uid,cat,'item_price_brand_based')
        model3=model3[['product_id','brand','price','predicted_interaction']]
        model3=HTML(model3.to_html(index=True, header=True))
        # print(model3)
        
        
        return [uid,cat,model1,model2,model3]


def top_5_recommendations(user_id, prod_category, model_type):
  if model_type == 'item_based':
    ui_condition = (X_item_df['user_id'] == user_id) & (X_item_df['category_code'] == prod_category)
    user_cat_df = X_item_df.loc[ui_condition]
    top_5_df = user_cat_df.sort_values('interaction_score', ascending=False).head(5)
    return top_5_df
  if model_type == 'item_price_based':
    ui_condition = (X_item_price_df['user_id'] == user_id) & (X_item_price_df['category_code'] == prod_category)
    user_cat_df = X_item_price_df.loc[ui_condition]
    top_5_df = user_cat_df.sort_values('interaction_score', ascending=False).head(5)
    return top_5_df
  if model_type == 'item_price_brand_based':
    ui_condition = (X_item_price_brand_df['user_id'] == user_id) & (X_item_price_brand_df['category_code'] == prod_category)
    user_cat_df = X_item_price_brand_df.loc[ui_condition]
    top_5_df = user_cat_df.sort_values('interaction_score', ascending=False).head(5)
    return top_5_df

# top5 = top_5_recommendations(512444451, 'computers.notebook', 'item_price_brand_based')
