country=["america","autrstailia","canada","argentina"]
print(country)
country.append("germany")
print(country)
country[1]="australia"
print(country)
del(country[2])
print(country)
size=len(country)
print(size)
place=country.index("argentina")
print(place)
places=country[-2: ]
print(places)

name=max(country)
print(name)
name1=min(country)
print(name1)

country.sort(reverse=True)
print(country)