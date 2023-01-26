from replit import db
import datetime, os, time


def tweet():
  tweet = input("My tweet>> ")
  ctime = datetime.datetime.now()
  key = f"twee{ctime}"
  db[key] = tweet
  time.sleep(1)
  os.system("clear")


def view():
  matches = db.prefix("twee")
  matches = matches[::-1]
  print(matches)
  counter = 0
  for i in matches:
    print(db[i])
    print()
    time.sleep(0.5)

    counter += 1
    if counter % 10 == 0:
      more = input("View 10 more tweets?\ny/n>> ").lower()
      if more == "n":
        break


while True:
  print("\033[44m")
  print("🐦My Tweeterial🐦")
  menu = input("1. Add tweets\n2. View tweets\n>>")
  if menu == "1":
    tweet()
  else:
    view()
    time.sleep(1)
    os.system("clear")
