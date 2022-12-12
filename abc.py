# x=[10,20,30,40.9,True,"abc",10]
# print(x[0:5])
# print(len(x))
# loop in List
# i=0
# while(i<len(x)):
#     print(x[i])
#     i=i+1
x=(100,398,432,245,678,546,367,998,156,561)
number_of_salesPerson=0
a=0
while(a<len(x)):
    if(x[a]>500):
        number_of_salesPerson=number_of_salesPerson+1
    a=a+1
print(number_of_salesPerson)