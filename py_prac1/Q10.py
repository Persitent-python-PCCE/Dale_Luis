def inventory_report(inv,gst=0.05,**filters):
  
  cat=sorted({cat for _, cat, _, _ in inv})
  print(f"Categories: {cat}")
  restock=list(filter(lambda x: x[2]<10,inv))
  print(f"[!] Reorder soon (stock<10): {restock}")
  gst_calc=dict(map(lambda x: (x[0], x[3]+ x[3]*gst),inv))
  print(f"Prices incl. GST: {gst_calc}")
  
  
  
  matchin=list(filter(
    lambda item:("category" not in filters or item[1] == filters["category"]) and
                ("max_pice" not in filters or item[3]<= filters["max_price"]) and
                ("min_price" not in filters or item[3]>= filters["min_pice"]) and
                ("min_stock" not in filters or item[2]>= filters["min_stock"]) and
                ("max_stock" not in filters or item[2]<= filters["max_stock"]), inv))
  
  matchin=list(map(lambda item: item[0],matchin))
  print(f"Matching filters {filters}: {matchin}")
  

  return 1

inv=[
  ("Masala Chai","Tea",5,20),
  ("Green Tea","Tea",15,30,),
  ("Samosa","Snack",8,15),
  ("Biscuit","Snack",25,10)
]

inventory_report(inv,category="Snack",max_price=15)