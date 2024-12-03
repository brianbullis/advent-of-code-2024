"""
Advent of Code 2024 - Day 1, Part 1
Brian Bullis - brian [AT] bullis [DOT] me
"""

if __name__ == '__main__':
    with open('input.txt', 'r') as input_file:
        data = input_file.read().splitlines()

        # every line contains 2 values that the difference between needs to be calculated
        list1 = []
        list2 = []
        differences = []

        for line in data:
            # add the first number in the line to list 1, and the second to list 2
            numbers = line.split()
            list1.append(int(numbers[0]))
            list2.append(int(numbers[1]))

        # the numbers need to be sorted in ascending order for the operation
        list1.sort()
        list2.sort()

        for i in range(len(list1)):
            # calculate the difference between the 2 numbers at each position in the list
            differences.append(abs(list1[i] - list2[i]))

        # the answer is the sum of all the differences
        print(sum(differences))
