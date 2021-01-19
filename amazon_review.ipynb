from bs4 import BeautifulSoup as bs
import requests
from urllib.request import urlopen as uReq 
import datetime
import pandas as pd


amazon_all_review = {}
for k in range(1,500):
    link = f'https://www.amazon.in/OnePlus-Mirror-Black-128GB-Storage/product-reviews/B07DJHV6VZ/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={k}'
    page = requests.get(link)
    soup = bs(page.content,'html.parser')
    ##Find all users names
    names = soup.findAll('span',class_='a-profile-name')
    user = []
    for i in names:
        user.append(i.get_text())
    users = user[2:]
    ##Find all individual reviews titles
    products = soup.findAll('a',{'data-hook':'review-title'})
    review_title = []
    for i in products:
        review_title.append(i.get_text().strip())
    ##Find all stars rating
    stars = soup.findAll('i',{'data-hook':'review-star-rating'})
    stars_review = []
    for i in stars:
        stars_review.append(float(i.get_text().replace('out of 5 stars','')))
    ##Find all comments
    comments = soup.findAll('span',{'data-hook':'review-body'})
    comments_review = []
    for i in comments:
        comments_review.append(i.get_text().strip())
    ##Store review times
    times = soup.findAll('span',{'data-hook':'review-date'})
    time_review = []
    for i in times:
        #print(i.get_text().replace('Reviewed in India on ','').strip())
        time_review.append(datetime.datetime.strptime(i.get_text().replace('Reviewed in India on ',''),'%d %B %Y').date())
    ##Store them in a dictionary
    for i in range(len(users)):
        amazon_review[users[i]]={'review_title':review_title[i],'review_stars':stars_review[i],'review_time':time_review[i],
                             'comments_review':comments_review[i]}
                             
                             
##save the dictionary in a csv file
amazon_review_pd = pd.DataFrame(amazon_review)
amazon_review_pd = amazon_review_pd.T
amazon_review_pd.to_csv('amazon_review.csv')
