from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import *
from .forms import ProductForm, OrderForm, WorkerForm
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required

def generatepdf(request):
	response = HttpResponse(content_type = 'application/pdf')
	response ['Content-Dispositon'] = 'filename = "test.pdf"'
	
	
	pdf = canvas.Canvas(response)
	pdf.setFont("Verdana", 12)
	
	allProducts = Products.objects.all().order_by("-name")
	allOrders = Orders.objects.all().order_by("-orderName")
	allWorkers = Workers.objects.all().order_by("-name")
	
	
	
	pdf.drawString(0,820, "Wykaz produktów znajdujących się w magazynie")
	pdf.line(0,815,800,815)
	pdf.drawString(0,800, "Nazwa produktu:")
	pdf.drawString(400,800, "Ilość produktu:")
	
	y = 780
	for product in allProducts:
		pdf.drawString(0,y , product.name)
		pdf.drawString(400,y , product.count)
		y -= 10
	
	y -= 20
	pdf.drawString(0,y, "Zlecenia w systemie:")
	pdf.line(0,y-5,800,y-5)
	y -= 20
	pdf.drawString(0,y, "Nazwa zamówienia:")
	y -= 20
	for order in allOrders:
		pdf.drawString(0,y , order.orderName)
		y -= 10
	
	y -= 20
	pdf.drawString(0,y, "Pracownicy w systemie:")
	pdf.line(0,y-5,800,y-5)
	y -= 20
	pdf.drawString(0,y, "Imię:")
	pdf.drawString(400,y, "Nazwisko:")
	y -= 20
	for worker in allWorkers:
		pdf.drawString(0,y , worker.name)
		pdf.drawString(400,y , worker.forename)
		y -= 10
		
	pdf.showPage()
	pdf.save()
	
	return response

def home(request):
	allProducts = Products.objects.all().order_by("-name")
	allOrders = Orders.objects.all().order_by("-orderName")
	allWorkers = Workers.objects.all().order_by("-name")
	return render(request, "product/index.html", {'projectnameandversion':'Magazyn SiloAdmin 1.0.0.!', 'allOrders' : allOrders, 'allProducts' : allProducts, 'allWorkers' : allWorkers})
	
	
def prod_edit(request, cpk):
	if request.method == 'POST':
		form=ProductForm(data=request.POST)
		if form.is_valid():
			try:
				prod = Products.objects.get(pk=cpk)
				prod.name = form.cleaned_data['name']
				prod.count = form.cleaned_data['count']
				prod.save()
				return redirect('home')
			except:
				raise Http404("Produkt do edycji nie istnieje!")	
	else:
		try:
			prod = Products.objects.get(pk = cpk)
		except:
			raise Http404("Produkt do edycji nie istnieje!")
	return render(request, "product/prod_edit.html", {'projectnameandversion':'Magazyn SiloAdmin 1.0.0.!', 'prod' : prod})
	
def prod_new(request):
	if request.method == 'POST':
		form=ProductForm(data=request.POST)
		if form.is_valid():
			p=Products()
			p.name = form.cleaned_data['name']
			p.count = form.cleaned_data['count']
			p.save()
			return redirect('home')
	else:
		form = ProductForm()
	return render(request, "product/prod_new.html", {'projectnameandversion':'Magazyn SiloAdmin 1.0.0.!', 'form' : form })

@login_required
def prod_delete(request, cpk):
	try:
		Products.objects.get(pk = cpk).delete()
	except Product.DoesNotExist:
		raise Http404("Produkt nie istnieje!")
	return redirect('home')
	
	return render(request, "product/prod_edit.html", {'projectnameandversion':'Magazyn SiloAdmin 1.0.0.!', 'allProducts' : allProducts})
	

	################################################################################################################################################################
def order_edit(request, cpk):
	if request.method == 'POST':
		form=OrderForm(data=request.POST)
		if form.is_valid():
			try:
				order = Orders.objects.get(pk=cpk)
				allProducts = Products.objects.all()
				order.orderName = form.cleaned_data['orderName']
				order.startDate = form.cleaned_data['startDate']
				order.stopDate = form.cleaned_data['stopDate']
				order.item_id = form.cleaned_data['item']
				order.save()
				return redirect('home')
			except:
				raise Http404("Zamowienie do edycji nie istnieje!")	
	else:
		order = Orders.objects.get(pk = cpk)
		allProducts = Products.objects.all()
	return render(request, "product/order_edit.html", {'projectnameandversion':'Magazyn SiloAdmin 1.0.0.!', 'order' : order, 'allProducts' : allProducts})

def order_new(request):
	if request.method == 'POST':
		form=OrderForm(data=request.POST)
		if form.is_valid():
			o=Orders()
			o.orderName = form.cleaned_data['orderName']
			o.startDate = form.cleaned_data['startDate']
			o.stopDate = form.cleaned_data['stopDate']
			o.item = form.cleaned_data['item']
			o.save()
			return redirect('home')
	else:
		form = OrderForm()
	return render(request, "product/order_new.html", {'projectnameandversion':'Magazyn SiloAdmin 1.0.0.!', 'form' : form })

@login_required	
def order_delete(request, cpk):
	try:
		Orders.objects.get(pk = cpk).delete()
	except Order.DoesNotExist:
		raise Http404("Zlecenie nie istnieje!")
	return redirect('home')
	
	return render(request, "product/order_edit.html", {'projectnameandversion':'Magazyn SiloAdmin 1.0.0.!', 'allOrders' : allOrders})

	################################################################################################################################################################
def worker_edit(request, cpk):
	if request.method == 'POST':
		form=WorkerForm(data=request.POST)
		if form.is_valid():
			try:
				worker = Workers.objects.get(pk=cpk)
				allOrders = Orders.objects.all()
				worker.name = form.cleaned_data['name']
				worker.forename = form.cleaned_data['forename']
				worker.orderid_id = form.cleaned_data['orderid']
				worker.save()
				return redirect('home')
			except:
				raise Http404("Pracownik do edycji nie istnieje!")	
	else:
		worker = Workers.objects.get(pk = cpk)
		allOrders = Orders.objects.all()
	return render(request, "product/worker_edit.html", {'projectnameandversion':'Magazyn SiloAdmin 1.0.0.!', 'worker' : worker, 'allOrders' : allOrders})

def worker_new(request):
	if request.method == 'POST':
		form=WorkerForm(data=request.POST)
		if form.is_valid():
			w=Workers()
			w.name = form.cleaned_data['name']
			w.forename = form.cleaned_data['forename']
			w.orderid = form.cleaned_data['orderid']
			w.save()
			return redirect('home')
	else:
		form = WorkerForm()
	return render(request, "product/worker_new.html", {'projectnameandversion':'Magazyn SiloAdmin 1.0.0.!', 'form' : form })

@login_required	
def worker_delete(request, cpk):
	try:
		Workers.objects.get(pk = cpk).delete()
	except Worker.DoesNotExist:
		raise Http404("Pracownik nie istnieje!")
	return redirect('home')
	
	return render(request, "product/worker_edit.html", {'projectnameandversion':'Magazyn SiloAdmin 1.0.0.!', 'allWorkers' : allWorkers})
