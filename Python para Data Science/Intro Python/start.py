num_gastos = 3
gasto_total = 0

while (num_gastos > 0):
    valor_gasto = (input('Digite um valor: '))
    print(type(valor_gasto))
    valor_gasto = int(valor_gasto)
    gasto_total += valor_gasto
    num_gastos -= 1

print('Gasto total', gasto_total)
