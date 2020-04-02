gem_list=["Emerald","Ivary","Jasper","Ruby","Garnet"]
price_list=[1760,2119,1599,3920,3999]

required_gem="Ruby"
required_index=None

# for i in range(0,len(gem_list)):
#     if gem_list[i]==required_gem:
#         required_index=i

# print("Price of required Item is ",price_list[required_index])

reqd_gems=["Ivary","Emerald","Garnet"]
reqd_quantity=[3,10,12]
total_price=0

for i in range(0,len(reqd_gems)):
    if(reqd_gems[i] in gem_list):
        print("Found")
    qty = reqd_quantity[i]

    for j in range(0,len(gem_list)):
        if reqd_gems[i]==gem_list[j]:
            required_index=j
    total_price += price_list[required_index]*qty
