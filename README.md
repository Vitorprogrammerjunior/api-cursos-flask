# API Cursos Flask

API simples em Python + Flask para a atividade prática da escola. Os dados ficam em **listas na memória** (não usa banco de dados). As respostas saem em JSON.

A documentação interativa (estilo Swagger) fica em `/docs`. A rota `GET /` continua sendo o health check em JSON, como o enunciado pede.

## Como rodar

No terminal, entre na pasta do projeto e instale as dependências:

```bash
pip install -r requirements.txt
```

Depois suba o servidor:

```bash
python app.py
```

O Flask sobe em `http://127.0.0.1:5000` (modo debug).

## Documentação

Abra no navegador:

- [http://127.0.0.1:5000/docs](http://127.0.0.1:5000/docs)

Na página de docs dá para ler cada rota, ver exemplos de resposta e testar os endpoints (Try it).

## URLs para testar

| Método | URL | O que retorna |
| --- | --- | --- |
| GET | `/` | `{"mensagem": "API funcionando!"}` |
| GET | `/cursos` | lista completa de cursos |
| GET | `/cursos/1` | um curso (troque o número) |
| GET | `/cursos/99` | 404 `{"erro": "Curso não encontrado"}` |
| GET | `/alunos` | lista de alunos (desafio) |
| GET | `/alunos/1` | um aluno |
| GET | `/alunos/99` | 404 `{"erro": "Aluno não encontrado"}` |
| GET | `/docs` | documentação visual da API |

Exemplos no terminal:

```bash
curl http://127.0.0.1:5000/
curl http://127.0.0.1:5000/cursos
curl http://127.0.0.1:5000/cursos/1
curl http://127.0.0.1:5000/alunos
curl http://127.0.0.1:5000/alunos/2
```

## Entrega (prints)

Os **prints de tela** para entregar na escola são responsabilidade do aluno. Sugestão: tire um print da página `/docs` e de cada rota testada no navegador (incluindo um 404).

## Estrutura

- `app.py` — rotas da API e dados em memória
- `templates/docs.html` — página de documentação
- `static/` — CSS e JavaScript da docs
- `RESPOSTAS.md` — respostas das perguntas da atividade (para estudar)
- `requirements.txt` — dependências (`flask`)
