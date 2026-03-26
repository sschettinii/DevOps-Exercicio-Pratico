from db import create_app, db
from models.tarefa_model import Tarefa

# Definição dos Mocks (Dados de teste estruturados)
MOCK_TAREFAS = [
    {"titulo": "Configurar CI/CD", "desc": "Finalizar o YAML do GitHub Actions", "status": True},
    {"titulo": "Validar SQLAlchemy", "desc": "Testar conexão com o banco de dados", "status": True},
    {"titulo": "Criar Mocks", "desc": "Popular o banco com dados de teste", "status": False},
    {"titulo": "Reunião de Sprints", "desc": "Alinhar tarefas com o grupo da UEL", "status": False},
    {"titulo": "Documentar Readme", "desc": "Atualizar instruções de execução", "status": False},
    {"titulo": "Fix Bug Import", "desc": "Corrigir erro de path no scripts.seeds", "status": True},
    {"titulo": "Estudar DevOps", "desc": "Leitura sobre automação de infra", "status": False},
    {"titulo": "Refatorar Models", "desc": "Padronizar nomes de colunas", "status": True},
    {"titulo": "Teste de Unidade", "desc": "Validar criação de registros", "status": False},
    {"titulo": "Backup SQL", "desc": "Gerar dump do banco tarefas.db", "status": False}
]

def seed():
    app = create_app()
    with app.app_context():
        print("--- Iniciando Seed do Banco de Dados ---")
        
        # Idempotência: Limpa a tabela para não duplicar dados
        db.session.query(Tarefa).delete()
        
        for item in MOCK_TAREFAS:
            nova_tarefa = Tarefa(
                titulo=item["titulo"],
                descricao=item["desc"],
                status=item["status"]
            )
            db.session.add(nova_tarefa)
        
        db.session.commit()
        print(f"Sucesso: {len(MOCK_TAREFAS)} mocks inseridos.")

if __name__ == "__main__":
    seed()