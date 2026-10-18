# Fluxos de investigação

Estes roteiros são procedimentos de trabalho propostos. Sua presença não significa que um alvo ou provider foi testado neste repositório.

## Programas nativos

Registre o hash e identifique formato, arquitetura e endianness. Em ELF, `readelf -h arquivo` ajuda a examinar o cabeçalho; `file arquivo` fornece identificação inicial quando disponível. Use ferramentas equivalentes para outros formatos. Para PE, consulte a especificação da Microsoft em [sources.md](sources.md).

Busque uma string ou import relacionado à pergunta, examine referências cruzadas e delimite a função responsável. Renomeie funções como hipóteses até confirmar sua finalidade. Confronte pseudocódigo com instruções quando tipos, ponteiros ou condições forem decisivos.

Separe offset de arquivo, endereço virtual e RVA. Em PE, a conversão depende das seções e de seus intervalos físicos e virtuais; um endereço válido em memória pode não ter bytes correspondentes no arquivo. Para endereços de execução, registre o módulo e sua base naquela sessão. ASLR torna endereços absolutos inadequados como identificadores estáveis.

## Jogos e estruturas de dados

Escolha uma pergunta observável: como a pontuação muda, como um item é serializado ou qual estado seleciona uma animação. Registre versão, cenário e sequência de ações.

Em um jogo de laboratório com código disponível, compile ou exporte duas variantes controladas e compare a análise do binário com a implementação como referência de validação. Em um alvo sem fonte, mantenha tipos e nomes reconstruídos como hipóteses.

Ao examinar uma possível estrutura, registre tamanho de ponteiro, alinhamento, deslocamentos e evidências de acesso. Um padrão de acesso contíguo pode sugerir array ou estrutura; confirme limites, stride e uso em outras rotinas antes de concluir. Coordenadas podem estar em espaço local, de mundo ou de tela: não conclua o significado só por encontrar três floats.

## Saves e formatos de recursos

1. Preserve três amostras: A inicial, B após mudar um único valor e C repetindo a mudança com outro valor.
2. Compare tamanho e intervalos de bytes alterados. Controle timestamps, IDs e estado aleatório para evitar atribuir todas as diferenças ao campo estudado.
3. Teste interpretações de largura, sinal e endianness. Procure também evidências de texto, compressão ou tabelas de offsets.
4. Se houver compressão identificada e suportada, extraia para outro diretório com limites de tamanho. Alta entropia, isoladamente, não prova criptografia.
5. Descreva campos confirmados e candidatos em uma tabela com offset, tamanho, interpretação e evidências. Valide com uma amostra não usada para formar a hipótese.

Checksum, dados redundantes e serialização variável podem alterar regiões distantes. Mantenha essas alternativas abertas. Produza leitores apenas depois de estabelecer limites e comportamento para entradas truncadas.

## .NET e Unity

Confirme metadados CLI para escolher a rota managed. Use tipos, métodos e referências de ILSpy ou do provider disponível. Inspecione IL quando a reconstrução em C# for ambígua.

Para Unity, determine o backend por artefatos e metadados. Mono e IL2CPP têm rotas diferentes: IL2CPP converte IL para C++ e depois código nativo. Uma DLL nativa não deve ser tratada como assembly managed. Registre a versão da engine quando houver evidência e deixe-a desconhecida caso contrário. Base conceitual: [manual da Unity e ILSpy](sources.md).

## Depuração controlada

Escolha x64dbg no Windows ou GDB em plataformas compatíveis, conforme disponibilidade. Confirme identidade do executável e do processo. Registre a ação reproduzida e um breakpoint ligado à hipótese; examine argumentos, pilha e memória relevantes. Um breakpoint pode inserir uma instrução no processo, portanto não descreva toda sessão de depuração como observação sem efeitos.

Use observações pequenas em vez de dumps indiscriminados. Anote módulo, base, thread e momento. Desative os breakpoints criados e encerre apenas processos iniciados para o laboratório. Não altere memória, registros ou arquivos para validar uma hipótese se a observação já for suficiente.

## Comparação de versões

Registre hashes e versões de A e B, além de arquitetura e configuração de compilação conhecidas. Compare inventários, strings, imports e funções relacionadas à pergunta. Endereços diferentes e pequenas mudanças em assembly podem resultar de relocação, otimização ou compilador; descreva mudança de comportamento apenas quando sustentada por fluxo de código ou experimentos equivalentes.

