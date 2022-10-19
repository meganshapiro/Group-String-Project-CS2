'''
Created on Oct 17, 2022

@author: chidalgo24
'''

def rightcirc(x,text):   
        circ = text[-x:]
        text = text[:-x]
        text = circ + text
        
        return text

y = rightcirc(3, 'COMPUTER') 
print(y)
    

