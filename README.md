# 📓 Diário Pessoal — Python

Um diário pessoal desenvolvido em Python, utilizando manipulação de arquivos para armazenar e consultar anotações diretamente pelo terminal.

O projeto foi criado com o objetivo de praticar lógica de programação, estruturas condicionais, funções e manipulação de arquivos utilizando a biblioteca `pathlib`.

## 🚀 Funcionalidades

- ✍️ **Adicionar anotações:** registra novas anotações no diário.
- 📖 **Consultar diário:** exibe todas as anotações salvas.
- 📁 **Criação automática:** cria um novo arquivo caso o diário ainda não exista e o usuário solicite.
- 🔍 **Verificação de conteúdo:** identifica quando o diário está vazio.
- ⚠️ **Tratamento de opções inválidas:** informa quando uma opção incorreta é selecionada.
- 💾 **Armazenamento local:** mantém as anotações salvas no arquivo `diario.txt`.

## 🛠️ Tecnologias utilizadas

- **Python 3**
- `pathlib` — gerenciamento de caminhos e arquivos.
- `open()` — abertura e manipulação de arquivos.
- `read()` — leitura de conteúdo.
- `write()` — escrita de anotações.
- `while` — repetição do menu.
- `if / elif / else` — controle de decisões.

## 📂 Estrutura do projeto

```text
diario-pessoal/
│
├── main.py
├── diario.txt
└── README.md
```

> O arquivo `diario.txt` é criado automaticamente quando necessário.

## ▶️ Como executar

**1. Clone o repositório:**

```bash
git clone URL_DO_REPOSITORIO
```

**2. Entre na pasta do projeto:**

```bash
cd diario-pessoal
```

**3. Execute o programa:**

```bash
python main.py
```

## 🖥️ Como funciona

Ao executar o programa, um menu interativo será apresentado:

```text
Você deseja escrever uma anotação ou consultar o diário?

[1] Escrever
[2] Consultar
[3] Sair
```

O usuário pode escolher entre registrar novas anotações, consultar o conteúdo armazenado ou encerrar o programa.

## 🎯 Objetivo do projeto

Este projeto faz parte da minha jornada de aprendizado em Python, com foco no desenvolvimento da lógica de programação e na aplicação prática dos fundamentos da linguagem.

A proposta foi construir uma aplicação funcional, compreendendo como trabalhar com arquivos, preservar informações e organizar a execução de um programa.

---

**Desenvolvido por Pedro Luizeto** 💻

*Aprendendo, praticando e evoluindo com Python.*
