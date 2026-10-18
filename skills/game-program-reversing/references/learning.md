# Estudo e atualização

## Trilha prática

| Etapa | Prática | Resultado verificável |
| --- | --- | --- |
| Fundamentos | C, ponteiros, tamanhos, endianness, stack e convenções de chamada | Explicar uma função pequena compilada por você |
| Formatos | Examinar cabeçalhos e seções de um binário conhecido | Inventário com offsets e limites |
| Análise estática | Localizar string, referências e função no Ghidra | Mapa de chamadas que responde a uma pergunta |
| Estado em execução | Observar uma função em um jogo próprio ou demo aberto | Registro de entrada, estado e saída |
| Arquivos de jogo | Comparar saves A/B/C | Especificação parcial validada em nova amostra |
| Managed e engines | Comparar rotas .NET, Unity e nativas | Identificação fundamentada da rota |
| Comparação | Compilar duas variantes e comparar artefatos | Diferença de comportamento ligada à mudança |

Use demos do Godot com a versão correspondente da engine ou um programa pequeno escrito por você. Registre commit, compilador, flags e versão da engine. Os exercícios são sugestões; esta publicação não executou esses laboratórios.

## Ciclo de pesquisa

1. Escreva a lacuna concreta: por exemplo, “como esta versão representa RVA?”.
2. Consulte a fonte primária e registre URL, data de acesso e versão aplicável.
3. Quando usar um fórum, localize o tópico exato e procure confirmação independente.
4. Faça uma síntese própria. Separe documentação, hipótese e resultado observado.
5. Defina um experimento pequeno com entrada conhecida e resultado esperado.
6. Execute quando houver ambiente e autorização para aquele alvo; caso contrário, marque “não testado”.
7. Atualize a referência e o histórico somente com o que foi realmente verificado.

Uma busca finita não cobre todos os programas, games ou fóruns. A base é um material versionado de consulta, não uma alteração dos pesos do modelo. Atualizações futuras precisam ser solicitadas e executadas; não há tarefa recorrente configurada.

## Registro de conhecimento

Para cada descoberta nova, registre:

```text
Pergunta:
Fonte e URL exata:
Data de acesso:
Versão / arquitetura:
Síntese própria:
Evidência local / hash:
Experimento e resultado:
Estado: documentado | reproduzido | hipótese | não testado
Limitações / divergências:
Arquivos atualizados:
```

Ao encerrar uma atualização, revise links locais, consistência das rotas e afirmações de validação. Fontes inacessíveis continuam pendentes. Nunca transforme um teste proposto em um teste realizado no histórico.

