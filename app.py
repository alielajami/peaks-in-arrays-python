''' Peaks in arrays application '''

array_size = int(input("Enter the size of the array: ")) # Size of the array
integers_array = [] # Array to store integers

for i in range(array_size): # Loop to get integers from user
    integers_array.append(int(input(f"Enter the integer {i + 1}: "))) # Append integers to the array

def find_peaks(array):
    ''' Function to find peaks in an array '''
    peaks = [] # List to store peaks
    for j in range(1, len(array) - 1): # Loop to find peaks
        if array[j] > array[j - 1] and array[j] > array[j + 1]: # Check if the element is greater than its neighbours
            peaks.append(array[j]) # Append the element to the peaks list
    return peaks # Return the peaks list

print(f"There are {len(find_peaks(integers_array))} peaks in the array.")
print(f"Peaks in the array: {find_peaks(integers_array)}")
