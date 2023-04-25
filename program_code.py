# Write a method in python to write multiple line of text contents into a text file mylife.txt.
# Sample output:
# Enter line: Beautiful is better than ugly.
# Are there more lines y/n? y
# Enter line: Explicit is better than implicit.
# Are there more lines y/n? y
# Enter line: Simple is better than complex.
# Are there more lines y/n? n

from colorama import Back

# create list of colors for font
cyan = '\033[96m'
blue = '\033[94m'


def multiple_lines():
    # open text file
    with open('mylife.txt', 'a') as file:
        while True:
            # ask user for input
            enter = input(Back.BLACK + f'{cyan}Enter line: ')
            # write input into mylife.txt
            file.write(f'Enter line: {enter}\n')
            # ask if there are more
            count = input(f'{blue}Are there more lines y/n? ')
            # write input into mylife.txt
            file.write(f'Are there more lines y/n? {count}\n')
            # if no (n),
            if count == 'n':
                # stop execution
                break
            # if yes (y),
            else:
                # ask user for another input
                continue


multiple_lines()
