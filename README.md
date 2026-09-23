# Raízes do Brasil

## Descrição do Projeto

O Raízes do Brasil é uma plataforma digital desenvolvida com o objetivo de valorizar e divulgar o artesanato brasileiro.

O sistema funcionará como uma vitrine virtual para apresentação de artesãos e seus produtos, permitindo a organização dos itens por categorias e regiões do Brasil.

A proposta busca aumentar a visibilidade dos artesãos e facilitar o acesso do público aos produtos artesanais brasileiros.

---

## Tecnologias Utilizadas

- Python
- Django
- HTML
- CSS
- Bootstrap
- SQLite
- Git
- GitHub

---

## Equipe

- Ágatha Lopes — a definir
- Izabella Vitória — a definir
- Yasmin Borges — a definir
- Janaine Martins — a definir
- Integrante 5 — a definir
- Integrante 6 — a definir

---

## Apps Django

### Core

Responsável pelas páginas gerais e institucionais da plataforma.

Principais páginas:

- Home
- Quem Somos
- Sobre a plataforma

Views:

- `home`
- `quem_somos`

Principais arquivos:

- `views.py`
- `urls.py`
- `templates/core/index.html`
- `templates/core/quem_somos.html`

---

### Artesãos

Responsável pelas informações relacionadas aos artesãos cadastrados e às regiões do Brasil.

Models planejados:

- `Artesao`
- `Regiao`

Views planejadas:

- Listagem de artesãos
- Cadastro de artesão
- Edição de artesão
- Exclusão de artesão
- Detalhes do artesão
- Visualização das regiões

Principais arquivos:

- `models.py`
- `views.py`
- `forms.py`
- `urls.py`
- `admin.py`
- `templates/artesaos/`

---

### Produtos

Responsável pelo cadastro e gerenciamento dos produtos artesanais exibidos na plataforma.

Models planejados:

- `Produto`
- `Categoria`

Views planejadas:

- Listagem de produtos
- Cadastro de produto
- Edição de produto
- Exclusão de produto
- Detalhes do produto
- Produtos por categoria

Principais arquivos:

- `models.py`
- `views.py`
- `forms.py`
- `urls.py`
- `admin.py`
- `templates/produtos/`

---

### Usuários

Responsável pela autenticação e controle de acesso ao sistema.

Funcionalidades planejadas:

- Login
- Logout
- Cadastro
- Dashboard
- Controle de acesso

Principais arquivos:

- `views.py`
- `forms.py`
- `urls.py`
- `templates/usuarios/`

---

## Estrutura Inicial do Projeto

```text
RaizesDoBrasil/
│
├── artesaos/
├── config/
├── core/
├── produtos/
├── static/
│   ├── css/
│   └── img/
├── usuarios/
├── manage.py
├── requirements.txt
└── README.md