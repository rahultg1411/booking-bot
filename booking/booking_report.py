# This file is going to include method that will parse
# The specific data that we need from each one of the deal boxes.
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

class BookingReport:
    def __init__(self, boxes_section_element:WebElement):
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(By.CSS_SELECTOR,
            'div.a826ba81c4.fe821aea6c.fa2f36ad22.afd256fc79.d08f526e0d.ed11e24d01.ef9845d4b3.da89aeb942[data-testid="property-card"]'
        )

    def pull_deal_box_attributes(self):
        collection = []
        for deal_box in self.deal_boxes:
            # Pulling the hotel name
            hotel_name = deal_box.find_element(By.CSS_SELECTOR,
                'div.fcab3ed991.a23c043802[data-testid="title"]'
            ).get_attribute('innerHTML').strip()
            hotel_price = deal_box.find_element(By.CSS_SELECTOR,
                'span.fcab3ed991.bd73d13072'
            ).get_attribute('innerHTML').strip()

            hotel_score = deal_box.find_element(By.CSS_SELECTOR,
                'div.b5cd09854e.d10a6220b4'
            ).get_attribute('innerHTML').strip()

            collection.append(
                [hotel_name, hotel_price, hotel_score]
            )
        return collection