#G-TASK (PYTHON)
#Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
#MASALAN: get_highest_index([5, 21, 12, 21, 8]) return qiladi 1 sonini.

def get_highest_index(arr):
    if not arr:
        return None
    max_value = max(arr)
    return arr.index(max_value)

print(get_highest_index([5, 21, 12, 21, 8]))