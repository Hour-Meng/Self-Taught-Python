# dictionary : a collection of {key:value} pairs
#              ordered and changeable. No duplicates

Capital = {"Cambodia": "Pnhom Pehn",
           "Russia": "Moscow",
           "Japan": "Tokyo",
           "China": "Beijing"}

print(Capital.get("China"))

Capital.update({"German": "Berlin"})
#Capital.pop() #Will pop(delete) a selected one
#Capital.popitem() #Will randomly pop

print(Capital)

keys = Capital.keys()
print("---Counties---")
for i in keys:
    print(i)
print("---Capitals---")
# ---  to print the inside value ---
value = Capital.values()
for i in value:
    print(i)

for country, capital in zip(keys, value):
   print(f"{country}:{capital}")