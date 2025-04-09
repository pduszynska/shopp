import streamlit as st

# Meal data with ingredients and quantities in grams
meal_data = {
    "Śniadanie": [
        {"name": "Owsianka z owocami", "ingredients": {"Płatki owsiane": 40, "Mleko": 200, "Banan": 100, "Jagody": 50}, "kcal": 350, "cost": 3.00},
        {"name": "Jajka na twardo z grzankami", "ingredients": {"Jajka": 100, "Chleb pełnoziarnisty": 80}, "kcal": 350, "cost": 1.80},
        {"name": "Grecki jogurt z miodem i orzechami", "ingredients": {"Jogurt grecki": 150, "Miód": 10, "Orzechy mieszane": 20}, "kcal": 400, "cost": 4.30},
        {"name": "Jajecznica na tostach", "ingredients": {"Jajka": 150, "Chleb pełnoziarnisty": 80, "Masło": 20}, "kcal": 380, "cost": 2.50},
        {"name": "Tosty z awokado", "ingredients": {"Awokado": 100, "Chleb pełnoziarnisty": 80}, "kcal": 350, "cost": 2.80},
        {"name": "Naleśniki z syropem", "ingredients": {"Mieszanka do naleśników": 60, "Syrop klonowy": 30}, "kcal": 450, "cost": 3.50},
        {"name": "Sałatka owocowa z jogurtem", "ingredients": {"Owoce mieszane": 200, "Jogurt grecki": 100}, "kcal": 300, "cost": 3.00},
        {"name": "Omlet ze szpinakiem", "ingredients": {"Jajka": 150, "Szpinak": 50}, "kcal": 280, "cost": 2.20},
        {"name": "Smoothie z jagodami", "ingredients": {"Jagody": 100, "Banan": 50, "Mleko": 150}, "kcal": 250, "cost": 2.50},
        {"name": "Płatki śniadaniowe z mlekiem", "ingredients": {"Płatki śniadaniowe": 50, "Mleko": 200}, "kcal": 350, "cost": 2.00}
    ],
    "Przekąska": [
        {"name": "Jabłko z masłem orzechowym", "ingredients": {"Jabłko": 150, "Masło orzechowe": 30}, "kcal": 200, "cost": 1.50},
        {"name": "Marchewki z hummusem", "ingredients": {"Marchewki": 100, "Hummus": 50}, "kcal": 150, "cost": 1.00},
        {"name": "Banan i migdały", "ingredients": {"Banan": 100, "Migdały": 20}, "kcal": 250, "cost": 1.50},
        {"name": "Jogurt z jagodami", "ingredients": {"Jogurt": 150, "Jagody": 100}, "kcal": 180, "cost": 2.00},
        {"name": "Baton granola", "ingredients": {"Granola": 50, "Miód": 10}, "kcal": 200, "cost": 1.00},
        {"name": "Ogórek z hummusem", "ingredients": {"Ogórek": 100, "Hummus": 50}, "kcal": 100, "cost": 1.50},
        {"name": "Tost z masłem orzechowym", "ingredients": {"Chleb pełnoziarnisty": 80, "Masło orzechowe": 30}, "kcal": 250, "cost": 2.00},
        {"name": "Mieszanka orzechów", "ingredients": {"Orzechy mieszane": 30}, "kcal": 150, "cost": 1.00},
        {"name": "Ryżowy placek z awokado", "ingredients": {"Placek ryżowy": 50, "Awokado": 50}, "kcal": 220, "cost": 2.50},
        {"name": "Białkowy shake", "ingredients": {"Białko w proszku": 30, "Mleko": 250}, "kcal": 250, "cost": 3.00}
    ],
    "Obiad": [
        {"name": "Sałatka z kurczakiem", "ingredients": {"Pierś z kurczaka": 150, "Sałata": 50, "Pomidor": 50, "Ogórek": 50}, "kcal": 450, "cost": 4.50},
        {"name": "Stir fry warzywne z ryżem", "ingredients": {"Warzywa mieszane": 200, "Ryż": 100, "Sos sojowy": 10}, "kcal": 500, "cost": 5.00},
        {"name": "Spaghetti z sosem pomidorowym", "ingredients": {"Spaghetti": 100, "Sos pomidorowy": 100}, "kcal": 600, "cost": 3.80},
        {"name": "Grillowany łosoś z warzywami", "ingredients": {"Łosoś": 150, "Warzywa mieszane": 200}, "kcal": 550, "cost": 7.00},
        {"name": "Stir fry z kurczakiem", "ingredients": {"Pierś z kurczaka": 150, "Warzywa mieszane": 200}, "kcal": 450, "cost": 5.00},
        {"name": "Tacos z wołowiną", "ingredients": {"Wołowina mielona": 150, "Taco shell": 2}, "kcal": 600, "cost": 6.00},
        {"name": "Stir fry z tofu", "ingredients": {"Tofu": 150, "Warzywa mieszane": 200, "Sos sojowy": 10}, "kcal": 450, "cost": 5.00},
        {"name": "Pasta z krewetkami", "ingredients": {"Krewetki": 150, "Pasta": 100, "Sos pomidorowy": 100}, "kcal": 550, "cost": 6.00},
        {"name": "Wegańska chili", "ingredients": {"Fasola": 200, "Pomidory": 150}, "kcal": 400, "cost": 4.50},
        {"name": "Zupa soczewicowa", "ingredients": {"Soczewica": 200, "Marchew": 100}, "kcal": 350, "cost": 3.50}
    ]
}

# Funkcja do obliczeń i przygotowania planu posiłków
def calculate_meals(breakfast_index, snack_index, dinner_index, days):
    breakfast = meal_data["Śniadanie"][breakfast_index]
    snack = meal_data["Przekąska"][snack_index]
    dinner = meal_data["Obiad"][dinner_index]

    total_kcal = (breakfast["kcal"] + snack["kcal"] + dinner["kcal"]) * days
    total_cost = (breakfast["cost"] + snack["cost"] + dinner["cost"]) * days
    shopping_list = {}

    for ingredient, grams in breakfast["ingredients"].items():
        shopping_list[ingredient] = shopping_list.get(ingredient, 0) + grams * days
    for ingredient, grams in snack["ingredients"].items():
        shopping_list[ingredient] = shopping_list.get(ingredient, 0) + grams * days
    for ingredient, grams in dinner["ingredients"].items():
        shopping_list[ingredient] = shopping_list.get(ingredient, 0) + grams * days

    return total_kcal, total_cost, shopping_list, breakfast, snack, dinner

# Streamlit interface
st.title("Planer Posiłków")

# Użytkownik wybiera liczbę dni
days = st.number_input("Ile dni chcesz zaplanować?", min_value=1, value=1)

# Wybór posiłków na każdy dzień
meals_for_each_day = []

for day in range(days):
    st.subheader(f"Dzień {day + 1}")
    breakfast_choice = st.selectbox(f"Wybierz śniadanie na Dzień {day + 1}", [meal['name'] for meal in meal_data["Śniadanie"]], key=f"breakfast{day}")
    snack_choice = st.selectbox(f"Wybierz przekąskę na Dzień {day + 1}", [meal['name'] for meal in meal_data["Przekąska"]], key=f"snack{day}")
    dinner_choice = st.selectbox(f"Wybierz obiad na Dzień {day + 1}", [meal['name'] for meal in meal_data["Obiad"]], key=f"dinner{day}")
    
    meals_for_each_day.append({
        "breakfast": breakfast_choice,
        "snack": snack_choice,
        "dinner": dinner_choice
    })

# Po naciśnięciu przycisku obliczania
if st.button("Oblicz Plan Posiłków"):
    total_kcal = 0
    total_cost = 0
    shopping_list = {}

    for day, meals in enumerate(meals_for_each_day):
        breakfast_index = [meal['name'] for meal in meal_data["Śniadanie"]].index(meals["breakfast"])
        snack_index = [meal['name'] for meal in meal_data["Przekąska"]].index(meals["snack"])
        dinner_index = [meal['name'] for meal in meal_data["Obiad"]].index(meals["dinner"])
        
        day_total_kcal, day_total_cost, day_shopping_list, breakfast, snack, dinner = calculate_meals(
            breakfast_index, snack_index, dinner_index, 1
        )

        total_kcal += day_total_kcal
        total_cost += day_total_cost
        
        # Aktualizacja listy zakupów
        for item, grams in day_shopping_list.items():
            shopping_list[item] = shopping_list.get(item, 0) + grams
        
        st.write(f"### Dzień {day + 1}")
        st.write(f"**Śniadanie**: {breakfast['name']} - {breakfast['kcal']} kcal, £{breakfast['cost']}")
        for ingredient, grams in breakfast["ingredients"].items():
            st.write(f"  {ingredient}: {grams}g")
        
        st.write(f"**Przekąska**: {snack['name']} - {snack['kcal']} kcal, £{snack['cost']}")
        for ingredient, grams in snack["ingredients"].items():
            st.write(f"  {ingredient}: {grams}g")
        
        st.write(f"**Obiad**: {dinner['name']} - {dinner['kcal']} kcal, £{dinner['cost']}")
        for ingredient, grams in dinner["ingredients"].items():
            st.write(f"  {ingredient}: {grams}g")

    st.write(f"### Całkowita liczba kalorii dla {days} dni: {total_kcal} kcal")
    st.write(f"### Całkowity koszt dla {days} dni: £{total_cost:.2f}")
    
    # Wyświetlenie listy zakupów
    st.write("### Lista zakupów")
    for item, grams in shopping_list.items():
        st.write(f"{item}: {grams}g")
