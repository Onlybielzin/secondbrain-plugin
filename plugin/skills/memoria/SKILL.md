---
name: memoria
description: Regras de uso da memória persistente do Second Brain (ferramentas memory_search, memory_save, memory_update, memory_entity, memory_get e memory_delete). Use no início de qualquer tarefa não trivial para buscar o que já se sabe, e sempre que o usuário revelar uma preferência, um fato de projeto, um aprendizado ou uma referência que valha lembrar em outras sessões.
---

# Memória do Second Brain

O servidor MCP `second-brain` guarda memórias do usuário entre sessões. Cada memória tem um tipo, um escopo e uma importância de 0 a 10.

## Carregar as ferramentas

As ferramentas `memory_*` podem aparecer só pelo nome, como ferramentas adiadas. Nesse caso, carregue o esquema delas com o ToolSearch (por exemplo, a query `memory_search` ou `select:` com os nomes completos) antes de chamar.

## 1. Buscar no início

- Antes de uma tarefa não trivial, chame `memory_search` com o assunto da tarefa (ex.: "deploy da api", "preferências de escrita").
- Use o que voltar. Não pergunte ao usuário o que a memória já responde.
- Para ver tudo sobre uma pessoa, máquina ou projeto, chame `memory_entity` com o nome. Para ler uma memória inteira, chame `memory_get` com o id.

## 2. Salvar sozinho

Salve sem pedir permissão quando o usuário revelar algo durável e reutilizável:

| Tipo | Quando | Escopo usual |
|------|--------|--------------|
| `preference` | Jeito de trabalhar, escolhas, correções que se repetem | `global` |
| `project_fact` | Fato, decisão ou restrição de um projeto específico | `project` (passe `project`) |
| `learning` | Erro cometido, o que funcionou, padrão que vale repetir | `global` ou `project` |
| `reference` | Documentação, API ou link útil | normalmente `global` |

Não salve trivialidades, nem o que o próprio código ou o repositório já registra.

## 3. Importância honesta

- Dê `importance` de 0 a 10 pelo valor real para sessões futuras.
- O servidor descarta memórias com importância abaixo de 6. Não infle a nota para forçar a gravação.
- Referência: 6 a 7 para fatos úteis, 8 a 10 para preferências fortes e decisões críticas.

## 4. Supersessão em vez de duplicar

- Antes de salvar, busque se já existe memória sobre o mesmo assunto.
- Se o fato novo contradiz ou substitui um salvo, passe `supersedesId` com o id antigo no `memory_save`, ou use `memory_update`.
- Não grave uma segunda memória dizendo o contrário da primeira.

## 5. Links com entidades

Uma entidade é a ficha de uma pessoa, máquina ou projeto (ex.: "maria", "vps").

1. Quando a memória for sobre uma dessas coisas, chame `memory_entity` sem nome para listar as entidades existentes.
2. Passe em `links` os nomes exatos das entidades que já existem (ex.: `links: ["vps"]`).
3. Um link para um nome que não existe é recusado. Se a entidade fizer falta, crie antes com `type: "entity"`, `scope: "global"` e `name`.

## 6. Nunca salvar segredos

Não grave senhas, tokens, chaves de API, chaves privadas, cookies de sessão nem dados de cartão. Se precisar lembrar onde um segredo fica, salve só o local (ex.: "o token do deploy está no cofre X"), nunca o valor.

## Limites do plano

Se o `memory_save` voltar erro de limite do plano, a gravação está bloqueada, mas busca, leitura e `memory_delete` continuam funcionando. Avise o usuário uma vez e siga a tarefa.
