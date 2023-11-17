import argparse


def cut_text(text, delimiter='\t', fields=None):
    """
    Mimics the functionality of the 'cut' command in Linux.
    
    Arguments:
    text: The input text to be processed.
    delimiter: The delimiter used to separate fields (default is tab).
    fields: A list of field numbers or ranges to be extracted. 
            Example: [1, 3-5, 7] will extract fields 1, 3, 4, 5, and 7.
    
    Returns:
    A string containing the extracted fields.
    """
    lines = text.split('\n')
    result = []

    for line in lines:
        fields_list = line.split(delimiter)
        extracted_fields = []

        if fields:
            for field in fields:
                if '-' in str(field):
                    start, end = map(int, field.split('-'))
                    extracted_fields.extend(fields_list[start - 1:end])
                else:
                    extracted_fields.append(fields_list[field - 1])
        else:
            extracted_fields = fields_list

        result.append(delimiter.join(extracted_fields))

    return '\n'.join(result)

# # Example usage:
# input_text = """1,John,Doe,25
# 2,Jane,Smith,30
# 3,Bob,Johnson,28"""

# output = cut_text(input_text, ',', [2, 3])
# print(output)

def wc(text):
    """
    Mimics the functionality of the 'wc' command in Linux.
    
    Arguments:
    text: The input text to be processed.
    
    Returns:
    A tuple containing the number of lines, words, and characters.
    """
    lines = text.split('\n')
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)
    
    return len(lines), word_count, char_count

# # Example usage:
# input_text = """Hello, how are you?
# I am doing well, thank you.
# """

# lines, words, characters = wc(input_text)
# print(f"Lines: {lines}, Words: {words}, Characters: {characters}")


def extract_text_from_file(file_path, in_line_no, out_line_no):
    """
    Extracts text from a file based on input and output line numbers.
    
    Arguments:
    file_path: Path to the file.
    in_line_no: Line number to start extracting text (inclusive).
    out_line_no: Line number to end extracting text (inclusive).
    
    Returns:
    A string containing the text from in_line_no to out_line_no.
    """

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            total_lines = len(lines)

            if in_line_no < 1 or out_line_no < 1 or in_line_no > total_lines or out_line_no > total_lines:
                return "Invalid line numbers provided."

            if in_line_no > out_line_no:
                return "Input line number should be less than or equal to output line number."

            extracted_lines = lines[in_line_no - 1:out_line_no]
            extracted_text = ''.join(extracted_lines)
            return extracted_text
    except FileNotFoundError:
        return "File not found."

# # Example usage:
# file_path = 'your_file.txt'  # Replace with your file path
# input_line = 3
# output_line = 5

# result = extract_text_from_file(file_path, input_line, output_line)
# print(result)





def main():
    parser = argparse.ArgumentParser(description="Command line text manipulation tool")
    parser.add_argument('operation', choices=['cut', 'wc', 'extract'],
                        help="Operation to perform: cut, wc, or extract")
    parser.add_argument('--file', '-f', help="Path to the file")
    parser.add_argument('--delimiter', '-d', default='\t',
                        help="Delimiter character (for cut operation)")
    parser.add_argument('--fields', '-F', nargs='+', type=str,
                        help="Fields to extract (for cut operation)")
    parser.add_argument('--in_line', '-i', type=int,
                        help="Starting line number (for extract operation)")
    parser.add_argument('--out_line', '-o', type=int,
                        help="Ending line number (for extract operation)")

    args = parser.parse_args()

    if args.operation == 'cut':
        # Handle cut operation
        if not args.fields:
            print("Please specify fields to cut.")
            return

        text = input("Enter text: ")
        result = cut_text(text, args.delimiter, args.fields)
        print(result)

    elif args.operation == 'wc':
        # Handle wc operation
        text = input("Enter text: ")
        lines, words, characters = wc(text)
        print(f"Lines: {lines}, Words: {words}, Characters: {characters}")

    elif args.operation == 'extract':
        # Handle extract operation
        if not all([args.file, args.in_line, args.out_line]):
            print("Please specify file path, input line number, and output line number.")
            return

        result = extract_text_from_file(args.file, args.in_line, args.out_line)
        print(result)

if __name__ == "__main__":
    main()
