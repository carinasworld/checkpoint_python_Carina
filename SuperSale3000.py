# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 11:19:08 2021

@author: Carin
"""

jordan_belfort = {
    'calls' : 178,
    'meetings': 17,
    'sales': 6
    }

# Oppgave a
def get_score(dictionary):
    total_score = 0
    total_score += dictionary['calls']*10
    total_score += dictionary['meetings']*30
    total_score += dictionary['sales']*100
    return total_score

# Oppgave b
def get_score(dictionary):
    total_score = 0
    total_score += dictionary['calls']*10
    total_score += dictionary['meetings']*30
    total_score += dictionary['sales']*100
    
    if dictionary['calls'] > 150:
        total_score += 100
    if dictionary['meetings'] > 20:
        total_score += 100
    if dictionary['sales'] > 5:
        total_score += 100
    return total_score
    
        
get_score(jordan_belfort)


# Oppgave c
all_employees = {'jordan_belfort':{'calls': 178, 'meetings':17, 'sales':6    },'warren_buffett':{'calls': 137, 'meetings':28, 'sales':4    },'peter_lynch':{'calls': 128, 'meetings':14, 'sales':3    }}
    
for key, value in all_employees.items():  
    score = get_score(value)
    value['score'] = score
    all_employees[key]=(value)
    

            
    







