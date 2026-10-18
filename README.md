# Engenharia reversa de jogos e programas

Skill em português para investigar binários, entender comportamentos e documentar resultados reproduzíveis. Inclui o [REA](https://github.com/morluto/rea) como submódulo fixado em uma revisão, preservando o projeto original e sua licença.

## Conteúdo

- `skills/game-program-reversing/SKILL.md`: instruções para o agente.
- `references/workflows.md`: análise de programas, jogos, saves e versões.
- `references/sources.md`: fontes consultadas, comunidades e limitações.
- `references/learning.md`: trilha de estudo e atualização do conhecimento.
- `references/plugins.md`: comparação de extensões, integrações MCP e ferramentas auxiliares.
- `references/ecosystem.md`: Unity, Unreal, saves, Java/Android, diff de binários e gráficos.
- `references/foundations.md`: assembly, ABI, emulação, instrumentação, rede e áudio.
- `references/coverage.md`: mapa das áreas, lacunas e próximos laboratórios.
- `references/methods.md`: catálogo de 40 métodos e abordagens, com ferramentas e evidências esperadas.
- `references/installations.md`: indicações de instalação por função e preferência do usuário.
- `references/protections-crypto.md`: criptografia, anti-cheat, anti-tamper, assinatura e licenciamento.
- `references/freshness.md`: checagem de versões e reprodução do toolkit instalado.
- `references/research-gaps.md`: pesquisa obrigatória quando faltar uma resposta ou recurso.
- `references/practical-training.md`: exercícios próprios de modificação de estado e licenciamento.
- `references/real-license-analysis.md`: investigação de programas reais, formatos de licença e rotinas de validação.
- `templates/report.md`: modelo de relatório com evidências.
- `scripts/verify_toolkit.py`: verificações sintéticas e consulta opcional de versões no PyPI.
- `scripts/run_practice_labs.py` e `labs/game_state.c`: laboratórios executáveis com código próprio.
- `requirements-toolkit.txt`: dependências nas versões verificadas.
- `docs/verification/`: relatório das funções realmente executadas.
- `rea/`: projeto original como submódulo.

Os caminhos `references/` e `templates/` acima ficam dentro da pasta da skill.

## Baixar junto com o REA

Repositório privado: https://github.com/gustavo-moreto2/game-program-reversing-skill. Para a distribuição ZIP, siga `REA-REVISION.txt` para obter o REA na revisão correta; o ZIP não inclui o conteúdo do submódulo.

```bash
git clone --recurse-submodules https://github.com/gustavo-moreto2/game-program-reversing-skill.git
cd game-program-reversing-skill
```

Se já clonou sem o submódulo, use `git submodule update --init rea`. Os submódulos internos do REA são opcionais conforme o fluxo escolhido; siga a documentação dele quando precisar dessas dependências.

## Instalar a skill no Codex

Copie a pasta `skills/game-program-reversing` para uma pasta de skills reconhecida pelo seu agente. No Codex, uma opção é `~/.agents/skills/game-program-reversing`. Preserve uma instalação existente antes de substituí-la. Reabra a sessão e peça:

> Use a skill game-program-reversing para analisar este executável. Primeiro identifique o formato, depois investigue como ele lê o arquivo de configuração. Separe fatos de hipóteses.

A skill contém instruções; ferramentas e provedores precisam estar disponíveis separadamente. Para instalar e configurar o REA, siga o [guia oficial](https://github.com/morluto/rea#quick-start). O setup do REA instala a skill geral dele; esta skill complementar é instalada à parte. Consulte o plano do setup antes de aplicar alterações de configuração.

## Exemplos de pedidos

A skill pode analisar programas reais e artefatos fornecidos pelo usuário no
escopo autorizado. Os laboratórios verificam conceitos e ferramentas; não são
uma exigência para analisar um alvo real.

- Descubra a estrutura deste save usando três amostras controladas.
- Compare duas versões deste programa e mostre as alterações com evidências.
- Explique a rotina de pontuação de um jogo local de laboratório.
- Identifique se este pacote usa .NET, código nativo ou JavaScript.
- Pesquise uma dúvida específica e atualize a base com fonte, data e validação.
- Analise este arquivo de licença e o programa correspondente para explicar seu formato e a causa da rejeição.

## Como o conhecimento evolui

A skill deve pesquisar quando faltar uma resposta ou recurso, avisar sobre ferramentas úteis e também instalá-las dentro do ambiente e escopo autorizados. Deve explicar a função, o benefício, a fonte oficial e como verificar a instalação. Isso não significa instalar todos os programas do catálogo.

A versão inicial reúne pesquisa realizada em 16/10/2026. Não existe coleta contínua nem treinamento automático do modelo. A evolução acontece por atualizações versionadas dos arquivos, com fontes e experimentos. UnknownCheats está registrado como referência solicitada com acesso não confirmado; nenhum conteúdo inacessível foi apresentado como lido.

Na versão 0.6.0, foram instalados em ambiente Python separado no executor Linux:
Capstone 5.0.9, LIEF 1.0.0, pyelftools 0.33 e cryptography 50.0.2. As versões
coincidiram com os metadados públicos do PyPI no momento da consulta. Passaram
checks de disassembly sintético, leitura ELF, AES-GCM e assinatura Ed25519,
incluindo rejeição de dados alterados. Isso não testa anti-cheats ou proteções
comerciais. Confira o [relatório](docs/verification/toolkit-2026-10-16.json) e o
[guia de atualização](skills/game-program-reversing/references/freshness.md).

Na versão 0.7.0, também foram executados dois laboratórios: estado de jogo próprio
em C (compilação, disassembly e modificação controlada) e licença sintética assinada
(aceitação válida e rejeições de alteração, expiração, aplicação e recurso).
O [relatório prático](docs/verification/practice-labs-2026-10-16.json) registra dez
checks aprovados. São exercícios de fundamentos, não cheats/cracks comerciais.

## Licenças

O conteúdo original deste repositório está sob MIT. O REA mantém sua própria licença e autoria no submódulo. Links externos não concedem permissão de republicação: publique sínteses próprias e referências, respeitando a licença de cada material.


