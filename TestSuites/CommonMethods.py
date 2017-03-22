from selenium import webdriver
from openpyxl import *


def initialize():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.tripadvisor.in")
    return driver

def read_from_excel(path):
    workbook =  load_workbook(path)
    workbook.get_sheet_by_name("Sheet 1")


