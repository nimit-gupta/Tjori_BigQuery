#Big query pageviews

import psycopg2 as pg
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
%matplotlib inline

def getting_credentials():
    credentials = service_account.Credentials.from_service_account_file('C:/Users/sachi/OneDrive/Desktop/Google_BigQuery/client_secret_358050000476-cn1c98do5mg0e43jvvvh3fgpklkdqlhs.apps.googleusercontent.com.json')
    client = bigquery.Client(credentials = credentials)
    return client

def sql_query():
    client = getting_credentials()
    
    sql = '''
          --strucutred query language; query

          SELECT 
              TO_CHAR(DATE,'WW') AS week_of_the_year
             ,SUM(page_views) AS total_pageviews
          FROM 
              ga_union_pageviews
          WHERE 
              DATE BETWEEN '2019-01-01' AND '2020-01-01'
          GROUP BY 
              1
          ORDER BY 
              MIN(DATE)
             ;
          '''
    df = client.query(sql).to_dataframe()
    return df

def plot_query():
    df = sql_query()
    fig, ax = plt.subplots(1, figsize = (30,8))
    ax.bar(df['week_of_the_year'], df['total_pageviews'])
    ax.set_xlabel('Weeks')
    ax.set_ylabel('Pageviews')
    ax.set_title('Weeks/Pageviews', bbox={'facecolor':'0.8', 'pad':3})
    plt.show()
    
def main():
    plot_query()
    
if __name__ == '__main__':
    main()
    