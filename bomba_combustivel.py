class BombaCombustivel:
  def __init__(self, tipo_combustivel:str, valor_litro: float, quantidade_combustivel: float):
    self.valor_litro = valor_litro
    self.tipo_combustivel = tipo_combustivel
    self.quantidade_combustivel = quantidade_combustivel

  def abastecer_por_valor(self, valor:float):
    litros_abastecidos = valor / self.valor_litro
    self._apresentar_abastecimento_se_possivel(litros_abastecidos, valor)

  def _apresentar_abastecimento_se_possivel(self, litros_abastecidos:float, valor:float):
    if litros_abastecidos > self.quantidade_combustivel:
      print(f'Não é possílve abastecer, faltam {litros_abastecidos - self.quantidade_combustivel:.2f} litros.')
      print('Reabasteça a bomba')
    else:
      self.quantidade_combustivel -= litros_abastecidos
      print(f'Foram abastecidos {litros_abastecidos:.2f} litros a um valor de R$ {valor:.2f}.')
      print(f'Sobraram na bomba {self.quantidade_combustivel:.2f} litros de {self.tipo_combustivel}.')

  def abastecer_por_litros(self, litros_abastecidos:float):
    valor =  litros_abastecidos * self.valor_litro
    self._apresentar_abastecimento_se_possivel(litros_abastecidos, valor)

  def adicionar_mais_combustivel(self, quantidade:float):
    if quantidade >= 0:
      self.quantidade_combustivel += quantidade
    else:
      print('Malandrinho, você não vai roubar combustível dessa bomba')


bomba = BombaCombustivel('Gasolina', 4.59, 100.0)

bomba.abastecer_por_valor(100)

bomba.abastecer_por_litros(50)

bomba.valor_litro = 5.59
bomba.abastecer_por_litros(50)

bomba.adicionar_mais_combustivel(100)
bomba.abastecer_por_litros(50)

bomba.adicionar_mais_combustivel(-100)