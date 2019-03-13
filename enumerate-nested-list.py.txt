# Example: using enumerate to access a nested list
# The second argument is optional - just identifies where to start.
# You can output as tuples.
# By the way, an array would look like this: arr = { 3, 5, 10, 12, 20 }

lst = [[4,6,6,5], [7,9,4,2], [2,9,7,7]]

def row_avg(lst):
    for i, row in enumerate(lst, 1):
        avg = sum(row)/len(row)
        print(f' Row {i}:  Average: {avg:3.2f}')

row_avg(lst)
