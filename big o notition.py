def find_max(arr):
    """
    O(1) Auxiliary Space: استخدام متغير واحد فقط ثابت
    """
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


def get_squared_numbers(arr):
    """
    O(n) Auxiliary Space: إنشاء قائمة جديدة بحجم العناصر
    """
    squared_list = []
    for num in arr:
        squared_list.append(num ** 2)
    return squared_list


# تجربة التشغيل والطباعة
numbers = [10, 20, 30, 40, 50]

print("--- O(1) Constant Space ---")
print("Max value:", find_max(numbers))

print("\n--- O(n) Linear Space ---")
print("Squared list:", get_squared_numbers(numbers))
EOFcat << 'EOF' > "big o notition.py"
def find_max(arr):
    """
    O(1) Auxiliary Space: استخدام متغير واحد فقط ثابت
    """
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


def get_squared_numbers(arr):
    """
    O(n) Auxiliary Space: إنشاء قائمة جديدة بحجم العناصر
    """
    squared_list = []
    for num in arr:
        squared_list.append(num ** 2)
    return squared_list


# تجربة التشغيل والطباعة
numbers = [10, 20, 30, 40, 50]

print("--- O(1) Constant Space ---")
print("Max value:", find_max(numbers))

print("\n--- O(n) Linear Space ---")
print("Squared list:", get_squared_numbers(numbers))
