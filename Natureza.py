from flask import render_template
from database import connect, insert_natureza, get_natureza_from_database

class Natureza:
    @staticmethod
    def cadastrar_natureza(request):
        if request.method == 'POST':
            # Obtenha os dados do formulário
            natureza = request.form.get('nome_natureza')
            descricao = request.form.get('descricao')
            status_nat = request.form.get('status_natureza')

            # Valide os dados conforme necessário

            # Insira os dados no banco de dados (substitua pela lógica real)
            # insert_natureza(connection, natureza, descricao, status_nat)

            flash('Natureza cadastrada com sucesso!', 'success')

        # Obtém as naturezas cadastradas (substitua pela lógica real)
        natureza = get_natureza_from_database(connect(), 'natureza')

        return render_template('cadastro_natureza.html', natureza=natureza)
    
    