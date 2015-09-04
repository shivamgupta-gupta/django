from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from polls.models import Task
def index(request):
	a=Task.objects.all()
	context={'polls':a}
	return render(request,'polls/task.html',context)

def purchase(request):
	return render(request,'polls/purchase.html')

def charoli(request):
	return render(request,'polls/charoli.html')

def almonds(request):
	return render(request,'polls/almonds.html')

def aniseed(request):
	return render(request,'polls/aniseed.html')

def anjir(request):
	return render(request,'polls/anjir.html')

def apricots(request):
	return render(request,'polls/apricots.html')

def bayleaf(request):
	return render(request,'polls/bayleaf.html')

def blackcardamom(request):
	return render(request,'polls/blackcardamom.html')

def blackcumin(request):
	return render(request,'polls/blackcumin.html')

def blackpepper(request):
	return render(request,'polls/blackpepper.html')

def cashew(request):
	return render(request,'polls/cashew.html')

def coconutpowder(request):
	return render(request,'polls/coconutpowder.html')

def contact_us(request):
	return render(request,'polls/contact_us.html')

def elaichi(request):
	return render(request,'polls/elaichi.html')

def fruitnuts(request):
	return render(request,'polls/fruitnuts.html')

def hing(request):
	return render(request,'polls/hing.html')

def kalimirch(request):
	return render(request,'polls/kalimirch.html')

def kesar(request):
	return render(request,'polls/kesar.html')

def khajur(request):
	return render(request,'polls/khajur.html')

def milkpowder(request):
	return render(request,'polls/milkpowder.html')

def pista(request):
	return render(request,'polls/pista.html')

def plum(request):
	return render(request,'polls/plum.html')

def raisins(request):
	return render(request,'polls/raisins.html')

def redchilli(request):
	return render(request,'polls/redchilli.html')

def whitepepper(request):
	return render(request,'polls/whitepepper.html')

def contact_us(request):
	return render(request,'polls/contact_us.html')