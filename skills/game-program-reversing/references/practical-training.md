# Trilha prática: modificação de jogos e análise de proteção

Esta trilha desenvolve fundamentos usados na análise de modificações de jogos,
trainers e desafios de engenharia reversa de licenciamento. Execute os exercícios
com programas próprios ou laboratórios feitos para esse estudo. Não transfira a
conclusão de um exemplo simples para anti-cheats, DRM ou sistemas comerciais.

Esta restrição descreve os exercícios incluídos neste arquivo, não os alvos que
a skill pode analisar. Para um programa real e seu arquivo de licença, siga o
[fluxo de análise real](real-license-analysis.md) em vez de substituir o alvo
por uma fixture. Use os exemplos abaixo para praticar ou testar uma hipótese isolada.

## Exercício executável 1: estado de jogo próprio

O arquivo `labs/game_state.c`, na raiz do repositório, define uma estrutura com
vida e pontuação e funções pequenas de dano e recompensa. O script
`scripts/run_practice_labs.py` compila uma biblioteca temporária, examina seus
símbolos, decodifica todos os bytes de `apply_damage` com Capstone e chama a
biblioteca por ctypes.

O experimento compara dano normal com uma alteração deliberada de vida na memória
do objeto do próprio script. Também verifica dano negativo, limite inferior da
vida e pontuação. É uma modificação controlada do estado em processo próprio,
não um scanner de memória, injetor ou trainer genérico de terceiros.

Resultado esperado: relacionar layout de estrutura, bytes de função e comportamento
concreto. O hash do fonte e do binário gerado e os resultados ficam no relatório.
O fonte está disponível como referência; isso é uma demonstração de análise de
artefato conhecido, não evidência de descoberta independente em binário desconhecido.

## Exercício executável 2: licença sintética assinada

O mesmo script cria claims de aplicação, expiração e recurso habilitado. Assina
esses dados com Ed25519 usando chave efêmera e verifica cinco situações:

1. Licença sintética válida aceita.
2. Campo alterado sem nova assinatura rejeitado.
3. Licença expirada rejeitada.
4. Aplicação diferente rejeitada.
5. Recurso ausente rejeitado.

A verificação da assinatura ocorre antes de usar os claims. A fixture não é um
servidor de licenciamento pronto para produção: não modela persistência, revogação,
relógio real, parser hostil, segredo distribuído ou todas as falhas operacionais.
Não é um crack nem demonstra remoção de proteção comercial; serve para entender
o contrato que uma análise de licenciamento precisa verificar.

## Reproduzir

Na raiz do repositório, em Linux x86-64 com GCC e as dependências do toolkit:

```bash
.venv/bin/python scripts/run_practice_labs.py
```

Use o Python do ambiente instalado se ele tiver outro caminho. O script compila
somente o fonte original incluído, usa diretório temporário e não persiste chaves
ou binários. Ele executa código nativo gerado a partir dessa fixture. Falhas
interrompem o processo; só reporte aprovação se a execução terminar com sucesso.

## Próximos exercícios, ainda não executados

- Localizar os campos da fixture por observação de acessos em um depurador,
  registrando módulo, base e watchpoint.
- Comparar duas compilações próprias com uma mudança de lógica e explicar o diff.
- Repetir a análise em binário próprio sem símbolos, mantendo fonte como gabarito
  separado da investigação.
- Analisar um save sintético e escrever um leitor limitado aos campos confirmados.
- Modelar validação de ações no servidor de um jogo próprio e medir casos válidos,
  inválidos e falsos positivos.
- Criar um desafio próprio de validação simples e estudar seu grafo de condições,
  sem generalizar o resultado para assinatura criptográfica ou produto comercial.

Se faltar uma técnica ou ferramenta para a etapa escolhida, pesquise e instale
o necessário dentro do escopo autorizado, conforme os demais guias da skill.

## Critério para alegar experiência

Classifique separadamente: documentação consultada, exercício proposto, exercício
executado e alvo analisado com evidências. Para cada competência, registre artefato,
versões, passos, resultado e limitações. Não se autodenomine especialista em cheats
ou cracks por possuir um catálogo de ferramentas ou passar nestes exemplos.

O resultado desta trilha está em `docs/verification/practice-labs-2026-10-16.json`
na raiz do projeto. Somente os checks desse arquivo representam execução comprovada.

