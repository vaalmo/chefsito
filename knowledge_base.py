

def tiene_nombre_receta(recipes, nombre_receta):
	for k, v in recipes.items():
		if k == nombre_receta:
			print(k, v)


origen_dict = {}


def tiene_tipo_comida(tipo_comida, origen):
		key = origen
		value = tipo_comida
		origen_dict[key] = value
		print(origen_dict)
		return origen_dict
		
	 

def tiene_origen(tipo_comida,origen):
    print(tiene_tipo_comida(tipo_comida, origen))


def main():
	
    recipes = {
		"sancocho": (4, "colombiana", ["Beans", "Rice", "Avocado", "Sausage", "Chicharron", "Ripe Banana"]),
		"tacos": ( 5, "mexican", ["corn", "beans", "cheese"]),
		"chinese rice": ( 4, "chinese", ["rice", "chicken", "soy sauce"]),
		"bibimbap":  (4, "Korean", ["carrot", "egg", "rice", "beef", "gochujang sauce"])
    }

    nombre_receta= "tacos"
	
    ##tiene_nombre_receta(recipes, nombre_receta)
	
    tipo_comida = "burger"
    origen = "american"

    ##tiene_tipo_comida(tipo_comida, origen)
	
    tiene_origen(tipo_comida,origen)

if __name__ == "__main__":
    main()