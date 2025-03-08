def int_to_roman(num):
    roman_string= " "
    while num > 0 : 
        if num >= 1000 :
            roman_string += 'M'
            num -= 1000
        elif num >= 900 : 
            roman_string += 'CM'
            num -= 900 
        elif num >= 500 : 
            roman_string += 'D'
            num -= 500 
        elif num >= 400 :
            roman_string += 'CD'
            num -= 400 
        elif num >= 100 : 
            roman_string += 'C'
            num -= 100 
        elif num >= 90 : 
            roman_string += 'XC'
            num -= 90 
        elif num >= 50 : 
            roman_string  += 'L'
            num -= 50 
        elif num >= 40 :
            roman_string  += 'XL'
            num -= 40 
        elif num >= 10 : 
            roman_string += 'X'
            num -= 10 
        elif num >= 9 :
            roman_string += 'IX'
            num -= 9 
        elif num >= 5 : 
            roman_string += 'V'
            num -= 5 
        elif num >= 4 : 
            roman_string += 'IV'
            num -= 4 
        elif num >= 1 :
            roman_string += 'I'
            num -= 1 
    return roman_string


        
