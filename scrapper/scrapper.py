from selenium import webdriver
from webdriverinstaller import driverinstaller
from selenium.webdriver.common.by import By
import time
import requests
import os
import io
from PIL import Image
import sqlite3

#=========================================== connect to database ===========================================================================#

conn = sqlite3.connect('images.db')
cur = conn.cursor()

#cur.execute('''CREATE TABLE imagedata (filename VARCHAR(50),source VARCHAR(50), location VARCHAR(50), link VARCHAR(200) ,image BLOB )''')



#============================================ DB connect ====================================================================================#

driver = driverinstaller("firefox")

wd = webdriver.Firefox(driver)

THUMBNAIL = "bRMDJf"
IMAGE = "n3VNCb"

#===================================================== GOOGLE SCRAPPER =====================================================================#

def get_images_from_google(wd, delay, max_images):
	def scroll_down(wd):
		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(delay)

	url = "https://www.google.com/search?q=person+face&sxsrf=ALiCzsYkwzMBF701790qjKGdk0OIklatdw:1669060112866&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjO-oq5hcD7AhWmXvEDHaQwBjcQ_AUoAXoECAEQAw&biw=1366&bih=662&dpr=1"
	wd.get(url)

	image_urls = set()
	skips = 0
	image_path = list(image_urls)


	while len(image_urls) + skips < max_images:
		scroll_down(wd)

		thumbnails = wd.find_elements(By.CLASS_NAME, THUMBNAIL)

		for img in thumbnails[len(image_urls) + skips:max_images]:
			try:
				img.click()
				time.sleep(delay)
			except:
				continue

			images = wd.find_elements(By.CLASS_NAME, IMAGE)
			for image in images:
				if image.get_attribute('src') in image_urls:
					max_images += 1
					skips += 1
					break

				if image.get_attribute('src') and 'http' in image.get_attribute('src'):
					image_urls.add(image.get_attribute('src'))
					print(f"Found {len(image_urls)}")
	return image_urls

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

urls = get_images_from_google(wd, 1, 20)

# save images to folder & database

for i, url in enumerate(urls):
	path = ('./scrapper/googleimages/')
	if not os.path.exists(path):
		os.makedirs(path)
	source = ("google")	
	filename = (str(i) + ".jpg")
	download_image(path, url, filename)
	fpath = (path + filename)
	image = open(fpath,"rb").read()
	link = (url)
	location = (path)
	cur.execute('''INSERT INTO imagedata VALUES (?,?,?,?,?)''', ( filename, source ,location ,link ,sqlite3.Binary(image)))
	conn.commit()
	

wd.quit()
#======================================================  SCRAP ===================================================================#

