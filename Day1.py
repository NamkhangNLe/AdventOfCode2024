import heapq

def main():
    data = """
    1   4
    2   5
    3   6
    """
    solve(data)

def solve(data):
    heap1, heap2 = [], []
    lines = data.strip().split('\n')
    for line in lines:
        num1, num2 = line.split()
        heapq.heappush(heap1, int(num1))
        heapq.heappush(heap2, int(num2))
    sum = 0
    for i in range(len(heap1)):
        sum += abs(heapq.heappop(heap1) - heapq.heappop(heap2)) 
    print(sum)
main()