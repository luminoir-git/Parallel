import multiprocessing
import time

# Fungsi mengalikan satu baris Matrix A dengan seluruh Matrix B
def multiply_row(args):
    row_A, matrix_B = args
    result_row = []
    # Iterasi dari setiap kolom di Matrix B
    for col_B in range(len(matrix_B[0])):
        sum_val = 0
        # Elemen baris A * kolom B
        for i in range(len(row_A)):
            sum_val += row_A[i] * matrix_B[i][col_B]
        result_row.append(sum_val)
    return result_row

if __name__ == '__main__':
    # Matrix A (3x3)
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

    # Matrix B (3x3)
    B = [[9, 8, 7],
         [6, 5, 4],
         [3, 2, 1]]

    args = [(row, B) for row in A]

    start_time = time.time()
    
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        result_matrix = pool.map(multiply_row, args)
        
    end_time = time.time()

    print("Hasil Perkalian Matrix:")
    for row in result_matrix:
        print(row)
        
    print(f"\nWaktu eksekusi paralel: {end_time - start_time:.5f} detik")