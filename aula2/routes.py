#import database_utils
from flask import Blueprint, request, json, jsonify
from sqlalchemy import create_engine, select, update, func, null, insert
from sqlalchemy.orm.session import sessionmaker
import database

urls_blueprint = Blueprint('urls', __name__,)


@urls_blueprint.route('/')
def index():
    return 'urls index route'


@urls_blueprint.route('/create_tables', methods=['GET'])
def create_database():
    try:
        database.init_db()
        ret = {"status": "Tables are created!!"}

    except Exception as e:
        print(e)
        ret = {"status": "Tables are not created!!"}
    return ret


@urls_blueprint.route('/usuarios', methods=['POST'])
def add_usuario():
    req_data = request.get_json()
    usuario_json = {"nome": req_data['nome'], "email": req_data['email']}
    # database.add_usuario() --> sem o JSON
    ret = database.add_usuario_json(usuario_json)
    print(usuario_json)
    #ret = {"status": "User has been added"}
    return ret


@urls_blueprint.route('/usuarios', methods=['GET'])
def get_all_users():
    database.get_all_users()
    ret = {"status": "List of users"}
    return ret


#ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
# >>> session.add(ed_user)
    # Session = sessionmaker(self.db)
    # self.session = Session()

    # query = (
    #         insert(Envios_Lembretes).
    #         values(
    #             id_lembrete = envio_lembrete.id_lembrete,
    #             id_usuario = envio_lembrete.id_usuario,
    #             lembrete = envio_lembrete.lembrete,
    #             data_para_envio = envio_lembrete.data_para_envio,
    #             data_enviado = None,
    #             meio_envio = envio_lembrete.meio_envio,
    #             criado_em = datetime.now()
    #             )
    # )
    # conn = self.db.connect()
    # result = conn.execute(query)

    # self.session.commit()
    # logging.debug("ATUALIZANDO ADCIONANDO UM NOVO ENVIOS_LEMBRETES")
