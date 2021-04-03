def intersection_of_two_string(str1, str2):
    result = ""
    for ch in str1:
        if ch in str2 and not ch in result:
            result += ch
    return result

str1 = input('Entrez une première chaîne : ')
str2 = input('Entrez une deuxième chaîne : ')
print("Chaînes:")
print(str1)
print(str2)
print("\nIntersection:") 
print(intersection_of_two_string(str1, str2))

