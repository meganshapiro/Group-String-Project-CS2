
    
def rightshift (x, text):
    
    pound = text [0:x] 
    pound = len(pound) * '#'
    
    print(pound)

    x = len(text) - x
    text = text [0:x]
    text = pound + text
    return text
    
y = rightshift(3, 'MEOWZERS') 
print(y)
    
    
