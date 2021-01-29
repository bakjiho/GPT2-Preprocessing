import re

def align_space(input_string):
    if len(input_string) == 0:
        return input_string
    output_string = re.sub(r'  +', ' ', input_string)
    return output_string

def remove_wiki_title(input_string):
    if len(input_string) == 0:
        return input_string
    output_string = re.sub(r'==+[\S\s]*==+', '', input_string)
    return output_string


def write_dot(input_string):
    if len(input_string) == 0:
        return input_string
    last = input_string[-1]
    p = re.compile(r'[a-zA-Z0-9]')
    if p.match(last) is not None:
        input_string += '.'
    return input_string

f = open('result.txt', mode='wt', encoding='utf-8')
with open("wikipedia.txt") as infile:
    for line in infile:
        # Trim
        line = line.strip()
        # Blank line
        if len(line) == 0:
            continue
        # Change more than 2 spaces to 1 space.
        line = align_space(line)
        # Remove wiki title
        line = remove_wiki_title(line)
        # Align space
        line = align_space(line)
        # Write dot
        line = write_dot(line)
        # Trim
        line = line.strip()
        if len(line) == 0:
            continue
        f.write(line + "\n")

