print(f'{" LOJAS GUANABARA ":=^40}')
preço = float(input('Preço das compras: R$'))
print('''ESCOLHA A FORMA DE PAGAMENTO:
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Digite a forma de pagamento: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f} SEM JUROS')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    total_parcela = int(input('Quantas parcelas: '))
    parcela = total / total_parcela
    print(f'Sua compra será parcelada em {total_parcela}x de R${parcela:.2f} COM JUROS')
else: 
    total = preço
    print('Opção Inválida')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final.')