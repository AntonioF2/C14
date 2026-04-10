.PHONY: help install test run docker-build docker-run docker-stop clean lint

help:
	@echo "Conversor de Medidas - Comandos Disponíveis"
	@echo "==========================================="
	@echo "  make install       - Instala dependências"
	@echo "  make test          - Executa testes"
	@echo "  make run           - Executa app localmente"
	@echo "  make docker-build  - Faz build da imagem Docker"
	@echo "  make docker-run    - Executa container Docker"
	@echo "  make docker-stop   - Para container Docker"
	@echo "  make docker-compose - Executa com docker-compose"
	@echo "  make clean         - Remove arquivos temporários"
	@echo "  make lint          - Verifica qualidade do código"

install:
	pip install -r requirements.txt

test:
	pytest tests/ -v --tb=short

test-coverage:
	pytest tests/ --cov=. --cov-report=html --cov-report=term

run:
	streamlit run app.py

docker-build:
	docker build -t conversor-medidas:latest .

docker-run: docker-build
	docker run -p 8501:8501 conversor-medidas:latest

docker-stop:
	docker stop $$(docker ps -q --filter "ancestor=conversor-medidas:latest") 2>/dev/null || true

docker-compose:
	docker-compose up -d

docker-compose-down:
	docker-compose down

clean:
	find . -type d -name __pycache__ -exec rm -r {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -r {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	rm -rf htmlcov/
	rm -rf .coverage

lint:
	python -m py_compile converter.py app.py tests/test_converter.py

all: clean install test docker-build
