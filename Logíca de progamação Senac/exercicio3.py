def situacao_aluno(nota_a,nota_b,nota_c):
    media = (nota_a + nota_b + nota_c) /3
if  media >= 6:
    situacao = "aprovado"
elif media >=4:
    situacao = "recuperacao"
else:
    situacao = "reprovado"
    print(f""media: {media},situacao:{situacao}")
situacao_aluno(8,6,7)
situacao_aluno(5,6,4)
situacao_aluno(4,2,3)