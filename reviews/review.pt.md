# Independent native review of README.pt.md (score 7.5/10)

This is a faithful, complete translation with no omitted caveats, no invented claims and sound technical terminology. Several false friends and calques (Retratado, zoológico, distilação, "equipe de manutenção", decimal points) keep it from being publish-ready until they are fixed.

1. [major] line 435
   quote: **Retratado na v3: "o layer streaming é limitado pela transferência de host para dispositivo, não pela GPU."**
   problem: "Retratado" is a false friend: in Portuguese "retratar" means to portray or depict. It also does not agree in gender with "explicação". The English means "Retracted".
   fix: **Retirada na v3: "o layer streaming é limitado pela transferência de host para dispositivo, e não pela GPU."**

2. [major] line 64
   quote: **119.6 tok/s, pico de 3.32 GB** — idêntico bit a bit a
uma execução residente normal, e reproduzido de forma independente em uma H100 a 113.00 tok/s
   problem: Brazilian Portuguese uses a decimal comma, not a point (119,6; 3,32; 113,00; 4,8%; 1,4%; 0,20%; 71,3%; 9,8%). The point is used throughout the prose, the alt text and the captions.
   fix: **119,6 tok/s, pico de 3,32 GB** — idêntico bit a bit a uma execução residente normal, e reproduzido de forma independente em uma H100 a 113,00 tok/s. Apply the same rule to every decimal in the file, but not to version numbers (v0.75.0) or code.

3. [major] line 268
   quote: zoológico de otimizadores e PEFT
   problem: Literal calque of "optimizer & PEFT zoo". It is unnatural and a native reader would not understand it as a catalogue.
   fix: catálogo de otimizadores e métodos PEFT

4. [major] line 267
   quote: distilação
   problem: Spelling error. The correct word is "destilação".
   fix: destilação

5. [major] line 267
   quote: detectores de endurecimento de loops
   problem: "Loop-hardening detectors" was rendered word for word. "Endurecimento" does not mean making robust in this context and reads as nonsense.
   fix: detectores de proteção contra loops de geração

6. [major] line 94
   quote: vieram de fora da equipe de
manutenção
   problem: The English says "from outside the maintainer", a single person. Elsewhere the file uses "mantenedor" in the singular and says the project is run from one laptop. "Equipe de manutenção" invents a team.
   fix: vieram de fora, não do mantenedor, de 22 pessoas.

7. [major] line 66
   quote: antes do reparo de correção da v0.73.0
   problem: "Correctness repair" is a clumsy calque. "Reparo de correção" is tautological and does not say it is a fix for incorrect results. The word "reparo" is also repeated in the "#331" caption.
   fix: antes da correção de corretude da v0.73.0

8. [major] line 112
   quote: A loss de validação não existia em lugar nenhum.
   problem: Mistranslation of "existed nowhere". The next sentence says the loss was computed and then discarded, so it did exist. The meaning is that it was not recorded or shown anywhere.
   fix: A loss de validação não ficava registrada em lugar nenhum.

9. [major] line 128
   quote: que travam na extensão nativa antes mesmo de o Soup rodar
   problem: "Crash" was translated as "travar", which means to hang or freeze. Line 121 uses "trava" for "hangs", so the two different English words are collapsed into one.
   fix: que quebram na extensão nativa antes mesmo de o Soup rodar

10. [major] line 389
   quote: Eles são entregues atrás de
gates honestos de "requer \<hardware\>"
   problem: "Ship behind honest gates" was translated literally. "Entregues atrás de" is stiff and unidiomatic. It weakens the "honest limits" idea.
   fix: Eles são lançados com avisos honestos de "requer \<hardware\>", em vez de afirmações não verificadas;

11. [minor] line 254
   quote: Uma chave que nenhum modelo
> declara
   problem: In the source, "model" means a Pydantic model. In this file "modelo" otherwise means an LLM, so the sentence is ambiguous.
   fix: Uma chave que nenhum modelo do schema declara

12. [minor] line 101
   quote: Todas as receitas e templates carregam sem problemas, os nomes das chaves
são escapados antes de chegar ao terminal e a varredura tem limite.
   problem: "Load clean" means without warnings, and "sem problemas" is vague. "A varredura tem limite" is a weak rendering of "the scan is bounded".
   fix: Todas as receitas e templates carregam sem avisos, os nomes das chaves são escapados antes de chegar ao terminal e a varredura é limitada.

13. [minor] line 456
   quote: um foi resolvido e quatro foram
  reduzidos
   problem: "One closed and four more narrowed" lost "more" ("outros"). "Reduzidos" is vague for "narrowed".
   fix: um foi resolvido e outros quatro tiveram o escopo reduzido

14. [minor] line 447
   quote: Um defeito silencioso de gradiente errado, encontrado e reparado.
   problem: "Silent wrong-gradient defect" is a calque. Also "gated against controls" (line 450) was flattened to "validado", losing the gate sense.
   fix: Um defeito silencioso que gerava gradientes errados, encontrado e corrigido. ... a correção só é liberada após passar por controles em modelos reais de 32B e 72B.

15. [minor] line 451
   quote: em vez de brinquedos de três camadas
   problem: "Toys" used as a noun is a calque. A native speaker says "modelos de brinquedo".
   fix: em vez de modelos de brinquedo de três camadas

16. [minor] line 444
   quote: Replicação em um hardware nada parecido com o original
   problem: Awkward, with the article "um" before "hardware" and a stiff "nada parecido com".
   fix: Replicação em um hardware completamente diferente do original

17. [minor] line 212
   quote: O `soup ui` serve um painel local
   problem: "Serves" is a calque. Used with a dashboard it sounds odd in Portuguese.
   fix: O `soup ui` sobe um painel local

18. [minor] line 210
   quote: ## Interface Web
   problem: The heading says "Interface Web" but the rest of the file says "Web UI" (lines 119, 223, 272). The terminology is inconsistent, and the link label "Documentação da Web UI" does not match the heading it sits under.
   fix: Use "Interface Web" everywhere, with "[Documentação da interface web]", or keep "Web UI" everywhere including the heading.

19. [minor] line 85
   quote: Um simples arquivo YAML é tudo de que você precisa.
   problem: "Um simples" before the noun is an English calque. A native speaker would put the adjective after it or rephrase.
   fix: Basta um arquivo YAML simples.

20. [minor] line 309
   quote: acompanham como receitas prontas
   problem: "Ship as ready-made recipes" is rendered with "acompanham", which suggests they merely accompany the models.
   fix: já vêm incluídos como receitas prontas

21. [minor] line 307
   quote: ## Modelos Suportados
   problem: "Suportado" is a calque of "supported", used in a heading, a table header and prose (line 336 "não é suportado"). Native editors prefer "compatível" or "com suporte".
   fix: ## Modelos compatíveis (and "o 3.13+ ainda não é compatível")

22. [minor] line 405
   quote: Bugs e pedidos de recursos devem ir para o
   problem: "Pedidos de recursos" is a calque of "feature requests". "Recursos" suggests resources.
   fix: Bugs e sugestões de funcionalidades devem ir para o

23. [minor] line 389
   quote: rodar uma das issues
[`help wanted`](...)
e publicar os números
   problem: "Running one of the issues" is a literal rendering. Issues are not run. It means carrying out what the issue asks for.
   fix: executar o que uma das issues [`help wanted`](...) pede e publicar os números

24. [minor] line 270
   quote: o pipeline com paridade Axolotl/LF
   problem: The structure is a calque. In Portuguese the parity is with something.
   fix: o pipeline com paridade em relação ao Axolotl/LF

25. [minor] line 271
   quote: tunabilidade
   problem: "Tunability" was Portuguesised into a barely used word.
   fix: capacidade de ajuste (tunability)

26. [minor] line 346
   quote: ## Solução de Problemas
   problem: Headings are inconsistent. Most use English-style Title Case ("Formatos de Dados", "Comandos Comuns", "Início Rápido"), but "Como citar o Soup" uses sentence case. Brazilian Portuguese normally uses sentence case.
   fix: Use sentence case for all headings ("Solução de problemas", "Formatos de dados", "Comandos comuns", "Início rápido"). Update the anchors at lines 16-19 and 252 to match.

27. [nit] line 482
   quote: Copyright © os colaboradores do Soup.
   problem: "© os" is ungrammatical because the article is left over from the English "the".
   fix: Copyright © Colaboradores do Soup.

28. [nit] line 251
   quote: única fonte da verdade
   problem: The usual developer idiom for "single source of truth" is "fonte única da verdade".
   fix: fonte única da verdade

29. [nit] line 374
   quote: Ele é construído e mantido de forma aberta
   problem: "In the open" was rendered as "de forma aberta", which is stiff.
   fix: Ele é construído e mantido abertamente

30. [nit] line 383
   quote: pelo Stripe
   problem: Stripe is a company, and the feminine article is more usual here.
   fix: pela Stripe

31. [nit] line 196
   quote: ### 3. Treine, teste, publique
   problem: "Ship" in this context is closer to delivering than publishing, since the commands also export and merge.
   fix: ### 3. Treine, teste, entregue
