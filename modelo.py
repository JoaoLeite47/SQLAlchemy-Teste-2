from config import *

class Planta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80))
    nome_cientifico = db.Column(db.String(80))
    tamanho_folha = db.Column(db.String(80))
    periodo_poda = db.Column(db.Integer)

    def __str__(self):  # para mostrar o nome da planta
        return self.nome + ',' + self.nome_cientifico + ',' + self.tamanho_folha + ',' + str(self.periodo_poda)

    def json(self):  # envia os dados para o back end em formato json
        return {
            'id': self.id,
            'nome': self.nome,
            'nome_cientifico': self.nome_cientifico,
            'tamanho_folha': self.tamanho_folha,
            'periodo_poda': self.periodo_poda
        }


# se for o main(modelo.py) em execução, as linhas abaixo serão executadas
if '__main__' == __name__:

    if os.path.exists(arquivo_banco):  # se o banco de dados existir
        os.remove(arquivo_banco)  # remove o banco de dados

    db.create_all()  # cria a tabela

    nova = Planta(nome='Hortelã', nome_cientifico='Mantha Spicata',
                  tamanho_folha='pequena', periodo_poda='60')
    db.session.add(nova)
    db.session.commit()
    todas = db.session.query(Planta).all()
    for p in todas:
        print(p)
        print(p.json())
