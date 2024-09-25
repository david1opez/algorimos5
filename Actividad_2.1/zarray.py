# Algoritmo Z para buscar un patrón en un texto
# Input: Texto y patrón a buscar
# Output: Índices donde se encuentra el patrón en el texto
# Complejidad: O(n)

def z_algorithm(pattern, text):
    s = pattern + '$' + text

    n = len(s)
    Z = [0] * n
    L, R, K = 0, 0, 0
    
    for i in range(1, n):
        if i > R:
            L, R = i, i
            while R < n and s[R] == s[R - L]:
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            K = i - L
            if Z[K] < R - i + 1:
                Z[i] = Z[K]
            else:
                L = i
                while R < n and s[R] == s[R - L]:
                    R += 1
                Z[i] = R - L
                R -= 1
    return Z

pattern = "aba"
text = "ababcabcabababd"
Z = z_algorithm(pattern, text)
print(Z)
