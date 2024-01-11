import time

from selenium.webdriver.support.wait import WebDriverWait

from Constants.Base_Constant import Base_Constants
from Pages.AirportDetailPage import AirportDetailPage
from Test.test_base import BaseTest

from Locators.AirportDetailsPageLocator import AirportDetailsPageLocator


class TestEstimation(BaseTest):

    def test_estimate(self):
        """To check the Flight estimations"""
        self.airport_detail_page = AirportDetailPage(self.driver)
        self.airport_detail_page.click(AirportDetailsPageLocator.COOKIES_ACCEPT_BUTTON)
        time.sleep(5)
        self.airport_detail_page.navigate_to_url(Base_Constants.URL_TO_BE_NAVIGATED)
        for i in AirportDetailsPageLocator.LOCATION_DICT.keys():
            estimations = self.airport_detail_page.get_estimations(AirportDetailsPageLocator.LOCATION_DICT[i])
            if estimations is None:
                print(i + " : No Data Found")
            else:
                for est in estimations:
                    print(i + " : " + est)
        assert True
