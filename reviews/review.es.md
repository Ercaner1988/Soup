# Independent native review of README.es.md (score 8/10)

The translation is faithful and complete, with natural, consistent usted register and well-chosen terminology. It has one clear blocker, the donation link labelled "Done" instead of "Donar", and a few meaning-affecting ambiguities (the PR/people count and the PyTorch wheels sentence) that should be fixed before publishing.

1. [blocker] line 379
   quote: **[❤️ Done](https://buy.stripe.com/4gMcN441k3pha3T19ye7m04)**
   problem: The English call to action is "Donate". "Done" is an English word that in this context means "finished", so the donation button label is wrong and meaningless to a Spanish reader.
   fix: **[❤️ Donar](https://buy.stripe.com/4gMcN441k3pha3T19ye7m04)**

2. [major] line 126
   quote: En 3.13+, pip solía resolver wheels de PyTorch sin probar que
> fallan en la extensión nativa antes de que Soup llegue a ejecutarse.
   problem: The relative clause is lost. "sin probar que fallan" reads as "without testing that they fail". The English means untested wheels that crash in the native extension before Soup even runs.
   fix: En 3.13+, pip solía resolver wheels de PyTorch sin probar, que se bloquean en la extensión nativa incluso antes de que Soup llegue a ejecutarse.

3. [major] line 93
   quote: **Los 60 pull requests de esta versión vinieron de personas ajenas al
mantenedor**, 22 en total.
   problem: "22 en total" is ambiguous: it could mean 22 pull requests. The English says the 60 PRs came from 22 people. "personas ajenas al mantenedor" is also stiff.
   fix: **Los 60 pull requests de esta versión vinieron de personas distintas del mantenedor**: 22 colaboradores en total.

4. [major] line 387
   quote: Se publican tras
compuertas honestas de "requires \<hardware\>" en lugar de afirmaciones sin verificar
   problem: "compuertas honestas" is a literal calque of "honest gates" and sounds odd in Spanish. The subject of "Se publican" is also unclear (it means "they ship"). The "honest limits" nuance is weakened.
   fix: Esos puntos se publican con una advertencia explícita del tipo «requiere \<hardware\>», en lugar de afirmaciones sin verificar, así que

5. [major] line 389
   quote: ejecutar uno de los issues
   problem: "Running an issue" translated literally is nonsensical in Spanish: an issue is not executed. The intent is running the experiment or benchmark that the issue describes.
   fix: ejecutar lo que pide uno de los issues

6. [major] line 435
   quote: La
  medimos el 11 de agosto y es falsa en la configuración publicada
   problem: The English "We measured it" refers to the claim. "La medimos" has an unclear antecedent (the feminine "inferencia" or "réplica"). It should be "Lo medimos" for the claim itself.
   fix: Lo medimos el 11 de agosto y resulta ser falso en la configuración publicada

7. [minor] line 104
   quote: los nombres de clave se escapan antes de llegar a la terminal
   problem: "se escapan" is a calque of "are escaped". In Spanish it reads as "they flee". A native developer would say a escape or sanitisation is applied.
   fix: a los nombres de clave se les aplica escape (se sanean) antes de mostrarlos en la terminal

8. [minor] line 66
   quote: que costó
−4.8 % en 32B
   problem: "costó −4.8 %" is a literal rendering of "cost −4.8%" and sounds unnatural (a cost of a negative number).
   fix: que supuso una pérdida de 4.8 % de rendimiento en 32B

9. [minor] line 62
   quote: la GPU de un portátil de 4 GB
   problem: "portátil" as a noun for a laptop is Peninsular Spanish. The brief asks for neutral Latin-American/international Spanish (where "laptop" or "computadora portátil" is used), and the file elsewhere uses LatAm "Video". It recurs on lines 62, 77, 373, 384 and 421.
   fix: la GPU de una laptop de 4 GB (y igual en las demás apariciones)

10. [minor] line 103
   quote: reasignación de `lora:` en la raíz
   problem: "remap" rendered as "reasignación" is imprecise (it means reassigning or moving a key from the root into the nested structure).
   fix: el remapeo de `lora:` desde la raíz que el esquema admite

11. [minor] line 108
   quote: MLX también maneja el panel en vivo, el rastreador y
`soup ui`
   problem: "drives" (powers or feeds) is rendered with the weak "maneja", which suggests managing rather than supplying data to the dashboard.
   fix: MLX ahora también alimenta el panel en vivo, el rastreador y `soup ui`

12. [minor] line 111
   quote: La pérdida de validación no existía en ninguna parte.
   problem: "existed nowhere" is calqued. The point is that it was computed but never recorded anywhere, which the next sentence explains.
   fix: La pérdida de validación no se registraba en ningún lado.

13. [minor] line 92
   quote: una receta distinta a la de transformers,
en silencio
   problem: "distinta a" is considered incorrect in careful usage (use "distinta de"), and "en silencio" is a calque of "silently".
   fix: una receta distinta de la de transformers, sin avisar

14. [minor] line 82
   quote: dedican entre 30 y 50 % de su tiempo
   problem: The range needs the article in standard usage ("entre el 30 y el 50 %"). Also "una molestia" on line 82 undersells "painful".
   fix: dedican entre el 30 y el 50 % de su tiempo

15. [minor] line 82
   quote: Entrenar LLM sigue siendo una molestia.
   problem: "painful" is softened to "una molestia". The original conveys real difficulty and frustration. The same softening happens with "complicación" for "pain" on line 54.
   fix: Entrenar LLM sigue siendo un dolor de cabeza.

16. [minor] line 264
   quote: detectores de endurecimiento de bucles
   problem: A literal calque of "loop-hardening detectors". "Endurecimiento" does not convey robustness or hardening in this technical sense.
   fix: detectores de robustecimiento de bucles (loop hardening)

17. [minor] line 266
   quote: zoo de optimizadores y PEFT
   problem: "zoo" is an English calque used jokingly. A Spanish reader will not recognise it as "wide catalogue".
   fix: catálogo de optimizadores y métodos PEFT

18. [minor] line 270
   quote: (entrene y mida su propio borrador)
   problem: "draft" in speculative decoding is the draft model. "su propio borrador" alone suggests a text draft.
   fix: (entrene y mida su propio modelo borrador)

19. [minor] line 11
   quote: post-entrenamiento
   problem: Inconsistent with "preentrenamiento" elsewhere (lines 265 and 266). The RAE-preferred form has no hyphen, and the English "post-train" is a verb here.
   fix: Haga fine-tuning y postentrenamiento de LLM con un solo comando.

20. [minor] line 339
   quote: Todas las tareas de entrenamiento se ejecutan en CPU para pruebas
   problem: Rendered more categorically than the English ("all training tasks run on CPU for testing", meaning they can be run). Read as a mandatory behaviour, it contradicts the GPU recommendation.
   fix: Todas las tareas de entrenamiento pueden ejecutarse en CPU con fines de prueba (la cuantización se desactiva automáticamente).

21. [minor] line 367
   quote: informar de una vulnerabilidad
   problem: Inconsistent terminology: "reportar/reportes" is used elsewhere for "report" ("reportes de seguridad", "se reportó"), while this line uses "informar de".
   fix: reportar una vulnerabilidad

22. [minor] line 384
   quote: el trabajo que depende de hardware
   problem: "hardware-gated work" means work blocked or conditioned by hardware availability. The Spanish is vague, since much work "depends on" hardware.
   fix: el trabajo condicionado por el hardware

23. [minor] line 442
   quote: Réplica en un hardware que no se parece en nada al original
   problem: Stiff, literal rendering of "hardware nothing like the original".
   fix: Réplica en un hardware completamente distinto del original

24. [minor] line 457
   quote: siempre resuelve a
la última versión
   problem: "resolves to" is a calque. Spanish uses "apunta a" or "redirige a".
   fix: siempre redirige a la última versión

25. [minor] line 462
   quote: Los registros de medición detrás de cada cifra
   problem: The English says "every number in it" (in the paper). The reference to the paper is dropped, so it is unclear which figures are meant.
   fix: Los registros de medición detrás de cada cifra del artículo están en [`benchmarks/`](benchmarks/)

26. [nit] line 254
   quote: de modo que la ejecución seguía con el ajuste simplemente sin aplicar
   problem: Clumsy. "seguía con el ajuste ... sin aplicar" is a literal order from the English.
   fix: de modo que la ejecución continuaba sin aplicar ese ajuste

27. [nit] line 255
   quote: La v0.74 lo informaba al cargar
   problem: "informar" without "de" or "al respecto" is slightly off ("lo avisaba" or "lo reportaba" is more natural).
   fix: La v0.74 lo advertía al cargar la configuración

28. [nit] line 437
   quote: (el registro)
   problem: "the record" as link text for a benchmark log is vague. "registro" could be read as a log or a registry.
   fix: (el informe de medición)

29. [nit] line 429
   quote: que es también la forma más breve de describir para qué sirve el artículo
   problem: A heavy literal calque. "para qué sirve el artículo" is unusual for what a paper is for.
   fix: que es también la manera más breve de resumir el propósito del artículo

30. [nit] line 414
   quote: (reportes de seguridad, consulte [SECURITY.md](SECURITY.md),
asuntos del Código de conducta o prensa)
   problem: The imperative "consulte" is embedded inside a list of nouns, so the parenthesis is syntactically messy.
   fix: (reportes de seguridad —véase [SECURITY.md](SECURITY.md)—, asuntos del Código de conducta o prensa)
