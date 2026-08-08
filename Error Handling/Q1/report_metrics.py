import math

def average_order_value(total_revenue, num_orders):
    try:
        avg = total_revenue / num_orders
        return round(avg,2)
    
    except ZeroDivisionError:
        return 0.0
    
def project_revenue(current_revenue,growth_rate,period):
    
    try:
        projected = current_revenue * (1.0+ growth_rate) ** period
        return round(projected,2)
    except OverflowError:
        return float("inf")
    except ArithmeticError:
        return 0.0

print(average_order_value(15000,120))
print(average_order_value(15000,0))
print(project_revenue(50000,0.08,5))
print(project_revenue(1e6,8.0,100000))