import datetime
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db

# Definindo um modelo de dados para a tabela ScoreMQA, herdando de db.Model (classe base do Flask-SQLAlchemy)
class ScoreMQA(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    nome_arquivo: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    score: so.Mapped[int] = so.mapped_column(index=True)
    avaliado_em: so.Mapped[datetime.datetime] = so.mapped_column(index=True, default=datetime.datetime.now(datetime.timezone.utc))

    # Método para transformar uma instância do modelo em dict, para depois ser enviado para o client como JSON
    def to_dict(self):
        return {
            'id': self.id,
            'nome_arquivo': self.nome_arquivo,
            'score': self.score,
            'avaliado_em': self.avaliado_em.isoformat()
        }
    
    # Método para transformar um dicionário em uma instância do modelo, para ser salva no banco de dados
    def from_dict(self, data):
        for field in ['nome_arquivo', 'score']:
            if field in data:
                setattr(self, field, data[field])

    def __repr__(self) -> str:
        return f'<ScoreMQA {self.nome_arquivo}: {self.score}>'