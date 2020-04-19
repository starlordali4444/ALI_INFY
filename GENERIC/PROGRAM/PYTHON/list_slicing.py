list_of_airline=["AI","SJ","JA","EM","BA"]
#slicing can be done using : 1:4  1= starting index, 4 = ending index
# it creates new list as per the given index
''' 
[ 1  2  3  4  ]
[ 0  1  2  3  ] positive indexing
[ -4  -3  -2  -1  ] negative indexing
indexing always move from left to right

[1:4:2]
1 - starting index
4 - ending index
2 - increment
'''

new_list=list_of_airline[1:2,3:4]


print(new_list)