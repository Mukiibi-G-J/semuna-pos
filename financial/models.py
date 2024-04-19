from django.db import models

# Create your models here.


# Income/Balance 

INCOME_BALANCE = [('Income Statement','Income Statement' ),('Balance sheet', 'Balance Sheet')]
ACCOUNT_TYPES= [
		('Assest', 'Assest'),
		('Liability', 'Liability'),
		('Equity', 'Equity'),
		('Income', 'Income'),
		('Expense', 'Expense')

	]
	
class Account(models.Model):
	code = models.CharField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	income_balance = models.CharField(max_length=255,choices=INCOME_BALANCE)
	account_category =models.CharField(max_length=255, choices=ACCOUNT_TYPES)

class GLAccountCategories(models.Model):
	description = models.CharField(max_length=255)
	account_category = models.CharField(max_length=255,choices=ACCOUNT_TYPES)
	balance = models.IntegerField()

	class Meta:
		verbose_name = 'G/L Account Category'
		verbose_name_plural = 'G/L Account Categories'


	