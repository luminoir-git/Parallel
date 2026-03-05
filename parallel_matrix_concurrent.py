import concurrent.futures
import time

# Fungsi yang mewakili isi dari loop terdalam pada C (menghitung 1 baris matrix)
def hitung_baris(i, matrix_a, matrix_b):
    ukuran = len(matrix_a)
    baris_hasil = [0] * ukuran
    
    for j in range(ukuran):
        for k in range(ukuran):
            baris_hasil[j] += matrix_a[i][k] * matrix_b[k][j]
            
    return i, baris_hasil

if __name__ == '__main__':
    # Matrix A dan B (Ukuran 3x3)
    A = [[1, 2, 3], 
         [4, 5, 6], 
         [7, 8, 9]]
         
    B = [[9, 8, 7], 
         [6, 5, 4], 
         [3, 2, 1]]
         
    ukuran = len(A)
    # Menyiapkan matrix kosong untuk hasil (Matrix C)
    C = [[0] * ukuran for _ in range(ukuran)]

    print("Memulai komputasi paralel...")
    start_time = time.time()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(hitung_baris, i, A, B) for i in range(ukuran)]
        
        for future in concurrent.futures.as_completed(futures):
            indeks_baris, hasil_baris = future.result()
            C[indeks_baris] = hasil_baris

    end_time = time.time()

    print("\nHasil Perkalian Matrix:")
    for baris in C:
        print(baris)

    print(f"\nWaktu eksekusi: {end_time - start_time:.5f} detik")
