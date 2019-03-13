import os

no_of_pagedowns=1
_add_for_all_reviews="&showAllReviews=true"


current_dir=os.getcwd()
print("current directory is ",current_dir)
env="heroku_uat"
# env="dev"

if env=="heroku_uat":
	# chrome_driver_location='/app/.chromedriver/bin/chromedriver'
	# google_chrome_bin="/app/.apt/usr/bin/google-chrome"
	# media_location='/app/media/app_reviews/'
	# output_location='/app/app_reviews/outputs/'
	chrome_driver_location=os.path.join(current_dir,".chromedriver","bin","chromedriver")
	google_chrome_bin=os.path.join(current_dir,".apt","usr","bin","google-chrome")
	media_location=os.path.join(current_dir,"media","app_reviews")
	output_location=os.path.join(current_dir,"app_reviews","outputs")

elif env=="dev":
	# chrome_driver_location='app_reviews/software/chromedriver'
	# media_location='media/app_review_tools/'
	# output_location='./app_reviews/outputs/'
	chrome_driver_location=os.path.join(current_dir,"app_reviews","software","chromedriver")
	media_location=os.path.join(current_dir,"media","app_reviews")
	output_location=os.path.join(current_dir,"app_reviews","outputs")

output_pickle_location=os.path.join(output_location,"pickles")