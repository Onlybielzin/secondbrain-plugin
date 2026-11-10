"""Plugin do Second Brain para o Hermes Agent.

- Hook pre_llm_call: a cada mensagem, injeta um lembrete curto para buscar na
  memória (equivalente ao UserPromptSubmit do plugin do Claude Code).
- Skill memoria: as regras de quando buscar e salvar.

O servidor MCP vai no ~/.hermes/config.yaml (mcp_servers.second-brain com
auth: oauth) e o login é `hermes mcp login second-brain`.
"""
from pathlib import Path

LEMBRETE = (
    "Second Brain ativo: antes de uma tarefa não trivial, chame memory_search "
    "(servidor MCP second-brain) com o assunto e use o que voltar. Salve com "
    "memory_save preferências, fatos de projeto e aprendizados duráveis. Regras "
    "completas na skill segundo-cerebro:memoria."
)


def _lembrete(*_args, **_kwargs):
    return {"context": LEMBRETE}


def register(ctx):
    ctx.register_hook("pre_llm_call", _lembrete)
    skill = Path(__file__).parent / "skills" / "memoria"
    if skill.exists() and hasattr(ctx, "register_skill"):
        ctx.register_skill("memoria", str(skill))
