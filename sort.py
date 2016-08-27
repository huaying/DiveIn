import random
import time
class Sort:
    def __init__(self, arr = []):
        self.arr = arr

    def timer(self,func_name):
        start = time.time()
        result = eval("".join(["self.",func_name,"()"]))
        print func_name + ": " + str(time.time() - start)
        return result

    def bubble_sort(self):
        arr = self.arr[:]
        stop = False
        for i in xrange(len(arr)-1):
            if stop: break
            stop = True
            for j in xrange(1,len(arr)-i):
                if arr[j-1] > arr[j]: 
                    arr[j-1], arr[j] = arr[j],arr[j-1]
                    stop = False
        return arr
    
    def selection_sort(self):
        arr = self.arr[:]
        for i in xrange(len(arr)):
            m = i
            for j in xrange(i+1,len(arr)):
                if arr[m] > arr[j]: m = j
            arr[i],arr[m] = arr[m],arr[i]
        return arr

    def insertion_sort(self):
        arr = self.arr[:]
        for i in xrange(1,len(arr)):
            target = arr[i]
            j = i
            while j > 0 and target < arr[j-1]: 
                arr[j] = arr[j-1]
                j-=1
            arr[j] = target
        return arr
   
    def merge_sort(self):
        def mergeSort(arr):
            if len(arr) < 2: return arr
            m = len(arr)/2
            first = mergeSort(arr[:m])
            sec = mergeSort(arr[m:])
            return merge(first,sec)
        
        def merge(a,b):
            i = j = 0
            r = []
            while i != len(a) and j != len(b):
                if a[i] > b[j]:
                    r.append(b[j])
                    j+=1
                else:
                    r.append(a[i])
                    i+=1
        
            if i!=len(a): r.extend(a[i:])
            else: r.extend(b[j:])
            return r

        return mergeSort(self.arr[:])

    def quick_sort(self):
        def quickSort(arr, begin, end):
            if begin >= end: return
            i,j = begin+1, end
            while True:
                while i <= end and arr[i] <= arr[begin]: i+=1
                while j > begin and arr[j] > arr[begin]: j-=1
                if i>j: break
                arr[i],arr[j] = arr[j],arr[i]
            arr[begin], arr[j] = arr[j], arr[begin]
            quickSort(arr,begin,j-1)
            quickSort(arr,j+1,end)
            return arr

        begin,end = 0,len(self.arr)-1
        return quickSort(self.arr[:],begin,end)

    def radix_sort(self):
        arr = self.arr[:]
        hi = max(arr)
        base,r = 10, 1
        while r <= hi:
            bucket = [[] for _ in xrange(base)]
            for num in arr:
                bucket[num/r % base].append(num)

            arr= reduce(lambda x,y: x+y, bucket)
            r*=10

        return arr



sorted_arr = range(3000)
unsorted_arr = sorted_arr[:]
random.shuffle(unsorted_arr)

sort = Sort(unsorted_arr)
assert sort.timer("bubble_sort") == sorted_arr, "bubble_sort fails"
assert sort.timer("selection_sort") == sorted_arr, "selection_sort fails"
assert sort.timer("insertion_sort") == sorted_arr, "insertion_sort fails"
assert sort.timer("merge_sort") == sorted_arr, "merge_sort fails"
assert sort.timer("quick_sort") == sorted_arr, "quick_sort fails"
assert sort.timer("radix_sort") == sorted_arr, "radix_sort fails"


print "ok"
