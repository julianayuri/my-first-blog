from django.db import models

class Produto(models.Model):
	nome = models.CharField(max_length = 100)
	preco = models.FloatField() 
	
	def criar(self):
		self.save()
	def __str__(self):
		return self.nome

