from flask import Blueprint, request

from controllers.jogo_controllers import create_jogo, get_jogos, get_jogo_by_id, update_jogo, delete_jogo

jogo_routes = Blueprint('jogos_routes', __name__)  

@jogo_routes.route('/Jogos', methods=['GET'])
def jogos_get_all():
    return get_jogos()

@jogo_routes.route('/Jogos', methods=['POST'])    
def jogos_post():                                  
    jogo_data = request.json                        
    return create_jogo(jogo_data)

@jogo_routes.route('/Jogos/<int:id>', methods=['GET'])
def jogos_get_by_id(id):
    return get_jogo_by_id(id)

@jogo_routes.route('/Jogos/<int:id>', methods=['PUT'])
def jogos_put(jogo_id):
    return update_jogo(jogo_id, request.json)

@jogo_routes.route('/Jogos/<int:id>', methods=['DELETE'])
def jogos_delete(jogo_id):
    return delete_jogo(jogo_id)