from flask import Flask, render_template, request, redirect, url_for, flash
from database import connect, create_tables, insert_ocorrencia, insert_natureza, get_natureza_from_database
from Ocorrencia import Ocorrencia
from Natureza import Natureza

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

# Função para inicializar o banco de dados
def initialize_database():
    connection = connect()
    create_tables(connection)
    connection.close()

# Rota para a página inicial
@app.route('/')
def home():
    return render_template('login.html')

# Rota para a página de login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        # Lógica para verificar as credenciais do usuário
        # Se as credenciais estiverem corretas, redirecione para a página do menu
        username = request.form['username']
        # Adicione sua lógica de verificação de senha aqui

        # Redirecione para a página do menu
        return redirect(url_for('menu', username=username))

    return render_template('login.html')

# Rota para cadastrar natureza
@app.route('/cadastro_natureza', methods=['GET', 'POST'])
def cadastro_natureza():
    return Natureza.cadastrar_natureza(request)

# Rota para a página de cadastro
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

# Rota para a página de cadastro de ocorrência
@app.route('/cadastro_ocorrencia')
def cadastro_ocorrencia():
    return render_template('cadastro_ocorrencia.html')

# Rota para salvar uma ocorrência
@app.route('/salvar_ocorrencia', methods=['POST'])
def salvar_ocorrencia():
    connection = connect()

    # Validar os dados da ocorrência
    ocorrencia = Ocorrencia(
        request.form.get('Bombeiro', ''),  # Use get para fornecer um valor padrão
        request.form['Bombeiro'],
        request.form['guarnicao'],
        request.form['endereco_ocorr'],
        request.form['bairro_ocorr'],
        request.form['municipio_ocorr'],
        request.form['status'],
        request.form['custodia_id_custodia'],
        request.form['unid_saude_id_unid_saude'],
        request.form['natureza_id_natureza'],
        request.form['usuario_id_usuario'],
        request.form['usuario_cadvit_pessoa_id'],
        request.form['usuario_cadvit_pessoa_envolvidos_ocorr_id_envolvidos'],
        request.form['usuario_guarnicao_id_guarnicao']
    )

    if not ocorrencia.get('Bombeiro'):
        flash('Nome do Bombeiro é obrigatório', 'error')
        return redirect(url_for('cadastro_ocorrencia'))

    if not ocorrencia.validar():
        for erro in ocorrencia.erros:
            flash(erro, 'error')
        return redirect(url_for('cadastro_ocorrencia'))

    # Inserir a ocorrência no banco de dados
    insert_ocorrencia(connection, ocorrencia.to_dict())
    connection.close()

    return redirect(url_for('pagina_sucesso'))

# Rota para a página de sucesso
@app.route('/pagina_sucesso')
def pagina_sucesso():
    return render_template('pagina_sucesso.html')

# Rota para a página do menu
@app.route('/menu/', defaults={'username': None})
@app.route('/menu/<username>')
def menu(username):
    if username:
        # Lógica da página do menu com nome de usuário
        return render_template('menu.html', username=username)
    else:
        # Lógica da página do menu sem nome de usuário
        return render_template('menu.html')

@app.route('/cadastro_pessoa')
def cadastro_pessoa():
    return render_template('cadastro_pessoa.html')

# Rota para salvar uma pessoa
@app.route('/salvar_pessoa', methods=['POST'])
def salvar_pessoa():
    # Lógica para salvar a pessoa no banco de dados
    return 'Pessoa cadastrada com sucesso!'

# Rota para a página de cadastro de guarnição
@app.route('/cadastro_guarnicao')
def cadastro_guarnicao():
    return render_template('cadastro_guarnicao.html')

# Rota para a página de cadastro de unidade de saúde
@app.route('/cadastro_unidade_saude')
def cadastro_unidade_saude():
    return render_template('cadastro_unidade_saude.html')

# Inicializar o banco de dados quando o aplicativo é executado
initialize_database()

if __name__ == '__main__':
    app.run(debug=True)
