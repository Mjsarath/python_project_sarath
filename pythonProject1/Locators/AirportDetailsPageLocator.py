from selenium.webdriver.common.by import By
from Constants.AirportDetailsConstants import AirportDetailsConstants


class AirportDetailsPageLocator:
    DELHI_ESTIMATED_TIMES = (By.XPATH, "//tr/td/div/span[contains(text(),'Delhi')]/parent::div/ancestor::tr//td["
                                       "@class='ng-binding'][2]")
    COOKIES_ACCEPT_BUTTON = (By.ID, 'onetrust-accept-btn-handler')
    BENGALURU_ESTIMATED_TIMES = (By.XPATH, "//tr/td/div/span[contains(text(),"
                                           "'Bengaluru')]/parent::div/ancestor::tr//td["
                                           "@class='ng-binding'][2]")
    GOA_ESTIMATED_TIMES = (By.XPATH, "//tr/td/div/span[contains(text(),'Goa')]/parent::div/ancestor::tr//td["
                                     "@class='ng-binding'][2]")
    DUBAI_ESTIMATED_TIMES = (By.XPATH, "//tr/td/div/span[contains(text(),'Dubai')]/parent::div/ancestor::tr//td["
                                       "@class='ng-binding'][2]")
    LOCATION_DICT = {AirportDetailsConstants.DELHI_LOCATION: DELHI_ESTIMATED_TIMES,
                     AirportDetailsConstants.BENGALURU_LOCATION: BENGALURU_ESTIMATED_TIMES,
                     AirportDetailsConstants.GOA_LOCATION: GOA_ESTIMATED_TIMES,
                     AirportDetailsConstants.DUBAI_LOCATION: DUBAI_ESTIMATED_TIMES}
