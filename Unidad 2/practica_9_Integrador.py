from abc import ABC, abstractmethod
 
# ========== ABSTRACCIÓN ===========
# Clase abstracta: define qué DEBE tener todo empleado
class Empleado(ABC):
    def __init__(self, nombre, id_empleado):
        self.nombre      = nombre
        self.id_empleado = id_empleado
        self.__activo    = True       # ENCAPSULAMIENTO: privado
 
    # ENCAPSULAMIENTO: getter para el estado
    @property
    def activo(self):
        return self.__activo
 
    def desactivar(self):
        self.__activo = False
 
    # ABSTRACCIÓN: método que cada tipo debe implementar
    @abstractmethod
    def calcular_salario(self):
        pass
 
    @abstractmethod
    def tipo_empleado(self):
        pass
 
    def __str__(self):
        estado = 'Activo' if self.__activo else 'Inactivo'
        return (f'[{self.tipo_empleado()}] {self.nombre} '
                f'(ID: {self.id_empleado}) - {estado}')
 
# ========== HERENCIA ===========
# EmpleadoFijo hereda de Empleado
class EmpleadoFijo(Empleado):
    def __init__(self, nombre, id_empleado, salario_base):
        super().__init__(nombre, id_empleado)
        self._salario_base = salario_base   # ENCAPSULAMIENTO: protegido
 
    def tipo_empleado(self):
        return 'Fijo'
 
    def calcular_salario(self):             # POLIMORFISMO
        return self._salario_base
 
# EmpleadoConBono hereda de EmpleadoFijo
class EmpleadoConBono(EmpleadoFijo):
    def __init__(self, nombre, id_empleado, salario_base, bono):
        super().__init__(nombre, id_empleado, salario_base)
        self.__bono = bono
 
    def tipo_empleado(self):
        return 'Con Bono'
 
    def calcular_salario(self):             # POLIMORFISMO: sobreescribe
        return self._salario_base + self.__bono
 
class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, id_empleado, tarifa_hora):
        super().__init__(nombre, id_empleado)
        self.__tarifa = tarifa_hora
        self.__horas  = 0
 
    def registrar_horas(self, horas):
        self.__horas += horas
 
    def tipo_empleado(self):
        return 'Por Horas'
 
    def calcular_salario(self):             # POLIMORFISMO: implementación propia
        return self.__tarifa * self.__horas
 
# ========== SISTEMA DE EMPRESA ===========
class Empresa:
    def __init__(self, nombre):
        self.nombre     = nombre
        self.__empleados = []
 
    def contratar(self, empleado):
        self.__empleados.append(empleado)
        print(f'Contratado: {empleado.nombre}')
 
    def calcular_nomina(self):
        print(f'\n=== Nómina de {self.nombre} ===')
        total = 0
        for emp in self.__empleados:
            if emp.activo:
                salario = emp.calcular_salario()  # POLIMORFISMO en acción
                print(f'  {emp.nombre}: ${salario:,.2f}')
                total += salario
        print(f'  TOTAL: ${total:,.2f}')
 
# --- Usando el sistema ---
empresa = Empresa('Tech Solutions')
 
emp1 = EmpleadoFijo('Ana García', 'E001', 50000)
emp2 = EmpleadoConBono('Luis Pérez', 'E002', 45000, 8000)
emp3 = EmpleadoPorHoras('María Torres', 'E003', 150)
emp3.registrar_horas(160)         # 160 horas al mes
 
empresa.contratar(emp1)
empresa.contratar(emp2)
empresa.contratar(emp3)
 
empresa.calcular_nomina()
print(emp1)

# === Nómina de Tech Solutions ===
#   Ana García:   $50,000.00
#   Luis Pérez:   $53,000.00
#   María Torres: $24,000.00
#   TOTAL:        $127,000.00
