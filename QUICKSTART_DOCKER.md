# 🚀 Quick Start Docker

## ⚡ Teste Rápido (2 minutos)

### 1. Build e Run com Docker Compose
```bash
docker-compose up -d
```
Aplicação em: http://localhost:8501

### 2. Parar
```bash
docker-compose down
```

---

## 📦 Build Manual

```bash
# Build
docker build -t conversor-medidas:latest .

# Run
docker run -p 8501:8501 conversor-medidas:latest
```

---

## 🎯 Usando Makefile

```bash
# Ver todos os comandos
make help

# Executar tudo (testes + build)
make all

# Rodar com Docker
make docker-run

# Parar Docker
make docker-stop
```

---

## ✅ Verificar se funciona

```bash
# Em outro terminal
curl http://localhost:8501
```

Se retornar HTML, está funcionando! 🎉

---

## 🔧 Troubleshooting

**Porta ocupada?**
```bash
docker-compose down
docker container prune
```

**Rebuild?**
```bash
docker-compose up -d --build
```

---

## 📍 Próximos Passos

1. Configurar secrets no GitHub
2. Push para gerar imagem automática
3. Deploy no Railway/AWS/etc

Ver [DOCKER_DEPLOY.md](DOCKER_DEPLOY.md) para detalhes.
