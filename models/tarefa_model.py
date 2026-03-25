from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Tarefa(db.Model):
    __tablename__ = "tarefas"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(100))
    descricao = db.Column(db.String(300))
    status = db.Column(db.Boolean)

    def __repr__(self):
        return f"<Tarefa {self.id} - {self.titulo}>"