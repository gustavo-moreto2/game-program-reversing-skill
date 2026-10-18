# Atualização verificável

“Atualizado” precisa ter escopo, fonte e data. Não afirme que toda a base ou todos os métodos do mundo estão 100% atualizados. Use as verificações abaixo para sustentar o estado de cada dependência.

## Ao usar uma ferramenta

1. Confirme a versão instalada e a função necessária.
2. Consulte release/changelog oficial quando a atualidade afetar a tarefa.
3. Diferencie versão estável, prerelease e branch de desenvolvimento.
4. Confira compatibilidade do SO, Python/Java, arquitetura, hospedeiro e plugins.
5. Se uma atualização resolver o objetivo, instale dentro do escopo autorizado e verifique a função após a mudança.
6. Registre versão anterior/nova, data, fonte, resultado e limitações.

A release mais recente anunciada pode não ter uma build compatível com o ambiente atual. Não force a atualização de um hospedeiro inteiro para satisfazer um plugin sem avaliar o impacto nas demais integrações.

## Toolkit instalado nesta sessão

O arquivo `requirements-toolkit.txt` fixa as versões efetivamente instaladas no laboratório. Não é uma declaração de que elas serão as mais novas para sempre.

No executor desta sessão, o ambiente está em `/workspace/reversing-tools-env`. Ele não é distribuído no ZIP e não representa instalação no computador do usuário.

Para reproduzir em um ambiente Python/Linux compatível:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --index-url https://pypi.org/simple --only-binary=:all: -r requirements-toolkit.txt
.venv/bin/python scripts/verify_toolkit.py
```

Em outro SO, use os caminhos do Python do venv correspondentes. A disponibilidade de wheels depende da combinação de sistema, arquitetura e versão do Python. O script de verificação atual requer um interpretador ELF de 64 bits; não é teste de Windows/macOS.

Para consultar a versão que o PyPI anuncia para cada uma das quatro dependências principais:

```bash
.venv/bin/python scripts/verify_toolkit.py --check-updates
```

Esse comando consulta metadados públicos e executa os checks locais. Não instala atualizações. Falhas de rede ficam como estado desconhecido. Igualdade com a versão anunciada é uma observação daquele momento, não uma análise de segurança ou garantia de compatibilidade futura.

Não há atualização silenciosa em segundo plano nem tarefa recorrente configurada. Faça a checagem ao iniciar uma tarefa que dependa dessas versões e sempre que houver um problema de compatibilidade.

