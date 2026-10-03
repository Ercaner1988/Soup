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

MIN_STREAM_BUFFERS = 2
MAX_STREAM_BUFFERS = 8
DEFAULT_STREAM_BUFFERS = 2

# --- layer streaming: disk read-ahead -----------------------------------

MIN_STREAM_READ_AHEAD = 1
MAX_STREAM_READ_AHEAD = 8
DEFAULT_STREAM_READ_AHEAD = 2

# --- layer streaming: tasks -----------------------------------------------

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

# --- ship verdict: noise floor -----------------------------------------

#: A floor needs a spread, and a spread needs at least two samples.
MIN_NOISE_FLOOR_RUNS = 2
#: Each run is a full pass over the base model; ten is already expensive.
MAX_NOISE_FLOOR_RUNS = 10
