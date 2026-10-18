# Plugins, extensões e integrações

Pesquisa documental: **2026-10-16**. Os projetos abaixo tiveram páginas ou documentação consultadas; não foram instalados nem testados nesta sessão. As recomendações são escolhas de organização do laboratório, não uma certificação de compatibilidade.

## O que cada componente faz

Uma skill orienta o agente. Um plugin estende uma ferramenta. Um servidor MCP expõe ferramentas para um cliente compatível. Um programa auxiliar pode produzir arquivos e scripts para outro programa, sem ser um plugin dele. Uma entrada no catálogo do ChatGPT não equivale a uma extensão instalada no computador.

## Seleção por necessidade

| Projeto | Tipo | Quando considerar | Limitação relevante |
| --- | --- | --- | --- |
| [REA](https://github.com/morluto/rea) | CLI/MCP e skill geral | Coordenar análise de diferentes formatos com Evidence | Providers e recursos disponíveis variam por plataforma e instalação |
| [GhidraMCP](https://github.com/LaurieWired/GhidraMCP) | Extensão Ghidra e servidor MCP | Expor decompilação, listagens e renomeação a agentes | README consultado especifica Ghidra 12.1.4; renomeações alteram o projeto de análise |
| [BSim](https://github.com/NationalSecurityAgency/ghidra/blob/master/GhidraDocs/GhidraClass/BSim/README.md) | Recurso do Ghidra | Buscar funções estruturalmente semelhantes entre binários | Semelhança gera candidatos, não prova equivalência de comportamento |
| [ghidra-nativeaot](https://github.com/Washi1337/ghidra-nativeaot) | Analyzer e UI do Ghidra | Investigar programas .NET compilados com Native AOT | Não substitui análise managed e não equivale ao backend Unity IL2CPP |
| [Gx64Sync](https://github.com/diommsantos/Gx64Sync) | Conjunto de plugins Ghidra/x64dbg | Correlacionar análise estática com a sessão do depurador | Confirmar versões e mapeamento dos módulos; instalação não foi testada |
| [x64dbgpython](https://github.com/ElvisBlue/x64dbgpython) | Plugin Python 3 para x64dbg | Automatizar tarefas dentro do depurador | Scripts executam no ambiente do depurador; validar API e versão |
| [x64dbg Automate](https://dariushoule.github.io/x64dbg-automate-pyclient/) | Automação Python do x64dbg | Controlar tarefas repetitivas por um cliente Python | Avaliar instalação e ciclo de vida do alvo separadamente do REA |
| [ImHex](https://github.com/WerWolv/ImHex) | Aplicativo auxiliar extensível | Examinar saves e recursos com estruturas descritas em Pattern Language | Não é um plugin do Ghidra nem do ChatGPT |
| [Il2CppDumper](https://github.com/Perfare/Il2CppDumper) | Aplicativo auxiliar com scripts de saída | Estudar metadados de artefatos Unity IL2CPP compatíveis | README anuncia Unity 5.3–2022.2; não presumir suporte a versões posteriores nem recuperação do código original |

Os últimos dois são ferramentas auxiliares incluídas para evitar confundir todas as peças do laboratório com plugins. A pesquisa do Il2CppDumper não altera as fronteiras de integração do REA: as capacidades e os padrões upstream precisam ser avaliados antes de qualquer incorporação.

## Escolha prática para este projeto

Comece com REA e um provider nativo já instalado, como Ghidra. Para arquivos de save, acrescente ImHex quando as ferramentas existentes não bastarem. Para busca de funções semelhantes, avalie BSim antes de adicionar outro serviço.

Considere GhidraMCP como uma alternativa de conexão direta ao Ghidra quando esse fluxo resolver uma necessidade concreta. Não é necessário instalar REA e GhidraMCP simultaneamente para ler pseudocódigo. Se usar ambos, identifique qual serviço possui cada sessão e quais operações modificam a base de análise.

Para análise dinâmica em Windows, avalie primeiro x64dbg e depois uma única extensão de automação ou sincronização. Para Native AOT ou Unity, confirme o formato antes de selecionar a extensão específica.

## Compatibilidade do x64dbg

O [índice oficial de plugins](https://github.com/x64dbg/x64dbg/wiki/Plugins) reúne ferramentas de autores diferentes. A listagem não prova que cada extensão funciona com a versão local do depurador.

O [x64dbgpy original](https://github.com/x64dbg/x64dbgpy) documenta dependências de Python 2.7 e Visual Studio 2015. Não o confunda com projetos Python 3 como x64dbgpython. Para um ambiente novo, avalie as alternativas Python 3 e confirme os requisitos do projeto escolhido, sem atualizar runtimes de outros programas por consequência.

## Antes de instalar

Registre ferramenta hospedeira, versão, arquitetura, origem da release e dependências. Escolha uma release ou commit identificável. Confira quais recursos leem arquivos, alteram bases de análise, executam scripts ou controlam processos. Mantenha um exemplo pequeno para verificar a função desejada e preserve configurações existentes.

Para MCP, confirme o cliente e transporte suportados. O README do GhidraMCP descreve stdio e HTTP, além de modo headless com requisitos próprios. Uma URL local na máquina do usuário não é automaticamente acessível por um agente em ambiente remoto. Registre de onde o cliente e o servidor executam antes de propor a conexão.

Não execute instaladores apenas por terem sido citados neste guia. Este documento é pesquisa e seleção; nenhuma configuração foi alterada e nenhum plugin foi conectado.

## Catálogo desta sessão

A busca por Ghidra não retornou plugins correspondentes no catálogo disponível. Uma busca mais ampla por Ghidra, x64dbg, engenharia reversa e REA também não retornou uma opção pertinente. Isso não prova ausência em todo o [diretório de plugins](https://chatgpt.com/plugins). Os projetos externos acima foram encontrados em suas fontes originais e não foram apresentados como plugins conectados ao ChatGPT.

## Próxima validação

Quando houver uma máquina e um alvo definidos, escolha apenas o componente necessário, registre a versão e teste uma ação observável: listar funções, decompilar uma função conhecida, procurar uma correspondência BSim ou sincronizar um endereço de módulo. Publique resultados medidos separadamente desta pesquisa documental.

