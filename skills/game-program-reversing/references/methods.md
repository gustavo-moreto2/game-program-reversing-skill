# Catálogo de métodos de engenharia reversa

Este catálogo organiza **40 técnicas e abordagens comuns** para escolher um caminho de investigação. A divisão é prática: métodos se sobrepõem, variam por alvo e continuam evoluindo. Não é uma lista exaustiva de todas as técnicas existentes.

As tabelas são uma síntese metodológica desta skill. Ferramentas são candidatas documentadas nos guias vinculados; não significa que cada ferramenta implemente automaticamente a abordagem inteira. Nenhuma operação desta tabela foi executada apenas por ter sido catalogada.

## Identificar e delimitar

| Nº | Método | Como conduzir | Ferramentas candidatas | Evidência a entregar |
| --- | --- | --- | --- | --- |
| 1 | Identificação de formato e arquitetura | Confrontar assinatura, cabeçalho e parser; não depender só da extensão | file, DiE, REA | Formato e arquitetura com origem da conclusão |
| 2 | Inventário de artefatos | Enumerar arquivos, membros de pacotes, tamanhos, hashes e relações | REA, ferramentas de arquivo | Inventário com cobertura e itens não lidos |
| 3 | Metadados de build | Examinar dados de compilador/runtime e registros disponíveis | REA, DiE, LIEF | Dados originais separados das heurísticas |
| 4 | Símbolos e informações de depuração | Associar símbolos/tipos à identidade do binário | Ghidra, GDB, LLDB, DWARF | Correspondência de versão e limites dos símbolos |
| 5 | Strings, imports e exports | Usar nomes e texto como âncoras e seguir referências | Ghidra, REA, llvm-objdump | Referências concretas e função candidata |

## Reconstruir código e estruturas

| Nº | Método | Como conduzir | Ferramentas candidatas | Evidência a entregar |
| --- | --- | --- | --- | --- |
| 6 | Disassembly | Decodificar bytes no modo/arquitetura corretos | Ghidra, Capstone, llvm-objdump | Bytes, endereços e instruções relevantes |
| 7 | Decompilação | Reconstruir representação de alto nível e conferir trechos decisivos no assembly | Ghidra, Hex-Rays, ILSpy, JADX | Pseudocódigo com ambiguidades identificadas |
| 8 | Grafo de fluxo de controle | Mapear blocos e desvios da rotina | Ghidra, Cutter, angr | Condições e caminhos examinados |
| 9 | Grafo de chamadas e referências cruzadas | Seguir chamadores, funções chamadas e dados usados | REA, Ghidra, Recaf | Caminho da entrada até o comportamento |
| 10 | Fluxo de dados e slicing | Rastrear a origem ou os usos de um valor | Análise manual, Ghidra, angr | Dependências e pontos não resolvidos |
| 11 | Reconstrução de tipos e layout | Inferir largura, alinhamento, campos e stride pelos acessos | Ghidra, CodeXplorer | Estrutura candidata com offsets e justificativas |
| 12 | Reconstrução de objetos C++ | Examinar dispatch virtual, vtables e usos dos objetos | Ghidra, CodeXplorer | Relações candidatas sem inventar classes originais |
| 13 | Reconhecimento de bibliotecas e funções | Comparar assinaturas ou semelhança estrutural | BSim e recursos do analisador | Correspondências candidatas e confiança |
| 14 | Análise de bytecode e metadados | Inspecionar IL, DEX, JVM ou WASM conforme o alvo | ILSpy, JADX, Recaf, REA | Métodos e instruções efetivamente observados |

## Observar execução

| Nº | Método | Como conduzir | Ferramentas candidatas | Evidência a entregar |
| --- | --- | --- | --- | --- |
| 15 | Depuração com breakpoints | Parar em função ligada à pergunta e examinar argumentos e retorno | x64dbg, GDB, LLDB | Cenário, thread, módulo e valores |
| 16 | Watchpoints de dados | Observar quando um endereço selecionado é acessado ou alterado | GDB, x64dbg | Instrução e contexto do acesso; limites do mecanismo |
| 17 | Trace de instruções | Registrar uma janela delimitada da execução | Depurador, DynamoRIO | Trace, limites e condição de parada |
| 18 | Trace de chamadas/API | Relacionar chamadas a ações observáveis | Depurador, Frida | Funções, argumentos selecionados e temporalidade |
| 19 | Trace de chamadas de sistema | Relacionar interação com o SO ao cenário | strace, ProcMon Linux | Chamadas registradas e filtros |
| 20 | Monitoramento de arquivos/registro/processos | Observar recursos acessados sem presumir a lógica interna | Process Monitor | Caminhos, operações, processos e intervalo |
| 21 | Instrumentação dinâmica | Inserir observação específica em processo selecionado | Frida, DynamoRIO | Código utilizado, efeitos, cobertura e limpeza |
| 22 | Snapshots e comparação de memória | Comparar regiões pertinentes em estados controlados | Depurador | Identidade dos estados, mapas e diferenças relevantes |
| 23 | Gravação e replay | Gravar um cenário compatível e revisitar a mesma execução | rr e GDB | Identidade do trace e passos da análise |
| 24 | Análise de falha e dump | Relacionar stack, registros e módulos de uma falha gravada | GDB, LLDB, REA quando suportado | Estado registrado, hipóteses e informações ausentes |

## Modelar e experimentar

| Nº | Método | Como conduzir | Ferramentas candidatas | Evidência a entregar |
| --- | --- | --- | --- | --- |
| 25 | Experimento de caixa-preta | Alterar uma entrada e observar a saída em estado controlado | Harness próprio e logs | Matriz entrada/saída e alternativas descartadas |
| 26 | Análise diferencial A/B | Comparar builds ou cenários equivalentes | BinDiff, REA, ferramentas de diff | Diferenças e causas ainda incertas |
| 27 | Emulação de rotina | Fornecer CPU, memória e serviços mínimos de uma rotina pequena | Unicorn | Estado inicial, modelos, limites e saída |
| 28 | Execução simbólica | Definir entradas simbólicas e condições de interesse | angr | Restrições, caminhos, modelo e validação concreta pendente |
| 29 | Perfil de chamadas, CPU e alocações | Medir atividades relevantes para localizar comportamento | Valgrind, Android Studio Profiler | Perfil e impacto da medição no cenário |
| 30 | Análise de concorrência | Correlacionar threads e eventos com um defeito observável | Depuradores, Helgrind/DRD onde compatíveis | Interleavings observados e limites de reprodução |

## Entender formatos, engines e recursos

| Nº | Método | Como conduzir | Ferramentas candidatas | Evidência a entregar |
| --- | --- | --- | --- | --- |
| 31 | Inferência de formato binário | Comparar amostras A/B/C e validar campos em nova amostra | ImHex, Kaitai Struct | Especificação parcial e regiões desconhecidas |
| 32 | Extração de containers e compressão reconhecida | Inventariar e extrair formatos suportados para diretório separado | Binwalk, Unblob, REA conforme suporte | Relação origem/saída, hashes e limites |
| 33 | Análise de assets e serialização de engine | Identificar engine/versão e interpretar recursos específicos | AssetRipper, UAssetAPI, CUE4Parse | Inventário, propriedades e falhas de parsing |
| 34 | Análise de frame e pipeline gráfico | Capturar cenário de projeto próprio/aberto e relacionar recursos e draw calls | RenderDoc | Frame, API, eventos e recursos pertinentes |
| 35 | Perfil de memória de GPU | Investigar alocações de um cenário em hardware compatível | Radeon Memory Visualizer | Trace, GPU, driver e padrões observados |
| 36 | Análise de áudio e mídia | Identificar streams, metadados e codecs antes de converter | vgmstream, FFmpeg | Formato, canais, duração e artefatos derivados |

## Protocolos e reconstrução de comportamento

| Nº | Método | Como conduzir | Ferramentas candidatas | Evidência a entregar |
| --- | --- | --- | --- | --- |
| 37 | Análise de captura de rede | Examinar gravação com filtros e limites explícitos | Wireshark/TShark, REA | Mensagens observadas e cobertura da captura |
| 38 | Análise de protocolo de aplicação | Correlacionar ações com framing, mensagens e estados | Wireshark, parser próprio; mitmproxy para HTTP compatível | Especificação candidata e exemplos reproduzíveis |
| 39 | Reconstrução de máquina de estados | Variar entradas e associar transições às evidências | Logs, depurador e harness | Estados, transições e eventos não explicados |
| 40 | Reimplementação e teste de equivalência limitada | Implementar um comportamento delimitado e comparar casos conhecidos | Código próprio e corpus controlado | Casos cobertos e diferenças; sem alegar identidade total |

## Sequência de escolha

Comece pela pergunta e por um método de baixo custo que produza evidência suficiente. Se uma âncora estática resolver a dúvida, conclua com essa evidência. Se faltarem estados, observe um cenário. Se precisar explicar condições em muitos caminhos, avalie modelagem. Combine métodos quando suas evidências forem complementares.

Quando uma ferramenta ausente fizer falta ou facilitar significativamente uma dessas etapas, **recomende a instalação explicitamente**, conforme [installations.md](installations.md). Não apresente quarenta itens como quarenta instalações obrigatórias.

## Referências adicionais consultadas nesta rodada

- [llvm-objdump](https://llvm.org/docs/CommandGuide/llvm-objdump.html): documentação para inspeção de objetos e disassembly.
- [LLDB](https://lldb.llvm.org/): página do depurador.
- [strace](https://github.com/strace/strace): apresentação do utilitário Linux.
- [rr](https://rr-project.org/): gravação/replay e limitações de plataforma e execução.
- [Valgrind Tool Suite](https://valgrind.org/info/tools.html): índice de Memcheck, Callgrind, Massif, Helgrind e outros componentes; requisitos precisam ser verificados por ferramenta.
- [Android Studio Profiler](https://developer.android.com/studio/profile): perfil de desempenho de aplicações Android; não substitui decompilação de APK.
- [Binwalk](https://github.com/ReFirmLabs/binwalk) e [Unblob](https://github.com/onekey-sec/unblob): apresentação dos projetos de análise/extração. Conteúdo arbitrário não se torna suportado por uma descrição geral de container.

Os demais programas e fontes estão nos guias de [plugins](plugins.md), [ecossistema](ecosystem.md), [fundamentos](foundations.md) e [fontes](sources.md). Este catálogo não acrescenta providers ao REA.

