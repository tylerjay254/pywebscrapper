from selenium import webdriver
from webdriverinstaller import driverinstaller
from selenium.webdriver.common.by import By
from PIL import Image
import time 
import requests
import os
import io
from PIL import Image


driver = driverinstaller("firefox")

wd = webdriver.Firefox(driver)


#============================================ CONFIG =========================================#

driver = driverinstaller("firefox")

wd = webdriver.Firefox(driver)

GTHUMBNAIL = "bRMDJf"
GIMAGE = "n3VNCb"
BING_THUMBNAIL = "YVj9w"
BING_IMAGE = "ht4YT"
GLINK = "https://www.google.com/search?q=person+face&sxsrf=ALiCzsYkwzMBF701790qjKGdk0OIklatdw:1669060112866&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjO-oq5hcD7AhWmXvEDHaQwBjcQ_AUoAXoECAEQAw&biw=1366&bih=662&dpr=1"
BLINK = "https://unsplash.com/s/photos/person-face"

#======================== GOOGLE SCRAPPER ================================#

def googleScrapper(wd, delay, max_images):
	def scroll_down(wd):
		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(delay)

	url = (GLINK)
	wd.get(url)

	image_urls = set()
	skips = 0
	


	while len(image_urls) + skips < max_images:
		scroll_down(wd)

		thumbnails = wd.find_elements(By.CLASS_NAME, GTHUMBNAIL)

		for img in thumbnails[len(image_urls) + skips:max_images]:
			try:
				img.click()
				time.sleep(delay)
			except:
				continue

			images = wd.find_elements(By.CLASS_NAME, GIMAGE)
			for image in images:
				if image.get_attribute('src') in image_urls:
					max_images += 1
					skips += 1
					break

				if image.get_attribute('src') and 'http' in image.get_attribute('src'):
					image_urls.add(image.get_attribute('src'))
					print(f"Found {len(image_urls)}")
	return image_urls

#============================== Downloader ===============================#


def download_image(download_path, url, file_name):
	try:
		image_content = requests.get(url).content
		image_file = io.BytesIO(image_content)
		image = Image.open(image_file)
		file_path = download_path + file_name

		with open(file_path, "wb") as f:
			image.save(f, "JPEG")

		print("Success")
	except Exception as e:
		print('FAILED -', e)

		

	urls = googleScrapper(wd, 1, 20)

	# save images to folder & database

	for i, url in enumerate(urls):
		path = ('./scrapper/googleimages/')
		if not os.path.exists(path):
			os.makedirs(path)
		source = ("google")	
		filename = (str(i) +".jpg")
		download_image(path, url, filename)
		fpath = (path + filename)
		image = open(fpath,"rb").read()
		link = (url)
		location = (path)
		# CURR.execute('''INSERT INTO imagedata VALUES (?,?,?,?,?)''', ( filename, source ,location ,link ,sqlite3.Binary(image)))
		# CONN.commit()
		
wd.quit()
