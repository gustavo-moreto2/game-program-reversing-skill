# Fontes e comunidades

Pesquisa inicial: **2026-10-16**. “Consultada” significa que foi possível ler conteúdo retornado pelo navegador nesta pesquisa; não significa revisão integral, execução de exemplos ou aprovação de todo o site. Não foram copiados artigos ou posts completos.

A pesquisa complementar de extensões e integrações, com links dos projetos e
limites de compatibilidade, está no [guia de plugins](plugins.md).
A ampliação sobre Unity, Unreal, saves, Java, diff e gráficos está no
[guia do ecossistema](ecosystem.md), com fontes primárias e estado de validação.
As fontes de arquitetura, ABI, emulação, instrumentação, rede e mídia estão no
[guia de fundamentos](foundations.md). O [mapa de cobertura](coverage.md)
distingue documentação disponível de validações ainda pendentes.
O [catálogo de métodos](methods.md) acrescenta fontes de depuração, profiling e
extração. O [guia de instalações](installations.md) aplica a preferência do usuário
de receber recomendações quando uma ferramenta for necessária ou facilitar a tarefa.
As fontes de criptografia, anti-cheat, integridade e licenciamento estão no
[guia de proteções](protections-crypto.md). Consulte também
[atualização verificável](freshness.md) e [pesquisa de lacunas](research-gaps.md).

## Fontes primárias consultadas

| Fonte | Uso na skill | Estado |
| --- | --- | --- |
| [REA](https://github.com/morluto/rea) | Fluxos CLI/MCP, Evidence e limites de integração | README, skill geral e diretrizes consultados no clone; revisão `781d5751ad18b25a1fe1ffa8c6035388be8c3283` |
| [Introdução ao Ghidra](https://ghidra.re/ghidra_docs/GhidraClass/Beginner/Introduction_to_Ghidra_Student_Guide.html) | Projetos, importação, navegação e referências | Consultada |
| [Ghidra: estado da máquina](https://ghidra.re/ghidra_docs/GhidraClass/Debugger/A4-MachineState.html) | Memória, registros e diferença entre edição estática e dinâmica | Consultada |
| [Manual do GDB](https://sourceware.org/gdb/current/onlinedocs/gdb.html/) | Referência para sessões e comandos de depuração | Índice consultado; confirmar comandos na versão instalada |
| [Introdução ao x64dbg](https://help.x64dbg.com/en/latest/introduction/) | Valores, expressões, breakpoints e tracing | Índice consultado; consultar a seção específica antes de usar |
| [Formato PE — Microsoft](https://learn.microsoft.com/en-us/windows/win32/debug/pe-format) | Cabeçalhos, seções e endereços PE | Consultada |
| [ILSpy](https://github.com/icsharpcode/ILSpy) | Decompilação e metadados .NET | Página do projeto consultada |
| [Unity: IL2CPP](https://docs.unity3d.com/Manual/scripting-backends-il2cpp.html) | Distinguir backend IL2CPP de código managed | Consultada |
| [Godot demo projects](https://github.com/godotengine/godot-demo-projects) | Projetos abertos para laboratório com versão correspondente da engine | README consultado; exemplos não executados |

## Comunidades

- [Reverse Engineering Stack Exchange](https://reverseengineering.stackexchange.com/help/on-topic): escopo da comunidade consultado; inclui análise estática/dinâmica, disassembly e decompilação. Pesquise perguntas específicas e confira as fontes citadas nas respostas. Nenhuma resposta individual foi usada como prova técnica nesta versão.
- [Retro Reversing](https://www.retroreversing.com/): página inicial consultada como índice de temas sobre ferramentas, formatos e desenvolvimento de jogos antigos. Artigos individuais não foram validados nesta versão.
- [UnknownCheats — wiki](https://www.unknowncheats.me/wiki/) e [seção de programação e reversing](https://www.unknowncheats.me/forum/general-programming-and-reversing/): referências solicitadas pelo usuário. O navegador não conseguiu abrir esses endereços nesta sessão e a busca inicial não forneceu conteúdo útil para validação. Estado: **acesso não confirmado; conteúdo não incorporado**. Não atribuir técnicas ou recomendações a posts que não foram lidos.

## Como usar fóruns

Procure a combinação de ferramenta, versão, arquitetura e sintoma. Registre o link do tópico exato, autor quando disponível, data e a parte que responde à dúvida. Confirme a informação na documentação da ferramenta e em um experimento próprio. Se as fontes discordarem, preserve a divergência e a versão de cada uma.

Não baixe executáveis anexados apenas para aprender uma técnica. Prefira exemplos com código-fonte inspecionável e builds reproduzíveis. Não republique posts completos nem trate popularidade como prova de correção. Os limites de integração do REA continuam valendo para contribuições que o acompanhem.

