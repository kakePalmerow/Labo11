cuenta1 = {"Titular": "Andres", "Saldo": 100}
cuenta2 = {"Titular": "Andres", "Saldo": 100}

def depositar(cuenta, monto):
    if monto > 0:
        cuenta["Saldo"] = cuenta["Saldo"] + monto
        return True
    else:
        return False

print(depositar(cuenta1, 100)) #True
print(f"el saldo de la cuenta 1 es:{cuenta1['Saldo']}") #200

print(depositar(cuenta2, -100)) # False
print(f"el saldo de la cuenta 2 es:{cuenta2['Saldo']}") #100