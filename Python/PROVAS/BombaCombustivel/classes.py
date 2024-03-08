class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel
    
    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos <= self.quantidade_combustivel:
            self.quantidade_combustivel -= litros_abastecidos
            return f"Abastecimento realizado com sucesso. Foram abastecidos {litros_abastecidos:.2f} litros de {self.tipo_combustivel}."
        else:
            return "Quantidade de combustível insuficiente na bomba."
    
    def abastecer_por_litro(self, litros):
        valor_a_pagar = litros * self.valor_litro
        return f"O valor a ser pago é R${valor_a_pagar:.2f}."
    
    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
        return f"Valor do litro de {self.tipo_combustivel} alterado para R${novo_valor:.2f}."

    def alterar_combustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel
        return f"Tipo de combustível alterado para {novo_tipo_combustivel}."

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade
        return f"Quantidade de combustível na bomba atualizada para {nova_quantidade} litros."
