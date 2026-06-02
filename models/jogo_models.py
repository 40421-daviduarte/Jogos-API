from db import db                       

class Jogos(db.Model):                  
    __tablename__ = 'jogos'              

    id = db.Column(db.Integer, primary_key=True)       
    titulo = db.Column(db.String(255), nullable=False)     
    genero = db.Column(db.String(255), nullable=False)
    desenvolvedor = db.Column(db.Integer, nullable=False) 
    plataforma = db.Column(db.Integer, nullable=False)

    def json(self):                                
        return {
            'id': self.id,           
            'titulo': self.titulo,   
            'genero': self.genero,
            'desenvolvedor': self.desenvolvedor,
            'plataforma': self.plataforma,       
        }