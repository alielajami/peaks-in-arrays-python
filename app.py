''' Peaks in arrays application '''

array_size = int(input("Enter the size of the array: "))
integers_array = []

for i in range(array_size):
    integers_array.append(int(input(f"Enter the integer {i + 1}: ")))

def find_peaks(array):
    ''' Function to find peaks in an array '''
    peaks = []
    for j in range(1, len(array) - 1):
        if array[j] > array[j - 1] and array[i] > array[j + 1]:
            peaks.append(array[j])
    return peaks

print(f"There are {len(find_peaks(integers_array))} peaks in the array.")
print(f"Peaks in the array: {find_peaks(integers_array)}")
