# Write a method in python to write multiple line of text contents into a text file mylife.txt.
# Sample output:
# Enter line: Beautiful is better than ugly.
# Are there more lines y/n? y
# Enter line: Explicit is better than implicit.
# Are there more lines y/n? y
# Enter line: Simple is better than complex.
# Are there more lines y/n? n

def multiple_lines():
    # open text file
    with open('mylife.txt', 'a') as file:
        # ask user for input
        enter = input('Enter line: ')
        # write input into mylife.txt
        file.write(f'Enter line: {enter}')
        # ask if there is more
        count = input('Are there more lines y/n? ')
        file.write(f'Are there more lines y/n? {count}\n')
        # if no (n),
        # stop execution
        # if yes (y),
        # ask user for another input


multiple_lines()
