# Mapa de cobertura e próximos laboratórios

Esta base organiza pesquisa sobre engenharia reversa de jogos e programas. Não é uma enciclopédia completa nem comprova domínio de todas as ferramentas citadas. Estado em **2026-10-16**.

Para selecionar uma técnica, use o [catálogo de 40 métodos](methods.md).
Para recomendar recursos ausentes ou vantajosos, use o [guia de instalações](installations.md).

## Navegação por área

| Área | Onde consultar | Estado |
| --- | --- | --- |
| Identidade, evidências e relatório | SKILL e modelo de relatório | Instruções e modelo disponíveis |
| Rotinas nativas, tipos e endereços | Fluxos e fundamentos | Roteiros documentados |
| .NET e Native AOT | Fluxos e plugins | Rotas e projetos pesquisados |
| Unity Mono/IL2CPP e assets | Fluxos, plugins e ecossistema | Diferenças e limites de versão documentados |
| Unreal e propriedades | Ecossistema | Bibliotecas e experimento proposto |
| Saves e recursos binários | Fluxos e ecossistema | Método A/B/C e ferramentas de formato |
| Java/Android | Ecossistema | Decompilação e limitações documentadas |
| JavaScript/Electron | SKILL e skill geral do REA | Roteamento para capacidades do REA |
| Assembly, ABI, ELF, DWARF e WASM | Fundamentos | Fontes e cautelas de interpretação |
| Emulação e análise simbólica | Fundamentos | Modelagem e limites de conclusão |
| Depuração e instrumentação | Plugins e fundamentos | Categorias, efeitos e seleção |
| Diff e busca de funções | Plugins e ecossistema | BSim, BinDiff e evidências necessárias |
| GPU e renderização | Ecossistema | Ferramentas e limites de plataforma |
| Rede e arquivos acessados | Fundamentos | Evidências históricas e observação de sistema |
| Áudio de jogos | Fundamentos | Fontes de ferramentas e preservação dos originais |
| Jogos antigos | Ecossistema | Pan Docs consultado; Nesdev pendente |
| Comunidades e fóruns | Fontes | RE Stack Exchange consultado; UnknownCheats pendente |
| Criptografia e integridade | Proteções e criptografia | Fontes primárias; checks sintéticos de AEAD e assinatura executados |
| Anti-cheat, anti-tamper e licença | Proteções e criptografia | Arquitetura, distinções e roteiro de avaliação; sem teste de produtos comerciais |
| Atualizações e lacunas | Atualização e pesquisa de lacunas | Versões verificadas de quatro bibliotecas e busca orientada por necessidade |
| Modificação de estado e licenciamento próprio | Trilha prática | Dois laboratórios executados, dez checks aprovados; sem extrapolação comercial |
| Programas reais e arquivos de licença | Análise real de licenciamento | Fluxo disponível; sem artefato real fornecido para validação |

Documentação nesta tabela não equivale a teste prático. Foram verificados estrutura,
links locais e integridade ZIP. O toolkit Python teve checks sintéticos de
disassembly, leitura ELF e criptografia executados; veja o relatório em
`docs/verification/` na raiz do projeto. Isso não comprova execução real dos
providers REA ou compatibilidade de plugins e produtos comerciais.
O relatório `docs/verification/practice-labs-2026-10-16.json` também comprova os
exercícios próprios de estado de jogo e licença sintética da trilha prática.

## Ordem sugerida para validação prática

1. **Rotina conhecida:** compilar um programa pequeno próprio e relacionar entrada, chamada e saída com a análise estática.
2. **Formato conhecido:** produzir saves sintéticos, comparar A/B/C e validar um leitor com amostra nova e entrada truncada.
3. **Engine conhecida:** exportar um projeto próprio Unity, Unreal ou Godot e confrontar inventário do build com o fonte.
4. **Versões conhecidas:** modificar uma função, recompilar e separar alterações de comportamento de mudanças produzidas pelo compilador.
5. **Execução conhecida:** reproduzir uma ação em laboratório e relacionar trace com função e módulo corretos.
6. **Modelo conhecido:** emular uma rotina pequena e comparar com execução concreta, registrando dependências não modeladas.

Não marque as etapas acima como realizadas até executá-las e registrar evidências. Escolha o próximo laboratório a partir de um alvo e uma pergunta, em vez de instalar todas as ferramentas do catálogo.

## Estudo organizado

Além dos guias oficiais de Ghidra, GDB e das ferramentas listadas, a página de [pwn.college](https://pwn.college/) foi consultada como referência de ambiente educacional. Não foram cursados módulos nem executados desafios nesta sessão. Selecione conteúdos ligados ao objetivo atual e conserve a distinção entre exercícios educacionais e suporte oficial do REA.

## Perguntas que impedem conclusões precipitadas

- Qual arquivo e versão sustentam esta afirmação?
- A arquitetura e a ABI foram estabelecidas ou supostas?
- O texto veio do fonte, do decompilador, de uma string ou de um fórum?
- O parser examinou todo o intervalo declarado e informou falhas?
- O cenário observado permite generalizar para outras entradas?
- Houve alteração de processo, arquivo, configuração ou banco de análise?
- Um resultado simulado foi confirmado em execução concreta?
- O programa citado está instalado e conectado ou apenas pesquisado?

## Lacunas declaradas

Permanecem sem validação prática os providers REA, plugins, produtos comerciais e
os exercícios explicitamente marcados como propostos. As quatro bibliotecas do toolkit tiveram apenas as funções
registradas no relatório verificadas, não uma auditoria integral. Mach-O, engines
específicas, formatos particulares de cada jogo e hardware especializado exigem
pesquisa focada adicional quando forem o alvo. Documentação de proteção não
constitui integração de fluxos de evasão ao REA; preserve o escopo do projeto.

Uma atualização útil deve fechar uma lacuna concreta, acrescentar uma fonte original ou reproduzir uma hipótese. Acrescentar nomes sem contexto não torna a base completa.

