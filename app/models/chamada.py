from app import app,db



class Chamada(db.Document):
    chd_telefone    = db.StringField()
    chd_solicitante = db.StringField()
    chd_municipio   = db.StringField()
    chd_endereco    = db.StringField()
    chd_numero      = db.IntField()
    chd_bairro      = db.StringField()
    chd_referencia  = db.StringField()
    chd_paciente    = db.StringField()
    chd_observacoes = db.StringField()
    chd_emergencia  = db.BoolField()
    chd_emergencia_info  = db.StringField()
