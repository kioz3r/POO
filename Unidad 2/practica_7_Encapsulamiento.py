class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular   = titular           # Público
        self._banco    = 'Banco Nacional'  # Protegido
        self.__saldo   = saldo_inicial     # Privado
        self.__historial = []              # Privado
 
    # Getter: leer el saldo de forma controlada
    @property
    def saldo(self):
        return self.__saldo
 
    # Método público para depositar
    def depositar(self, monto):
        if monto <= 0:
            return 'El monto debe ser positivo.'
        self.__saldo += monto
        self.__historial.append(f'+ Depósito: ${monto}')
        return f'Depósito exitoso. Saldo: ${self.__saldo}'
 
    # Método público para retirar
    def retirar(self, monto):
        if monto <= 0:
            return 'El monto debe ser positivo.'
        if monto > self.__saldo:
            return 'Fondos insuficientes.'
        self.__saldo -= monto
        self.__historial.append(f'- Retiro: ${monto}')
        return f'Retiro exitoso. Saldo: ${self.__saldo}'
 
    # Ver historial (controlado)
    def ver_historial(self):
        print(f'Historial de {self.titular}:')
        for mov in self.__historial:
            print(f'  {mov}')
 
# --- Usando la clase ---
cuenta = CuentaBancaria('María López', 1000)
 
print(cuenta.saldo)              # 1000 (vía @property)
print(cuenta.depositar(1500))     # Depósito exitoso. Saldo: $1500
print(cuenta.retirar(200))       # Retiro exitoso. Saldo: $1300
print(cuenta.retirar(2000))      # Fondos insuficientes.
cuenta.ver_historial()
 
# ❌ Esto daría error (acceso privado bloqueado):
# print(cuenta.__saldo)          # AttributeError
