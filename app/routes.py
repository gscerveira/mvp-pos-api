from app import app, db
from models import ScoreMQA

@app.route('/')
def main_page():
    return 'Hello, World!'

# Endpoint para realizar a avaliação do score de metadata de um dataset
@app.route('/avaliar', methods=['POST'])
def avaliar():
    pass

# Endpoint para listar os scores de metadata de todos os datasets avaliados
@app.route('/avaliacoes', methods=['GET'])
def list_avaliacoes():
    pass

# Endpoint para listar os scores de metadata de um dataset avaliado
@app.route('avaliacoes/<dataset_id>', methods=['GET'])
def get_avaliacao(dataset_id):
        return db.get_or_404(ScoreMQA, dataset_id).to_dict()
    