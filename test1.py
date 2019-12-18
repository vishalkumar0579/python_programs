# a=[10,20,30,40]
# max=""
# min=""
# sum=""
def list2(list):
    max = list[0]
    # for a in list:
    #     if a>max:
    #         max=a
    # return a
    min = list[0]
    for i in list:
        if i<min:
            min=i
    return i
print(list2([10,20,30,40]))
# for i in a:
#     if a>max:
#         max=a
# return a
