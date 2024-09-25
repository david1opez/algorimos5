# Algoritmo Knuth-Morris-Pratt para buscar un patrón en un texto
# Input: Texto y patrón a buscar
# Output: Índice donde se encuentra el patrón en el texto
# Complejidad: O(n + m)

def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    
    lps = compute_lps(pattern)
    i = j = 0
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
        if j == m:
            print(f"Patron encontrado desde índice {i - j}")
            j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

text = "ababcabcabababd"
pattern = "ababd"
kmp_search(text, pattern)
