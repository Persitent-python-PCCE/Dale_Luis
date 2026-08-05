grp_data=[
  ("Brazil",3,0,0),
  ("Japan",1,2,0),
  ("Spain",2,0,1),
  ("Ghana",0,1,2)
]
qual=list(filter(lambda team: (team[1]*3+team[2])>=6 and team[3]<2, grp_data))

qual.sort(key=lambda team:team[1]* 3+ team[2], reverse=True)

print("Advancing to knockouts:")
for country, w, d, l in qual:
  pts=w*3+d
  print(f"   {country} - {pts}pts")
