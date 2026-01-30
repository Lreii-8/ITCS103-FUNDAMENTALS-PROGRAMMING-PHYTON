def average_1(numbers):
    total = 0

    for num in numbers:
        total += num

    average = total / len(numbers)
    return average

def values(word_length, average):
    if word_length > average:
        print("The length of the word is greater than the average.")
    elif word_length < average:
        print("The length of the word is less than the average.")
    else:
        print("The length of the word is equal to the average.")

word = input("Enter a word: ")
word_length = len(word)
numbers = []

for x in range(word_length):
    number = float(input("Enter a number " + str(x + 1) + ": "))
    numbers.append(number)

average = average_1(numbers)

print(numbers)
print("Length of the word:", word_length)
print("Average of the numbers:", average)

values(word_length, average)
