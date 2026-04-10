# 🐳 Guia Docker & Deploy

## 📦 Requisitos Docker

- Docker Desktop (Windows/Mac) ou Docker Engine (Linux)
- Docker Compose (opcional, geralmente incluso)

## 🚀 Executar Localmente com Docker

### Opção 1: Docker Compose (Recomendado)

```bash
docker-compose up -d
```

A aplicação estará disponível em: `http://localhost:8501`

Para parar:
```bash
docker-compose down
```

### Opção 2: Docker CLI Manual

```bash
# Build da imagem
docker build -t conversor-medidas:latest .

# Run do container
docker run -p 8501:8501 conversor-medidas:latest
```

## 🔄 CI/CD com GitHub Actions

O pipeline automático já está configurado em `.github/workflows/ci-cd-docker.yml`:

1. **Testes** - Executa 20 testes unitários
2. **Build Docker** - Constrói imagem e push em paralelo aos testes
3. **Notificação** - Envia status final

### Configurar Secrets no GitHub

Para fazer push da imagem no Docker Hub:

1. Vá para: **Settings → Secrets and variables → Actions**
2. Adicione:
   - `DOCKER_USERNAME` = seu usuário Docker Hub
   - `DOCKER_PASSWORD` = seu token Docker Hub

## ☁️ Opções de Deploy

### 1️⃣ **AWS ECR + ECS** (Produção)
```bash
# Push para ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <ECR_URI>
docker tag conversor-medidas:latest <ECR_URI>/conversor-medidas:latest
docker push <ECR_URI>/conversor-medidas:latest
```

### 2️⃣ **Railway.app** (Recomendado para estudantes)
```bash
# Conectar repositório GitHub diretamente
# Railway detecta Dockerfile automaticamente
```

### 3️⃣ **Docker Hub + Any Host**
```bash
# Push para Docker Hub
docker tag conversor-medidas:latest USERNAME/conversor-medidas:latest
docker push USERNAME/conversor-medidas:latest

# Em um servidor remoto:
docker pull USERNAME/conversor-medidas:latest
docker run -d -p 8501:8501 USERNAME/conversor-medidas:latest
```

### 4️⃣ **Heroku** (Legado, pago agora)
```bash
heroku container:push web
heroku container:release web
```

## 📊 Estrutura de Deployment

```
GitHub Repository
    ↓ (push)
GitHub Actions (CI/CD)
    ├── Testes (pytest)
    ├── Build Docker
    └── Push ECR/Docker Hub
         ↓
    Staging/Produção
    ├── AWS ECS
    ├── Railway
    └── DigitalOcean
```

## 🔍 Troubleshooting Docker

### Erro: "Port 8501 is in use"
```bash
# Linux/Mac
lsof -i :8501
kill -9 <PID>

# Windows
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# Ou mudar porta:
docker run -p 9000:8501 conversor-medidas:latest
```

### Logs do container
```bash
docker logs container_id
docker logs -f container_id  # Follow mode
```

### Limpar recursos
```bash
docker system prune -a
docker image prune
docker container prune
```

## ✅ Checklist de Deploy

- [ ] Testes passando localmente
- [ ] Docker image buildando sem erros
- [ ] Container rodando em `localhost:8501`
- [ ] Secrets configurados no GitHub
- [ ] Workflow CI/CD passando
- [ ] Imagem publicada no registry
- [ ] Deploy testado em staging
- [ ] Monitoramento configurado

## 📚 Referências

- Docker Docs: https://docs.docker.com/
- Streamlit Docker: https://discuss.streamlit.io/t/docker-deployment/5049
- GitHub Actions: https://docs.github.com/en/actions
- Railway.app: https://railway.app/docs
