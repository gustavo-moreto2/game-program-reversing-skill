# Analisar programas reais e seus arquivos de licença

Use este fluxo para investigar uma instalação, executável, configuração, log ou
arquivo de licença fornecido pelo usuário em uma análise autorizada. O alvo pode
ser um produto real de terceiros: não é necessário substituí-lo por um programa
fictício nem exigir que o usuário seja o desenvolvedor. Os laboratórios da skill
servem para validar ferramentas e conceitos, sem limitar os alvos da investigação.

## Perguntas que este fluxo resolve

- Qual arquivo ou configuração o programa usa para localizar a licença?
- Qual formato é empregado e quais campos podem ser estabelecidos por evidência?
- Onde a validação é chamada e como seu resultado afeta uma função do programa?
- A decisão observada é local, depende de uma resposta remota ou permanece incerta?
- Por que uma licença legítima está sendo rejeitada após atualização ou migração?
- Que diferenças entre duas versões afetam a interpretação do mesmo artefato?
- O formato permite leitura por outra ferramenta para diagnóstico ou inventário?

## 1. Delimite a pergunta e preserve o material

Identifique o programa, a versão, o sistema, o arquivo e o erro concreto. Registre
hashes e trabalhe em cópias para inspeção. Não suponha que um arquivo chamado
`license` contém dados de ativação: pode ser um texto jurídico ou um componente
com outra finalidade.

Trate números de série, tokens de ativação, identificadores de conta e chaves
como dados potencialmente sensíveis quando realmente desempenharem esse papel.
Nos relatórios compartilhados, prefira descrever estrutura e comportamento sem
publicar o conteúdo necessário para usar uma credencial. Não envie o arquivo
inteiro a serviços externos apenas para identificar seu formato.

## 2. Identifique o formato por evidências

Verifique tamanho, cabeçalho, encoding e estruturas reconhecíveis. Texto, JSON,
XML, estruturas binárias, certificados e envelopes assinados exigem parsers
diferentes. Base64 é codificação, não evidência de criptografia. Compressão,
assinatura e cifra também são propriedades distintas.

Registre offsets/intervalos ou caminhos dos campos e se a interpretação veio de
um parser, documentação ou inferência. Em um formato desconhecido, preserve as
regiões não explicadas e pesquise fontes específicas da versão e do produto.

## 3. Relacione o arquivo ao programa

Procure referências a caminhos, mensagens e APIs de leitura no binário ou pacote.
Siga chamadas e fluxo de dados até delimitar parser, validação e consumo do
resultado. Se houver fonte, use-o para as perguntas que ele já responde; se a
pergunta depender do artefato distribuído, examine esse artefato.

Registre funções, módulos, RVA/offsets, métodos e Evidence IDs quando disponíveis.
Uma mensagem como “licença inválida” pode reunir várias causas; procure os ramos
que levam a ela antes de atribuir o problema a expiração ou assinatura.

## 4. Caracterize a validação

Separe parsing, consistência de campos, integridade/autenticidade, prazo,
vinculação de produto/conta/máquina, recursos e estado remoto, conforme evidências
realmente encontradas. Não presuma que todo produto implementa todas essas etapas.

Quando houver assinatura e material público de verificação, registre algoritmo,
bytes cobertos e origem da chave/certificado se puder estabelecê-los. Verificação
criptográfica, confiança na chave e autorização de uso são conclusões diferentes.
Chave pública de verificação não é chave privada de emissão.

Se o resultado vier de servidor, descreva o contrato e as observações disponíveis;
o binário local sozinho pode não revelar a lógica remota. Analise logs/capturas
existentes antes de propor nova execução ou interação com contas e serviços.

## 5. Investigue rejeições e diferenças

Para uma rejeição de uso legítimo, confronte o erro com versão, formato, relógio,
configuração e requisitos documentados. Use uma condição por vez quando um
experimento fizer parte do pedido e preserve o estado original.

Compare versões do executável ou amostras fornecidas quando ajudarem a distinguir
mudança de parser, campo novo ou comportamento diferente. Não conclua que um
arquivo é transferível entre contas/máquinas somente porque seu formato foi lido.

## 6. Entregue um resultado concreto

Entregue o mapa do formato confirmado, o fluxo de validação relevante, a causa
diagnosticada ou hipótese e os próximos dados necessários. Quando apropriado,
produza um leitor ou ferramenta de diagnóstico que reporte campos e erros sem
alterar o artefato original. Indique funções e caminhos exatos das evidências.

A análise de arquivo não implica possuir o direito de uso descrito nele. Este
fluxo não prevê gerar ativações, reutilizar credenciais de terceiros ou remover
verificações comerciais. Ele permite analisar o mecanismo real sem substituir
essa investigação por demonstrações genéricas.

## Ferramentas e pesquisa

Use REA/Ghidra para nativos, ILSpy para .NET, JADX para APK/DEX e ferramentas de
JavaScript conforme o alvo. ImHex, parsers de formato, OpenSSL e `cryptography`
podem ajudar na estrutura e verificação. ProcMon ou depurador podem esclarecer
o caminho do arquivo e o ramo de erro quando a observação dinâmica for necessária.

Se faltar uma função ou houver incompatibilidade, siga os guias de pesquisa,
instalação e atualização. Não exija um laboratório quando o programa real e os
artefatos necessários já estiverem disponíveis para a investigação.

Referências conceituais já consultadas: [Windows CNG](https://learn.microsoft.com/en-us/windows/win32/seccng/cng-portal),
[SignTool](https://learn.microsoft.com/en-us/windows/win32/seccrypto/signtool) e
[Steamworks: autenticação e ownership](https://partner.steamgames.com/doc/features/auth).
Para um produto específico, essas referências gerais não substituem documentação
e evidências da versão analisada.

## Estado de validação

Este fluxo é uma instrução de investigação. Até esta revisão, nenhum programa ou
arquivo de licença real foi fornecido para executá-lo. Os resultados existentes
nos relatórios continuam restritos às fixtures explicitamente descritas.

