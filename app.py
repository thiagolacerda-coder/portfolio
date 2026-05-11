from flask import Flask, render_template, jsonify

app = Flask(__name__)

# ── Dados do portfólio ──! ──────────────────────────────────────
PROFILE = {
    "name": "Thiago Lacerda",
    "title": "Estudante de ADS & Futuro Dev",
    "tagline": "Apaixonado por tecnologia, dados e soluções que fazem diferença.",
    "about": (
        "Sou estudante de Análise e Desenvolvimento de Sistemas na UNIPE (João Pessoa/PB), "
        "com certificação em Engenharia de Dados e Machine Learning. "
        "Tenho experiência profissional em atendimento consultivo e vendas, onde desenvolvi "
        "habilidades de comunicação, negociação e foco em resultados. "
        "Hoje canalizo essa energia para a tecnologia, buscando minha primeira oportunidade na área de TI."
    ),
    "email": "thiagolacerdalan@gmail.com",
    "phone": "(83) 98718-6070",
    "github": "https://github.com/thiagolacerda-coder",
    "linkedin": "https://linkedin.com/in/thiagolacerdadev/",
    "location": "João Pessoa, PB — Brasil",
}


PROJECTS = [
    {
        "title": "Portfólio Pessoal",
        "description": "Este site! Desenvolvido com Python e Flask, com design responsivo, animações CSS e dados dinâmicos servidos pelo backend.",
        "tags": ["Python", "Flask", "HTML", "CSS"],
        "link": "#",
        "emoji": "🌐",
    },
    {
        "title": "Sistema de I.A Generativa",
        "description": "Projeto desenvolvido em Python que gera dados fictícios de clientes bancários, expõe esses dados via API REST local e utiliza IA generativa para criar mensagens personalizadas de marketing financeiro para cada usuário.",
        "tags": ["Python", "Pandas", "FastAPI"],
        "link": "https://github.com/thiagolacerda-coder/sistema-ia-generativa",
        "emoji": "🤖",
    },
    {
        "title": "Dash de Análise de Dados",
        "description": "Este projeto consiste na criação de um Dashboard interativo no Microsoft Excel com foco na análise de assinaturas do Xbox Game Pass.",
        "tags": ["Excel"],
        "link": "https://github.com/thiagolacerda-coder/Dashboard_Vendas_Xbox-",
        "emoji": "🔄",
    },
    {
        "title": "Sistema Bancário em Python",
        "description": "Sistema bancário simples desenvolvido em Python como parte dos estudos na trilha de desenvolvimento. O projeto simula operações bancárias básicas como depósito, saque e extrato, com validações e regras de negócio reais.",
        "tags": ["Python"],
        "link": "https://github.com/thiagolacerda-coder/sistema-bancario-python",
        "emoji": "🤖",
    },
]

EXPERIENCE = [
    {
        "role": "Consultor de Televendas",
        "company": "Positivo Brasil",
        "period": "Jul 2024 – Jan 2026",
        "desc": (
            "Atendimento ativo e consultivo a clientes com restrições financeiras via telefone e WhatsApp. "
            "Condução de negociações, contorno de objeções e fechamento de contratos. "
            "Atuação com metas comerciais, KPIs de conversão e premiação por desempenho."
        ),
    },
    {
        "role": "Operador de Atendimento (Nubank)",
        "company": "AeC Centro de Contatos S/A",
        "period": "Nov 2023 – Jul 2024",
        "desc": (
            "Suporte ao cliente via chat e e-mail para produtos financeiros do Nubank. "
            "Indicadores de qualidade (QA) e NPS consistentemente acima da meta. "
            "Trabalho em equipe em ambiente de alta demanda com foco em resolução."
        ),
    },
]

CERTIFICATES = [
    {
        "title": "Fundamentos de Engenharia de Dados e Machine Learning",
        "institution": "Digital Innovation One",
        "hours": "60h",
        "desc": "Python, Git/GitHub, Ciência de Dados, ETL, bancos de dados relacionais e análise com Excel + IA Copilot.",
    }
]
# ───────────────────────────────────────────────────────────────────────────


@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=PROFILE,
        projects=PROJECTS,
        experience=EXPERIENCE,
        certificates=CERTIFICATES,
    )


@app.route("/api/data")
def api_data():
    return jsonify({"profile": PROFILE, "projects": PROJECTS})


if __name__ == "__main__":
    app.run(debug=True)
