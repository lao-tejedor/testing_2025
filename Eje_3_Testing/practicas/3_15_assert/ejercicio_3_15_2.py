# ejercicio_3_15_2.py
"""
Completa la función calcular_imc usando ASSERT
Reglas:
- Peso debe ser > 0 y < 300 kg
- Altura debe ser > 0 y < 3 metros
- IMC debe ser un número positivo
"""

def calcular_imc(peso, altura):
    try:
        # TU CÓDIGO AQUÍ - Agrega asserts para validar peso y altura
        assert 0 < peso < 300, "El peso debe ser mayor que 0 y menor que 300 kg"
        assert 0 < altura < 3, "La altura debe ser mayor que 0 y menor que 3 metros"
        imc = peso / (altura ** 2)
    
        # TU CÓDIGO AQUÍ - Verifica que el IMC sea razonable
        assert imc > 0, "El IMC debe ser un número positivo"

        print(f"✅ IMC calculado: {imc:.2f}")
        return imc
    except AssertionError as e:
        print(f"Error de validacion: {e}")
    except Exception as e:
        print(f" Error inesperado: {e}")
        return None
# Pruebas:
if __name__ == "__main__":
    print("⚖️ Probando calculadora de IMC:")
    
    calcular_imc(70, 1.75)    # ✅ Debe funcionar
    calcular_imc(-5, 1.75)  # ❌ Debe fallar
    calcular_imc(70, 0)     # ❌ Debe fallar
