s = input('Enter a string: ')

print("Choose a transformation:")
print("1. Convert to uppercase")
print("2. Replace vowels with \'*\'")
print("3. Reverse the string")
print("4. Append \'EVEN\' or \'ODD\'")

choice = input('Enter your choice: ')

match choice:
    case "1":
        s = s.upper()
    case "2":
        temp = ''
        for i in s:
            if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u':
                temp += '*'
            else:
                temp += i
        s = temp
    case "3":
        temp = ''
        for i in reversed(s):
            temp += i
        s = temp
    case "4":
        if len(s) % 2 == 0:
            s = s + "EVEN"
        else:
            s = s + "ODD"
    case _:
        print("Invalid choice. No transformation applied.")
        
print(f"Transformed string: {s}")
print("Transformation complete. Goodbye!")