def custom_hash(input_string):
    hash_value = 0
    prime = 31
    
    for char in str(input_string):
        hash_value = hash_value * prime + ord(char)
        hash_value = hash_value % (2**32)
    
    return hex(hash_value)[2:].zfill(8)

# Test cases
print(custom_hash("Hello"))
print(custom_hash("hello"))
print(custom_hash("Hello!"))
print(custom_hash(""))
print(custom_hash("test") == custom_hash("test"))
