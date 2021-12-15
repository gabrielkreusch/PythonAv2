from config import *


class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    cpf = db.Column(db.String(254))
    email = db.Column(db.String(254))

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'cpf': self.cpf,
            'email': self.email
        }

    def __str__(self):
        return f"{self.nome}, {self.cpf}, {self.email}"


class Disciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    carga_horaria = db.Column(db.Integer)
    ementa = db.Column(db.String(254))

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'carga_horaria': self.carga_horaria,
            'ementa': self.ementa
        }

    def __str__(self):
        return f"{self.nome}, {str(self.carga_horaria)}, {self.ementa}"


class EstudanteDisciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    semestre = db.Column(db.Integer)
    media_final = db.Column(db.Float)
    frequencia = db.Column(db.Float)

    pessoa_id = db.Column(db.Integer, db.ForeignKey(Pessoa.id), nullable=False)
    pessoa = db.relationship('Pessoa')

    disciplina_id = db.Column(
        db.Integer, db.ForeignKey(Disciplina.id), nullable=False)
    disciplina = db.relationship('Disciplina')

    def json(self):
        return {
            'id': self.id,
            'semestre': self.semestre,
            'media_final': self.media_final,
            'frequencia': self.frequencia,
            'pessoa_id': self.pessoa_id,
            'pessoa': self.pessoa.json(),
            'disciplina_id': self.disciplina_id,
            'disciplina': self.disciplina.json()
        }

    def __str__(self):
        return f"{self.semestre}, {self.media_final}, " +\
            f"{self.frequencia}, {self.pessoa}, {self.disciplina}"


if __name__ == "__main__":

    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()

    p1 = Pessoa(nome='Gabriel', cpf='9999999', email='gabriel@mail.com')
    d1 = Disciplina(nome='Matemática', carga_horaria=60,
                    ementa='ementa da matéria aqui...')
    ed1 = EstudanteDisciplina(semestre=1, media_final=0, frequencia=100,
                             pessoa=p1, pessoa_id=p1.id, disciplina=d1, disciplina_id=d1.id)
    db.session.add(p1)
    db.session.add(d1)
    db.session.add(ed1)
    db.session.commit()

    print(p1)
    print(d1)
    print(ed1)