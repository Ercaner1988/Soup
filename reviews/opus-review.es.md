# Opus review of README.es.md (8.5/10)

This is a faithful, complete and mostly natural Spanish translation: every section, number, caveat and the honest-limits wording (the retraction, the pending re-measurement, the BETA status, the self-critical DeepSpeed result) are kept, and the usted register is consistent throughout. What remains is mostly polish: one false friend ('se bloquean' for 'crash'), one ungrammatical 'y que', a few calques and mixed terminology ('gate', 'rastreador', 'funciones'), and some small agreement and punctuation slips.

Source check: It reads as translated straight from the English. I found no Turkish word order or calques, and nothing else that suggests a relay through another language. The awkward spots, such as 'una clave de configuración desconocida ahora rechaza la carga' and 'a los nombres de clave se les aplica escape', are literal renderings of the English phrasing, not of any third language.

1. [major] line 127
   quote: > se bloquean en la extensión nativa incluso antes de que Soup llegue a ejecutarse.
   problem: False friend in this context: 'crash' means the process fails or aborts, but 'se bloquean' reads as 'hang/freeze' (the same verb is used correctly for 'hangs' at line 120, 'se cuelga'). This changes the technical meaning.
   fix: > fallan en la extensión nativa incluso antes de que Soup llegue a ejecutarse.

2. [major] line 384
   quote: Las donaciones sirven para comprar tiempo de GPU para el trabajo condicionado por el hardware (multi-GPU, validación de 8B+, Apple Silicon)
y que una única laptop de 4 GB no puede abordar.
   problem: Ungrammatical coordination: 'y que' joins a relative clause to a participle phrase ('condicionado por el hardware'), so the sentence does not parse. The doubled 'para ... para' is also clumsy.
   fix: Las donaciones se destinan a comprar tiempo de GPU para el trabajo que depende del hardware (multi-GPU, validación de 8B+, Apple Silicon) y que una única laptop de 4 GB no puede cubrir.

3. [minor] line 97
   quote: una clave de configuración desconocida ahora rechaza la carga.
   problem: Calque of 'refuses the load': in Spanish it sounds as if the key itself rejects the loading, which is illogical.
   fix: una clave de configuración desconocida ahora impide cargar la configuración.

4. [minor] line 104
   quote: a los nombres de clave se les aplica escape antes de llegar a la terminal y el análisis está acotado.
   problem: Stiff, machine-like construction for 'key names are escaped'.
   fix: los nombres de clave se escapan antes de mostrarse en la terminal y el análisis tiene un límite acotado.

5. [minor] line 101
   quote: El detector aplica el remapeo de `lora:` desde la raíz que el esquema admite
   problem: 'desde la raíz' is ambiguous (it can read as 'starting from the root'). The source means a remap of the root-level `lora:` key. Also, 'admite' is weak for 'has honoured'.
   fix: El detector aplica la reasignación de `lora:` en el nivel raíz que el esquema respeta

6. [minor] line 109
   quote: MLX ahora también alimenta el panel en vivo, el rastreador y
   problem: Inconsistent terminology: 'tracker' (experiment tracker) is 'rastreador' here but 'seguimiento de experimentos' in the docs table (line 273). 'Rastreador' sounds like a GPS or web crawler.
   fix: MLX ahora también alimenta el panel en vivo, el seguimiento de experimentos y

7. [minor] line 269
   quote: Diseño y gate de evaluación, entrenamiento controlado por evaluación
   problem: Inconsistent handling of 'gate': it is left in English here and at line 272 ('gate de CI'), yet translated as 'controlado por' in the same cell. English left where a natural Spanish term exists.
   fix: Diseño de evaluaciones y umbral de aprobación, entrenamiento condicionado a la evaluación

8. [minor] line 272
   quote: gate de CI (`soup ci init`)
   problem: Untranslated 'gate'; inconsistent with the other renderings.
   fix: control de aprobación en CI (`soup ci init`)

9. [minor] line 261
   quote: La referencia completa de funciones está en [`docs/`](docs/).
   problem: In a developer README 'funciones' reads as code functions. 'Feature' here means product functionality. The same issue appears at line 403 ('solicitudes de funciones').
   fix: La referencia completa de funcionalidades está en [`docs/`](docs/).

10. [minor] line 336
   quote: GPU con CUDA (recomendado), Apple Silicon (MPS) o CPU (experimental, muy lenta)
   problem: Gender agreement: 'GPU' is feminine in Spanish, as the same line's 'CPU ... lenta' shows, so 'recomendado' should be 'recomendada'.
   fix: GPU con CUDA (recomendada), Apple Silicon (MPS) o CPU (experimental, muy lenta)

11. [minor] line 85
   quote: Nunca más tendrá que conectarse por SSH a un equipo con la GPU averiada.
   problem: Meaning shift: the source says the GPU box (the machine) is broken, not that its GPU is damaged.
   fix: Nunca más tendrá que conectarse por SSH a un servidor de GPU que no funciona.

12. [minor] line 410
   quote: Todo lo que deba poder encontrarse dentro de seis meses
   problem: The word 'still' is dropped, which weakens the point that the content must stay findable over time. 'deba poder encontrarse' is also clunky.
   fix: Todo lo que deba seguir siendo fácil de encontrar dentro de seis meses

13. [minor] line 387
   quote: Esos puntos se publican con una
advertencia explícita del tipo «requires \<hardware\>», en lugar de afirmaciones sin verificar
   problem: The 'honest' nuance of the gates is lost, and 'esos puntos' repeats from the previous sentence. The «» quotes are also inconsistent with the straight double quotes used elsewhere in the file (lines 381, 433).
   fix: Esas funciones se publican tras un aviso honesto de tipo "requires \<hardware\>", en lugar de afirmaciones sin verificar

14. [minor] line 433
   quote: **Retractado en la v3: "el layer streaming está limitado por la transferencia de host a dispositivo, no por la GPU."**
   problem: 'Retractado' (masculine, normally said of persons who retract) sits awkwardly in front of a quoted claim. Spanish also puts the period outside the closing quote.
   fix: **Afirmación retirada en la v3: "el layer streaming está limitado por la transferencia de host a dispositivo, no por la GPU".**

15. [minor] line 459
   quote: la retractación anterior es una versión nueva
   problem: 'anterior' is ambiguous: it can mean 'the previous/earlier retraction', but the source means 'the retraction above'.
   fix: la retractación descrita arriba es una versión nueva

16. [nit] line 133
   quote: ### 1. Instalación
   problem: Heading style is inconsistent with steps 2 and 3, which use the imperative ('Cree', 'Entrene'). The source uses the imperative throughout.
   fix: ### 1. Instale

17. [nit] line 310
   quote: Phi-4 y más de 100 otros vienen como recetas listas para usar
   problem: 'más de 100 otros' is unidiomatic in Spanish.
   fix: Phi-4 y más de 100 modelos más vienen como recetas listas para usar

18. [nit] line 281
   quote: basta con apuntar `data.train` a un archivo y nada más cambia.
   problem: Literal rendering; Spanish would say 'no hay que cambiar nada más'.
   fix: basta con apuntar `data.train` a un archivo, sin cambiar nada más.

19. [nit] line 423
   quote: el paso hacia adelante y el hacia atrás se presentan
   problem: 'el hacia atrás' is an awkward ellipsis.
   fix: el paso hacia adelante y el paso hacia atrás se presentan

20. [nit] line 72
   quote: compruébelo usted mismo en una Colab T4 gratuita
   problem: Colab is the platform and T4 is the GPU. 'una Colab T4' is an odd construction.
   fix: compruébelo usted mismo en una GPU T4 gratuita de Colab

21. [nit] line 372
   quote: Soup es Apache-2.0 y gratuito, y seguirá siéndolo.
   problem: 'es Apache-2.0' is a calque. In Spanish the license is something the software has.
   fix: Soup tiene licencia Apache-2.0 y es gratuito, y seguirá siéndolo.

22. [nit] line 111
   quote: **La pérdida de validación no se registraba en ningún lado.**
   problem: 'en ningún lado' is colloquial for written docs. The source's starker 'existed nowhere' is also slightly softened.
   fix: **La pérdida de validación no aparecía en ninguna parte.**

23. [nit] line 417
   quote: llega a la misma persona y sirve como alternativa.
   problem: 'a fine fallback' is softened; 'buena' is missing.
   fix: llega a la misma persona y es una buena alternativa.

24. [nit] line 391
   quote: y publicar los números ayuda tanto como financiar el tiempo de GPU.
   problem: Inconsistent terminology: the file otherwise uses 'cifras' for measured numbers.
   fix: y publicar las cifras ayuda tanto como financiar el tiempo de GPU.
