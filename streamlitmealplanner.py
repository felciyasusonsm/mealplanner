import streamlit as st
import pandas as pd

# Sample recipe database
RECIPES = {
    'vegan': {
        'breakfast': [
            {'name': 'Oatmeal with Berries', 'ingredients': ['oats', 'almond milk', 'berries', 'chia seeds'], 'instructions': 'Cook oats with almond milk, top with berries and chia seeds.'},
            {'name': 'Avocado Toast', 'ingredients': ['whole grain bread', 'avocado', 'tomato', 'lemon juice'], 'instructions': 'Mash avocado, spread on toasted bread, top with tomato and lemon juice.'}
        ],
        'lunch': [
            {'name': 'Chickpea Salad', 'ingredients': ['chickpeas', 'cucumber', 'tomato', 'olive oil', 'lemon juice'], 'instructions': 'Mix chickpeas, chopped cucumber, tomato, olive oil, and lemon juice.'},
            {'name': 'Veggie Wrap', 'ingredients': ['tortilla', 'hummus', 'spinach', 'carrots', 'bell peppers'], 'instructions': 'Spread hummus on tortilla, add veggies, and wrap.'}
        ],
        'dinner': [
            {'name': 'Lentil Curry', 'ingredients': ['lentils', 'coconut milk', 'curry powder', 'tomato', 'onion'], 'instructions': 'Cook lentils with coconut milk, curry powder, tomato, and onion.'},
            {'name': 'Stuffed Bell Peppers', 'ingredients': ['bell peppers', 'quinoa', 'black beans', 'corn', 'salsa'], 'instructions': 'Stuff peppers with cooked quinoa, beans, corn, and salsa; bake.'}
        ]
    },
    'keto': {
        'breakfast': [
            {'name': 'Keto Omelette', 'ingredients': ['eggs', 'spinach', 'cheese', 'bacon'], 'instructions': 'Whisk eggs, cook with spinach, cheese, and bacon in a pan.'},
            {'name': 'Avocado Smoothie', 'ingredients': ['avocado', 'almond milk', 'protein powder', 'stevia'], 'instructions': 'Blend avocado, almond milk, protein powder, and stevia.'}
        ],
        'lunch': [
            {'name': 'Cobb Salad', 'ingredients': ['lettuce', 'chicken', 'bacon', 'avocado', 'blue cheese'], 'instructions': 'Toss lettuce with chicken, bacon, avocado, and blue cheese.'},
            {'name': 'Zucchini Noodles with Pesto', 'ingredients': ['zucchini', 'pesto', 'cherry tomatoes', 'parmesan'], 'instructions': 'Spiralize zucchini, toss with pesto, tomatoes, and parmesan.'}
        ],
        'dinner': [
            {'name': 'Salmon with Asparagus', 'ingredients': ['salmon', 'asparagus', 'butter', 'garlic'], 'instructions': 'Bake salmon and asparagus with butter and garlic.'},
            {'name': 'Keto Meatballs', 'ingredients': ['ground beef', 'almond flour', 'egg', 'parmesan'], 'instructions': 'Mix beef, almond flour, egg, and parmesan; form meatballs and bake.'}
        ]
    }
}

def generate_meal_plan(diet, goal):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    meal_plan = []
    shopping_list = set()
    
    for day in days:
        daily_meals = {'Day': day}
        for meal_type in ['breakfast', 'lunch', 'dinner']:
            # Simple logic: select first recipe for weight loss, second for muscle gain
            recipe_index = 0 if goal == 'weight loss' else 1
            recipe = RECIPES[diet][meal_type][recipe_index]
            daily_meals[meal_type.capitalize()] = recipe['name']
            shopping_list.update(recipe['ingredients'])
        meal_plan.append(daily_meals)
    
    return pd.DataFrame(meal_plan), list(shopping_list)

def get_recipe_details(diet, meal_type, meal_name):
    for recipe in RECIPES[diet][meal_type]:
        if recipe['name'] == meal_name:
            return recipe
    return None

# Streamlit app
st.title("Meal Plan Generator")

# User inputs
diet = st.selectbox("Select Dietary Preference", ["vegan", "keto"])
goal = st.selectbox("Select Goal", ["weight loss", "muscle gain"])

if st.button("Generate Meal Plan"):
    meal_plan, shopping_list = generate_meal_plan(diet, goal)
    
    st.subheader("Weekly Meal Plan")
    st.table(meal_plan)
    
    st.subheader("Shopping List")
    st.write(", ".join(shopping_list))
    
    st.subheader("Recipe Details")
    for day in meal_plan['Day']:
        st.write(f"**{day}**")
        for meal_type in ['Breakfast', 'Lunch', 'Dinner']:
            meal_name = meal_plan[meal_plan['Day'] == day][meal_type].iloc[0]
            recipe = get_recipe_details(diet, meal_type.lower(), meal_name)
            if recipe:
                st.write(f"**{meal_type}: {meal_name}**")
                st.write(f"Ingredients: {', '.join(recipe['ingredients'])}")
                st.write(f"Instructions: {recipe['instructions']}")