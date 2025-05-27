import pandas as pd
import random

# List of 100 food items (sample)
food_items = [
    "Idli", "Pasta", "Biryani", "Burger", "Salad", "Fries", "Pizza", "Rice", "Noodles", "Sandwich",
    "Fried Chicken", "Grilled Chicken", "Steak", "Soup", "Lasagna", "Tacos", "Sushi", "Chili", "Wrap", "Hot Dog",
    "Ice Cream", "Brownie", "Pancake", "Waffle", "Cupcake", "Muffin", "Cheesecake", "Smoothie", "Fruit Salad", "Toast",
    "Mashed Potatoes", "Roast Chicken", "BBQ Ribs", "Chicken Wings", "Popcorn", "Chicken Caesar Salad", "Cheese Pizza", "Vegetable Soup", "Spaghetti", "Chicken Tenders", "Pasta Alfredo",
    "Fried Rice", "Vegetable Stir Fry", "Tofu Stir Fry", "Beef Stir Fry", "Vegetable Samosa", "Chicken Samosa", "Falafel", "Hummus", "Chana Masala", "Paneer Butter Masala",
    "Butter Chicken", "Chicken Korma", "Fish Curry", "Shrimp Curry", "Prawn Masala", "Vegetable Biryani", "Chow Mein", "Pad Thai", "Spring Roll", "Egg Roll",
    "Frittata", "Quiche", "Grilled Salmon", "Grilled Shrimp", "Omelette", "Ceviche", "Pork Belly", "Beef Burrito", "Chicken Burrito", "Beef Tacos",
    "Chicken Tacos", "Shawarma", "Gyro", "Kebab", "Steamed Dumplings", "Peking Duck", "Ramen", "Pho", "Pasta Primavera", "Fettuccine Alfredo",
    "Mac and Cheese", "Chicken Pesto", "Lamb Chops", "Ratatouille", "Moussaka", "Crepes", "Tempura", "Sushi Rolls", "Crispy Chicken", "Salmon Salad",
    "Chicken Parmesan", "Eggplant Parmesan", "Cauliflower Rice", "Sweet Potato Fries", "Grilled Veggies", "Zucchini Noodles", "Quinoa Salad", "Lentil Soup", "Minestrone", "Pasta Carbonara",
    "Peking Duck", "Tempura Shrimp", "Chicken Fried Rice", "Vegetarian Chili", "Buffalo Wings", "Baked Potato", "Tuna Salad", "Shrimp Scampi", "Clams", "Baked Salmon",
    "Steak Frites", "Chicken Biryani", "Vegetable Lasagna", "Lamb Shawarma", "Chicken Shawarma", "Beef Kebabs", "Vegetarian Tacos", "Chicken Noodle Soup", "Vegetable Wrap", "Fruit Smoothie"
]

# Generate random nutrition data for each food item
data = []
for food in food_items:
    salt_mg = random.randint(50, 1500)  # Random salt content between 50 mg and 1500 mg
    calories = random.randint(100, 800)  # Random calories between 100 and 800
    protein_g = round(random.uniform(2.0, 30.0), 1)  # Random protein between 2g and 30g
    fat_g = round(random.uniform(1.0, 50.0), 1)  # Random fat between 1g and 50g
    
    # Append data as a tuple (food, salt_mg, calories, protein_g, fat_g)
    data.append([food, salt_mg, calories, protein_g, fat_g])

# Convert data to a DataFrame
df = pd.DataFrame(data, columns=["food", "salt_mg", "calories", "protein_g", "fat_g"])

# Save DataFrame to CSV
df.to_csv("nutrition_data.csv", index=False)

print("CSV file 'nutrition_data.csv' has been generated successfully!")
