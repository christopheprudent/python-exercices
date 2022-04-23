import pandas as pd
student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
        'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})

s6 = pd.Series(['S6', 'Scarlette Fisher', 205], index=['student_id', 'name', 'marks'])
print("Original DataFrames:")
print(student_data1)
print("\nNew Row(s)")
print(s6)

# méthode obsolète!
combined_data = student_data1.append(s6, ignore_index = True)
print("\nCombined Data (with append):")
print(combined_data)

# FIXME: ajout 3 nouvelles lignes et 1 nouvelle colonne !
print("\nCombined Data (with concat):")
result_data = pd.concat([student_data1, s6], ignore_index = True)
print(result_data)
