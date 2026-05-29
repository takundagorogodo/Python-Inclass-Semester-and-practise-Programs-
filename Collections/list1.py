sports = ["football","football","baseball","hockey","basketball"]
print(sports)
print(type(sports))
sports.append("golf")
sports.insert(0, "racing")
print(sports)
sports.remove("baseball")
sports.reverse()
print(sports)
del sports[0]
print(sports)
del sports[2:]
print(sports)
print(sports.count("football"))
print(sports.pop())
print(sports.clear())