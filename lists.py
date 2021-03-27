
countries=["Kenya","Uganda","Rwanda", "South Sudan"]
print(countries[1:3])


newCountries=["Burundi","Tanzania"]
countries.extend(newCountries)
print (countries)

countries.sort(reverse=True)
print(countries)


a=[[1,2,3],[4,5,6],[7,8,9]]
b=[]
for i in a:
    for number in i:
            b.append(number)

print(b)

c=[val%2 for val in b ]
print(c)



        

    
    
