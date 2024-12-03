"""
Advent of Code 2024 - Day 1, Part 2
Brian Bullis - brian [AT] bullis [DOT] me
"""

if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        data = input_file.read().splitlines()

        # every line contains 2 values that the difference between needs to be calculated
        list1 = []
        list2 = []
        similarities = []

        for line in data:
            # add the first number in the line to list 1, and the second to list 2
            numbers = line.split()
            list1.append(int(numbers[0]))
            list2.append(int(numbers[1]))

        for number in list1:
            # calcualte a similarity score by multiplying each number from list 1 by the times it appears in list 2
            similarities.append(number * list2.count(number))

        # the answer is the sum of all the similarity scores
        print(sum(similarities))
