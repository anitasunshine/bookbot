file_name = "books/frankenstein.txt"

with open(file_name) as f:
    file_contents = f.read()

words = file_contents.split()

letters = {}
for letter in file_contents.lower():
    if letter in letters:
        letters[letter] += 1
    else:
        letters[letter] = 1

print(f"--- Begin report of {file_name} ---")
print(f"{len(words)} words found in the document.")
print()
for letter in letters:
    print(f"The '{letter}' character was found {letters[letter]} times.")
print("--- End report ---")
