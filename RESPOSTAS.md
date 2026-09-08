# Respostas da atividade

Respostas em linguagem de aluno, para estudar e adaptar se o professor pedir um relatório.

---

## 1. Rota inicial `GET /`

Essa rota só confirma que a API está no ar. Quando alguém acessa `/`, o Flask devolve um JSON com a mensagem `"API funcionando!"`.

Usei `jsonify` porque a atividade pede resposta em JSON, não HTML. Assim o navegador (ou o `curl`) recebe um objeto pronto, no formato que APIs usam.

## 2. Listar cursos `GET /cursos`

Os cursos estão numa lista Python chamada `cursos`, com `id`, `nome` e `carga_horaria`. Não tem banco de dados: os dados ficam na memória enquanto o servidor está rodando.

A rota `/cursos` devolve essa lista inteira em JSON. Se eu mudar a lista no código e reiniciar o `app.py`, a API já mostra os novos valores.

## 3. Buscar um curso `GET /cursos/<id>`

Aqui o Flask pega o número da URL (`id_curso`) e procura na lista. Eu fiz uma função `buscar_por_id` que percorre os itens e compara o `id`.

- Se achar, devolve o curso (status 200).
- Se não achar, devolve `{"erro": "Curso não encontrado"}` com status **404**.

O 404 é o código HTTP de “não encontrado”. Sem isso, a API poderia devolver `null` ou uma lista vazia, e quem consome não saberia se o curso existe ou não.

## 4. Desafio: listar alunos `GET /alunos`

Fiz a mesma ideia dos cursos, mas com outra lista: `alunos`, com pelo menos 3 registros. Cada aluno tem `id`, `nome` e `turma`.

A rota `/alunos` devolve todos. Assim dá para mostrar que dá para ter mais de um “recurso” na mesma API, só criando outra lista e outra rota.

## 5. Desafio: buscar um aluno `GET /alunos/<id>`

Igual à busca de curso: uso `buscar_por_id` na lista `alunos`. Se o id existir, volta o aluno; se não, volta 404 com `{"erro": "Aluno não encontrado"}`.

Reaproveitar a mesma função evita copiar o `for` duas vezes e deixa o código mais fácil de ler.

---

## Observações rápidas

- `jsonify` transforma dict/lista Python em JSON e já coloca o header `Content-Type: application/json`.
- Listas em memória são boas para atividade de aula. Se o servidor reiniciar, os dados voltam para o que está no código (não há persistência).
- O `if __name__ == "__main__": app.run(debug=True)` só sobe o servidor quando rodamos `python app.py`, e o `debug=True` recarrega o app quando o arquivo muda.
