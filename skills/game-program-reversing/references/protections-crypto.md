# Criptografia, anti-cheat, anti-tamper e licenciamento

Pesquisa em **2026-10-16**. Este guia descreve como identificar, entender e avaliar mecanismos de proteção. Declarações de fabricantes são atribuídas às fontes; não demonstram funcionamento interno completo nem resistência comprovada. O guia não altera os limites de integração do REA.

## Separe os mecanismos

| Mecanismo | Finalidade | Evidências úteis |
| --- | --- | --- |
| Anti-cheat | Detectar/prevenir manipulação e preservar regras de uma partida | Arquitetura publicada, componentes, logs e decisões do servidor |
| Anti-tamper | Detectar alterações de código, recursos ou estado | Manifestos, hashes, assinaturas e eventos de integridade |
| Licenciamento / anti-crack | Verificar direitos de uso e condições da licença | Fluxo documentado de entitlement, validade e respostas de teste |
| Assinatura digital | Verificar autenticidade/integridade sob uma chave confiável | Mensagem/arquivo, assinatura, chave/certificado e política de confiança |
| Criptografia | Proteger confidencialidade e, conforme o esquema, autenticidade | Algoritmo, modo, formato, nonce, tag e gestão de chaves |
| Obfuscação / empacotamento | Alterar representação e dificultar interpretação | Indícios de transformação, seções, metadados e limites do analisador |

Não classifique como criptografia todo bloco de alta entropia: compressão também pode produzir essa aparência. Um hash sem chave não equivale a autenticação. Uma assinatura válida não demonstra que um programa é livre de defeitos. Identificar uma biblioteca não prova que toda chamada a ela foi usada corretamente.

## Roteiro de análise criptográfica

1. Defina a pergunta: identificar formato, entender integração, validar autenticidade ou analisar comportamento de erro.
2. Preserve o artefato e registre sua identidade. Diferencie conteúdo codificado, comprimido, cifrado e assinado a partir de evidências do formato e da implementação.
3. Localize imports, APIs, estruturas e chamadas relevantes. Nomes são âncoras; confirme parâmetros e uso no fluxo analisado.
4. Documente algoritmo/modo somente quando houver evidência suficiente. Registre os campos observáveis e deixe chave, nonce, salt ou tag desconhecidos quando não identificados.
5. Em uma implementação própria ou exemplo controlado, examine geração de nonce, autenticação de metadados, derivação de chaves e tratamento de falhas. Não use dados confidenciais reais como fixtures.
6. Valide o caso correto e casos alterados: dados, assinatura, tag ou metadados associados. A biblioteca rejeitar um caso não significa que a aplicação esteja propagando a falha corretamente.
7. Separe conclusão sobre o algoritmo de conclusão sobre o sistema inteiro. Não afirme certificação FIPS por apenas instalar uma biblioteca.

Ferramentas: OpenSSL para operações e inspeções suportadas; `cryptography` para laboratórios reprodutíveis; Ghidra/REA para relacionar uso de APIs ao binário; ferramentas oficiais da plataforma para assinaturas.

Fontes primárias: [NIST, padrões e guias](https://csrc.nist.gov/projects/cryptographic-standards-and-guidelines), [Windows CNG](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-portal), [pyca/cryptography](https://cryptography.io/en/stable/), [AEAD](https://cryptography.io/en/stable/hazmat/primitives/aead/) e [OpenSSL](https://docs.openssl.org/master/man1/openssl/). As páginas `latest` ou `master` podem descrever desenvolvimento: confira a documentação correspondente à release instalada.

## Anti-cheat: arquitetura e análise de compatibilidade

Descreva separadamente cliente do jogo, serviço local, driver quando documentado e servidor. Catalogue versão, assinatura, arquivos e eventos conhecidos. Preserve a distinção entre componentes observados, declarados pelo fabricante e apenas supostos.

O [suporte da Riot sobre Vanguard](https://support.riotgames.com/en-us/riot/performance/what-is-vanguard) descreve componentes do produto. A página [About do BattlEye](https://www.battleye.com/about/) descreve integração cliente/servidor e atuação em user/kernel mode; suas afirmações de eficácia são declarações do fornecedor, não testes desta skill.

Em projeto próprio, um laboratório útil avalia a validação no servidor: eventos válidos são aceitos e ações impossíveis ou inconsistentes são rejeitadas com motivo registrado. Mantenha cenários determinísticos e contabilize falsos positivos. Isso avalia aquele projeto; não reproduz o mecanismo interno de um anti-cheat comercial.

Para diagnosticar compatibilidade, use requisitos, logs e suporte oficiais antes de propor mudanças. Não carregue drivers só para ler documentação. O ambiente Linux desta publicação não comprova instalação ou teste de componentes Windows.

Fontes complementares: [assinatura de drivers Windows](https://learn.microsoft.com/en-us/windows-hardware/drivers/install/driver-signing) e [WinDbg](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/). Os requisitos dependem da plataforma e da versão. Nenhuma configuração de driver foi modificada neste trabalho.

## Anti-crack, licença e integridade

Para analisar instalações e arquivos reais fornecidos pelo usuário, use o
[fluxo de análise real de licenciamento](real-license-analysis.md). Ele não exige
que o programa seja fictício ou desenvolvido pelo próprio usuário. Os exemplos
de laboratório abaixo complementam essa análise, sem substituí-la.

Uma análise de projeto próprio pode mapear os estados: não autenticado, autenticado, licença válida, licença expirada, licença revogada, falha de rede e estado offline permitido. Registre onde a decisão é tomada e que evidência a fundamenta. Não confunda identidade do usuário com direito de uso de um produto.

Use um serviço de teste e licenças sintéticas para avaliar mensagens alteradas, expiração, revogação, replay de uma resposta de teste e comportamento em indisponibilidade. O objetivo é verificar o contrato do seu sistema; não produzir chaves, emular direitos de terceiros ou remover verificações comerciais.

Para integridade, verifique artefatos originais e cópias alteradas e documente exatamente qual política foi aplicada. Certificado presente, assinatura criptograficamente válida e cadeia confiável são verificações distintas. Timestamp e revogação também podem afetar a interpretação.

Fontes: [Steamworks, autenticação e ownership](https://partner.steamgames.com/doc/features/auth), [SignTool](https://learn.microsoft.com/en-us/windows/win32/seccrypto/signtool) e [ferramentas de criptografia Windows](https://learn.microsoft.com/en-us/windows/win32/seccrypto/cryptography-tools). Foram consultadas páginas públicas; não houve acesso a contas de desenvolvimento ou validação de jogos.

## O que foi instalado e verificado

Foi criado um ambiente Python separado no executor Linux, com Capstone, LIEF, pyelftools e cryptography. O relatório de execução em `docs/verification/` na raiz do repositório registra versões e resultados. Não conclua funcionamento de plugins Ghidra, drivers, anti-cheat ou sistemas comerciais a partir desse relatório.

O script `scripts/verify_toolkit.py` usa bytes sintéticos para disassembly, lê o interpretador Python como ELF e verifica operações AES-GCM e assinatura Ed25519 com chaves efêmeras. Não lê chaves de terceiros nem grava as chaves geradas. Os testes demonstram essas funções básicas, não uma auditoria completa da biblioteca.

## Limites da pesquisa e fontes pendentes

O endereço público inicial do Easy Anti-Cheat não abriu. A documentação Epic redirecionou, mas não forneceu texto legível; não foi usada para afirmar detalhes internos. A página consultada de política App Control também não abriu. Esses resultados ficam pendentes até consulta válida.

Documentar detecção, arquitetura e avaliação de integridade não adiciona ao REA fluxos de evasão de anti-cheat, anti-debug, DRM ou licença. Essa é uma fronteira do projeto original registrada em seu CONTRIBUTING; este pacote mantém uma referência ao REA sem modificar seus providers.

