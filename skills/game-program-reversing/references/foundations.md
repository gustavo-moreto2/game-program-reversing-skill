# Fundamentos, emulação e comportamento

Pesquisa documental: **2026-10-16**. As fontes originais abaixo foram consultadas em páginas de apresentação, índices ou seções indicadas. Não houve leitura integral de manuais, execução dessas ferramentas ou validação de todos os recursos anunciados. Recomendações metodológicas são propostas desta skill.

## Arquitetura, ABI e interpretação de assembly

Antes de interpretar uma função, estabeleça arquitetura, modo de execução, endianness e ABI. Arquitetura define instruções e registros; ABI estabelece contratos de chamada e organização de dados. O mesmo conjunto de instruções pode usar convenções diferentes em sistemas diferentes.

| Fonte primária | Aplicação | Cobertura desta pesquisa |
| --- | --- | --- |
| [Intel SDM](https://www.intel.com/content/www/us/en/developer/articles/technical/intel-sdm.html) | Arquiteturas Intel 64/IA-32 e referência de instruções | Página de apresentação e índice dos volumes |
| [Convenção x64 da Microsoft](https://learn.microsoft.com/en-us/cpp/build/x64-calling-convention) | Passagem de argumentos e retornos na ABI documentada | Artigo consultado |
| [ABI Arm](https://github.com/ARM-software/abi-aa) e [AAPCS64](https://github.com/ARM-software/abi-aa/blob/main/aapcs64/aapcs64.rst) | Contratos de chamadas AArch64 e layout de dados | Repositório e documento consultados parcialmente |
| [x86 psABI](https://github.com/hjl-tools/x86-psABI) | Localizar referências da ABI x86 System V | Página do repositório; seguir as referências vigentes antes de aplicar regras |

Na convenção x64 padrão descrita pela Microsoft, os argumentos inteiros nas quatro primeiras posições usam RCX, RDX, R8 e R9. Argumentos de ponto flutuante nessas posições usam os registros XMM correspondentes. Não transfira essa regra automaticamente para Linux, outra arquitetura ou uma convenção especializada. Fonte: artigo Microsoft acima.

Procedimento proposto: identifique chamadas conhecidas, confirme onde argumentos são preparados e como o retorno é consumido. Só então atribua tipos à função. Otimização, inlining e passagem indireta de estruturas podem dificultar a reconstrução. Registre interpretações alternativas quando os acessos não bastarem.

## Formato do arquivo e informação de depuração

- [System V ABI, índice ELF](https://www.sco.com/developers/gabi/latest/contents.html): referência consultada para localizar cabeçalhos, seções, símbolos, relocations e carregamento. A página é um draft datado de 2013, não uma especificação atual de todas as extensões de todas as plataformas.
- [DWARF](https://dwarfstd.org/): página do padrão consultada como ponto de entrada para informações de depuração. Símbolos ou tipos presentes precisam corresponder à identidade do artefato.
- [WebAssembly Core](https://webassembly.github.io/spec/core/): índice da especificação consultado. Registre versão e propostas efetivamente suportadas pelo runtime e pela ferramenta; não assuma equivalência a uma ABI nativa.

Para PE, use a referência Microsoft em [sources.md](sources.md). Ao interpretar offsets, preserve a distinção entre bytes no arquivo, endereços virtuais e mapeamentos da sessão. Um nome de símbolo é evidência útil, mas ainda precisa ser associado à versão correta.

## Disassembly, emulação e execução simbólica

| Projeto | O que acrescenta | Limite da conclusão |
| --- | --- | --- |
| [Capstone](https://github.com/capstone-engine/capstone) | Framework de disassembly de múltiplas arquiteturas | Decodificar instruções não reconstitui sozinho funções, tipos ou comportamento completo |
| [Unicorn](https://github.com/unicorn-engine/unicorn) | Framework de emulação de CPU | Um ambiente de CPU não fornece automaticamente todos os serviços do sistema e da aplicação |
| [angr](https://github.com/angr/angr) e [execução simbólica](https://docs.angr.io/en/latest/core-concepts/symbolic.html) | Explorar caminhos a partir de entradas simbólicas e restrições | O resultado depende do estado inicial, do modelo de ambiente e das fronteiras exploradas |

Escolha uma rotina pequena, especifique entradas e saídas e registre o estado necessário. Em emulação, documente memória, registradores, funções externas modeladas, limite de instruções e condição de parada. Em execução simbólica, documente quais entradas são simbólicas e quais hipóteses foram fixadas.

Não descreva um caminho não encontrado como impossível sem justificar cobertura e modelo. Não trate resultado do solver como confirmação em hardware: quando possível, reproduza a entrada em um laboratório concreto. Nenhum desses experimentos foi executado nesta atualização.

## Análise estática e depuradores alternativos

[Cutter](https://github.com/rizinorg/cutter) é uma interface de engenharia reversa baseada em Rizin; o projeto documenta plugins Python e C++ e integrações de comunidade. Consulte versões do hospedeiro e das extensões. Um plugin de Cutter não é automaticamente compatível com a interface de plugins do Ghidra.

[pwndbg](https://github.com/pwndbg/pwndbg) amplia a experiência de depuração com GDB/LLDB. Recursos disponíveis e requisitos precisam ser verificados na instalação escolhida. A pesquisa desta skill não iniciou uma sessão e não comprovou compatibilidade entre todas as combinações de versões.

## Observação de sistema e instrumentação

| Fonte | Papel | Efeito a registrar |
| --- | --- | --- |
| [Process Monitor, Windows](https://learn.microsoft.com/en-us/sysinternals/downloads/procmon) | Observação de atividade de sistema, incluindo arquivos, registro e processos/threads | Filtros, intervalo de captura e processos selecionados |
| [ProcMon Linux](https://github.com/microsoft/ProcMon-Linux) | Projeto separado para observação no Linux | Requisitos da versão e cobertura real; não presumir paridade com Windows |
| [Frida](https://frida.re/docs/home/) | Instrumentação dinâmica de aplicações | Processo selecionado, código injetado, hooks e alterações de estado |
| [DynamoRIO](https://github.com/DynamoRIO/dynamorio) | Plataforma de instrumentação dinâmica | Cliente de instrumentação, cenário e impacto sobre a execução |

Comece pela evidência menos invasiva que responde à pergunta. Um registro de arquivo aberto pode resolver “qual configuração é lida?” sem hooks. Se instrumentação for necessária e estiver no escopo do alvo, delimite o processo e a função antes de executar scripts.

Frida permite execução de código dentro de processos; portanto uma sessão instrumentada não deve ser descrita como simples leitura de um arquivo. Esta pesquisa documenta a categoria e sua fonte; não adiciona suporte genérico, scripts de injeção ou novos providers ao REA.

## Rede: registros históricos e captura ativa

[Wireshark](https://www.wireshark.org/docs/) publica guias de captura, análise e TShark. Comece por uma gravação já disponível quando ela responder à pergunta. Registre digest, filtros, horários e cobertura; o filtro exibido não significa que o tráfego omitido não existiu.

[mitmproxy](https://github.com/mitmproxy/mitmproxy) é um proxy HTTP com capacidade TLS. Configure um laboratório próprio somente quando esse caminho for necessário ao pedido. Alterar proxy ou confiança de certificados muda o ambiente: registre a alteração e sua reversão. Não presuma que possuir uma captura de rede permita ler conteúdo cifrado.

Se o aplicativo usar um protocolo não HTTP, primeiro identifique transporte, framing e evidências disponíveis. Não escolha mitmproxy apenas por o programa acessar a rede. Para formatos aceitos pelo REA, consulte os fluxos oficiais na revisão fixada do submódulo.

## Áudio e mídia de jogos

[vgmstream](https://github.com/vgmstream/vgmstream) oferece decodificação/reprodução de vários formatos de áudio usados em jogos. Confirme o formato e arquivos auxiliares necessários; o reconhecimento de uma extensão não garante suporte a todas as variantes.

[FFmpeg](https://github.com/FFmpeg/FFmpeg) reúne ferramentas e bibliotecas de mídia. Use inventário de streams e metadados antes de decidir conversão. Preserve o original: decodificação ou transcodificação gera outro artefato e pode alterar metadados ou representação dos dados.

## Limites das fontes

O índice genérico de documentação Arm redirecionou sem texto legível; as referências técnicas desta seção usam os documentos do repositório oficial de ABI. O endereço ELF da Linux Foundation não abriu; foi consultado o índice System V ABI indicado acima. UnknownCheats continuou inacessível nesta rodada. Não foram incorporadas alegações técnicas de páginas que não abriram.

