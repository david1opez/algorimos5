# Algoritmo de Manacher para encontrar el palíndromo más largo de una cadena
# Input: String
# Output: El palíndromo más largo de la cadena
# Complejidad: O(n)

def manacher(s):
    s = '#' + '#'.join(s) + '#'
    n = len(s)
    P = [0] * n
    C = R = 0
    
    for i in range(n):
        mirror = 2 * C - i
        if i < R:
            P[i] = min(R - i, P[mirror])
        
        while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and s[i + P[i] + 1] == s[i - P[i] - 1]:
            P[i] += 1
        
        if i + P[i] > R:
            C, R = i, i + P[i]
    
    max_len, center_index = max((n, i) for i, n in enumerate(P))
    start = (center_index - max_len) // 2
    return s[center_index - max_len: center_index + max_len].replace('#', '')

text = "babadaada"
print(f"Longest palindromic substring: {manacher(text)}")