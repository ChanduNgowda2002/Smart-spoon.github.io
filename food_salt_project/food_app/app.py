import gradio as gr
import random

# ---- Electrical stimulation logic ----
def adjust_stimulation(salt_mg):
    if salt_mg < 400:
        return "Low stimulation"
    elif 400 <= salt_mg < 1000:
        return "Medium stimulation"
    else:
        return "High stimulation"

def adjust_sentimental(salt_mg):
    if salt_mg < 400:
        return "positive"
    elif 400 <= salt_mg < 1000:
        return "Negative"
    else:
        return "No Comments"

# ---- Always give recommendations ----
def recommend_diet(salt_mg, food_title):
    recs = []

    # Salt-specific tips
    if salt_mg > 1000:
        recs.append("⚠️ High salt: Try to reduce salt intake.")
        recs.append("🥗 Include more fresh vegetables, fruits, and whole grains.")
    elif salt_mg < 300:
        recs.append("✅ Low salt: Great for a heart-healthy lifestyle.")
    else:
        recs.append("🧠 Moderate salt: Try to keep it balanced throughout the day.")

    # Food-specific tip (example)
    food = food_title.lower()
    if food in ["pizza", "burger", "noodles", "biryani", "fries"]:
        recs.append("💡 Try grilled, steamed, or home-cooked alternatives to reduce fat and salt.")
    else:
        recs.append("💧 Stay hydrated and balance meals with fiber-rich foods.")

    return recs

# ---- Main function for Gradio ----
def predict_salt_and_info(image, food_title):
    if not food_title:
        return "<span style='color:red;'>⚠️ Please enter the food title!</span>"

    # Simulated values
    salt_mg = random.randint(100, 1500)
    calories = random.randint(100, 800)
    protein = round(random.uniform(2.0, 25.0), 1)
    fat = round(random.uniform(5.0, 40.0), 1)

    stimulation = adjust_stimulation(salt_mg)
  
    diet_recs = recommend_diet(salt_mg, food_title)
    sentimental = adjust_sentimental(salt_mg)

    result = f"""
        <h3>🍽️ Food: <b>{food_title.title()}</b></h3>
        <ul>
            <li>🧂 <b>Salt</b>: {salt_mg} mg</li>
            <li>🔥 <b>Calories</b>: {calories} kcal</li>
            <li>💪 <b>Protein</b>: {protein} g</li>
            <li>🥑 <b>Fat</b>: {fat} g</li>
            <li>⚡ <b>Suggested Electrical Stimulation</b>: {stimulation}</li>
            <li> <b>Sentimental Analysis based on the data collected</b>: {sentimental}</li>
        </ul>
        <h3>🥗 Dietary Recommendations:</h3>
        <div style="display: flex; flex-direction: column; gap: 0.5rem;">
        
 
    """

    for rec in diet_recs:
        result += f"<div>👉 {rec}</div>"

    result += "</div>"
    
    return result

# ---- Gradio UI ----
demo = gr.Interface(
    fn=predict_salt_and_info,
    inputs=[
        gr.Image(label="📷 Upload Food Image"),  
        gr.Textbox(label="🍲 Food Title", placeholder="e.g., Idli, Pasta, Biryani")
    ],
    outputs=gr.HTML(label="📊 Nutrition + Health Guidance"),
  
    title="🥘 SmartSpoon - Food Recognition and Health Recommendations",
    description=(
        "### **Project Overview**\n\n"
        "This project uses a CNN model to recognize food items from images and provides nutritional information "
        "based on a dataset of food items, including salt content, calories, protein, and fat.\n\n"
        "In addition to recognizing the food, the project suggests **electrical stimulation** levels and provides "
        "**dietary recommendations** based on the nutritional data of the food.\n\n"
        "**Upload a food image** and enter a food title (optional) to get nutrition details and health suggestions."
    ),
)

demo.launch(share=True)
