# 🚀 Portfólio Flask

Site de portfólio pessoal feito com Python + Flask.

## Estrutura

```
portfolio/
├── app.py                  ← Dados e rotas (edite aqui!)
├── requirements.txt
├── templates/
│   └── index.html          ← Template HTML
└── static/
    ├── css/style.css       ← Estilos
    └── js/main.js          ← Interações
```

## ▶️ Como rodar

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Rode o servidor:**
   ```bash
   python app.py
   ```

3. **Acesse no navegador:**
   ```
   http://localhost:5000
   ```

## ✏️ Como personalizar

Abra o arquivo `app.py` e edite as variáveis no topo:

- `PROFILE` → seu nome, título, bio, links, localização
- `PROJECTS` → seus projetos com descrição e tags
- `EXPERIENCE` → sua experiência profissional

## 🌍 Deploy (Render.com — gratuito)

1. Crie uma conta em [render.com](https://render.com)
2. Conecte seu repositório GitHub
3. Configure:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `gunicorn app:app`
4. Adicione `gunicorn` ao `requirements.txt`
