from . import constants
import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options  


def browser_functions(url):
    print("chromedriver ",constants.chrome_driver_location)
    chrome_options = Options()  
    chrome_options.add_argument("--headless")  
    chromedriver_loc = constants.chrome_driver_location
    browser = webdriver.Chrome(executable_path=chromedriver_loc, chrome_options=chrome_options)  
    browser.get(url)


    no_of_pagedowns = constants.no_of_pagedowns
    elem = browser.find_element_by_tag_name("body")
    while no_of_pagedowns:
        print(no_of_pagedowns)
        dur=3
        elem.send_keys(Keys.END)
        time.sleep(dur)
        no_of_pagedowns-=1
        #click on the show more button if its there
        try:
            print("finding path")
            show_more=browser.find_element_by_xpath('//content[@class="CwaK9"]')
            print("find by span")
            show_more=show_more.find_element_by_tag_name("span")
            if show_more.text == "SHOW MORE":
                print("going to click")
                browser.execute_script("arguments[0].click();", show_more)
                print("just clicked")
    #             show_more.click()
        except Exception as e: 
            #code will come here when there are no buttons such as show more
            # print(e)
    #         print("Something wrong")
            continue

    source=browser.page_source
    print("got source successfully")
    browser.close()

    return source

def parse_html_page(source):

    soup = BeautifulSoup(source, 'html.parser')
    post_name_blocks=soup.find_all('div', class_='xKpxId zc7KVe')
    print("Number of posts = ",len(post_name_blocks))


    names=[]
    star_texts=[]
    star_numbers=[]
    review_dates=[]
    helpful_counts=[]
    count=0
    for post_name_block in post_name_blocks:

        #name of reviewer
        poster_name=post_name_block.find('span',class_='X43Kjb').text
        names.append(poster_name)

        #number of stars
        rating=post_name_block.find('div',class_='pf5lIe').findAll('div')
    #     print("rating",rating)
        rating_text=rating[0]
        rating_text=rating_text.get_attribute_list("aria-label")[0]
        rating_number=rating_text[6]

        star_texts.append(rating_text)
        star_numbers.append(rating_number)


        #get date of rating given
        rating_date=post_name_block.find('span',class_ = "p2TkOb").text    
        review_dates.append(rating_date)

        helpful_count=post_name_block.find("div",class_="jUL89d y92BAb").text
        helpful_counts.append(helpful_count)
        count+=1
        if count%100 == 0:
            print(count)

    review_texts=[]
    #for reviews

    reviews=soup.select('div.UD7Dzf > span')
    print("For this post")
    count=0
    while count<len(reviews):
        short_review=reviews[count].get_text(strip=True)
        count+=1
        if count==len(reviews):
            break
        long_review=reviews[count].get_text(strip=True)
        if len(short_review)!=0:
            review=short_review
        if len(long_review)!=0:
            review=long_review
        count+=1
        review_texts.append(review)
        if count%100 == 0:
            print(count)

    print("Final Review",len(review_texts))


    d={}
    d["reviewer_name"]=names
    d["review_date"]=review_dates
    d["review_star_text"]=star_texts
    d["review_star_count"]=star_numbers
    d["review_helpful_count"]=helpful_counts
    d["review"]=review_texts



    for key, value in d.items():
        print(len(value))

    df = pd.DataFrame(data=d)
    print(df.shape)
    print("Got df successfully")
    return df




def get_reviews(url):


    #adding the "get all review" part in the URL
    adder=constants._add_for_all_reviews
    if adder not in url:
        url=url+adder
    print("URL before call is",url)

    
    #get html source data after clicking on more review and tapping END
    html_source=browser_functions(url)
    if html_source==None:
        return False

    
    #parse the source to get the different components of the review
    df=parse_html_page(html_source)
    

    if df is None:
        return False

    
    df.to_csv(constants.output_location+"app_revs.csv")
    return True



