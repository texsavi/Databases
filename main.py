from replit import db
db["choir"] = {"Person0": "Tracy","Person1":"Kate","Person2":"Roselyne","Person3":"Njoro"}
db["bakery"] = {"Tuesday":"Zippos","Wednesday":"Nana's Cafe","Thursday":"Olaro Hotel"} 
db["chafua"]= {"Hotel1":"Eggs","Hotel2":"ndazi and eggs","Space3":"Fruits","Hotel3":"Chilli","MMU Chafua":"Chilli, Eggs"}

try:
  get = db["choir"]
  print(get["Person1"])
  print()
  keys = db.keys()
  print(keys)
  print()
  matches = db.prefix("ch")
  print(matches)
  print()
  print(".......just a break........")
  for key in keys:
    print()
    print(f"""{key}: {db[key]}""")
    
except:
  print("Lost your keys?... ")


