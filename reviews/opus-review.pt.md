# Opus review of README.pt.md (8/10)

This is a faithful, fluent and nearly complete Brazilian Portuguese translation. The numbers, caveats, negations and the honest-limits wording all survive intact. The problems left are one real mistranslation (loop-hardening), a softened 'gates' that reads as mere warnings, an ambiguous 'protocolo de correção' where the source means correctness, and some inconsistent terms (repair, Web UI, release, opt-in) plus a few calques that should be fixed before publishing.

Source check: The text reads as translated directly from the English. There is no sign of Turkish word order or Turkish calques: verbs come in normal SVO position and there are no postposition-style constructions. The only calques left are English ones ('contra' for 'against', 'pertence às' for 'belongs in', 'ele chega à mesma pessoa' for 'it reaches the same person', 'não conseguia ser importado'), and these confirm English was the source.

1. [major] line 267
   quote: detectores de proteção contra loops de geração
   problem: Mistranslation. 'Loop-hardening detectors' in docs/training.md#loop-hardening are detectors that harden the training loop (reward-hacking halts and similar). They have nothing to do with generation loops or repetitive output.
   fix: detectores de blindagem do loop de treinamento

2. [major] line 389
   quote: Eles são lançados com
avisos honestos de "requer \<hardware\>"
   problem: 'Ship behind honest "requires <hardware>" gates' means the features are locked behind a hardware requirement. 'Avisos' (warnings) weakens this and loses the sense that they are blocked until someone validates them.
   fix: Eles são lançados atrás de bloqueios honestos do tipo "requer \<hardware\>"

3. [major] line 424
   quote: junto com o protocolo de
correção que verifica uma execução com streaming contra uma residente
   problem: 'Correctness protocol' is rendered as 'protocolo de correção', which a Brazilian reader takes as 'correction/fix protocol'. That collides with 'correção' = repair used elsewhere. 'Contra' is also a calque of 'against'.
   fix: junto com o protocolo de verificação de corretude que compara uma execução com streaming a uma execução residente

4. [minor] line 66
   quote: antes da correção de corretude da v0.73.0
   problem: 'Correção de corretude' is redundant and clumsy. 'Repair' is also translated inconsistently across the file: correção (66, 449), reparo (76, 77, 445), corrigido (447).
   fix: antes do reparo de corretude da v0.73.0 (and use 'reparo' consistently for 'repair')

5. [minor] line 449
   quote: a correção só é liberada após passar por controles
  em modelos reais de 32B e 72B
   problem: 'The repair is gated against controls on real 32B and 72B' means it is validated against control runs. 'Só é liberada' adds a release step the source does not mention. 'Correção' should be 'reparo' for consistency.
   fix: o reparo é validado contra execuções de controle em modelos reais de 32B e 72B

6. [minor] line 69
   quote: É opcional
(`stream_layers: true`)
   problem: 'Opt-in' means off by default and must be enabled explicitly. 'Opcional' is vaguer, and line 370 keeps 'opt-in', so the terminology is inconsistent.
   fix: Precisa ser ativado explicitamente (`stream_layers: true`)

7. [minor] line 104
   quote: Todas as receitas e templates carregam sem avisos
   problem: 'Load clean' in this context means they load without being rejected or erroring under the new strict key check. 'Sem avisos' (without warnings) shifts the meaning.
   fix: Todas as receitas e templates carregam sem erros

8. [minor] line 119
   quote: Os endpoints de leitura da Web UI
   problem: Inconsistent terminology. The section heading and link labels use 'Interface Web' (lines 17, 210, 223), but lines 119 and 272 use 'Web UI'.
   fix: Os endpoints de leitura da interface web

9. [minor] line 123
   quote: no 2.5.1, o `trl>=0.29` não
  conseguia ser importado
   problem: 'Não conseguia ser importado' is a stiff calque, since a passive subject cannot 'conseguir'. 'No 2.5.1' is also unclear about what 2.5.1 refers to.
   fix: com o torch 2.5.1, o `trl>=0.29` não podia ser importado

10. [minor] line 94
   quote: **Todos os 60 pull requests desta versão vieram de fora, não do
mantenedor**, de 22 pessoas.
   problem: The trailing ', de 22 pessoas' dangles awkwardly after the bolded clause.
   fix: **Todos os 60 pull requests desta versão vieram de fora, não do mantenedor**: foram 22 pessoas no total.

11. [minor] line 437
   quote: Medimos
  em 11 de agosto e é falso na configuração publicada
   problem: There is no explicit object or subject. 'Medimos ... e é falso' reads as fragmentary, because the referent (the claim) is feminine and implicit.
   fix: Medimos isso em 11 de agosto, e a afirmação é falsa na configuração publicada

12. [minor] line 439
   quote: do teto de GEMM da mesma sessão daquela placa
   problem: A clunky chain of genitives that is hard to parse.
   fix: do teto de GEMM daquela placa, medido na mesma sessão

13. [minor] line 326
   quote: imagem publicada no GHCR a cada release
   problem: 'Release' is left in English here, while elsewhere it is translated as 'versão' (line 94 'desta versão').
   fix: imagem publicada no GHCR a cada nova versão

14. [minor] line 412
   quote: Tudo o que ainda deva ser encontrável daqui a seis meses
pertence às Issues ou às Discussions
   problem: 'Pertence às' calques 'belongs in'. In Portuguese, 'deve ir para' is natural.
   fix: Tudo o que precisar ser encontrado daqui a seis meses deve ir para as Issues ou as Discussions

15. [nit] line 419
   quote: ele chega à mesma pessoa e serve bem como alternativa
   problem: A literal calque of 'it reaches the same person'. It sounds unnatural.
   fix: as mensagens chegam à mesma pessoa, e ele serve bem como alternativa

16. [nit] line 381
   quote: uma vez só, em qualquer valor
   problem: 'Uma vez só' is colloquial and stiff for 'one-off'. Donation pages normally say 'doação única'.
   fix: doação única, de qualquer valor

17. [nit] line 374
   quote: O Soup é Apache-2.0 e gratuito
   problem: Calque. In Portuguese you say a project is licensed under Apache-2.0.
   fix: O Soup é licenciado sob Apache-2.0 e gratuito

18. [nit] line 175
   quote: e é por isso que aparecem primeiro acima
   problem: 'Primeiro acima' is awkward.
   fix: e é por isso que aparecem em primeiro lugar na lista acima

19. [nit] line 99
   quote: ou uma chave que só existe em um Soup mais novo, era descartado
   problem: Agreement. The coordinated subject (um erro ... ou uma chave) takes masculine singular 'descartado' after the feminine noun closest to it, which reads oddly.
   fix: ou uma chave que só existe em um Soup mais novo, eram descartados

20. [nit] line 460
   quote: continuam citáveis nos seus próprios DOIs de versão
   problem: 'Citáveis nos DOIs' is an odd preposition choice.
   fix: continuam citáveis pelos seus próprios DOIs de versão

21. [nit] line 172
   quote: Isso é o
> [PEP 668]
   problem: The Brazilian Python community usually treats PEP (Proposta) as feminine.
   fix: Isso é a [PEP 668]

22. [nit] line 2
   quote: <a href="README.ru.md">Русский</a>
   problem: The language bar links README.es.md and README.ru.md, which do not exist in the repo yet (only the ar/ja/tr translations exist). Unless they ship together, these links will be broken.
   fix: Link only languages that exist in the same commit, or ship all of them together.
