"""
Sisteminha de perguntas e respostas no python, utilizando dicionario em python

"""

print()
print('Digite apenas a letra que corresponde com a respotas exemplo : a, b, c ou d, e Digite enter')

perguntas = {
    'Pergunta1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {'a': '1', 'b': '2', 'c': '4', 'd': '5', },
        'resposta_certa': 'c',
    },
    'Pergunta2': {
        'pergunta': 'Quanto é 13 - 6?',
        'respostas': {'a': '7', 'b': '8', 'c': '4', 'd': '5', },
        'resposta_certa': 'a',
    },
    'Pergunta3': {
        'pergunta': 'Quanto é 5 * 5?',
        'respostas': {'a': '20', 'b': '25', 'c': '40', 'd': '10', },
        'resposta_certa': 'b',
    },
    'Pergunta4': {
        'pergunta': 'Quanto é 2 * 5?',
        'respostas': {'a': '7', 'b': '11', 'c': '9', 'd': '10', },
        'resposta_certa': 'd',
    },
    'Pergunta5': {
        'pergunta': 'Quanto é 3 * 5?',
        'respostas': {'a': '8', 'b': '11', 'c': '15', 'd': '10', },
        'resposta_certa': 'c',
    },
}

print()
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Resposta: ')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    respostas_usuario = input('Sua resposta é: ')

    if respostas_usuario == pv['resposta_certa']:
        print('Acertou miseravil')
        respostas_certas += 1
    else:
        print('Errou feio, errou rude')

    print()
quantidade_per = len(perguntas)
porcentagem_acerto = respostas_certas / quantidade_per * 100

if porcentagem_acerto >= 60:
    print('Parabens você atingiu a meta')
else:
    print('Você precisa estudar mais')

print(f'Voce acertou {respostas_certas} respostas')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%')
