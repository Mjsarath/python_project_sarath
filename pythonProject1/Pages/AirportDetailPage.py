from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.BasePage import BasePage


class AirportDetailPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_estimations(self, target_locator):
        """To get the estimation of the flights from the location/locator given
        :param target_locator : locator that Estimation to be found
        :returns list_estimation - when the location share is present"""
        try:
            elements = self.get_all_elements(target_locator)
            list_estimation = []
            for ele in elements:
                list_estimation.append(ele.text.strip())
            return list_estimation
        except TimeoutException:
            pass
