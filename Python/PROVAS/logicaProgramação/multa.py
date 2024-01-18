# Escreva um programa em python que pergunte ao usuário a velocidade de um carro. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado e o valor da multa, cobrando R$20,00 por cada km que exceder 80 km/h.


velocidadeUsuario = float(input('A qual a velocidade o veículo estava em km/h? '))

limiteVelocidade = 80
valor_multaKm = 20.0
excesso_velocidade = velocidadeUsuario - limiteVelocidade

if excesso_velocidade > 0:
    valor_multa_por_km = 20.0
    valor_multa = excesso_velocidade * valor_multa_por_km
    
    print(f"Você foi multado! Velocidade excedida: {velocidadeUsuario:.2f} km/h")
    print(f"Valor da multa: R${valor_multa:.2f}")
else:
    print(f"Velocidade dentro do limite: {velocidadeUsuario:.2f} km/h")