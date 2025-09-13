single_list = [1,2,3,4,5,6,7]
factor =2
counter=0

windows=[]
win2=[]
for i in range(0,len(single_list)-factor+1,factor-1):
    if len(single_list)-i<factor:
        break
    window_local=single_list[i:i+factor]
    print(f"window is {window_local}")
    average=sum(window_local)/factor
    windows.append(average)
    win2.append(sum((single_list[i:i+factor]))/factor)
print(windows)
print("win2 is ",win2)

def sliding_average(single_list, factor):
    windows=[]
    for i in range(0,len(single_list)-factor+1, factor-1):
        if factor > len(single_list)-i:
            break
        windows.append(sum((single_list[i:i+factor]))/factor)
    print(f"output is {windows}")
    return windows

sliding_average(single_list, 2)

#
# i=0
# sum=0
# counter=1
# result_list=[]
# for elements in single_list:
#     print(f"element is {elements}")
#
# while i< len(single_list):
#     sum= sum+single_list[i]
#     counter=counter+1
#
#     if counter ==factor:
#         result_list.append(sum/factor)
#         i=i-1
#         print(f"adding {sum/factor} to {result_list}, while i is {i}")
#     i=i+1
#
#
#
# print(f"result is {result_list}")
# def moving_average(single_list, factor):
#     i=0
#     sum=0
#     counter=1
#     for elements in single_list:
#         print(f"element is {elements}")
#     result_list = [1,2,3,4]
#
#     while( i< len(single_list)):
#         sum= sum+single_list[i]
#         counter=counter+1
#         if counter ==factor:
#             result_list.add(sum/factor)
#             i=i-1
#             break
#
#
#
