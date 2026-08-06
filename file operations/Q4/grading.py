def grade(percentage):
    if percentage>=90:
        return 'A'
    elif percentage<=89 and percentage>=75:
        return 'B'
    elif percentage<=74 and percentage>=60:
        return 'C'
    elif percentage<=59 and percentage>=40:
        return 'D'
    else:
        return 'F'