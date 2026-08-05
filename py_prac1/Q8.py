def launch(*stages, abort_tresh=5000):
  py_mass=0
  for i in range(len(stages)):
    py_mass+=stages[i]
    if py_mass >abort_tresh:
      print(f"[ABORT] at stage {i+1}: threshold {abort_tresh} kg exceeded")
      return
    else:
      print(f"Stage {i+1} armed -> cumulative {py_mass}kg")
      
  print(f"Launch successful! Total mass: {py_mass} kg")
  print(f"Stages fired: {len(stages)}")
      
launch(1200,1800,2500,900,5000, abort_tresh=9000)