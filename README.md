# scrape-playstore
scraping user reviews from playstore

### Installation
Use below command to install the required library
`pip install -r requirements.txt`

### Usage
To run the app hit the following

`python manage.py runserver`


If you are running the app locally, make sure you go to app_reviews/scripts/constants.py and change
from
env="heroku_uat"
# env="dev"

to
# env="heroku_uat"
env="dev"

Check the blog post to see how to make it run at
https://medium.com/tech-that-works/democratising-data-science-one-step-at-a-time-ccbb3640cced
