"""
Testes unitários para o módulo converter.py.
Total de 20 testes: 10 para fluxo normal e 10 para fluxos inoportunos/exceções.
"""
import pytest
from converter import (
    celsiusParaFahrenheit,
    fahrenheitParaCelsius,
    celsiusParaKelvin,
    kelvinParaCelsius,
    metrosParaPes,
    pesParaMetros,
    quilometrosParaMilhas,
    milhasParaQuilometros,
    quilogramasParaLibras,
    librasParaQuilogramas,
)


# ============================================================================
# FLUXO NORMAL - 10 TESTES
# ============================================================================

def test_celsius_para_fahrenheit_normal():
    """Testa conversão normal de Celsius para Fahrenheit com número inteiro."""
    resultado = celsiusParaFahrenheit(0)
    assert resultado == 32.0


def test_celsius_para_fahrenheit_decimal():
    """Testa conversão de Celsius para Fahrenheit com número decimal."""
    resultado = celsiusParaFahrenheit(100)
    assert resultado == 212.0


def test_fahrenheit_para_celsius_normal():
    """Testa conversão normal de Fahrenheit para Celsius com número inteiro."""
    resultado = fahrenheitParaCelsius(32)
    assert resultado == 0.0


def test_metros_para_pes_normal():
    """Testa conversão de metros para pés com número inteiro."""
    resultado = metrosParaPes(1)
    assert abs(resultado - 3.28084) < 0.0001


def test_pes_para_metros_normal():
    """Testa conversão de pés para metros com número inteiro."""
    resultado = pesParaMetros(3.28084)
    assert abs(resultado - 1.0) < 0.0001


def test_quilometros_para_milhas_normal():
    """Testa conversão de quilômetros para milhas com número decimal."""
    resultado = quilometrosParaMilhas(1.0)
    assert abs(resultado - 0.621371) < 0.0001


def test_milhas_para_quilometros_normal():
    """Testa conversão de milhas para quilômetros com número inteiro."""
    resultado = milhasParaQuilometros(1)
    assert abs(resultado - 1.60934) < 0.0001


def test_quilogramas_para_libras_normal():
    """Testa conversão de quilogramas para libras com número inteiro."""
    resultado = quilogramasParaLibras(1)
    assert abs(resultado - 2.20462) < 0.0001


def test_celsius_para_kelvin_normal():
    """Testa conversão de Celsius para Kelvin com número inteiro."""
    resultado = celsiusParaKelvin(0)
    assert resultado == 273.15


def test_libras_para_quilogramas_normal():
    """Testa conversão de libras para quilogramas com número inteiro."""
    resultado = librasParaQuilogramas(2.20462)
    assert abs(resultado - 1.0) < 0.0001


# ============================================================================
# FLUXO INOPORTUNOS/EXCEÇÕES - 10 TESTES
# ============================================================================

def test_celsius_para_fahrenheit_string():
    """Testa se TypeError é levantado quando string é passada."""
    with pytest.raises(TypeError):
        celsiusParaFahrenheit("25")


def test_celsius_para_fahrenheit_booleano():
    """Testa se TypeError é levantado quando booleano é passado."""
    with pytest.raises(TypeError):
        celsiusParaFahrenheit(True)


def test_celsius_para_kelvin_abaixo_zero_absoluto():
    """Testa se ValueError é levantado para temperatura abaixo do zero absoluto."""
    with pytest.raises(ValueError):
        celsiusParaKelvin(-300)


def test_kelvin_para_celsius_negativo():
    """Testa se ValueError é levantado quando Kelvin negativo é passado."""
    with pytest.raises(ValueError):
        kelvinParaCelsius(-10)


def test_metros_para_pes_negativo():
    """Testa se ValueError é levantado para metros negativo."""
    with pytest.raises(ValueError):
        metrosParaPes(-5)


def test_quilometros_para_milhas_string():
    """Testa se TypeError é levantado quando string é passada para quilômetros."""
    with pytest.raises(TypeError):
        quilometrosParaMilhas("100")


def test_quilogramas_para_libras_booleano():
    """Testa se TypeError é levantado quando booleano é passado para quilogramas."""
    with pytest.raises(TypeError):
        quilogramasParaLibras(False)


def test_libras_para_quilogramas_negativo():
    """Testa se ValueError é levantado para peso negativo em libras."""
    with pytest.raises(ValueError):
        librasParaQuilogramas(-50)


def test_pes_para_metros_none():
    """Testa se TypeError é levantado quando None é passado para pés."""
    with pytest.raises(TypeError):
        pesParaMetros(None)


def test_milhas_para_quilometros_negativo():
    """Testa se ValueError é levantado para distância negativa em milhas."""
    with pytest.raises(ValueError):
        milhasParaQuilometros(-10)
