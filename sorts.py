# importing files and dependencies
import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mp

# main function 
def sorting_visualizer(N, method, data, speed):

    # Helper function to swap elements
    def swap(A, i, j):
        
        A[i], A[j] = A[j], A[i]

    # Bubble sort algorithm (in-place)
    def bubblesort(A):

        if len(A) == 1:
            return

        swapped = True
        for i in range(len(A) - 1):
            if not swapped:
                break

            swapped = False
            for j in range(len(A) - 1 - i):
                bar_rects[j+1].set_color('b')

                if A[j] > A[j + 1]:
                    swap(A, j, j + 1)
                    swapped = True

                bar_rects[j+1].set_color('b')
                yield A
                bar_rects[j+1].set_color(color_map(data_normalizer(A))[j+1])

        # confirm sorted
        for k in range(len(A)):
            bar_rects[k].set_ec('b')
            yield A
            bar_rects[k].set_ec(None)
            iteration[0]-=1

    # Insertion sort algorithm
    def insertionsort(A):

        for i in range(1, len(A)):
            j = i
            while j > 0 and A[j] < A[j - 1]:
                swap(A, j, j - 1)
                j -= 1

                bar_rects[j+1].set_color('b')
                yield A
                bar_rects[j+1].set_color(color_map(data_normalizer(A))[j+1])

        for k in range(len(A)):
            bar_rects[k].set_ec('b')
            yield A
            bar_rects[k].set_ec(None)
            iteration[0]-=1

    # Merge sort algorithm calling function
    def mergesort_parent(A, start, end):
        yield from mergesort(A, start, end)
        for k in range(len(A)):
            bar_rects[k].set_ec('b')
            yield A
            bar_rects[k].set_ec(None)
            iteration[0]-=1
        
    # Merge sort algorithm
    def mergesort(A, start, end):

        if end <= start:
            return

        mid = start + ((end - start + 1) // 2) - 1
        yield from mergesort(A, start, mid)
        yield from mergesort(A, mid + 1, end)
        yield from merge(A, start, mid, end)
        yield A


    def merge(A, start, mid, end):
        
        merged = []
        leftIdx = start
        rightIdx = mid + 1

        while leftIdx <= mid and rightIdx <= end:
            if A[leftIdx] < A[rightIdx]:
                merged.append(A[leftIdx])
                leftIdx += 1
            else:
                merged.append(A[rightIdx])
                rightIdx += 1

        while leftIdx <= mid:
            merged.append(A[leftIdx])
            leftIdx += 1

        while rightIdx <= end:
            merged.append(A[rightIdx])
            rightIdx += 1

        for i, sorted_val in enumerate(merged):
            bar_rects[start+i].set_color('b')
            A[start + i] = sorted_val
            yield A
            bar_rects[start+i].set_color(color_map(data_normalizer(A))[start+i])

    # Quick sort calling function
    def quicksort_parent(A, start, end):
        yield from quicksort(A, start, end) 
        for k in range(len(A)):
            bar_rects[k].set_ec('b')
            yield A
            bar_rects[k].set_ec(None)
            iteration[0]-=1

    # Quick sort algorithm
    def quicksort(A, start, end):

        if start >= end:
            return

        pivot = A[end]
        pivotIdx = start

        for i in range(start, end):
            if A[i] < pivot:
                swap(A, i, pivotIdx)
                pivotIdx += 1

            bar_rects[i].set_color('b')
            yield A
            bar_rects[i].set_color(color_map(data_normalizer(A))[i])

        swap(A, end, pivotIdx)
        yield A

        bar_rects[pivotIdx].set_color(color_map(data_normalizer(A))[pivotIdx])
        bar_rects[end].set_color(color_map(data_normalizer(A))[end])

        yield from quicksort(A, start, pivotIdx - 1)
        yield from quicksort(A, pivotIdx + 1, end)

    # Selection sort algorithm
    def selectionsort(A):

        if len(A) == 1:
            return

        for i in range(len(A)):
            
            minVal = A[i]
            minIdx = i

            for j in range(i, len(A)):
                bar_rects[j].set_color('b')
                if A[j] < minVal:
                    minVal = A[j]
                    minIdx = j
                yield A

                bar_rects[j-1].set_color(color_map(data_normalizer(A))[j])
            swap(A, i, minIdx)
            yield A

        for k in range(len(A)):
            bar_rects[k].set_ec('b')
            yield A
            bar_rects[k].set_ec(None)
            iteration[0]-=1
            

    # heapify function for heap sort
    def heapify(A, n, i):
        # Find largest among root and children
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and A[i] < A[l]:
            largest = l

        if r < n and A[largest] < A[r]:
            largest = r

        # If root is not largest, swap with largest and continue heapifying
        if largest != i:
            swap(A,i,largest)
            bar_rects[i].set_color('b')
            yield from heapify(A, n, largest)
            bar_rects[i].set_color(color_map(data_normalizer(A))[i])
        yield A
        bar_rects[i].set_color(color_map(data_normalizer(A))[i])

    # Heap sort algorithm
    def heapSort(A):
        n = len(A)

        # Build max heap
        for i in range(n//2, -1, -1):
            yield from heapify(A, n, i)

        for i in range(n-1, 0, -1):
            # Swap
            swap(A,i,0)
            # Heapify root element
            yield from heapify(A, i, 0)
            bar_rects[i].set_color(color_map(data_normalizer(A))[i])
        yield A

        for k in range(len(A)):
            bar_rects[k].set_ec('b')
            yield A
            bar_rects[k].set_ec(None)
            iteration[0]-=1
        

    # MAIN PROGRAM

    # Creating color map
    data_normalizer = mp.colors.Normalize()
    color_map = mp.colors.LinearSegmentedColormap(
        "my_map",
        {
            "red": [(0, 1.0, 1.0),
                    (1.0, .5, .5)],
            "green": [(0, 0.5, 0.5),
                    (1.0, 0, 0)],
            "blue": [(0, 0.50, 0.5),
                    (1.0, 0, 0)]
        }
    )


    # Creating array for sorting 
    A = [x + 1 for x in range(N)]
    max_Y = N+1

    if data == 'r':
        random.seed(time.time())
        random.shuffle(A)
    elif data == 'd':
        A.reverse()
    else:
        for i in range(1,N-1,2):
            A[i],A[i-1]=A[i-1],A[i]

    # Get appropriate generator to supply to matplotlib FuncAnimation method.
    if method == "b":
        title = "Bubble Sort"
        generator = bubblesort(A)
        complexity = "BEST CASE: Ω(n) ,  AVERAGE: θ(n^2) ,  WORST CASE: O(n^2)"

    elif method == "i":
        title = "Insertion Sort"
        generator = insertionsort(A)
        complexity = "BEST CASE: Ω(n) ,  AVERAGE: θ(n^2) ,  WORST CASE: O(n^2)"

    elif method == "m":
        title = "Merge Sort"
        generator = mergesort_parent(A, 0, N - 1)
        complexity = "BEST CASE: Ω(n log n) ,  AVERAGE: θ(nlogn) ,  WORST CASE: O(nlogn)"

    elif method == "q":
        title = "Quick Sort"
        generator = quicksort_parent(A, 0, N - 1)
        complexity = "BEST CASE: Ω(n log n) ,  AVERAGE: θ(nlogn) ,  WORST CASE: O(n^2)"

    elif method == "h":
        title = "Heap Sort"
        generator = heapSort(A)
        complexity = "BEST CASE: Ω(n log n) ,  AVERAGE: θ(nlogn) ,  WORST CASE: O(nlogn)"

    else:
        title = "Selection Sort"
        generator = selectionsort(A)
        complexity = "BEST CASE: Ω(n^2) ,  AVERAGE: θ(n^2) ,  WORST CASE: O(n^2)"


    # Initialize figure and axis.
    fig, axs = plt.subplots(1,1,figsize=(10, 6))
    axs.set_title(title)
    axs.set_facecolor("#e4e6e8")

    # Initialize a bar plot. 
    # It makes a list of rectangle of given size
    # one element corresponds to one rectangle
    bar_rects = axs.bar(
        range(len(A)), 
        A, 
        align="edge", 
        color=color_map(data_normalizer(A)),
        linewidth=1)

    # Set axis limits. Set y axis upper limit high enough that the tops of
    # the bars won't overlap with the text label.
    axs.set_xlim(0, N)
    axs.set_ylim(0, max_Y)


    # Place text label for no. of operations and time complexity
    text = axs.text(0.02, 0.94, "", transform=axs.transAxes)
    plt.text(3, -3, complexity)

    # this function runs for each iteration of animation and updates the height of rectangle
    # and number of operations
    iteration = [0]
    def update_fig(A, rects, iteration):
        for rect, val in zip(rects, A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

   
    # Start animation with generator function for frame change
    anim1 = animation.FuncAnimation(fig, func=update_fig,
        fargs=(bar_rects, iteration), frames=generator, interval=speed,
        repeat=False)

    plt.show()
