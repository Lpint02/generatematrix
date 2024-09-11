import numpy as np
import os
from datetime import datetime

def generate_diagonally_dominant_matrix(n, factor, density=0.2):
    
    A = np.random.uniform(-5, 5, size=(n, n)).astype(np.float32)

    # Imposta alcuni elementi a zero per ridurre la densità della matrice
    zero_mask = np.random.rand(n, n) > density
    A[zero_mask] = 0

    for i in range(n):
        A[i, i] = np.sum(np.abs(A[i, :])) * factor

    # Approssima i valori a due cifre decimali
    A = np.round(A, 2)

    return A

def generate_known_terms_vector(n):
    # Genera un vettore b con valori casuali
    b = np.random.rand(n).astype(np.float32)

    # Approssima i valori a due cifre decimali
    b = np.round(b, 2)

    return b

def save_matrix_and_vector_to_file(matrix, vector, folder_path, n):
    # Verifica che la cartella esista, altrimenti la crea
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    file_name = f'matrice_{n}x{n}_{timestamp}.txt'
    
    # Componi il percorso completo del file
    file_path = os.path.join(folder_path, file_name)
    
    # Salva la matrice su un file .txt nel formato richiesto
    with open(file_path, 'w', newline='') as f:
        for row in matrix:
            row_str = ','.join([f'{num:.2f}'.rstrip('0').rstrip('.') if num != 0 else '0' for num in row]) + ';'
            f.write(row_str + '\n')

        f.write('---\n')

        # Salva il vettore b
        vector_str = ','.join([f'{num:.2f}'.rstrip('0').rstrip('.') for num in vector])
        f.write(vector_str + '\n')
    
    print(f"Matrice e vettori salvati in: {file_path}")

n = 7000
factor = 1.5
folder_path = 'C:\\Users\\leona\\OneDrive\\Desktop\\matricigenerate'  # Specifica il percorso della cartella


# Genera la matrice
matrix = generate_diagonally_dominant_matrix(n, factor)
vector = generate_known_terms_vector(n)

# Salva la matrice nel file specificato
save_matrix_and_vector_to_file(matrix, vector, folder_path, n)
