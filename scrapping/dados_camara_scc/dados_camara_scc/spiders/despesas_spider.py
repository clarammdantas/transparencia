#Author: Clara Moraes, 04/10/2018

import scrapy
import csv
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class DadosCamara(scrapy.Spider):
	name = "dados_camara"
	start_urls = ["http://transparenciape.com.br/CamaraSantaCruz/empenho.php"]

	def __init__(self):
		self.driver = webdriver.Chrome()
		self.DATA_INICIAL = "01/01/2018"
		self.NUM_EXIBICAO = "Todos"
		self.DELAY = 8
	

	def parse(self, response):
		self.driver.get(response.url)
		element = self.driver.find_element_by_id("campoDataInicial")
		element.send_keys(self.DATA_INICIAL)

		self.driver.find_element_by_xpath("//*[@id='tabelaDados-header']/div/div/div[2]/div[1]/button").click()
		self.driver.wait_for_page_to_load(30000)
		self.driver.find_element_by_xpath("//*[@id='tabelaDados-header']/div/div/div[2]/div[1]/ul/li[4]").click()
		# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
		# table = WebDriverWait(self.driver, self.DELAY).until(EC.presence_of_element_located((By.XPATH, "//*[@id='tabelaDados']/tbody/tr")))
		# self.driver.find_element_by_xpath("//*[@id='tabelaDados']/tbody").submit()


		# print(response.body)
		# count = 0
		# rows = self.driver.find_element_by_xpath("//*[@id='tabelaDados']/tbody")
		# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
		# print(len(rows))
		# for r in rows:
		# 	count += 1

		# print("@@@@@@@@@@@@@@@@@@@@@@")
		# print(count)