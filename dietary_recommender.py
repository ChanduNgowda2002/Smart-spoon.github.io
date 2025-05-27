def recommend_diet(salt_level, food_label):
    recommendations = []

    if salt_level > 0.7:
        recommendations.append("⚠️ High salt: Try low-sodium alternatives.")
    elif salt_level < 0.3:
        recommendations.append("✅ Low salt: Suitable for low-sodium diet.")

    if food_label.lower() in ["pizza", "burger", "noodles"]:
        recommendations.append("🍃 Consider fresh fruits, grilled vegetables, or salad.")

    return recommendations
