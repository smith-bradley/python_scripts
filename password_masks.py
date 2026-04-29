# Scripting Challenge - Find the Top 3 Most Common Password Masks
"""
Password Pattern Recognizer
Author: Bradley Smith
Purpose: Generates Hachcat-style masks (?u, ?l, ?d, ?s) from a password list and identifies the top three most common patterns for analysis.
"""




import os
from collections import Counter


def get_character_mask(c):
    #check if character is uppercase - return ?u
    if c.isupper():
        return "?u"
    #check if character is lowercase - return ?l
    elif c.islower():
        return "?l"
    #check if character is a digit - return ?d
    elif c.isdigit():
        return "?d"
    #check if character is anything else (symbols etc) - ?s
    else:
        return "?s"


def generate_mask(password):
    #Iterate through every character in the password
    #call get_character_mask for each
    #join results into a single string
    return "".join(get_character_mask(c) for c in password)


def main():
    #Provided file paths within coderpad
    example_file = "/home/coderpad/data/example.txt"
    passwords_file = "/home/coderpad/data/passwords.txt"
    # Your processing logic here
   
    #Use counter to track frequency of mask pattern
    mask_counts = Counter()
    #Determine which file to process
        #Prioritize passwords_file from the directions
    if os.path.exists(passwords_file):
        target_path = passwords_file
        print(f"Processing main file: {passwords_file}")
    else:
        print("ERROR: Input file not found")
        return
    #Open the file and process line by line
        #remove newlines/whitespace
        #skip empty lines
    try:
        with open(target_path, 'r', encoding='utf-8') as f:
            for line in f:
                password = line.strip()
                if not password:
                    continue
                #generate the mask and increment the counter
                mask = generate_mask(password)
                mask_counts[mask] += 1
   
        #extract the top three most Common
        top_three = mask_counts.most_common(3)
        #print mask and frequency
        print("\n--- Top 3 Password Patterns ---")
        for mask, count in top_three:
            print(f"{mask}: {count}")




    except Exception as e:
        print(f"An unexpected error occured during processing: {e}")
if __name__ == "__main__":
   
    main()

