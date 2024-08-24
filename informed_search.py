import heapq

class RecipeNode:
    def __init__(self, recipe_id, name, portions, origin, ingredients):
        self.recipe_id = recipe_id
        self.name = name
        self.portions = portions
        self.origin = origin
        self.ingredients = ingredients
        self.parent = None
        self.f = 0
        self.g = 0
        self.h = 0

    # Definir cómo comparar los RecipeNode basados en f
    def __lt__(self, other):
        return self.f < other.f

# Define los criterios para la heurística
def calculate_h_function(recipe, preferences):
    h = 0
    h += len(set(recipe.ingredients) - set(preferences["ingredients"]))
    h += 1 if recipe.origin != preferences["origin"] else 0
    h += abs(recipe.portions - preferences["portions"])
    
    return h


##def calculate_g_function(recipe, preferences):
##    g = 0
##    g += 


def search_recipes(recipes, preferences):

    # Se cefine la cola de prioridad junto con los valores iniciales
    open_list = []
    best_recipe = None
    minimum_f = float('inf')  # se inicializa con un valor muy grande

    # Calcula la heurística de cada una de las recetas y las agrega a la cola de prioridad
    for _, recipe in recipes.items():
        recipe.g = 0
        recipe.h = calculate_h_function(recipe, preferences)
        recipe.f = recipe.g + recipe.h
        heapq.heappush(open_list, (recipe.f, recipe))

    # Itera la cola de prioridad
    while open_list:
        f, current_node = heapq.heappop(open_list)
        
    # 'current_node' es un RecipeNode
        if current_node.f < minimum_f:
            minimum_f = current_node.f
            best_recipe = current_node
            print("Hola")

    if best_recipe:
        print("Best recipe found:", best_recipe.name)
        return best_recipe.name
    else:
        print("No suitable recipe found")
        return None

def main():
    # Definimops las recetas dentro de un diccionario 
    recipes = {
        1: RecipeNode(1, "Bandeja Paisa", 4, "Colombian", ["Beans", "Rice", "Avocado", "Sausage", "Chicharron", "Ripe Banana"]),
        2: RecipeNode(2, "Tacos", 5, "Mexican", ["corn", "beans", "cheese"]),
        3: RecipeNode(3, "Chinese Rice", 4, "Chinese", ["rice", "chicken", "soy sauce"]),
        4: RecipeNode(4, "Pasta Napolitana", 6, "Italian", ["pasta", "basil", "tomato"]),
        5: RecipeNode(5, "Sushi", 3, "Japanese", ["Fish", "rice", "salmon"]),
        6: RecipeNode(6, "Paella", 4, "Spanish", ["rice", "sausage", "seafood"]),
        7: RecipeNode(7, "Ceviche", 2, "Peruvian", ["white fish", "shrimp", "garlic"]),
        8: RecipeNode(8, "Burger", 1, "American", ["ground beef", "burger bun", "cheese"]),
        9: RecipeNode(9, "Bibimbap", 4, "Korean", ["carrot", "egg", "rice", "beef", "gochujang sauce"]),
        10: RecipeNode(10, "Ratatouille", 6, "French", ["eggplant", "pumpkin", "garlic", "tomato"]),
    }

    # Definimos las preferencias del usuario
    user_preferences = {
        "portions": 2,
        "ingredients": ["cheese"],
        "origin": "American"
        
    }

    # Llamamos la función de búsqueda
    search_recipes(recipes, user_preferences)

if __name__ == "__main__":
    main()
