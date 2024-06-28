from app import app, db
from app.models import ScoreMQA
import datetime
from flask import request
import os
from app.utils import calcular_score_mqa, arquivo_permitido
from werkzeug.utils import secure_filename

@app.route('/')
def main_page():
    return 'Hello, World!'

# Endpoint para realizar a avaliação do score de metadata de um dataset
@app.route('/avaliar', methods=['POST'])
def avaliar():
    if 'file' not in request.files:
        return {'erro': 'Arquivo não encontrado'}, 400
    arquivo = request.files['file']
    if arquivo.filename == '':
        return {'erro': 'Nenhum arquivo selecionado'}, 400
    
    if arquivo and arquivo_permitido(arquivo.filename):
        nome_arquivo = secure_filename(arquivo.filename)
        caminho_arquivo = os.path.join(app.config['UPLOAD_FOLDER'], nome_arquivo)
        arquivo.save(caminho_arquivo)
        score = calcular_score_mqa(caminho_arquivo)

    # Salvar ou atualizar score na base de dados
        score_atual = ScoreMQA.query.filter_by(nome_arquivo=arquivo.filename).first()
        if score_atual:
            score_atual.score = score
            score_atual.avaliado_em = datetime.datetime.now(datetime.timezone.utc)
        else:
            novo_score = ScoreMQA(nome_arquivo=arquivo.filename, score=score)
            db.session.add(novo_score)
        
        db.session.commit()
        return {'message': 'Score avaliado com sucesso', 'score': score}, 200

# Endpoint para listar os scores de metadata de todos os datasets avaliados
@app.route('/avaliacoes', methods=['GET'])
def list_avaliacoes():
    avaliacoes = ScoreMQA.query.all()
    return {'avaliacoes': [avaliacao.to_dict() for avaliacao in avaliacoes]}

# Endpoint para listar os scores de metadata de um dataset avaliado
@app.route('/avaliacoes/<dataset_id>', methods=['GET'])
def get_avaliacao(dataset_id):
        return db.get_or_404(ScoreMQA, dataset_id).to_dict()
    