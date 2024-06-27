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

    def __repr__(self) -> str:
        return f'<ScoreMQA {self.nome_arquivo}: {self.score}>'