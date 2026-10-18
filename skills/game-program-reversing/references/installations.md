# Recomendar instalações quando fizerem falta ou facilitarem

Preferência explícita do usuário: **sempre avisar, indicar e também instalar programas/plugins pertinentes quando faltarem funções ou facilitarem o trabalho, no ambiente e escopo autorizados**. Esta regra vale durante a investigação e na apresentação do resultado. Não se limita a bloqueios completos. Se não houver uma opção conhecida, [pesquise](research-gaps.md).

## Antes da recomendação

Identifique o alvo, a plataforma onde a ferramenta vai executar e o benefício concreto. Confira ferramentas já disponíveis quando houver acesso ao ambiente. Um ambiente remoto Linux não estabelece o que está instalado no Windows do usuário. Não afirme ausência na máquina do usuário a partir da ausência no container.

Se a ferramenta já estiver disponível, use-a dentro do escopo e confirme a função necessária. Se o recurso não estiver disponível ou se uma alternativa trouxer vantagem clara, faça a recomendação. Não peça ao usuário que descubra sozinho qual plugin resolve o problema.

## Formato da indicação

```text
Ferramenta/plugin:
Situação: necessário para esta etapa | recomendado para facilitar
Função que vamos usar:
Benefício nesta tarefa:
Onde instalar: máquina do usuário | ambiente do agente | ambos, explicando por quê
Fonte oficial:
Sistema/arquitetura e dependências verificadas:
Passos de instalação confirmados para essa versão:
Como verificar que a função ficou disponível:
Alternativa disponível enquanto isso:
```

Na conversa, condense esses campos ao necessário. Exemplo:

> Recomendo instalar ImHex para visualizar os campos deste save e comparar amostras. Isso facilita a investigação; posso continuar a comparação de bytes com as ferramentas atuais. Vou indicar a release oficial e os passos adequados ao seu sistema.

Se os passos dependem de um sistema desconhecido, peça a plataforma e continue o que for independente. Não invente um comando universal. Uma dependência opcional só deve ser apresentada como necessária se a função escolhida realmente depender dela.

## Seleção por função

| Necessidade atual | O que indicar se faltar ou trouxer vantagem | Onde conferir a compatibilidade |
| --- | --- | --- |
| Analisar função nativa | Ghidra e integração REA, ou provider existente equivalente | Guia oficial REA e release Ghidra |
| Conectar agente diretamente ao Ghidra | GhidraMCP, quando resolver essa necessidade | README e release do GhidraMCP |
| Depurar Windows | x64dbg | Documentação e release oficial |
| Depurar Linux/macOS | GDB ou LLDB conforme alvo e suporte | Documentação do depurador e provider |
| Automatizar x64dbg | Uma extensão Python 3 compatível | Projeto escolhido; não confundir com x64dbgpy Python 2 |
| Procurar funções semelhantes | BSim | Documentação da versão local do Ghidra |
| Comparar duas versões | BinDiff/BinExport quando o fluxo justificar | Requisitos das duas peças e do exportador |
| Ler assemblies .NET | ILSpy ou provider managed já disponível | Projeto ILSpy e recursos do REA |
| Investigar .NET Native AOT | ghidra-nativeaot | Versão da extensão e Ghidra |
| Analisar DEX/APK | JADX | Release, Java requerido e suporte do provider |
| Explorar aplicação JVM | Recaf | Runtime Java e versão do projeto |
| Ler assets Unity | AssetRipper | Engine, formato e edição da ferramenta |
| Ler propriedades Unreal | UAssetAPI/CUE4Parse conforme a pergunta | Versão/variante de serialização e dependências .NET |
| Visualizar save/recurso | ImHex | Plataforma e release oficial |
| Gerar leitor de formato conhecido | Kaitai Struct | Compilador e runtime da linguagem de saída |
| Disassembly automatizado | Capstone ou llvm-objdump | Arquiteturas da versão instalada |
| Automação de cabeçalhos e seções | LIEF | Binding e formatos suportados |
| Emular rotina isolada | Unicorn | Arquitetura, dependências e modelo de execução |
| Explorar caminhos simbólicos | angr | Arquitetura e ambiente modelado |
| Observar arquivos/chamadas de sistema | ProcMon no Windows; strace/alternativa compatível no Linux | Sistema, permissões e cobertura desejada |
| Instrumentar uma função | Frida/DynamoRIO somente quando o método for pertinente ao alvo | Plataforma, versão e efeitos sobre o processo |
| Repetir uma falha gravada | rr em ambiente compatível | Hardware, kernel e limitações do projeto |
| Ler captura de rede | Wireshark/TShark | Formato, dissectors e versão |
| Investigar HTTP em laboratório | mitmproxy | Cliente, proxy e confiança de certificados |
| Investigar renderização | RenderDoc | API gráfica e plataforma do projeto |
| Investigar memória GPU AMD | RMV | GPU, API, driver e SO |
| Identificar áudio de jogo | vgmstream | Formato e arquivos auxiliares |
| Inventariar mídia | FFmpeg/ffprobe | Demuxers/codecs da build |
| Extrair firmware/container conhecido | Binwalk/Unblob conforme suporte | Versão, formatos e limites de extração |

Os links dos projetos estão em [plugins.md](plugins.md), [ecosystem.md](ecosystem.md), [foundations.md](foundations.md) e [methods.md](methods.md). Essa seleção é orientativa, não uma afirmação de que qualquer ferramenta é indispensável para toda tarefa da linha.

## Instalação e verificação

Quando instalação estiver autorizada e for possível, use o mecanismo oficial adequado à plataforma. Preserve configurações e restrinja alterações à tarefa. Registre versão instalada e verifique a função pretendida com um artefato conhecido, não apenas a existência do executável.

O usuário autorizou instalações pertinentes à tarefa; não solicite novamente essa
mesma autorização para um ambiente isolado compatível. Continue respeitando regras
específicas de ferramentas/projetos e identifique quando uma ação afetaria outra
máquina, configuração ampla ou recurso não abrangido pelo pedido.

Para plugins, confirme que o hospedeiro os carregou. Para MCP, confirme que as ferramentas aparecem no cliente ativo. Para providers, execute uma operação representativa e confira o resultado. Dependência presente, plugin carregado e integração funcional são estados diferentes.

Se a instalação não puder ocorrer nesta sessão, entregue a indicação concreta e a próxima ação necessária. Não encerre uma análise possível só porque uma ferramenta opcional ainda não foi instalada. Se a conexão negar uma operação, explique o erro observado sem afirmar que uma reinstalação resolverá permissões de conta.

Para criptografia e integridade, avalie OpenSSL e `cryptography`; para assinatura
de artefatos Windows, ferramentas oficiais como SignTool; para dumps Windows,
WinDbg quando houver esse alvo. Não instale serviços anti-cheat ou drivers como
pré-requisito genérico de estudo. Consulte [protections-crypto.md](protections-crypto.md).

