# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Despesa(scrapy.Item):
	self.num_empenho = scrapy.Field()
    self.data_publicacao = scrapy.Field()
    self.favorecido = scrapy.Field()
    self.historico = scrapy.Field()
    self.valor = scrapy.Field()
    self.fonte_recurso = scrapy.Field()
    self.categoria_despesa = scrapy.Field()
    self.grupo_despesa = scrapy.Field()
    self.modalidade = scrapy.Field()
    self.servico_prestado = scrapy.Field()
		
