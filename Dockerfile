# Base leve do Python
FROM python:3.11-slim

# Pasta central de operações dentro do container
WORKDIR /app

# Faz os logs/prints aparecerem imediatamente no terminal
ENV PYTHONUNBUFFERED=1

# Copia o código local para dentro do container
COPY src/ /app/src/

# Comando que dispara a execução da aplicação
CMD ["python", "src/main.py"]
