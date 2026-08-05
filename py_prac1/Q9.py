def create_hero(name,*powers,**stats):
  print(f"Hero: {name}")
  print(f"Powers: {powers}")
  print("Stats:")
  for k,v in stats.items():
    print(f"   {k}: {v}")
    
  
  
create_hero("Spider-Man", "wall-crall","spider-sens",strength=85,agility=95,intelligence=92)