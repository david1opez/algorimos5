# Algoritmo de Suffix Array para encontrar todos los sufijos de una cadena
# Input: String
# Output: Lista con los índices de los sufijos ordenados alfabéticamente
# Complejidad: O(n^2 log n)

def suffix_array(s):
    suffixes = [(s[i:], i) for i in range(len(s))]
    suffixes.sort()
    return [suffix[1] for suffix in suffixes]

text = "banana"
sa = suffix_array(text)
print(f"Suffix array: {sa}")