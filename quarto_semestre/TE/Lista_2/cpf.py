import re

def validarCPF(cpf):
  total = 0
  index = 10

  for n in cpf:
    if(index > 1): 
      total += int(n) * index 
      index -= 1

  # reset
  total = 0
  index = 11

  digito1 = total * 10 % 11

  for n in cpf:
    if(index > 1): 
      total += int(n) * index 
      index -= 1

  digito2 = total * 10 % 11

  if (cpf[9] + cpf[10] == str(digito1) + str(digito2)): 
    print("CPF Válido")
  else: 
    print("CPF Inválido")


validarCPF(re.sub('(\.|-)', '', input("Insira o CPF que será validado: ")))