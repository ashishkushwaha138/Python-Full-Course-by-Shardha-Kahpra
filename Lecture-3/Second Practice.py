# [1,2,3,1]  this is palidrome symstem copy karne par reverse par same aa jaye

list1 = [1, 2 ,1]


copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palidrome")
else:
    print("Not Palidrome")