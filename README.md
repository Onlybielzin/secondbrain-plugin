# Second Brain

Memória de longo prazo para o seu agente de código. Ele lembra o que você ensinou ontem, sem você repetir.

Funciona no Claude Code, no Cursor, no Antigravity e no Hermes. Login com GitHub.

## Resumo em 1 minuto

- **O problema:** cada sessão nova do agente começa do zero. Você explica de novo como o projeto faz deploy, qual biblioteca prefere, o que já deu errado.
- **O que muda:** o agente salva sozinho o que vale lembrar e busca antes de começar uma tarefa. Na sessão seguinte, ele já sabe.
- **O que você faz:** instala com um comando e entra com o GitHub. Depois disso, nada. Não precisa pedir para salvar nem para buscar.
- **Onde ficam os dados:** no servidor do Second Brain, num cofre separado por conta. Dá para ligar o backup num repositório seu do GitHub.
- **Estado:** em uso diário, com mais de 2.000 memórias numa conta real. O acesso ainda é liberado por convite.

Este README segue esta ordem: um exemplo, como ele decide o que salvar, como ele acha a memória certa, entidades, o cérebro ao vivo, instalação, planos e privacidade.

## Um exemplo

Segunda-feira, você diz ao agente: "nesse projeto o deploy é push na main, nunca rode migration em produção".

O agente salva isso como um **fato de projeto**, com importância 8.

Quinta-feira, numa sessão nova, você pede: "sobe essa correção". Antes de agir, o agente busca "deploy" na memória, encontra a regra e faz o push na main, sem rodar a migration.

## Como ele decide o que salvar

O próprio agente decide, seguindo regras que vêm no plugin (a skill `memoria`). O servidor confere cada gravação em quatro passos:

1. **Tipo.** Toda memória é de um tipo: `preference` (seu jeito de trabalhar), `project_fact` (fato ou decisão de um projeto), `learning` (um erro ou algo que funcionou) ou `reference` (um link ou doc útil).
2. **Importância de 0 a 10.** O agente dá a nota. Abaixo de 6, a memória é descartada. Isso segura o lixo: "o usuário disse oi" não entra.
3. **Sem duplicata.** Se já existe uma memória quase igual no mesmo escopo, a nova não é gravada de novo.
4. **Sem contradição escondida.** Se a memória nova parece com uma antiga, o servidor devolve a antiga para o agente. Ele decide se a nova **substitui** a antiga. A substituída deixa de aparecer nas buscas, mas fica no histórico.

O agente nunca salva senhas, tokens, chaves ou dados de cartão. Essa regra também vem na skill.

**Escopo.** A memória é `global` (vale em qualquer projeto, como suas preferências) ou de um `project` (vale só dentro daquele projeto). Dentro do projeto A, o agente vê as globais e as do A, nunca as do projeto B.

## Como ele acha a memória certa

A busca junta dois jeitos de procurar e depois ordena o resultado:

1. **Por significado.** "como subo o projeto" encontra "o deploy é push na main", mesmo sem palavra em comum.
2. **Por palavra.** Nomes exatos, como `ERE-1080` ou `syncpay`, aparecem mesmo quando o significado é vago. A busca entende português: "imprimindo" encontra "imprime".
3. **Ordem final.** Cada resultado ganha uma nota que soma três coisas: quanto combina com a pergunta, quão recente é e quão importante é. Uma decisão de ontem com importância 9 passa na frente de uma nota antiga de importância 6.

Memórias substituídas ou invalidadas nunca aparecem. O agente recebe as 10 melhores, com o texto inteiro, e usa o que for útil.

## Entidades

Uma **entidade** é a ficha de uma pessoa, máquina ou projeto. Por exemplo: `vps` (com o host e como entrar) ou `maria` (quem é e em que projeto trabalha).

Cada memória pode ser ligada a entidades. Quando você pergunta "o que eu sei da vps?", o agente abre a ficha e todas as memórias ligadas a ela de uma vez, em vez de depender da busca.

Uma entidade também pode ser dona de uma pasta de projeto. Aí as memórias daquele projeto já ficam agrupadas nela.

## O cérebro ao vivo

Em https://secondbrain.vings.app/graph você vê suas memórias como um cérebro em 3D, ou como um grafo em 2D.

Quando qualquer agente seu busca, lê, salva ou liga uma memória, o neurônio correspondente acende na hora. Dá para ver em tempo real o que o agente está consultando.

## Instalação

### Claude Code

```
/plugin marketplace add Onlybielzin/secondbrain-plugin
/plugin install segundo-cerebro@second-brain
```

Reinicie o Claude Code, rode `/mcp`, escolha `second-brain` e clique em **Authenticate**. Entre com o GitHub e clique em **Conectar**.

Para atualizar depois, rode no terminal (fora do Claude Code):

```
claude plugin marketplace update second-brain
claude plugin update segundo-cerebro@second-brain
```

### Cursor

Windows (PowerShell):

```
irm https://secondbrain.vings.app/cursor | iex
```

macOS ou Linux:

```
curl -fsSL https://secondbrain.vings.app/cursor.sh | sh
```

No Cursor, rode `Developer: Reload Window`. Em **Settings > MCP**, clique em **Connect** no `second-brain` e entre com o GitHub.

No Cursor, o lembrete de buscar na memória vem como regra sempre ativa e como um aviso no início de cada chat.

### Antigravity

```
agy plugin install https://github.com/Onlybielzin/secondbrain-plugin
```

Ao conectar o servidor `second-brain`, o navegador abre para o login com o GitHub. No Antigravity, o lembrete vem como regra sempre ativa (`rules/AGENTS.md`).

### Hermes Agent

1. Instale o plugin (lembrete a cada mensagem e skill `memoria`):
   ```
   hermes plugins install Onlybielzin/secondbrain-plugin --enable
   ```
2. Adicione o servidor no `~/.hermes/config.yaml`:
   ```yaml
   mcp_servers:
     second-brain:
       url: https://secondbrain.vings.app/mcp
       auth: oauth
   ```
3. Faça o login (num terminal novo, fora de uma sessão):
   ```
   hermes mcp login second-brain
   ```

Hermes num servidor sem navegador: gere uma chave em https://secondbrain.vings.app/conta e use `headers: { Authorization: "Bearer sbk_..." }` no lugar de `auth: oauth`.

## Planos

| | Teste | Pro |
|---|---|---|
| Memórias | 500 | 10.000 |
| Buscas e gravações por dia | 200 | 2.000 |
| Editores conectados ao mesmo tempo | 1 | 3 |
| Entidades | 10 | ilimitadas |
| Animações do cérebro | não | sim |
| Backup no seu GitHub | não | sim |

Passou do limite: as gravações param e a busca continua funcionando.

## Privacidade

- Cada conta tem o próprio cofre. Uma conta nunca lê as memórias de outra.
- A busca roda no próprio servidor. Suas memórias não são enviadas para nenhuma IA de terceiros pelo Second Brain. O seu agente (Claude, Cursor...) lê as memórias que ele busca, como lê qualquer arquivo do seu projeto.
- Em https://secondbrain.vings.app/conta você vê os editores conectados, revoga o acesso de qualquer um e liga o backup num repositório seu do GitHub.
- Para apagar uma memória, peça ao agente: "esquece que eu uso X".
