import pytest

from pom.homepage_nav import HomepageNav
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.support.ui import WebDriverWait

@pytest.mark.usefixtures('setup')
class TestHomepage:
    
    # def test_homepage(self):
    #     driver = webdriver.Chrome()
    #     element1 = driver.find_element(By.CSS_SELECTOR, '#id_123')

    #     wait = WebDriverWait(driver, 15, 0.3)
    #     element = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#id_123')))
    
    def test_nav_links(self):
        homepage_nav = HomepageNav(self.driver) 
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.NAV_LINK_TEXT
        assert actual_links == expected_links, 'Validating Nav Links Text'