## before writing the sort_list function, we need a helper function smallest_item function that will pick the smallest number in a list
def smallest_Item(arr):

    smallest = arr[0]
    smallest_Index = 0

    for i in range(1, len(arr)):

        if arr[i] < smallest:
            smallest = arr[i]
            smallest_Index = i
    return smallest

def sortlist(arr):

    Newlist = []

    for i in range(len(arr)):
        smallestnum  = smallest_Item(arr)
        Newlist.append(smallest)
        arr.remove(smallest)
    return Newlist

sml = [4,9,7,2,5,8]

print(smallest_Item(sml))
print(sortlist(sml))