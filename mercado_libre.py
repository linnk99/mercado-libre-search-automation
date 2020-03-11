import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Opera(executable_path = "./operadriver")

    def test_search_men_shoes(self):
        #Data structures to be used
        search_term = 'zapatos de hombre'
        
        # Create browser instance and go to mercadolibre.com
        driver = self.driver
        driver.get("https://www.mercadolibre.com")

        #Select Colombia as country to search
        country = driver.find_element_by_id("CO")
        country.click()

        #Look for 'zapatos de hombre' as search term
        search_bar = driver.find_element_by_class_name("nav-search-input")
        search_bar.send_keys(search_term)
        search_bar.send_keys(Keys.ENTER)
        sleep(3)

        #Filter results by coditions as 'Nuevo' in 'Bogota'
        condition_as_new = driver.find_element_by_partial_link_text('Nuevo')
        condition_as_new.click()
        location = driver.find_element_by_partial_link_text("Bogotá D.C.")
        location.click()

        #Get number of results
        total_search_results = driver.find_element_by_class_name("quantity-results").text
        print(f'El total de resultados en la busqueda es: {total_search_results}')

        #Order price from lower
        order_dropdown = driver.find_element_by_class_name("ui-dropdown__indicator")
        order_dropdown.click()
        lower_price_option = driver.find_element_by_xpath('//*[@id="inner-main"]/aside/section[2]/dl/div/div/div/div/ul/li[2]/a')
        lower_price_option.click()
        
        #Scrap name of the first five articles
        items_to_add = 5
        first_results = []
        
        #Iteratio to scrap names
        for i in range(items_to_add):
            item_name = driver.find_element_by_xpath(f'/html/body/main/div[2]/div/section/ol/li[{i +1}]/div/a/div/h2/span')
            first_results.append(item_name.text)
            print(first_results)

        #Reverse order according to price
        print(first_results[::-1])


    def tearDown(self):
        print('Browser is about to close...')
        sleep(3)
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

'''
//*[@id="id_state"]/dd[2]/a/span[1]
/html/body/main/div[2]/div/aside/section[2]/dl/div/div/div/div/ul/li[2]/a

/html/body/main/div[2]/div/section/ol/li[1]/div/a/div/h2/span
/html/body/main/div[2]/div/section/ol/li[2]/div/a/div/h2/span
'''