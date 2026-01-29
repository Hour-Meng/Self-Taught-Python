# filer() = creates a collection of element from an iterable for which a function returns
# filer( function , iterable)

friends = [("John", 12), ("Jake", 18), ("Jame", 19), ("Joke", 20), ("Paul", 16), ("Prime", 15)]
age = lambda data: data[1] >= 18
age_checker = (filter(age, friends))
for i in age_checker:
    print(i)
