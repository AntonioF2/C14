"""
Interface Streamlit para o Conversor de Medidas.
"""
import streamlit as st
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


def main():
    """Função principal da aplicação Streamlit."""
    st.set_page_config(page_title="Conversor de Medidas", layout="centered")
    
    st.title("🔄 Conversor de Medidas")
    st.markdown("---")
    
    # Seletor de categoria
    categoria = st.selectbox(
        "Selecione a categoria:",
        ["Temperatura", "Comprimento", "Peso"]
    )
    
    st.markdown("---")
    
    if categoria == "Temperatura":
        st.subheader("🌡️ Conversor de Temperatura")
        
        tipoConversao = st.radio(
            "Escolha a conversão:",
            [
                "Celsius ↔ Fahrenheit",
                "Celsius ↔ Kelvin",
            ]
        )
        
        if tipoConversao == "Celsius ↔ Fahrenheit":
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Celsius para Fahrenheit**")
                celsius = st.number_input(
                    "Digite a temperatura em Celsius",
                    value=0.0,
                    key="c_to_f"
                )
                if st.button("Converter", key="btn_c_to_f"):
                    try:
                        resultado = celsiusParaFahrenheit(celsius)
                        st.success(f"{celsius}°C = {resultado:.2f}°F")
                    except (ValueError, TypeError) as e:
                        st.error(f"Erro: {e}")
            
            with col2:
                st.write("**Fahrenheit para Celsius**")
                fahrenheit = st.number_input(
                    "Digite a temperatura em Fahrenheit",
                    value=32.0,
                    key="f_to_c"
                )
                if st.button("Converter", key="btn_f_to_c"):
                    try:
                        resultado = fahrenheitParaCelsius(fahrenheit)
                        st.success(f"{fahrenheit}°F = {resultado:.2f}°C")
                    except (ValueError, TypeError) as e:
                        st.error(f"Erro: {e}")
        
        else:  # Celsius ↔ Kelvin
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Celsius para Kelvin**")
                celsius = st.number_input(
                    "Digite a temperatura em Celsius",
                    value=0.0,
                    key="c_to_k"
                )
                if st.button("Converter", key="btn_c_to_k"):
                    try:
                        resultado = celsiusParaKelvin(celsius)
                        st.success(f"{celsius}°C = {resultado:.2f}K")
                    except (ValueError, TypeError) as e:
                        st.error(f"Erro: {e}")
            
            with col2:
                st.write("**Kelvin para Celsius**")
                kelvin = st.number_input(
                    "Digite a temperatura em Kelvin",
                    value=273.15,
                    key="k_to_c"
                )
                if st.button("Converter", key="btn_k_to_c"):
                    try:
                        resultado = kelvinParaCelsius(kelvin)
                        st.success(f"{kelvin}K = {resultado:.2f}°C")
                    except (ValueError, TypeError) as e:
                        st.error(f"Erro: {e}")
    
    elif categoria == "Comprimento":
        st.subheader("📏 Conversor de Comprimento")
        
        tipoConversao = st.radio(
            "Escolha a conversão:",
            [
                "Metros ↔ Pés",
                "Quilômetros ↔ Milhas",
            ]
        )
        
        if tipoConversao == "Metros ↔ Pés":
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Metros para Pés**")
                metros = st.number_input(
                    "Digite o comprimento em metros",
                    value=0.0,
                    key="m_to_ft"
                )
                if st.button("Converter", key="btn_m_to_ft"):
                    try:
                        resultado = metrosParaPes(metros)
                        st.success(f"{metros}m = {resultado:.2f} pés")
                    except (ValueError, TypeError) as e:
                        st.error(f"Erro: {e}")
            
            with col2:
                st.write("**Pés para Metros**")
                pes = st.number_input(
                    "Digite o comprimento em pés",
                    value=0.0,
                    key="ft_to_m"
                )
                if st.button("Converter", key="btn_ft_to_m"):
                    try:
                        resultado = pesParaMetros(pes)
                        st.success(f"{pes} pés = {resultado:.2f}m")
                    except (ValueError, TypeError) as e:
                        st.error(f"Erro: {e}")
        
        else:  # Quilômetros ↔ Milhas
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Quilômetros para Milhas**")
                km = st.number_input(
                    "Digite a distância em quilômetros",
                    value=0.0,
                    key="km_to_mi"
                )
                if st.button("Converter", key="btn_km_to_mi"):
                    try:
                        resultado = quilometrosParaMilhas(km)
                        st.success(f"{km}km = {resultado:.2f} milhas")
                    except (ValueError, TypeError) as e:
                        st.error(f"Erro: {e}")
            
            with col2:
                st.write("**Milhas para Quilômetros**")
                milhas = st.number_input(
                    "Digite a distância em milhas",
                    value=0.0,
                    key="mi_to_km"
                )
                if st.button("Converter", key="btn_mi_to_km"):
                    try:
                        resultado = milhasParaQuilometros(milhas)
                        st.success(f"{milhas} milhas = {resultado:.2f}km")
                    except (ValueError, TypeError) as e:
                        st.error(f"Erro: {e}")
    
    elif categoria == "Peso":
        st.subheader("⚖️ Conversor de Peso")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Quilogramas para Libras**")
            kg = st.number_input(
                "Digite o peso em quilogramas",
                value=0.0,
                key="kg_to_lb"
            )
            if st.button("Converter", key="btn_kg_to_lb"):
                try:
                    resultado = quilogramasParaLibras(kg)
                    st.success(f"{kg}kg = {resultado:.2f} lb")
                except (ValueError, TypeError) as e:
                    st.error(f"Erro: {e}")
        
        with col2:
            st.write("**Libras para Quilogramas**")
            libras = st.number_input(
                "Digite o peso em libras",
                value=0.0,
                key="lb_to_kg"
            )
            if st.button("Converter", key="btn_lb_to_kg"):
                try:
                    resultado = librasParaQuilogramas(libras)
                    st.success(f"{libras}lb = {resultado:.2f}kg")
                except (ValueError, TypeError) as e:
                    st.error(f"Erro: {e}")


if __name__ == "__main__":
    main()
