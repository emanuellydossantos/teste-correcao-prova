print('Utilize apenas letras maiúsculas para colocar a resposta correta e do aluno')
print('Para finalizar o programa, em "Nome do(a) aluno(a)" aperte "ENTER" sem escrever')
print()
resposta1 = input ('Resposta correta da 1: ')
resposta2 = input ('Resposta correta da 2: ')
resposta3 = input ('Resposta correta da 3: ')
resposta4 = input ('Resposta correta da 4: ')
resposta5 = input ('Resposta correta da 5: ')
resultado = 0
print()
print()
nome = input('Nome do(a) aluno(a): ')

while (nome != ''):
    q1 = input('Questão 1: ')
    q2 = input('Questão 2: ')
    q3 = input('Questão 3: ')
    q4 = input('Questão 4: ')
    q5 = input('Questão 5: ')

    if (q1 == resposta1):
        resultado += 2
    if (q2 == resposta2):
        resultado += 2
    if (q3 == resposta3):
        resultado += 2
    if (q4 == resposta4):
        resultado += 2
    if (q5 == resposta5):
        resultado += 2
    print()
    print (resultado)
    if resultado >= 6:
        print ('Aprovado')
    if resultado == 4:
        print ('Recuperação')
    if resultado < 4:
        print ('Reprovado')
    print()
    resultado = 0
    nome = input('Nome do(a) aluno(a): ')
print ('Programa finalizado com sucesso!')
