# web solution

def quickSort(data_list):
   print(f'data={data_list}')
   _quickSort(data_list,0,len(data_list)-1)

def _quickSort(data_list,first,last):
   if first < last:

       splitpoint = partition(data_list,first,last)

       _quickSort(data_list,first,splitpoint-1)
       _quickSort(data_list,splitpoint+1,last)


def partition(data_list,first,last):
   pivotvalue = data_list[first]
   print(f'pivot={pivotvalue}')

   leftmark = first+1
   rightmark = last
   print(f'left={leftmark} right={rightmark}')

   done = False
   while not done:

       print('par la gauche...')
       while leftmark <= rightmark and data_list[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       print('par la droite...')
       while data_list[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       print(f'left={leftmark} right={rightmark}')
       if rightmark < leftmark:
           done = True
       else:
           temp = data_list[leftmark]
           data_list[leftmark] = data_list[rightmark]
           data_list[rightmark] = temp

   print(f'data={data_list}')
   temp = data_list[first]
   data_list[first] = data_list[rightmark]
   data_list[rightmark] = temp
   print(f'data={data_list}')

   return rightmark

data_list = [54,26,93,17,77,31,44,55,20]
quickSort(data_list)
print(data_list)
