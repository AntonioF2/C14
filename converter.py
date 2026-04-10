"""
Módulo de funções de conversão de medidas.
Contém lógica pura de conversão sem dependências externas.
"""


def celsiusParaFahrenheit(celsius):
    """Converte temperatura de Celsius para Fahrenheit.
    
    Args:
        celsius: Valor em Celsius (int ou float)
        
    Returns:
        float: Valor convertido em Fahrenheit
        
    Raises:
        ValueError: Se o valor não for um número válido
        TypeError: Se o valor for de tipo não suportado
    """
    if not isinstance(celsius, (int, float)) or isinstance(celsius, bool):
        raise TypeError(f"Esperado int ou float, recebido {type(celsius).__name__}")
    
    if celsius is None:
        raise ValueError("Valor não pode ser None")
    
    return (celsius * 9/5) + 32


def fahrenheitParaCelsius(fahrenheit):
    """Converte temperatura de Fahrenheit para Celsius.
    
    Args:
        fahrenheit: Valor em Fahrenheit (int ou float)
        
    Returns:
        float: Valor convertido em Celsius
        
    Raises:
        ValueError: Se o valor não for um número válido
        TypeError: Se o valor for de tipo não suportado
    """
    if not isinstance(fahrenheit, (int, float)) or isinstance(fahrenheit, bool):
        raise TypeError(f"Esperado int ou float, recebido {type(fahrenheit).__name__}")
    
    if fahrenheit is None:
        raise ValueError("Valor não pode ser None")
    
    return (fahrenheit - 32) * 5/9


def celsiusParaKelvin(celsius):
    """Converte temperatura de Celsius para Kelvin.
    
    Args:
        celsius: Valor em Celsius (int ou float)
        
    Returns:
        float: Valor convertido em Kelvin
        
    Raises:
        ValueError: Se o valor for muy negativo (abaixo de -273.15°C)
        TypeError: Se o valor for de tipo não suportado
    """
    if not isinstance(celsius, (int, float)) or isinstance(celsius, bool):
        raise TypeError(f"Esperado int ou float, recebido {type(celsius).__name__}")
    
    if celsius < -273.15:
        raise ValueError("Temperatura em Celsius não pode ser menor que -273.15K")
    
    return celsius + 273.15


def kelvinParaCelsius(kelvin):
    """Converte temperatura de Kelvin para Celsius.
    
    Args:
        kelvin: Valor em Kelvin (int ou float)
        
    Returns:
        float: Valor convertido em Celsius
        
    Raises:
        ValueError: Se o valor for negativo
        TypeError: Se o valor for de tipo não suportado
    """
    if not isinstance(kelvin, (int, float)) or isinstance(kelvin, bool):
        raise TypeError(f"Esperado int ou float, recebido {type(kelvin).__name__}")
    
    if kelvin < 0:
        raise ValueError("Temperatura em Kelvin não pode ser negativa")
    
    return kelvin - 273.15


def metrosParaPes(metros):
    """Converte comprimento de metros para pés.
    
    Args:
        metros: Valor em metros (int ou float)
        
    Returns:
        float: Valor convertido em pés
        
    Raises:
        ValueError: Se o valor for negativo
        TypeError: Se o valor for de tipo não suportado
    """
    if not isinstance(metros, (int, float)) or isinstance(metros, bool):
        raise TypeError(f"Esperado int ou float, recebido {type(metros).__name__}")
    
    if metros < 0:
        raise ValueError("Comprimento em metros não pode ser negativo")
    
    return metros * 3.28084


def pesParaMetros(pes):
    """Converte comprimento de pés para metros.
    
    Args:
        pes: Valor em pés (int ou float)
        
    Returns:
        float: Valor convertido em metros
        
    Raises:
        ValueError: Se o valor for negativo
        TypeError: Se o valor for de tipo não suportado
    """
    if not isinstance(pes, (int, float)) or isinstance(pes, bool):
        raise TypeError(f"Esperado int ou float, recebido {type(pes).__name__}")
    
    if pes < 0:
        raise ValueError("Comprimento em pés não pode ser negativo")
    
    return pes / 3.28084


def quilometrosParaMilhas(quilometros):
    """Converte distância de quilômetros para milhas.
    
    Args:
        quilometros: Valor em quilômetros (int ou float)
        
    Returns:
        float: Valor convertido em milhas
        
    Raises:
        ValueError: Se o valor for negativo
        TypeError: Se o valor for de tipo não suportado
    """
    if not isinstance(quilometros, (int, float)) or isinstance(quilometros, bool):
        raise TypeError(f"Esperado int ou float, recebido {type(quilometros).__name__}")
    
    if quilometros < 0:
        raise ValueError("Distância em quilômetros não pode ser negativa")
    
    return quilometros * 0.621371


def milhasParaQuilometros(milhas):
    """Converte distância de milhas para quilômetros.
    
    Args:
        milhas: Valor em milhas (int ou float)
        
    Returns:
        float: Valor convertido em quilômetros
        
    Raises:
        ValueError: Se o valor for negativo
        TypeError: Se o valor for de tipo não suportado
    """
    if not isinstance(milhas, (int, float)) or isinstance(milhas, bool):
        raise TypeError(f"Esperado int ou float, recebido {type(milhas).__name__}")
    
    if milhas < 0:
        raise ValueError("Distância em milhas não pode ser negativa")
    
    return milhas / 0.621371


def quilogramasParaLibras(quilogramas):
    """Converte peso de quilogramas para libras.
    
    Args:
        quilogramas: Valor em quilogramas (int ou float)
        
    Returns:
        float: Valor convertido em libras
        
    Raises:
        ValueError: Se o valor for negativo
        TypeError: Se o valor for de tipo não suportado
    """
    if not isinstance(quilogramas, (int, float)) or isinstance(quilogramas, bool):
        raise TypeError(f"Esperado int ou float, recebido {type(quilogramas).__name__}")
    
    if quilogramas < 0:
        raise ValueError("Peso em quilogramas não pode ser negativo")
    
    return quilogramas * 2.20462


def librasParaQuilogramas(libras):
    """Converte peso de libras para quilogramas.
    
    Args:
        libras: Valor em libras (int ou float)
        
    Returns:
        float: Valor convertido em quilogramas
        
    Raises:
        ValueError: Se o valor for negativo
        TypeError: Se o valor for de tipo não suportado
    """
    if not isinstance(libras, (int, float)) or isinstance(libras, bool):
        raise TypeError(f"Esperado int ou float, recebido {type(libras).__name__}")
    
    if libras < 0:
        raise ValueError("Peso em libras não pode ser negativo")
    
    return libras / 2.20462
