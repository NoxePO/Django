from django import forms
from .models import Products, Orders, Workers

class ProductForm(forms.Form):
	name = forms.CharField(label="Nazwa produktu", max_length=50)
	count = forms.CharField(label="Ilość produktu", max_length=15)

class OrderForm(forms.Form):
	orderName = forms.CharField(label="Nazwa zamówienia", max_length=20)
	startDate = forms.DateField(label="Początek zamówienia")
	stopDate = forms.DateField(label="Koniec zamówienia")
	item = forms.ModelChoiceField(queryset=Products.objects.all())

class WorkerForm(forms.Form):
	name = forms.CharField(label="Imię", max_length = 50)
	forename = forms.CharField(label="Nazwisko", max_length = 50)
	orderid = forms.ModelChoiceField(queryset=Orders.objects.all())


#class OrderForm(forms.ModelForm):
#    class Meta:
#        model = Orders
#       fields = ('orderName', 'startDate', 'stopDate', 'item')
#
#        labels = {
#            'orderName': ('Nazwa'),
#            'startDate': ('Start'),
#            'stopDate': ('Stop'),
#			'item': ('Przedmiot')
#        }
#
#        widgets = {
#            'Start': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),
#			#'Stop': forms.SelectDateWidget(empty_label=("Choose Year", "Choose Month", "Choose Day")),
#        }