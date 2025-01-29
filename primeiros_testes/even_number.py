""" crie uma função que receba um número e retorne True se ele for par ou False se for ímpar. 
Caso não seja um número, retorne um erro. Caso também não seja um número inteiro
retorne um erro. Caso o número seja negativo, retorne um erro. 
""" 

def even_number(number):
    if type(number) != int:
        raise TypeError("O valor inserido não é um número inteiro.")
    elif number < 0:    
        raise ValueError("O valor inserido é negativo.")

        "Caso o número seja 0, retorne um erro."
    elif number == 0:
        raise ValueError("O valor inserido é 0.")
        
    elif number % 2 == 0:
        return True
    else:
        return False
    
    def is_prime(number):
        if not isinstance(number, int):
            raise TypeError("O valor inserido não é um número inteiro.")
        if number <= 0:
            raise ValueError("O valor inserido é negativo ou zero.")
        if number == 1:
            return False
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for i in range(3, int(number**0.5) + 1, 2):
            if number % i == 0:
                return False
        return True

