"""
    Crie uma lista de questões com 5 perguntas e 4 respostas cada.
    Cada pergunta deve ter uma resposta correta.
    Cada resposta correta valerá 1 ponto.
    A lista deve ser sobre capitais do mundo.
    A resposta deve ser a letra correspondente a opção correta.
"""

questions = [
    {
        "question": "Qual é a capital da França?",
        "options": ["A) Londres", "B) Paris", "C) Berlim", "D) Roma"],
        "answer": "B"
    },
    {
        "question": "Qual é a capital do Brasil?",
        "options": ["A) Brasília", "B) São Paulo", "C) Rio de Janeiro", "D) Salvador"],
        "answer": "A"
    },
    {
        "question": "Qual é a capital da Espanha?",
        "options": ["A) Lisboa", "B) Madrid", "C) Barcelona", "D) Sevilha"],
        "answer": "B"
    },
    {
        "question": "Qual é a capital da Argentina?",
        "options": ["A) Buenos Aires", "B) Santiago", "C) Lima", "D) Montevidéu"],
        "answer": "A"
    },
    {
        "question": "Qual é a capital do Canadá?",
        "options": ["A) Toronto", "B) Montreal", "C) Vancouver", "D) Ottawa"],
        "answer": "D"
    }
]

""" escreva uma função que retorne as respostas do usuário e sua pontuação final."""

def quiz(questions):
    user_score = 0
    user_answers = []
    
    for question in questions:
        while True:
            user_answer = input(question["question"] + " " + str(question["options"]) + " ")
            if user_answer.upper() not in ["A", "B", "C", "D"]:
                print("Resposta inválida. Tente novamente.")
            else:
                break
        
        """ Caso a resposta não estives entre as opções, retorne um erro.
        Caso a respost estiver em minusculo troque para maiusculo. Caso a resposta estiver correta,
        some 1 ponto ao usuário."""

        if user_answer.islower():
            user_answer = user_answer.upper()
        if user_answer == question["answer"]:
            user_score += 1

    return user_score

def main():
    user_score = quiz(questions)

    print("Pontuação final: ", user_score)

    """ adicione um feedback ao usuário com a sua pontuação final.
    por exemplo de 0 a 3 acertos: "Você é burro. 4 acertos "OK. 5 acertos "Você é inteligente." """

    if user_score <= 3:
        print("Você é burro.")
    elif user_score == 4:
        print("Ok.")
    else:
        print("Você é inteligente.")
        

if __name__ == "__main__":
    main()