🌡️ Conversor de Medidas - Projeto CI/CD
Aplicação de conversão de medidas (temperatura, comprimento e peso) desenvolvida com Streamlit. Este projeto foi estruturado para demonstrar um pipeline completo de Integração e Entrega Contínua (CI/CD), utilizando Docker, GitHub Actions e Deploy automatizado.

🚀 Tecnologias Utilizadas
Linguagem: Python 3.11+

Interface: Streamlit

Testes: Pytest

Containerização: Docker & Docker Hub

Pipeline: GitHub Actions

Hospedagem: Railway

🛠️ Pipeline de CI/CD (GitHub Actions)
O projeto conta com um Pipeline Unificado (pipeline.yml) que garante a qualidade do código antes de qualquer publicação. O fluxo consiste em:

Job de Testes: Executa 20 testes unitários (10 de fluxo normal e 10 de exceção).

Job de Build (Paralelo): Realiza o empacotamento da aplicação em um container Docker e faz o push para o Docker Hub. Também gera Artifacts (o pacote .zip da app e o relatório de testes).

Job de Deploy: Realiza o deploy automático no Railway apenas se os jobs de Teste e Build passarem com sucesso (Branch main).

Job de Notificação: Executa um script Python (enviar_notificacao.py) que consome variáveis de ambiente (Secrets) para informar o status final da operação.

📊 Cobertura de Testes (20 Cenários)
O projeto mantém 100% de sucesso nos testes validados via Pytest:

✅ Fluxo Normal
Conversões de Temperatura (C/F/K), Comprimento (m/pés, km/milhas) e Peso (kg/lb).

❌ Fluxo de Exceção (Robustez)
Tratamento de tipos inválidos (Strings, Booleanos, None).

Validação de limites físicos (Zero absoluto, medidas negativas de distância/peso).

🤖 Uso de Inteligência Artificial
Conforme as diretrizes da disciplina, declaramos que este projeto contou com o auxílio de IA (Gemini/ChatGPT) para as seguintes atividades:

Unificação de Workflows: Consolidação de múltiplos arquivos YAML em um único pipeline com execução paralela.

Troubleshooting de DevOps: Resolução de erros de Pathing de importação no ambiente do GitHub Actions (ModuleNotFoundError) e configuração de Secrets.

Scripts de Apoio: Estruturação do script de notificação via e-mail consumindo variáveis de ambiente.

Resultado: O auxílio foi satisfatório, permitindo a implementação de boas práticas de infraestrutura que não seriam alcançadas apenas com o código base inicial.

⚙️ Como Executar Localmente
Instale as dependências:
pip install -r requirements.txt

Rode os testes:
python -m pytest tests/

Inicie a aplicação:
streamlit run app.py

⚙️ Link do Deploy:

c14-production.up.railway.app

👥 Equipe
Antônio Faria - 231
Matheus Gazzola - 2178
