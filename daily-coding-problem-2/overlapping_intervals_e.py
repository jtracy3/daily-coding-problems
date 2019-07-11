
input_list = [(1,3), (5,8), (4,10), (20,25)]

# output_list = [(1,3), (4,10), (20,25)]

output_list = list()

for i in range(len(input_list)):

    current_interval = input_list[i]
    new_list = [x for x in input_list if x != current_interval]

    j = 0
    while j <= (len(new_list) - 1):
        interval = new_list[j]
        left = current_interval[0]
        right = current_interval[1]

        if interval[0] in range(left, right):
            if interval[1] in range(left, right):
                out = (left, right)
            else:
                out = (left, interval[1])

        if interval[1] in range(left, right):
            if interval[0] in range(left, right):
                out = (left, right)
            else:
                out = (interval[0], right)

        j += 1