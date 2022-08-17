
# Ubuntu

- Branch Principal ( master )

- Branch (develop) para testar o commit, caso aprovado merge para master

## Subindo primeira vez o projeto
- python3 -m venv venv 
- source venv/bin/activate  (caso não tenha, sudo apt install python3.8-venv)
- pip install -r requirements.txt
- python -m flask --debug run


## Caso aparece erro de tabela não encontrada 
- flask shell
- from app import db
- db.create_all()
