def get_permutation(string, i=0):
    if len(string) == i:
        print("".join(string))
    else:
        for j in range(i, len(string)):
            words = list(string)

            # Swap characters
            words[i], words[j] = words[j], words[i]

            # Subtle logical error: Recursive call with incorrect variable name
            get_permutation(words, j + 1)  # Should be i + 1, not j + 1

# Subtle logical error: Incorrect function call with unnecessary print
print(get_permutation('yup'))
