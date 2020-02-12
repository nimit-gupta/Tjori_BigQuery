#Big Query

from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

def getting_credentials():
    
    credentials = service_account.Credentials.from_service_account_file('C:/Users/sachi/OneDrive/Desktop/Google_BigQuery/client_secret_358050000476-cn1c98do5mg0e43jvvvh3fgpklkdqlhs.apps.googleusercontent.com.json')
    client = bigquery.Client(credentials = credentials)
    return client

def sql_query(category):
    
    client = getting_credentials()
    
    sql = '''
             --strucutred query language; query

              SELECT 
                   TO_CHAR(soi.created, 'WW') AS week_of_the_year
                  ,SUM(soi.quanity) as total_quantity
              FROM 
                   order_order AS so
              LEFT JOIN 
                   order_orderproduct AS soi ON (so.id = soi.order_id)
              LEFT JOIN 
                   store_product AS sp ON (soi.product_id = sp.id)
              LEFT JOIN 
                   store_category AS sc ON (sp.category_id = sc.id)
              WHERE 
                  soi.created >= '2019-01-01' 
	              AND soi.created < '2020-01-01'
                  AND so.status = 'confirmed'
                  AND sc.name = '%s'
              GROUP BY 
                  1
                ; 
          '''%(
               category
              )
    return client.query(sql).to_dataframe()

def execute_query():
    
    df = []
    for category in ['Apparel','Wellness','Jewelry','Home & Decor','Footwear']:
      retval = sql_query(category)
      df.append(retval)
    return df

def plot_query():
    
    df = execute_query()
    
    fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, figsize = (30,30))
    ax1.bar(df[0]['week_of_the_year'], df[0]['total_quantity'], color = 'rosybrown')
    ax2.bar(df[1]['week_of_the_year'], df[1]['total_quantity'], color = 'lightcoral')
    ax3.bar(df[2]['week_of_the_year'], df[2]['total_quantity'], color = 'indianred')
    ax4.bar(df[3]['week_of_the_year'], df[3]['total_quantity'], color = 'brown')
    ax5.bar(df[4]['week_of_the_year'], df[4]['total_quantity'], color = 'firebrick')
    
    ax1.set_xlabel('Weeks')
    ax1.set_ylabel('Total quanity')
    ax1.set_title('Weeks/Total quanity - Apparel', bbox={'facecolor':'0.8', 'pad':3})
    ax2.set_xlabel('Weeks')
    ax2.set_ylabel('Total quanity')
    ax2.set_title('Weeks/Total quanity - Wellness', bbox={'facecolor':'0.8', 'pad':3})
    ax3.set_xlabel('Weeks')
    ax3.set_ylabel('Total quanity')
    ax3.set_title('Weeks/Total quanity - Jewelry', bbox={'facecolor':'0.8', 'pad':3})
    ax4.set_xlabel('Weeks')
    ax4.set_ylabel('Total quanity')
    ax4.set_title('Weeks/Total quanity - Home & Decor', bbox={'facecolor':'0.8', 'pad':3})
    ax5.set_xlabel('Weeks')
    ax5.set_ylabel('Total quanity')
    ax5.set_title('Weeks/Total quanity - Footwear', bbox={'facecolor':'0.8', 'pad':3})
    
    plt.show()
    
def main():
    plot_query()
   
if __name__ == '__main__':
    main()