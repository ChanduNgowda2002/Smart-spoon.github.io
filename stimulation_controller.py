def adjust_stimulation(salt_level):
    if salt_level < 0.3:
        return "Low stimulation"
    elif 0.3 <= salt_level < 0.7:
        return "Medium stimulation"
    else:
        return "High stimulation"
