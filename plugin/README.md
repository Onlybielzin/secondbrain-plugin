# Second Brain (segundo-cerebro)

Plugin do Claude Code que dá ao agente uma memória persistente entre sessões, guardada no serviço Second Brain hospedado.

## O que ele instala

- **Servidor MCP `second-brain`** (HTTP): conecta em `https://secondbrain.vings.app/mcp`. O login é pelo próprio `/mcp` do Claude Code, com a sua conta do GitHub (OAuth); não precisa copiar chave. Expõe `memory_search`, `memory_save`, `memory_get`, `memory_entity`, `memory_update` e `memory_delete`.
- **Hook `UserPromptSubmit`**: a cada mensagem, injeta um lembrete curto para buscar na memória antes de tarefas não triviais.
- **Skill `memoria`**: regras de quando buscar, quando salvar, como dar importância, como substituir memórias antigas e como ligar memórias a entidades.

## Instalação

1. No Claude Code:
   ```
   /plugin marketplace add Onlybielzin/secondbrain-plugin
   /plugin install segundo-cerebro@second-brain
   ```
2. Reinicie o Claude Code, rode `/mcp`, escolha `second-brain` e clique em **Authenticate**.
3. O navegador abre: entre com o GitHub e clique em **Conectar**. Pronto.

Sua conta precisa ter sido liberada por quem administra o serviço (com o seu usuário do GitHub). As conexões aparecem em https://secondbrain.vings.app/conta, onde dá para revogar.

## Limites do plano

Quando a conta passa do limite do plano, a gravação fica bloqueada. Busca, leitura e exclusão continuam funcionando.

## Privacidade

As memórias saem da sua máquina e ficam no servidor do serviço. A skill orienta o agente a nunca salvar senhas, tokens ou chaves.
