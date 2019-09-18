import random
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt


# Problem 7-2 (d)
class QuickSortAnalyzer:

    def __init__(self):
        self.num_recursive_call = 0

    def reset(self):
        self.num_recursive_call = 0

    def get(self):
        return self.num_recursive_call

    def partition(self, A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    def quicksort(self, A, p, r):
        if p < r:
            q = self.partition(A, p, r)
            self.quicksort(A, p, q - 1)
            self.quicksort(A, q + 1, r)
        return A

    def randomized_partition(self, A, p, r):
        i = random.randint(p, r)
        A[r], A[i] = A[i], A[r]
        return self.partition(A, p, r)

    def randomized_quicksort(self, A, p, r):
        self.num_recursive_call += 1
        if p < r:
            q = self.randomized_partition(A, p, r)
            self.randomized_quicksort(A, p, q - 1)
            self.randomized_quicksort(A, q + 1, r)
        return A

    def partition_(self, A, p, r):
        x = A[r]
        i = p - 1
        k = 0
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
                if A[i] == x:
                    k = k + 1
                if A[i] < x:
                    A[i - k], A[i] = A[i], A[i - k]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1 - k, i + 1

    def quicksort_(self, A, p, r):
        if p < r:
            q, t = self.randomized_partition_(A, p, r)
            self.quicksort_(A, p, q - 1)
            self.quicksort_(A, t + 1, r)
        return A

    def randomized_partition_(self, A, p, r):
        i = random.randint(p, r)
        A[r], A[i] = A[i], A[r]
        return self.partition_(A, p, r)

    def randomized_quicksort_(self, A, p, r):
        self.num_recursive_call += 1
        if p < r:
            q, t = self.partition_(A, p, r)
            self.randomized_quicksort_(A, p, q - 1)
            self.randomized_quicksort_(A, t + 1, r)
        return A


# Problem 7-4 (d)
class TailRecursiveAnalyzer:

    def __init__(self):
        self.stack = list()
        self.stack_history = list()

    def peek_stack(self):
        self.stack_history.append(len(self.stack))

    def reset(self):
        self.stack = list()
        self.stack_history = list()

    def get(self):
        return self.stack_history

    def partition(self, A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    def tail_recursive_quicksort(self, A, p, r):
        self.stack.append(1)
        self.peek_stack()
        while p < r:
            q = self.partition(A, p, r)
            self.tail_recursive_quicksort(A, p, q - 1)
            p = q + 1
        self.stack.pop()
        self.peek_stack()
        return A

    def optimized_tail_recursive_quicksort(self, A, p, r):
        self.stack.append(1)
        self.peek_stack()
        while p < r:
            q = self.partition(A, p, r)
            if q < (r - p) // 2:
                self.optimized_tail_recursive_quicksort(A, p, q - 1)
                p = q + 1
            else:
                self.optimized_tail_recursive_quicksort(A, q + 1, r)
                r = q - 1
        self.stack.pop()
        self.peek_stack()
        return A


if __name__ == "__main__":

    print('7-2 (d):')
    analyzer = QuickSortAnalyzer()
    case = [5, 6, 8, 10, 11, 13, 8, 8, 3, 5, 2, 11, 8]
    # analysis randomized quicksort
    analyzer.randomized_quicksort(case, 0, len(case) - 1)
    print('RANDOMIZED-QUICKSORT  recursive call:', analyzer.get())
    analyzer.reset()
    case = [5, 6, 8, 10, 11, 13, 8, 8, 3, 5, 2, 11, 8]
    # analysis randomized quicksort'
    analyzer.randomized_quicksort_(case, 0, len(case) - 1)
    print('RANDOMIZED-QUICKSORT\' recursive call:', analyzer.get())

    print('7-4 (d):')
    analyzer = TailRecursiveAnalyzer()
    case = [5, 6, 8, 10, 11, 13, 8, 8, 3, 5, 2, 11, 8]
    # analysis tail recursive quicksort
    analyzer.tail_recursive_quicksort(case, 0, len(case) - 1)
    original = analyzer.get()
    analyzer.reset()
    case = [5, 6, 8, 10, 11, 13, 8, 8, 3, 5, 2, 11, 8]
    # analysis optimized tail recursive quicksort
    analyzer.optimized_tail_recursive_quicksort(case, 0, len(case) - 1)
    optimized = analyzer.get()

    # plot
    fig, ax = plt.subplots()
    insertion_sort_plot = ax.plot(
        original,
        label='tail recursive quicksort',
    )
    merge_sort_plot = ax.plot(
        optimized,
        label='optimized tail recursive quicksort',
    )
    ax.set(
        xlabel='recursive call',
        ylabel='stack depth',
        title="original v.s. optimized",
    )
    ax.grid()
    ax.legend()
    fig.savefig("result.png", dpi=100)
    print('see reslut.png')