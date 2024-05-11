import random
# recommendations_list = ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "r10"]
def recommendations_fun(recommendations):
    my_list = recommendations
    recommendations_list = random.sample(my_list, 2)
    recod_1 = recommendations_list[0]
    recod_2 = recommendations_list[1]
#     print(recod_1)
#     print(recod_2)
    return recod_1, recod_2

