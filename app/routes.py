from app import app

@app.route('/')
def main_page():
    return 'Hello, World!'

# Endpoint para realizar a avaliação do score de metadata de um dataset
@app.route('/avaliar', methods=['POST'])
def avaliar():
    pass

# Endpoint para listar os scores de metadata de todos os datasets avaliados
@app.route('/avaliacoes', methods=['GET'])
def avaliacoes():
    pass

# Endpoint para listar os scores de metadata de um dataset avaliado
@app.route('avaliacoes/<dataset_id>', methods=['GET'])
def avaliacao(dataset_id):
    pass