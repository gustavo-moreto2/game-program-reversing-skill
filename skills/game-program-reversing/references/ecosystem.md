# Ecossistema de análise: código, assets, saves e gráficos

Pesquisa documental em **2026-10-16**. Páginas originais dos projetos e documentação foram consultadas. Nenhum dos programas desta rodada foi instalado ou executado. Intervalos de versão são declarações das páginas consultadas, não resultados de testes deste repositório.

## Identificação e automação de binários

| Projeto e fonte | Papel | O que confirmar |
| --- | --- | --- |
| [Detect It Easy](https://github.com/horsicq/Detect-It-Easy) | Identificação e inspeção estática, com parsers e assinaturas extensíveis | Corroborar detecções heurísticas com cabeçalhos e outras evidências; identificação não recupera código protegido |
| [LIEF](https://github.com/lief-project/LIEF) | Biblioteca para ler, modificar e abstrair ELF, PE e Mach-O | Usar apenas leitura para inventários; escrita precisa de cópia e objetivo definido |
| [RetDec](https://github.com/avast/retdec) | Decompilador de código de máquina baseado em LLVM | O README declara manutenção limitada; avaliar custo de instalação antes de preferi-lo ao provider existente |

LIEF é útil quando uma pergunta exige coletar a mesma informação estrutural em vários arquivos. Detect It Easy ajuda na triagem. Nenhuma das duas respostas, sozinha, comprova o comportamento de uma função.

## Unity: recursos e código são perguntas diferentes

[AssetRipper](https://github.com/AssetRipper/AssetRipper) analisa arquivos de jogos Unity e converte assets para formatos nativos da engine. O README consultado anuncia versões Unity de 3.5.0 a 6000.4.X, com qualidade de suporte variável. Também documenta uma edição premium com funcionalidades adicionais; não atribua automaticamente esses recursos à edição aberta.

Use essa rota para investigar referências quebradas, dependências de assets e estrutura dos recursos. Para código, confirme se há assemblies managed ou IL2CPP e siga o [fluxo de análise](workflows.md). Extrair recursos não demonstra recuperação do projeto original completo, dos scripts originais ou do histórico de edição.

Experimento proposto: exporte um projeto próprio com uma textura e uma cena conhecidas. Faça o inventário do build e compare os recursos reconhecidos com os originais. Registre os objetos não recuperados e diferenças de conversão. **Não executado nesta pesquisa.**

## Unreal: propriedades, pacotes e variações de serialização

- [UAssetAPI](https://github.com/atenfyr/UAssetAPI): biblioteca .NET para leitura e escrita de assets Unreal. O README anuncia uma variedade de arquivos cooked e uncooked aproximadamente de UE 4.13 a 5.7; descreve propriedades, exports, bytecode Kismet e uso de `.usmap`. Não é uma promessa de compatibilidade com todos os jogos dessas versões.
- [CUE4Parse](https://github.com/FabianFG/CUE4Parse): biblioteca para analisar arquivos e pacotes de Unreal Engine 4 e 5, incluindo classes como texturas, animações e meshes. Formatos específicos de um jogo podem exigir configuração ou tratamento próprio.

Antes de interpretar dados, identifique versão e variante do formato. Preserve arquivos auxiliares e mappings fornecidos para o projeto; registre sua origem. Um erro de parser pode indicar configuração incorreta, serialização específica ou arquivo truncado. Não classifique automaticamente toda falha como proteção.

Experimento proposto: gere um `.uasset` em um projeto próprio, registre a engine e leia uma propriedade conhecida. Faça uma segunda exportação alterando apenas essa propriedade. Comece pela leitura: a existência de suporte a escrita não prova que uma reserialização preserva o comportamento. **Não executado nesta pesquisa.**

## Saves e formatos binários

[Kaitai Struct](https://github.com/kaitai-io/kaitai_struct) usa descrições declarativas de formatos para gerar parsers. O [guia oficial](https://doc.kaitai.io/user_guide.html) explica estruturas, tipos e parâmetros. Combine-o com ImHex: primeiro explore bytes e amostras; depois formalize apenas os campos sustentados por evidências.

Uma especificação útil precisa declarar endianness, tamanhos, assinaturas, comprimentos e relações entre campos. Registre dados não compreendidos como regiões desconhecidas em vez de inventar nomes. Tamanhos provenientes do arquivo precisam respeitar limites da entrada e de recursos.

Experimento proposto: crie um formato simples próprio com magic, versão, contador e registros. Produza três arquivos válidos e um truncado. Confira valores lidos e comportamento diante do truncamento. Isso testa a especificação daquele formato, não de saves comerciais. **Não executado nesta pesquisa.**

## Java e Android

| Projeto | Onde ajuda | Limite |
| --- | --- | --- |
| [Recaf](https://github.com/Col-E/Recaf) | Explorar aplicações Java, alternar decompiladores e pesquisar referências e bytecode | Também é editor; preserve o arquivo original e diferencie navegação de alteração |
| [JADX](https://github.com/skylot/jadx) | Analisar DEX/APK com interface gráfica ou CLI | O próprio projeto avisa que geralmente não consegue decompilar 100% do código |

Quando dois decompiladores produzirem resultados diferentes, confronte o bytecode ou DEX relevante e relate a ambiguidade. Código Java reconstruído é uma interpretação, não prova de identidade com o fonte original. Bibliotecas nativas incluídas no APK continuam exigindo análise nativa.

## C++ e comparação entre versões

[HexRaysCodeXplorer](https://github.com/REhints/HexRaysCodeXplorer) é um plugin do decompilador Hex-Rays para navegação, reconstrução de tipos e identificação de vtables. Depende do ecossistema IDA/Hex-Rays e da compatibilidade do plugin; não é extensão do Ghidra. Estruturas reconstruídas continuam exigindo confirmação por usos e acessos.

[BinDiff](https://github.com/google/bindiff) compara diferenças e semelhanças em código disassemblado. Seu ecossistema inclui BinExport; confirme as versões e o fluxo de exportação compatível antes de instalar. Uma correspondência é uma pista para comparar funções, não uma prova de que a semântica permaneceu igual.

Escolha conforme a pergunta: BSim procura funções semelhantes em coleções; uma comparação de duas versões pode se beneficiar de um fluxo de diff. Use o recurso já disponível que resolva a pergunta antes de adicionar outra dependência.

## Gráficos e memória de GPU

[RenderDoc](https://github.com/baldurk/renderdoc) é um depurador gráfico baseado em captura de frames, com suporte documentado a APIs como Vulkan, D3D11, D3D12, OpenGL e OpenGL ES, dependendo da plataforma. Não é um decompilador geral de executáveis. O projeto orienta seu uso a programas próprios e projetos abertos e explicita limites de suporte nos canais oficiais.

Use-o em um projeto próprio ou aberto para investigar quais draw calls e recursos produziram um frame. Registre API, GPU, driver, plataforma e versão da captura. A captura controla/instrumenta o processo e precisa de um cenário definido; este guia não adiciona um provider gráfico ao REA.

[Radeon Memory Visualizer](https://github.com/GPUOpen-Tools/radeon_memory_visualizer) analisa consumo e padrões de memória de vídeo em hardware AMD compatível. O README lista DirectX 12 e Vulkan e restrições de GPU, sistema operacional e driver. Não o apresente como ferramenta universal para qualquer GPU. Esta pesquisa não aplicou as alterações de driver ou sistema descritas no guia upstream.

## Referências para jogos antigos

[Pan Docs](https://github.com/gbdev/pandocs) é uma referência técnica de Game Boy mantida pela comunidade. O repositório original foi consultado; a versão web em `gbdev.io/pandocs/` respondeu 403 nesta pesquisa. Use documentação da arquitetura e mapas de memória para fundamentar a análise de exemplos homebrew, sem extrapolar instruções de uma CPU para outra.

O acesso à wiki Nesdev também retornou 403. Essa fonte permanece pendente; não foi usada para sustentar explicações técnicas nesta atualização. Fontes pendentes não contam como material lido.

## Decisão antes de instalar

| Pergunta | Primeira rota sugerida |
| --- | --- |
| Que tipo de arquivo é este? | Cabeçalhos e triagem com ferramentas existentes; DiE se necessário |
| Qual função calcula este valor? | REA/Ghidra e referências cruzadas |
| Que recursos Unity estão no build? | AssetRipper |
| Como esta propriedade Unreal foi serializada? | UAssetAPI ou CUE4Parse, conforme formato |
| Qual é a estrutura deste save? | Amostras controladas, ImHex e depois Kaitai Struct |
| O que mudou nesta função entre builds? | Fluxo de comparação e, se necessário, BinDiff |
| Como uma aplicação Java faz isto? | Recaf; JADX para DEX/APK |
| Que chamadas gráficas geraram este frame? | RenderDoc em projeto próprio ou aberto |
| Como meu programa ocupa memória de vídeo AMD? | RMV, após confirmar hardware e driver |

As escolhas acima são recomendações de fluxo desta skill. Não indicam que os projetos estejam conectados ao ChatGPT nem que o REA já os suporte. Documentar um link não integra suas capacidades ao produto.

