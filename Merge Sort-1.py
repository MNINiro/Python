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

def merge_sort(data):
    if len(data) == 1:
        return data

    middle = len(data)//2
    left_data = merge_sort(data[:middle])
    right_data = merge_sort(data[middle:])

    return merge(left_data,right_data)


data = [100,5,200,3,100,4,8,9] 
print(merge_sort(data))
