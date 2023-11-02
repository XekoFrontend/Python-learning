# Programming Assignment: Read in data, store, manipulate and output new data to a file
# https://www.coursera.org/learn/programming-in-python/programming/2Frg6/read-in-data-store-manipulate-and-output-new-data-to-a-file/submission

def read_file(file_name):
    """ Reads in a file.

    [IMPLEMENT ME]
        1. Open and read the given file into a variable using the File read()
           function
        2. Print the contents of the file
        3. Return the contents of the file

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
    # WRITE SOLUTION HERE
    open_file = open(file_name, mode='r')
    read_data = open_file.read()
    print(read_data)
    return read_data

    raise NotImplementedError()


def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list

    [IMPLEMENT ME]
        1. Open the given file
        2. Read the file line by line and append each line to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    # WRITE SOLUTION HERE
    with open(file_name, 'r') as file:
        content = file.readlines()

    return content

    raise NotImplementedError()


def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.

    [IMPLEMENT ME]
        1. Get the first line of file_contents
        2. Use the File write() function to write the first line into a file
           with the name from output_filename

        We determine the first line to be everything in a string before the
        first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    # WRITE SOLUTION HERE
    list_lines = file_contents.split("\n")

    with open(output_filename, 'w') as file:
        file.write(list_lines[0])

    with open(output_filename, 'r') as file:
        read_first_line = file.read()
        print(read_first_line)

    return read_first_line

    raise NotImplementedError()


def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and add the even-numbered lines to a list
        3. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
    # WRITE SOLUTION HERE
    with open(file_name, 'r') as file:
        content = file.readlines()
        list1 = []
        # Hàm enumerate sẽ tạo ra các cặp (index, value) với index là chỉ số của phần tử và value là giá trị của phần tử tương ứng.
        for index, value in enumerate(content):
            # print(index, value)
            if index % 2 != 0:
                list1.append(value)

    return list1

    raise NotImplementedError()


def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order

    [IMPLEMENT ME]
        1. Open and read the given file into a variable
        2. Read the file line-by-line and store the lines in a list in reverse order
        3. Print the list
        4. Return the list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    # WRITE SOLUTION HERE
    with open(file_name, 'r') as file:
        orginal_list = file.readlines()

        reverse_list = []
        count = 0
        for i in orginal_list:
            count += -1
            reverse_item = orginal_list[count]
            reverse_list.append(reverse_item)

    return reverse_list

    raise NotImplementedError()


'''
Here are some sample commands to help you run/test your implementations.
Feel free to uncomment/modify/add to them as you wish.
'''


def main():
    print("----- Step 2 -----")
    file_contents = read_file("sampletext.txt")
    print("----- Step 3 -----")
    print(read_file_into_list("sampletext.txt"))
    print("----- Step 4 -----")
    write_first_line_to_file(file_contents, "online.txt")
    print("----- Step 5 -----")
    print(read_even_numbered_lines("sampletext.txt"))
    print("----- Step 6 -----")
    print(read_file_in_reverse("sampletext.txt"))


if __name__ == "__main__":
    main()
