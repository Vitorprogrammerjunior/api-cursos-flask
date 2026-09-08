from flask import Flask, jsonify, render_template

app = Flask(__name__)

cursos = [
    {"id": 1, "nome": "Python Básico", "carga_horaria": 40},
    {"id": 2, "nome": "Desenvolvimento Web", "carga_horaria": 60},
    {"id": 3, "nome": "Banco de Dados", "carga_horaria": 40},
]

alunos = [
    {"id": 1, "nome": "Ana Souza", "turma": "3A"},
    {"id": 2, "nome": "Bruno Lima", "turma": "3B"},
    {"id": 3, "nome": "Carla Mendes", "turma": "3A"},
    {"id": 4, "nome": "Diego Alves", "turma": "3C"},
]


def buscar_por_id(lista, identificador):
    """Percorre uma lista em memória e devolve o item com o id pedido."""
    for item in lista:
        if item["id"] == identificador:
            return item
    return None


@app.route("/")
def home():
    return jsonify({"mensagem": "API funcionando!"})


@app.route("/cursos")
def listar_cursos():
    return jsonify(cursos)


@app.route("/cursos/<int:id_curso>")
def obter_curso(id_curso):
    curso = buscar_por_id(cursos, id_curso)
    if curso is None:
        return jsonify({"erro": "Curso não encontrado"}), 404
    return jsonify(curso)


@app.route("/alunos")
def listar_alunos():
    return jsonify(alunos)


@app.route("/alunos/<int:id_aluno>")
def obter_aluno(id_aluno):
    aluno = buscar_por_id(alunos, id_aluno)
    if aluno is None:
        return jsonify({"erro": "Aluno não encontrado"}), 404
    return jsonify(aluno)


@app.route("/docs")
def documentacao():
    return render_template("docs.html")


if __name__ == "__main__":
    app.run(debug=True)
