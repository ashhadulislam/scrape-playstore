no_of_pagedowns=1
_add_for_all_reviews="&showAllReviews=true"
output_location='app_reviews/outputs/'
output_pickle_location=output_location+"pickles/"
media_location='media/app_review_tools/'

env="heroku_uat"
# env="dev"

if env=="heroku_uat":
	chrome_driver_location='/app/.chromedriver/bin/chromedriver'
	google_chrome_bin="/app/.apt/usr/bin/google-chrome"
elif env=="dev":
	chrome_driver_location='app_reviews/software/chromedriver'
