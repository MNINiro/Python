def merge(left,right):
    result=[] 
    i,j=0,0
    
    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1

    result.extend(left[i:]) # since we want to add each element and not the object list
    result.extend(right[j:])

    return result
# ==============================
def merge_sort_break(list):
    if len(list) == 1:
        return list

    middle = len(list)//2
    left_list = merge_sort_break(list[:middle])
    right_list = merge_sort_break(list[middle:])

    return merge(left_list,right_list)
# =============================================
list = [100,5,200,3,100,4,8,9]
print(merge_sort_break(list))
