#Import all dependencies to webscrape
from selenium import webdriver
from selenium.webdriver.common.by import By

#Scrape stuff
class WebScrape():

    def __init__(self):
        pass

    def read_parsons():

        """
        Reads in Parson's code written by compute.py to use as variable
        """

        #So that variable can be accessed elsewhere in the file
        global parsons_code 

        with open("parson.txt", "r") as parsons_file:
            parsons_code = parsons_file.read()

    def scrape_musipedia():

        """
        - Uses Selenium & ChromeDriver to extract information about top 3 most likely songs
        - Requires scraping html
        - Relies on Musipedia not being updated
        """

        #Path details
        path_of_driver = "/Users/adityatatwawadi/Downloads/chromedriver"
        driver = webdriver.Chrome(executable_path = path_of_driver)

        #Access musipedia's website
        website_url = "https://www.musipedia.org/melodic_contour.html"
        driver.get(website_url)
        #print(driver.title)

        #Enters in the Parson's code to search engine
        driver.find_element(By.NAME, 'tx_mpsearch_pi1[pc]').send_keys(parsons_code)

        #Submits & accesses database
        click_button = driver.find_element(By.NAME, 'tx_mpsearch_pi1[submit_button]')
        click_button.click()

        #Scrolls down to top 3 identified songs
        driver.execute_script("window.scrollBy(0,400)")

        #Reframes & takes a screenshot of top3 recommendtaions
        S = lambda X: driver.execute_script('return document.body.parentNode.scroll' +X)
        driver.set_window_size(S('Width'), S('Height'))
        driver.find_element_by_tag_name('body').screenshot("musipedia_recommendations.png")

        #Exits automated chrome
        driver.quit()

WebScrape.read_parsons()
WebScrape.scrape_musipedia()