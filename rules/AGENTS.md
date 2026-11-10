# Second Brain

O usuário tem uma memória persistente no Second Brain, pelas ferramentas `memory_*` do servidor MCP `second-brain` deste plugin.

- Antes de uma tarefa não trivial, chame `memory_search` com o assunto da tarefa e use o que voltar. Não pergunte ao usuário o que a memória já responde.
- Salve sozinho, com `memory_save`, quando o usuário revelar algo durável: preferência, fato ou decisão de projeto, aprendizado ou referência útil. Dê `importance` honesta de 0 a 10 (abaixo de 6 é descartado).
- Fato novo que substitui um antigo: use `supersedesId` ou `memory_update`, nunca duplique.
- Nunca salve senhas, tokens, chaves ou dados de cartão.
- As regras completas estão na skill `memoria`.
