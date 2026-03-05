import threading
import time

# Ukuran matrix (3x3)
UKURAN = 3

# Matrix C disiapkan secara global agar bisa diisi oleh berbagai thread
C = [[0] * UKURAN for _ in range(UKURAN)]

def hitung_baris(i, matrix_a, matrix_b):
    for j in range(UKURAN):
        for k in range(UKURAN):
            C[i][j] += matrix_a[i][k] * matrix_b[k][j]

if __name__ == '__main__':
    # Matrix A dan B
    A = [[1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9]]
         
    B = [[9, 8, 7], 
         [6, 5, 4], 
         [3, 2, 1]]

    daftar_thread = []
    
    print("Memulai komputasi multithreading...")
    start_time = time.time()

    for i in range(UKURAN):
        t = threading.Thread(target=hitung_baris, args=(i, A, B))
        daftar_thread.append(t)
        t.start()

    for t in daftar_thread:
        t.join()

    end_time = time.time()

    print("\nHasil Perkalian Matrix (Threading):")
    for baris in C:
        print(baris)
        
    print(f"\nWaktu eksekusi: {end_time - start_time:.5f} detik")