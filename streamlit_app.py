import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
import streamlit as st

# Meal data with ingredients and quantities in grams
meal_data = {
    "Breakfast": [
        {"name": "Porridge with Fruit", "ingredients": {"Porridge oats": 40, "Milk": 200, "Bananas": 100, "Berries": 50}, "kcal": 350, "cost": 3.00},
        {"name": "Boiled Eggs with Toast Soldiers", "ingredients": {"Eggs": 100, "Wholemeal bread": 80}, "kcal": 350, "cost": 1.80},
        {"name": "Greek Yogurt with Honey and Nuts", "ingredients": {"Greek yogurt": 150, "Honey": 10, "Mixed nuts": 20}, "kcal": 400, "cost": 4.30},
        {"name": "Scrambled Eggs on Toast", "ingredients": {"Eggs": 150, "Wholemeal bread": 80, "Butter": 20}, "kcal": 380, "cost": 2.50},
        {"name": "Avocado Toast", "ingredients": {"Avocado": 100, "Wholemeal bread": 80}, "kcal": 350, "cost": 2.80},
        {"name": "Pancakes with Syrup", "ingredients": {"Pancake mix": 60, "Maple syrup": 30}, "kcal": 450, "cost": 3.50},
        {"name": "Fruit Salad with Yogurt", "ingredients": {"Mixed fruits": 200, "Greek yogurt": 100}, "kcal": 300, "cost": 3.00},
        {"name": "Omelette with Spinach", "ingredients": {"Eggs": 150, "Spinach": 50}, "kcal": 280, "cost": 2.20},
        {"name": "Smoothie with Berries", "ingredients": {"Berries": 100, "Banana": 50, "Milk": 150}, "kcal": 250, "cost": 2.50},
        {"name": "Cereal with Milk", "ingredients": {"Cereal": 50, "Milk": 200}, "kcal": 350, "cost": 2.00}
    ],
    "Snack": [
        {"name": "Apple with Peanut Butter", "ingredients": {"Apple": 150, "Peanut butter": 30}, "kcal": 200, "cost": 1.50},
        {"name": "Carrot Sticks with Hummus", "ingredients": {"Carrots": 100, "Hummus": 50}, "kcal": 150, "cost": 1.00},
        {"name": "Banana and Almonds", "ingredients": {"Banana": 100, "Almonds": 20}, "kcal": 250, "cost": 1.50},
        {"name": "Yogurt with Berries", "ingredients": {"Yogurt": 150, "Berries": 100}, "kcal": 180, "cost": 2.00},
        {"name": "Granola Bar", "ingredients": {"Granola": 50, "Honey": 10}, "kcal": 200, "cost": 1.00},
        {"name": "Cucumber and Hummus", "ingredients": {"Cucumber": 100, "Hummus": 50}, "kcal": 100, "cost": 1.50},
        {"name": "Peanut Butter Toast", "ingredients": {"Wholemeal bread": 80, "Peanut butter": 30}, "kcal": 250, "cost": 2.00},
        {"name": "Mixed Nuts", "ingredients": {"Mixed nuts": 30}, "kcal": 150, "cost": 1.00},
        {"name": "Rice Cake with Avocado", "ingredients": {"Rice cake": 50, "Avocado": 50}, "kcal": 220, "cost": 2.50},
        {"name": "Protein Shake", "ingredients": {"Protein powder": 30, "Milk": 250}, "kcal": 250, "cost": 3.00}
    ],
    "Dinner": [
        {"name": "Chicken Salad", "ingredients": {"Chicken breast": 150, "Lettuce": 50, "Tomato": 50, "Cucumber": 50}, "kcal": 450, "cost": 4.50},
        {"name": "Veggie Stir Fry with Rice", "ingredients": {"Mixed vegetables": 200, "Rice": 100, "Soy sauce": 10}, "kcal": 500, "cost": 5.00},
        {"name": "Spaghetti with Tomato Sauce", "ingredients": {"Spaghetti": 100, "Tomato sauce": 100}, "kcal": 600, "cost": 3.80},
        {"name": "Grilled Salmon with Vegetables", "ingredients": {"Salmon": 150, "Mixed vegetables": 200}, "kcal": 550, "cost": 7.00},
        {"name": "Chicken Stir Fry", "ingredients": {"Chicken breast": 150, "Mixed vegetables": 200}, "kcal": 450, "cost": 5.00},
        {"name": "Beef Tacos", "ingredients": {"Ground beef": 150, "Taco shells": 2}, "kcal": 600, "cost": 6.00},
        {"name": "Tofu Stir Fry", "ingredients": {"Tofu": 150, "Mixed vegetables": 200, "Soy sauce": 10}, "kcal": 450, "cost": 5.00},
        {"name": "Shrimp Pasta", "ingredients": {"Shrimp": 150, "Pasta": 100, "Tomato sauce": 100}, "kcal": 550, "cost": 6.00},
        {"name": "Vegan Chili", "ingredients": {"Beans": 200, "Tomatoes": 150}, "kcal": 400, "cost": 4.50},
        {"name": "Lentil Soup", "ingredients": {"Lentils": 200, "Carrots": 100}, "kcal": 350, "cost": 3.50}
    ]
}

# Streamlit App

def calculate_meals(breakfast_index, snack_index, dinner_index, days):
    breakfast = meal_data["Breakfast"][breakfast_index]
    snack = meal_data["Snack"][snack_index]
    dinner = meal_data["Dinner"][dinner_index]

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
st.title("Interactive Meal Planner")

# User inputs
days = st.number_input("How many days would you like to plan?", min_value=1, value=1)

# Meal selections for each day
meals_for_each_day = []

for day in range(days):
    st.subheader(f"Day {day + 1}")
    breakfast_choice = st.selectbox(f"Choose your Breakfast for Day {day + 1}", [meal['name'] for meal in meal_data["Breakfast"]], key=f"breakfast{day}")
    snack_choice = st.selectbox(f"Choose your Snack for Day {day + 1}", [meal['name'] for meal in meal_data["Snack"]], key=f"snack{day}")
    dinner_choice = st.selectbox(f"Choose your Dinner for Day {day + 1}", [meal['name'] for meal in meal_data["Dinner"]], key=f"dinner{day}")
    
    meals_for_each_day.append({
        "breakfast": breakfast_choice,
        "snack": snack_choice,
        "dinner": dinner_choice
    })

# Show the selected meals
if st.button("Calculate Meal Plan"):
    total_kcal = 0
    total_cost = 0
    shopping_list = {}

    for day, meals in enumerate(meals_for_each_day):
        breakfast_index = [meal['name'] for meal in meal_data["Breakfast"]].index(meals["breakfast"])
        snack_index = [meal['name'] for meal in meal_data["Snack"]].index(meals["snack"])
        dinner_index = [meal['name'] for meal in meal_data["Dinner"]].index(meals["dinner"])
        
        day_total_kcal, day_total_cost, day_shopping_list, breakfast, snack, dinner = calculate_meals(
            breakfast_index, snack_index, dinner_index, 1
        )

        total_kcal += day_total_kcal
        total_cost += day_total_cost
        
        # Update shopping list
        for item, grams in day_shopping_list.items():
            shopping_list[item] = shopping_list.get(item, 0) + grams
        
        st.write(f"### Day {day + 1}")
        st.write(f"**Breakfast**: {breakfast['name']} - {breakfast['kcal']} kcal, £{breakfast['cost']}")
        for ingredient, grams in breakfast["ingredients"].items():
            st.write(f"  {ingredient}: {grams}g")
        
        st.write(f"**Snack**: {snack['name']} - {snack['kcal']} kcal, £{snack['cost']}")
        for ingredient, grams in snack["ingredients"].items():
            st.write(f"  {ingredient}: {grams}g")
        
        st.write(f"**Dinner**: {dinner['name']} - {dinner['kcal']} kcal, £{dinner['cost']}")
        for ingredient, grams in dinner["ingredients"].items():
            st.write(f"  {ingredient}: {grams}g")

    st.write(f"### Total Kcal for {days} days: {total_kcal} kcal")
    st.write(f"### Total cost for {days} days: £{total_cost:.2f}")
    
    # Display shopping list
    st.write("### Shopping List")
    for item, grams in shopping_list.items():
        st.write(f"{item}: {grams}g")
