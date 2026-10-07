<<<<<<< HEAD
"""Bounds and task sets that ``config.schema`` shares with their runtime owners (#780).

A LEAF: it imports nothing, so ``config.schema`` can take its bounds from here without
importing ``layer_stream`` (and through it ``rich.panel``, ``layer_shard``,
``async_disk_source`` and ``safetensors_reader``) or ``ship_verdict`` onto the import path
of ``soup version``. The runtime owners re-export these names rather than redeclaring
them, so the schema's bound and the runtime validator's message still come from ONE
definition and cannot disagree. ``tests/test_config_bounds_leaf.py`` pins the leaf
property, the re-export identity, and the freed modules staying off the CLI path.

Keep it that way: a value that needs an import does not belong here.
"""

# --- layer streaming: buffers --------------------------------------------

=======
"""Config bounds shared by ``config/schema.py`` and the runtimes that enforce them.

A leaf: it imports nothing, so ``schema.py`` can take these values without
pulling the streaming and ship-verdict runtimes (and their ``rich`` subtree)
onto the ``soup version`` import path (#780). The runtime modules re-export
these names, so the schema bound and the runtime message stay one object.
"""

# --- layer streaming: buffers (utils/layer_stream.py) ----------------------
>>>>>>> 6b7356730180d6afbdc029cdcd280e225fd26a82
MIN_STREAM_BUFFERS = 2
MAX_STREAM_BUFFERS = 8
DEFAULT_STREAM_BUFFERS = 2

<<<<<<< HEAD
# --- layer streaming: disk read-ahead -----------------------------------

=======
# --- layer streaming: read-ahead (utils/async_disk_source.py) --------------
>>>>>>> 6b7356730180d6afbdc029cdcd280e225fd26a82
MIN_STREAM_READ_AHEAD = 1
MAX_STREAM_READ_AHEAD = 8
DEFAULT_STREAM_READ_AHEAD = 2

<<<<<<< HEAD
# --- layer streaming: tasks -----------------------------------------------

=======
# --- layer streaming: tasks ------------------------------------------------
>>>>>>> 6b7356730180d6afbdc029cdcd280e225fd26a82
#: Tasks whose trainers can run against a streamed base (v0.72.4).
#:
#: DPO and KTO take their reference model from the SAME streamed base with the
#: adapters disabled (TRL's ``null_ref_context``), so the reference costs no
#: extra weights at all — measured 0.914x the SFT peak, where forcing a real
#: second instance cost 9.92x. ORPO and SimPO are reference-free.
SUPPORTED_STREAM_TASKS = ("sft", "dpo", "orpo", "simpo", "kto")

#: Tasks PERMANENTLY excluded, not merely unimplemented. Generation rollouts
#: re-read every layer once per generated token, which destroys the whole
#: premise: streaming amortises one weight read over a training step, not over a
#: single decoded token (plan §3.2).
ROLLOUT_STREAM_TASKS = ("grpo", "ppo")

<<<<<<< HEAD
# --- ship verdict: noise floor -----------------------------------------

=======
# --- ship verdict: noise floor (utils/ship_verdict.py) ---------------------
>>>>>>> 6b7356730180d6afbdc029cdcd280e225fd26a82
#: A floor needs a spread, and a spread needs at least two samples.
MIN_NOISE_FLOOR_RUNS = 2
#: Each run is a full pass over the base model; ten is already expensive.
MAX_NOISE_FLOOR_RUNS = 10
