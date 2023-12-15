import math


def calculate_wire_length(w, heights):
    total_length = 0

    for i in range(len(heights) - 1):
        x1, y1 = i * w, heights[i]
        x2, y2 = (i + 1) * w, heights[i + 1]

        if heights[i] == heights[i + 1]:
            segment_length = math.sqrt((x2-x1)**2 + (y2-y1)**2)
            total_length += segment_length
        else:
            segment_length = math.sqrt((x2-x1)**2 + (y2-y1)**2) + math.sqrt((x2-x1)**2 + (y2-y1)**2)
            total_length = segment_length

        total_length

    return round(total_length, 2)


# w = 2
# heights = [3, 1, 3]
# result = calculate_wire_length(w, heights)
# print(result)
#
# w1 = 100
# heights1 = [1, 1, 1, 1]
# result1 = calculate_wire_length(w1, heights1)
# print(result1)


with open('input.txt', 'r') as file:
    w = int(next(file).strip())
    heights = list(map(int, next(file).strip().split()))


result = calculate_wire_length(w, heights)

with open('output.txt', 'w') as file:
    file.write(str(result))





