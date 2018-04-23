from django.shortcuts import render
from django.http import HttpResponse
from tablib import Dataset
from desks.models import Desk
from desks.resources import DeskResource

# Create your views here.

def index(request):
	my_desks = Desk.objects
	context = {'my_desks':my_desks}
	return render(request, 'desks\index.html',context)

	
def import_desk(request):	
	if request.method == 'POST':
		desk_resource = DeskResource()
		dataset = Dataset()
		new_desks = request.FILES['myfile']

		imported_data = dataset.load(new_desks.read().decode('utf-8'),format='csv')
		result = desk_resource.import_data(dataset, dry_run=True)  # Test the data import
		if not result.has_errors():
			desk_resource.import_data(dataset, dry_run=False)  # Actually import now
			#return render(request, 'desks\import_desk.html')
			return HttpResponse("IMPORT DESKS OK!")
			
	return render(request, 'desks\import_desk.html')
	

def detail(request):
	return HttpResponse("VIEW DESK:" + str(desks_id))
	

	
	