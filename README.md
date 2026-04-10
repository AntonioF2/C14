# Conversor de Medidas

Aplicação simples de conversão de medidas (temperatura, comprimento e peso) com interface Streamlit. Projetada como base para pipeline de CI/CD com testes automatizados.


##  Como Executar

1. Clone o repositório (ou navegue até a pasta do projeto)

2. Instale as dependências:

pip install -r requirements.txt

### Executar a Aplicação

streamlit run app.py

A aplicação abrirá em `http://localhost:8501`

### Executar os Testes

pytest tests/

Para gerar relatório detalhado:

pytest tests/ -v --tb=short


## 📊 Cobertura de Testes

### Fluxo Normal (10 testes)
-  Celsius → Fahrenheit (inteiro)
-  Celsius → Fahrenheit (decimal)
-  Fahrenheit → Celsius (inteiro)
-  Metros → Pés (número inteiro)
-  Pés → Metros (número inteiro)
-  Quilômetros → Milhas (decimal)
-  Milhas → Quilômetros (inteiro)
-  Quilogramas → Libras (inteiro)
-  Celsius → Kelvin (inteiro)
-  Libras → Quilogramas (inteiro)

### Fluxo de Exceção (10 testes)
-  String passada como entrada (TypeError)
-  Booleano passado como entrada (TypeError)
-  Temperatura abaixo do zero absoluto (ValueError)
-  Kelvin negativo (ValueError)
-  Metros negativo (ValueError)
-  String passada para quilômetros (TypeError)
-  Booleano passado para quilogramas (TypeError)
-  Peso negativo em libras (ValueError)
-  None passado para pés (TypeError)
-  Distância negativa em milhas (ValueError)



## Tecnologias Utilizadas

- **Python 3.8+**
- **Streamlit 1.28.1** - Framework web para data science
- **Pytest 7.4.3** - Framework de testes

## 👥 Desenvolvido por

Aluno: Antônio Faria
matricula: 231