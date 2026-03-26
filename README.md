# Sistema de Gerenciamento de Tarefas (Task Manager)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) 
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) 
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

Este projeto consiste em um sistema web para criação e organização de atividades diárias, desenvolvido como parte da disciplina de Engenharia de Software. O objetivo é aplicar conceitos práticos de **Scrum**, **Kanban** e **DevOps** utilizando o ecossistema do GitHub.

| Aluno | GitHub |
| :--- | :--- |
| **Vinícius Yudi Oya** | [@arcseno](https://github.com/arcseno) |
| **André Tomonaga Schettini** | [@sschettinii](https://github.com/sschettinii) |
| **Leonardo Ryoichi Yakushijin Taniguti** | [@leonardoryoichi-web](https://github.com/leonardoryoichi-web) |
| **Vitor da Costa Garcia** | [@vitor-costa-garcia](https://github.com/vitor-costa-garcia) |

## Fluxo de Desenvolvimento (DevOps)
O projeto seguiu as etapas obrigatórias de engenharia de software:

* **Planejamento (Scrum):** Criação de um **Product Backlog** com **User Stories** nas Issues do GitHub.
* **Gestão (Kanban):** Fluxo de trabalho organizado no **GitHub Projects** através das colunas *To Do*, *In Progress*, *Review* e *Done*.
* **Desenvolvimento:** Uso de **branches** para cada funcionalidade e commits frequentes.
* **CI (Integração Contínua):** Automação via **GitHub Actions** para validar Pull Requests e realizar o build.

## Funcionalidades Entregues

O sistema implementa o CRUD completo conforme solicitado:

* **Criar tarefa:** Inclusão de novos itens.
* **Editar tarefa:** Modificação de registros existentes.
* **Excluir tarefa:** Remoção de atividades.
* **Listar tarefas:** Visualização em interface Web.
* **Concluir:** Check para marcar tarefas finalizadas.

## Como Executar
1.  Clonar o repositório:
    ```bash
    git clone https://github.com/sschettinii/DevOps-Exercicio-Pratico
    ```
2.  Navegar até a pasta:
    ```bash
    cd DevOps-Exercicio-Pratico
    ```

3.  Criar e ativar o ambiente virtual:
    ```bash
    python -m venv venv

    source venv/bin/activate -> Linux/Mac
    venv\Scripts\activate -> Windows
    ```

4.  Instalar as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5.  Rodar a aplicação:
    ```bash
    python app.py
    ```