from random import choice

frases = ['Maquinaria Rivero, lo mejor en Maquinaria ','Las Mejores Marcas solo para ti ']

from equipments.models import Equipment

def basico(request):
	equipments  = Equipment.objects.all()
	equipment = None
	for e in equipments:
		if request.path == e.get_absolute_url():
			equipment = e
			break
	return{'titulo':choice(frases),'equipments':equipments, 'selected_equipment': equipment}