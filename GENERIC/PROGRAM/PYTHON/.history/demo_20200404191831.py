def func(sample, res, key,val):
    index =- 1
    if(key in sample):
        res = True
        index = sample.index(key)
        values[index] = val
    else:
        res = False
    return index

res = None
sample = ["A","B","C","D"]
values = [1,1,3,4,5]
su = func(sample,res,"B",2)
print(values[su],res)