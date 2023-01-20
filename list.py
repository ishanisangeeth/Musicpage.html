country={"australia":"Canberra","Newzeland":"Wellington","india":"newdelhi"}
print(country)
print(country["india"])
#print(country["germany"])
print(country.get("france","value not found"))
print(country.get("Australia","not available"))
newelement={"france":"paris"}
country.update(newelement)
print(country)

country.update({"japan":"tokyo"})
print(country)

country['China'] = 'Beijing'
print(country)
country.update({"india":"delhi"})
print(country)

del(country["australia"])
print(country)

name=len(country)
print(name)

place=max(country.values())
print(place)

place1=min(country.values())
print(place1)




