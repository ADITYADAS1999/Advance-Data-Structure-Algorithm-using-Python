# Python program to merge and sort two list
def Merge(list1, list2):
    final_list = list1 + list2
    final_list.sort()
    return(final_list)
  
# Driver Code
list1 = [2,45,86,9,8]
list2 = [1,2,1,3]
print(Merge(list1, list2))
