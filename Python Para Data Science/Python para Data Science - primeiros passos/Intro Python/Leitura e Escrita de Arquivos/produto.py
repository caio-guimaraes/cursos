class Produto(object): 
  def __init__(self, nome, valor): 
    self.__nome = nome 
    self.__valor = valor

  @property 
  def nome(self): 
    return self.__nome

  @nome.setter 
  def nome(self, nome): 
    self.__nome = nome

  @property
  def valor(self): 
    return self.__valor

  @valor.setter 
  def valor(self, valor): 
    self.__valor = valor 

  def __repr__(self): 
    return "nome: %s valor: %s" % (self.__nome, self.__valor)