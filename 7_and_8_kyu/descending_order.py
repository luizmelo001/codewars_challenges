def Descending_Order(num):
    digits = []
    
    while num > 0:
        new_num = num // 10
        digits.append(num - new_num*10)
        num = new_num
        
    out = 0
    for i, digit in enumerate(sorted(digits)):
        out += digit * 10**i
        
    return out