def count_lower_upper():
    s = input("Enter the statement: ")
    result = {"Uppercase": 0, "Lowercase": 0}
    
    for ch in s:
        if ch.isupper():
            result["Uppercase"] += 1
        elif ch.islower():
            result["Lowercase"] += 1
    
    return result

print(count_lower_upper())
