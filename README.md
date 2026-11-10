# Second Brain

Memória persistente entre sessões para agentes de código, guardada no Second Brain hospedado (https://secundbrain.vings.app). O login é com a sua conta do GitHub; sua conta precisa ter sido liberada por quem administra o serviço.

O que vem junto: o servidor MCP `second-brain` (ferramentas `memory_search`, `memory_save`, `memory_get`, `memory_entity`, `memory_update`, `memory_delete`), a skill `memoria` com as regras de quando buscar e salvar, e um lembrete para buscar na memória antes das tarefas.

## Claude Code

```
/plugin marketplace add Onlybielzin/secundbrain-plugin
/plugin install segundo-cerebro@second-brain
```

Reinicie o Claude Code, rode `/mcp`, escolha `second-brain` e clique em **Authenticate**. Entre com o GitHub e clique em **Conectar**.

## Antigravity

```
agy plugin install https://github.com/Onlybielzin/secundbrain-plugin
```

Ao conectar o servidor `second-brain`, o navegador abre para o login com o GitHub. No Antigravity, o lembrete vem como regra sempre ativa (`rules/AGENTS.md`).

## Hermes Agent

1. Instale o plugin (lembrete a cada mensagem e skill `memoria`):
   ```
   hermes plugins install Onlybielzin/secundbrain-plugin --enable
   ```
2. Adicione o servidor no `~/.hermes/config.yaml`:
   ```yaml
   mcp_servers:
     second-brain:
       url: https://secundbrain.vings.app/mcp
       auth: oauth
   ```
3. Faça o login (num terminal novo, fora de uma sessão):
   ```
   hermes mcp login second-brain
   ```

Hermes num servidor sem navegador: gere uma chave em https://secundbrain.vings.app/conta e use `headers: { Authorization: "Bearer sbk_..." }` no lugar de `auth: oauth`.

## Privacidade

As memórias ficam no servidor do serviço, separadas por conta. A skill orienta o agente a nunca salvar senhas, tokens ou chaves. Em https://secundbrain.vings.app/conta você vê as conexões, revoga chaves e liga o backup das memórias num repositório seu do GitHub.
