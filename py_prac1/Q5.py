bill=[
  ("Masala Chai",3,20),
  ("Samosa",2,15), 
  ("Greeen Tea", 1, 30)
]

line_totals=list(map(lambda x:round(x[1] * x[2] *1.05,2), bill))

grd_total=sum(line_totals)

print("Line totals(incl. GST): ",line_totals)
print(f"Grand total: {grd_total:.2f}")