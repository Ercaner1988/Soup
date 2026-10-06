<!-- synced-from: README.md sha256:39dcbfa5200df070b0c1d02c0dad8fd2bccea99873ce6f2f59580b18aa3eb340 -->
<p align="center">🌍 <a href="README.md">English</a> | <a href="README.tr.md">Türkçe</a> | <a href="README.ar.md">العربية</a> | <a href="README.ja.md">日本語</a> | <a href="README.es.md">Español</a> | <a href="README.pt.md">Português</a> | <strong>中文</strong> | <a href="README.ru.md">Русский</a></p>

<p align="center">
  <img src="soup.png" alt="Soup" width="280">
</p>

<h1 align="center">Soup</h1>

<p align="center">
  <strong>一条命令完成 LLM 微调与后训练。无需 SSH，告别配置地狱。</strong>
</p>

<p align="center">
  <a href="https://trysoup.dev">官网</a> &middot;
  <a href="#快速开始">快速开始</a> &middot;
  <a href="#web-ui">Web UI</a> &middot;
  <a href="#配置">配置</a> &middot;
  <a href="#文档">文档</a> &middot;
  <a href="docs/commands.md">命令</a> &middot;
  <a href="docs/models.md">模型</a> &middot;
  <a href="https://discord.gg/dgd2pJcjwP">Discord</a> &middot;
  <a href="https://t.me/souptasters">Telegram</a> &middot;
  <a href="https://www.producthunt.com/products/soup-cli">Product Hunt</a>
</p>

<p align="center">
  <a href="https://pypi.org/project/soup-cli/"><img src="https://img.shields.io/pypi/v/soup-cli?color=blue" alt="PyPI"></a>
  <a href="https://pepy.tech/project/soup-cli"><img src="https://img.shields.io/pepy/dt/soup-cli?color=blue" alt="下载量"></a>
  <img src="https://img.shields.io/badge/python-3.10--3.12-blue" alt="Python 3.10-3.12">
  <img src="https://img.shields.io/badge/license-Apache--2.0-blue" alt="Apache-2.0 许可证">
  <a href="https://github.com/MakazhanAlpamys/Soup/actions"><img src="https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/MakazhanAlpamys/65fdc943f85f3b2c46ecddb415c2b779/raw/soup_tests.json" alt="测试"></a>
  <a href="https://github.com/MakazhanAlpamys/Soup/actions"><img src="https://github.com/MakazhanAlpamys/Soup/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://trysoup.dev"><img src="https://img.shields.io/badge/website-trysoup.dev-blue" alt="官网"></a>
  <a href="https://discord.gg/dgd2pJcjwP"><img src="https://img.shields.io/badge/Discord-join-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
  <a href="https://t.me/souptasters"><img src="https://img.shields.io/badge/Telegram-join-26A5E4?logo=telegram&logoColor=white" alt="Telegram"></a>
  <a href="https://doi.org/10.5281/zenodo.21771064"><img src="https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21771064-blue?logo=zenodo&logoColor=white" alt="DOI: 10.5281/zenodo.21771064"></a>
</p>

<p align="center">
  <a href="https://www.producthunt.com/products/soup-cli?embed=true&amp;utm_source=badge-featured&amp;utm_medium=badge&amp;utm_campaign=badge-soup-cli">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1217869&amp;theme=dark">
      <img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=1217869&amp;theme=light" alt="Soup CLI - 在 4 GB 笔记本 GPU 上微调 8B LLM | Product Hunt" width="250" height="54">
    </picture>
  </a>
  <a href="https://trendshift.io/repositories/98395?utm_source=repository-badge&amp;utm_medium=badge&amp;utm_campaign=badge-repository-98395" target="_blank" rel="noopener noreferrer">
    <img src="https://trendshift.io/api/badge/repositories/98395" alt="MakazhanAlpamys/Soup | Trendshift" width="250" height="55">
  </a>
</p>

---

Soup 把 LLM 微调的种种麻烦变成一套简单的工作流：一份配置，一条命令，搞定。

```bash
pip install "soup-cli[train]"   # add [train] to fine-tune; bare `soup-cli` is the light CLI
soup init --template chat
soup train
```

**在 4 GB 笔记本 GPU 上微调 8B 模型。** 层流式加载（layer streaming）让冻结的基座模型留在
显存之外，每次只把一个解码器层送入 GPU。在 RTX 3050 Laptop 4 GB 上的实测结果：
Llama-3.1-8B-Instruct + NF4 达到 **119.6 tok/s，峰值 3.32 GB**——与常规的全量驻留运行逐位一致，
并在 H100 上独立复现，同样占用 3.32 GB，速度为 113.00 tok/s。
（这两个数字均在 v0.72.2 上测得，早于 v0.73.0 的正确性修复，而该修复在 32B 上带来了 −4.8% 的开销；
此后都没有在 4 GB 显卡上重新运行——重新测量见
issue [#361](https://github.com/MakazhanAlpamys/Soup/issues/361)，尚待完成。）需主动开启（`stream_layers: true`），
目前仍为 BETA——
[工作原理](docs/performance-and-quantization.md#layer-streaming-beta-v0720-nf4-v0722-disk--wider-archs-v0723-preference-losses-v0724) ·
[全部测量数据](benchmarks/) · [论文](https://doi.org/10.5281/zenodo.21771064) ·
**[在免费的 Colab T4 上亲自验证](notebooks/proof-4gb.ipynb)**（将进程限制在
4 GB 以内，然后断言流式加载的模型与常规模型逐位完全相同）

<p align="center">
  <a href="https://youtu.be/T1LCErE943E"><img src="docs/assets/layer-streaming.gif" alt="在 4 GB 显卡上对 Llama-3.1-8B 执行 soup train 预检：3.60 GB 的基座存储固定在内存中，横跨 32 层，外加两个 113 MB 的显存缓冲区；实测峰值为 3.32 GB，速度 119.6 tok/s，未触及 4 GB 的上限（在 v0.72.2 上测得，早于 #331 修复；重新测量见 issue #361，尚待完成）"></a><br>
  <sub>Llama-3.1-8B-Instruct + NF4，LoRA，batch 1，序列长度 512，RTX 3050 Laptop 4 GB——<b>峰值 3.32 GB，119.6 tok/s</b>（在 v0.72.2 上测得，早于 #331 修复；重新测量见 issue #361，尚待完成）。<a href="https://youtu.be/T1LCErE943E">完整视频（90 秒）</a></sub>
</p>

## 为什么选择 Soup？

训练 LLM 依然是件苦差事。即便是经验丰富的团队，也有 30-50% 的时间耗在与基础设施的纠缠上，
而不是用来改进模型。Soup 就是为解决这个问题而生。

- **零 SSH。** 再也不用 SSH 登录出了故障的 GPU 机器。
- **一份配置。** 只需一个简单的 YAML 文件。
- **全自动。** 批大小、GPU 检测、量化——全部自动处理。
- **本地运行。** 用 QLoRA 在你自己的 GPU 上训练，无需云服务。

## 最新动态

**v0.75.0——同一份 `soup.yaml`，在 MLX 上训练出的配方竟与 transformers 上不同，而且毫无提示。**
有六个训练选项经过校验、写进了文档、也被接受，却在该后端上没有任何代码读取。
**这一版本的全部 60 个 pull request 都来自维护者之外的贡献者**，共 22 人。

- **破坏性变更：未知的配置键现在会拒绝加载。** v0.74 只给出警告，并把本版本定为最后期限。
  像 `quantizaton` 这样的拼写错误，或是只存在于更新版 Soup 中的键，过去会被直接丢弃，
  运行照常进行，只是该设置并未生效；现在 CLI 会报错退出（退出码 1），API 会抛出
  `ValueError`，并指出你可能想写的字段名。检测器会应用 schema 自 v0.40.1 起一直支持的根层级
  `lora:` 重映射，因此这种写法会被接受，而不是被拒绝；使用它的两个 `soup fetch examples`
  文件已迁移到规范的 `training.lora`。所有配方和模板均可正常加载，键名在输出到终端之前会先转义，
  扫描也有上限。
- **MLX 现在会真正按配置执行。** `train_on_responses_only`、`warmup_ratio` /
  `scheduler` / `weight_decay` / `optimizer`、`max_grad_norm`、`gradient_accumulation_steps`
  和 `gradient_checkpointing` 在 `backend: mlx` 下都是先通过校验，然后被丢弃。32 个优化器名称中，
  只有 8 个在 MLX 上有对应实现；其余 24 个会按名称明确拒绝，而不是悄悄变成 AdamW。MLX 现在也能驱动实时仪表盘、
  实验追踪器和 `soup ui`，`soup doctor --config` 会列出当前后端不会读取的设置。
- **验证损失此前无处可见。** 每个后端都会计算它，随后又把它丢弃：
  没有指标列，没有事件字段，面板上也看不到。现在它会被记录、流式输出并显示出来。
- **破坏性变更：`grpo_variant: gspo` 现在是已发表的序列级目标函数**
  （arXiv:2507.18071），取代了原先的按列中心化启发式方法；在那种方法中，一个 padding token 还会
  连带改变同一列所有行的梯度。已有的 gspo 配置将无法复现之前的运行结果。
- **Web UI 的读取端点和 SSE 现在需要认证**，改用短期有效、仅可使用一次的票据（ticket），
  不再把 token 放在查询字符串中；`--public` 不再向局域网提供 `/docs` 和
  `/openapi.json`；训练子进程也不会再因为无人读取其输出而挂起。
- **`torch>=2.6.0`** 解决了 v0.74.0 已知的限制：在 2.5.1 下 `trl>=0.29` 无法
  导入，所有偏好训练器都不可用。另外还修复了两个问题：设置 `training.loraplus_lr_ratio`
  会导致每次运行崩溃；`packing: true` 在 TRL 0.29 上会抛出异常。

> 仅支持 Python **3.10–3.12**。在 3.13+ 上，pip 过去会解析出未经测试的 PyTorch wheel，
> 它们在 Soup 开始运行之前就会在原生扩展中崩溃。

更早的重要更新见 [GitHub Releases](https://github.com/MakazhanAlpamys/Soup/releases) 页面。

## 快速开始

### 1. 安装

Soup 是一个命令行应用，因此最干净的安装方式是给它一个独立环境，
并把 `soup` 放进你的 `PATH`：

```bash
# Light core: CLI + config + data tools, no PyTorch
pipx install soup-cli
uv tool install soup-cli          # same idea, if you already use uv

# Add the training stack (torch, transformers, peft, trl, datasets, …)
pipx install "soup-cli[train]"

# Everything (train + serve + ui + data) in one shot
pipx install "soup-cli[all]"

# Or from GitHub (latest dev)
pipx install "git+https://github.com/MakazhanAlpamys/Soup.git"
```

如果你已经身处 virtualenv、Colab notebook 或 Docker 镜像之中，直接使用 `pip` 即可，
包名和 extras 都相同：

```bash
pip install soup-cli
pip install "soup-cli[train]"
pip install "soup-cli[all]"
pip install git+https://github.com/MakazhanAlpamys/Soup.git
```

如果你还想在自己的代码中 `import soup_cli`，请用 `pip` 而不是 `pipx`，
因为 pipx 有意把应用与其他一切隔离开。

完整的 extras 对照表（`fast`、`mlx`、`serve`、`eval`、`ui`、`vision`、`audio`、…）见
[`docs/models.md`](docs/models.md#optional-extras)。

> **遇到 `error: externally-managed-environment`？** 这是
> [PEP 668](https://peps.python.org/pep-0668/) 导致的，不是 Soup 的问题。Debian 12、
> Ubuntu 23.04 及之后的版本禁止 `pip` 向系统 Python 写入，因为
> `apt` 也在管理这些文件。`pipx` 和 `uv tool` 通过给 Soup 一个独立环境来绕开这一限制，
> 这也是上面把它们排在最前面的原因。先执行 `python3 -m venv
> .venv && source .venv/bin/activate`，再使用普通的 `pip`，效果同样很好。

> **请用双引号，不要用单引号。** `"soup-cli[train]"` 是唯一能在所有 shell 中通用的写法——
> `cmd.exe`、PowerShell、bash 和 zsh。如果你从旧教程里复制了 `'soup-cli[train]'`，
> 结果被 pip 拒绝，原因就在这里：
> [原因及具体报错](docs/models.md#quoting-the-extra)。

`soup init`、`soup data …` 以及其他数据/检查类命令在轻量安装下即可使用。
微调（`soup train`）则需要 `[train]` extra。

### 2. 创建配置

```bash
soup init                       # interactive wizard
soup init --template chat       # or start from a template
```

模板：`chat`、`code`、`tool-calling`、`medical`、`reasoning`、`vision`、`kto`、`orpo`、
`simpo`、`ipo`、`bco`、`rlhf`、`pretrain`、`moe`、`longcontext`、`embedding`、`audio`。

### 3. 训练、测试、发布

```bash
soup train --config soup.yaml                 # LoRA, quantization, batching — all handled
soup chat  --model ./output                    # talk to your model
soup push  --model ./output --repo you/my-model

soup merge  --adapter ./output                              # merge LoRA into the base
soup export --model ./output --format gguf --quant q4_k_m   # GGUF for Ollama / llama.cpp
```

更多导出目标（ONNX、TensorRT、AWQ、GPTQ、BitNet）和部署选项见
[`docs/serving-and-export.md`](docs/serving-and-export.md)。

## Web UI

更喜欢用浏览器？`soup ui` 会在本地提供一个仪表盘，涵盖实验、
训练设置、实时指标、数据集浏览和模型对话。

```bash
pip install "soup-cli[ui]"
soup ui
# Opens http://127.0.0.1:7860
```

![Soup Web UI — 新建训练](docs/assets/web-ui-new-training.png)

[Web UI 文档](docs/serving-and-export.md#web-ui)

## 配置

一份完整的 `soup.yaml`：

```yaml
base: meta-llama/Llama-3.1-8B-Instruct
task: sft
# backend: unsloth  # 2-5x faster, pip install "soup-cli[fast]"

data:
  train: ./data/train.jsonl
  format: alpaca
  val_split: 0.1

training:
  epochs: 3
  lr: 2e-5
  batch_size: auto
  lora:
    r: 64
    alpha: 16
  quantization: 4bit

output: ./output
```

`config/schema.py` 是每个字段的唯一权威来源。更高级的数据、训练
和 PEFT 选项见[文档](#文档)一节。

> **自 v0.75 起，未知的配置键会被拒绝。** 没有任何配置模型声明过的键——比如拼写错误的
> `quantizaton`，或是只存在于更新版 Soup 中的字段——过去能顺利通过校验然后被丢弃，
> 运行照常进行，只是该设置并未生效。
> v0.74 会在加载时报告它，并给出你可能想写的字段；从 **v0.75** 起，同样的
> 配置会加载失败，所以请修正或删除该键，而不要指望它被
> 忽略。参见[未知的配置键](docs/backends-and-ops.md#unknown-config-keys)。

## 文档

完整的功能参考位于 [`docs/`](docs/)。请从这里开始：

| 指南 | 涵盖内容 |
|---|---|
| [训练任务与方法](docs/training.md) | SFT、DPO/GRPO/PPO/KTO/ORPO/SimPO/IPO/BCO、工具调用、PRM、预训练、蒸馏、分类、视觉/音频/TTS、机器遗忘（unlearning）、RAFT/RA-DIT、循环加固检测器 |
| [PEFT、长上下文与效率](docs/peft-and-efficiency.md) | DoRA、LoRA+、rsLoRA、VeRA、OLoRA、NEFTune、PiSSA、ReLoRA、优化器与 PEFT 方法大全、LLaMA Pro、GaLore、YaRN/LongLoRA、packing、课程学习、自动调优 |
| [性能与量化](docs/performance-and-quantization.md) | QAT、FP8、Quant Menu（I + II）、KV cache、NVFP4、保存格式、Cut Cross-Entropy、梯度检查点、内核、激活值卸载、层流式加载、多 GPU / DeepSpeed / FSDP |
| [数据工程](docs/data.md) | 数据格式、与 Axolotl/LF 功能对齐的流水线、数据工具、合成数据生成与 forge、质量评分卡、trace 工具、远程数据集、混合、配方 DAG |
| [评估与探针](docs/evaluation.md) | 评估设计/门禁、评估门禁训练、基准测试、NLG 指标、校准、Elo 竞技场、诊断、训后 X 光探针、A/B、漂移、可调优性、`soup advise` |
| [服务与导出](docs/serving-and-export.md) | 兼容 OpenAI 的服务器、批量推理、性能压测、合并/导出、Anthropic Messages 端点、推测解码（训练并测量你自己的 draft 模型）、部署 autopilot（自动部署）、Web UI、Agent Forge |
| [适配器、注册表与治理](docs/adapters-and-governance.md) | 适配器生命周期/管理、模型注册表、Soup Cans、数据飞轮（`soup loop`）、知识编辑、steering、供应链管控（scan/sign/BOM/attest/audit/airgap） |
| [合规与治理快速入门](docs/compliance.md) | HIPAA/SOC2/EU-AI-Act/SR-11-7 的 `init` 模板、溯源（BOM/attest/repro-receipt）、审计日志、气隙隔离、模型卡自动生成（`soup card`）、CI 门禁（`soup ci init`） |
| [后端、平台与运维](docs/backends-and-ops.md) | MLX/Unsloth 后端、替代 Hub、HF Hub 集成、autopilot、实验追踪、plan/apply、环境锁定文件、硬件适配、补全脚本、插件、实用命令 |
| [命令参考](docs/commands.md) | 完整的 `soup` 命令列表 |
| [支持的模型与 extras](docs/models.md) | 推荐的模型系列、显存规格指南、pip extras 对照表 |

## 数据格式

Alpaca、ShareGPT、ChatML、偏好对（DPO / ORPO / SimPO / IPO / KTO）、视觉、音频、
ASR、纯文本、embedding、RAFT 等——均可从 JSONL、JSON、CSV、Parquet 或
TXT 中自动识别，因此在大多数情况下，你只需把 `data.train` 指向一个文件，其他都无需改动。每种格式的 schema 都附有
实例，数据流水线（远程 URI、流式加载、分片、
交错、词表扩展、文档摄取）也都在
[`docs/data.md`](docs/data.md#data-formats) 中。

## 常用命令

```bash
soup train  --config soup.yaml        # train (SFT/DPO/GRPO/PPO/KTO/ORPO/SimPO/IPO/...)
soup infer  --model ./output --input prompts.jsonl   # batch inference
soup chat   --model ./output          # interactive chat
soup serve  --model ./output          # OpenAI-compatible API server
soup ui                               # local browser dashboard
soup merge  --adapter ./output        # merge LoRA into the base model
soup export --model ./output --format gguf           # export for deployment
soup eval   benchmark --model ./output               # evaluate
soup data   inspect ./data/train.jsonl               # dataset stats
soup recipes list                     # 100+ ready-made model recipes
soup autopilot --model <id> --data d.jsonl --goal chat  # zero-config
soup doctor                           # check GPU / deps / environment
```

完整的命令列表见 [`docs/commands.md`](docs/commands.md)。

## 支持的模型

Soup 支持 [HuggingFace Hub](https://huggingface.co/models?pipeline_tag=text-generation) 上的**任意**
文本生成模型——只要能用
`AutoModelForCausalLM` 加载，就能直接运行，无需修改任何配置。Llama 3.x/4、Qwen 2.5/3、Gemma 3、Mistral、
Mixtral、DeepSeek R1/V3、Phi-4 以及 100 多个其他模型都已作为现成的配方提供（`soup recipes list`）。

| VRAM | 最大模型（QLoRA 4-bit） | 示例 |
|---|---|---|
| 8 GB | ~7B | Llama-3.1-8B, Mistral-7B |
| 16 GB | ~14B | Phi-4-14B, Qwen2.5-14B |
| 24 GB | ~34B | CodeLlama-34B, Yi-1.5-34B |
| 48 GB | ~70B | Llama-3.3-70B |
| 80 GB+ | 70B+（全量）或 MoE | Mixtral-8x22B, DeepSeek-V3 |

完整的模型与视觉模型表格，以及可选 extras 对照表，见 [`docs/models.md`](docs/models.md)。

## Docker

无需在本地安装 CUDA 或 PyTorch 即可运行 Soup（每个版本发布时都会同步推送镜像到 GHCR）：

```bash
docker pull ghcr.io/makazhanalpamys/soup:latest
docker run --gpus all -v $(pwd):/workspace ghcr.io/makazhanalpamys/soup train --config soup.yaml
docker compose up   # or build locally
```

## 环境要求

- Python 3.10、3.11 或 3.12（这是 CI 所测试的版本；暂不支持 3.13+，
  因为 PyTorch 技术栈尚未在其上经过验证）
- 带 CUDA 的 GPU（推荐）、Apple Silicon（MPS）或 CPU（实验性——非常慢）
- 用 QLoRA 训练 7B 模型需要 8 GB+ 显存

所有训练任务都可以在 CPU 上运行以供测试（量化会自动禁用）。可选的 extras
（`train`、`all`、`fast`、`vision`、`qat`、`serve`、`serve-fast`、`ui`、`eval`、`deepspeed`、
`liger`、`mlx`、`onnx`、`tensorrt`、…）列在
[`docs/models.md`](docs/models.md#optional-extras) 中。

## 故障排查

```bash
soup doctor    # GPU, system resources, dependencies, and version in one place
```

CUDA wheel、版本不匹配等问题：[`docs/backends-and-ops.md`](docs/backends-and-ops.md#troubleshooting)。

## 开发

```bash
git clone https://github.com/MakazhanAlpamys/Soup.git
cd Soup
pip install -e ".[dev]"

ruff check src/soup_cli/ tests/    # lint
pytest tests/ -v                   # unit tests (fast, no GPU)
pytest tests/ -m smoke -v          # smoke tests (downloads a tiny model, trains)
pytest tests/ -m gpu --no-cov -v   # GPU tests (need a CUDA card; report results, see CONTRIBUTING.md)

pre-commit install                 # optional: ruff lint+format on commit
```

完整的工作流程请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)，报告安全漏洞请参阅 [SECURITY.md](SECURITY.md)。
遥测完全由用户主动开启（`SOUP_TELEMETRY=1`，默认关闭；参见[隐私政策](docs/backends-and-ops.md#privacy-policy)）。

## 支持 Soup

Soup 采用 Apache-2.0 许可，免费，并且会一直如此。它以公开透明的方式开发和维护，
只用了一台 4 GB 的笔记本，因此这些文档中的每个性能数字都是实测得出的，
而非空口宣称。

如果 Soup 帮你省下了一次训练，[给仓库点个 star](https://github.com/MakazhanAlpamys/Soup)
是最有帮助的方式，而且不花一分钱。如果你想直接资助这项工作：

**[❤️ 捐赠](https://buy.stripe.com/4gMcN441k3pha3T19ye7m04)**——一次性捐赠，金额不限（请在结账页面使用
*Change amount* 修改金额）。款项由 Stripe 以维护者注册的公司 **MePlay, Inc.** 的名义处理——
结账页面和你的信用卡账单上显示的是这个名字，而不是“Soup”。

捐赠将用于购买 GPU 算力，推进那些受硬件限制的工作——多 GPU、8B+ 模型验证、Apple Silicon——
这些都是一台 4 GB 笔记本无法完成的。

想推动这些事项，另一个办法是提供**硬件本身**。这些事项都带有如实标注的
“需要 \<硬件\>”门槛，而不是未经验证的说法。因此，如果你能用上配置更高的
机器，或有闲置的 GPU 额度，就去运行其中一个
[`help wanted`](https://github.com/MakazhanAlpamys/Soup/issues?q=is%3Aissue+is%3Aopen+label%3A%22help+wanted%22)
issue 并贴出测得的数字，其帮助不亚于资助 GPU 算力。这些 issue 都写明了
目前究竟有哪些工作卡在硬件上。

## 贡献者

由社区共同打造 ❤️——感谢每一位贡献者。参见
[CONTRIBUTORS.md](CONTRIBUTORS.md)。

[![贡献者](https://contrib.rocks/image?repo=MakazhanAlpamys/Soup)](https://github.com/MakazhanAlpamys/Soup/graphs/contributors)

## 联系我们

Bug 和功能请求请提交到
[issue tracker](https://github.com/MakazhanAlpamys/Soup/issues)，问题请发到
[Discussions](https://github.com/MakazhanAlpamys/Soup/discussions)——这样回复更快，
也能帮到下一个遇到同样问题的人。

如需实时交流、安装帮助，以及一切更适合边聊边解决的问题，欢迎加入
[Discord](https://discord.gg/dgd2pJcjwP) 或 [Telegram 社区](https://t.me/souptasters)。
任何半年后仍应能被找到的内容，
都应放在 Issues 或 Discussions 中——Discord 上的回答只帮到一个人，而一个 issue 能帮到
每一个遇到同样情况的人。[行为准则](CODE_OF_CONDUCT.md)在这些渠道同样适用。

对于不适合公开的事项——安全报告（参见 [SECURITY.md](SECURITY.md)）、
行为准则相关事宜，或媒体联络——请发邮件至 **team@trysoup.dev**。这是项目的邮箱，
也是处理一切与 Soup 相关事务的正确渠道。**makazanalpamys@gmail.com** 是维护者的
个人邮箱；它同样会转到同一个人，可作为备用。

## 引用 Soup

层流式加载——把冻结的基座模型从主机内存中逐个解码器层地流式送入，从而在 4 GB 笔记本 GPU 上训练 8B 模型——
已在一篇预印本中加以阐述，其中还包含用于验证流式运行与全量驻留运行是否一致的正确性
验证协议（前向与反向分别陈述，因为它们是两个独立的结论，而不是一个）。

> Makazhan, A. (2026). *Exact Layer Streaming: LoRA Fine-Tuning of an 8B Model on a 4 GB Laptop
> GPU* (v3). Zenodo. https://doi.org/10.5281/zenodo.21918325

**第 3 版（2026 年 8 月 13 日）为当前版本。** 标题和核心结论——4 GB 上跑 8B——均未改变，
自 v1 以来也没有任何实测数字发生变化。v3 所做的是**撤回我们此前发表的一个解释**，
这也是概括这篇论文用途的最简洁方式：

- **v3 中撤回：“层流式加载受限于主机到设备的传输，而不是 GPU。”**
  那只是根据下文 H100 复现结果做出的*推断*，从未经过实测。我们在 8 月 11 日对其进行了测量，
  结果表明在已发布的配置下这一说法并不成立：去掉所有主机到设备的字节传输，只能换来 **1.4%** 的提升，
  计算流等待拷贝的时间仅占单步的 **0.20%**，而单步运行速度达到该卡在同一会话中 GEMM 上限的 **71.3%**。
  流式加载特有的最大开销是逐层的 NF4 反量化，占 9.8%
  （[相关记录](benchmarks/probe-v0.73.0-what-bounds-streaming.md)）。所有测量数据依然成立；
  复现结果以较弱的形式保留了下来——这一限制对两台机器是共同的，
  并不在于 GPU 的算力。
- **在与原环境截然不同的硬件上复现**（v2 中新增）：RTX
  3050 上为 119.6 tok/s，H100 上的中位数为 113.00，峰值同为 3.32 GB。两者都早于 #331
  修复；4 GB 上的重新测量见 issue #361，尚待完成。
- **发现并修复了一个会悄无声息地产生错误梯度的缺陷。** 在每层超过约 165 MiB 的 NF4 上，
  前向传播依然逐位一致，损失曲线看上去也很正常，但梯度其实是错的。
  根因已在上游库中定位并向其报告；修复已通过在真实 32B 和 72B 上的对照实验验证。
- **在真实模型规模上验证逐位一致**，而不再是三层的玩具模型：前向从 0.5B 到 72B，
  反向在 8B 和 14B 上。
- **首次测量训练后模型的质量**，结果与全量驻留运行无法区分。
- **与 DeepSpeed 的对比**——包括那个对我们并不有利的结果：八张卡的
  ZeRO-3 比一张卡的驻留训练还要慢。
- **重写了局限性一节**：v1 的十项中，一项已解决，另有四项范围缩小，
  并新增了七项。

请引用你所使用的版本。`10.5281/zenodo.21771064` 是概念 DOI，始终指向
最新版本（目前为 v3）；v1 和 v2 仍可通过各自的版本 DOI 引用，且不会被编辑——
上述撤回之所以以新版本的形式发布，正是为了让“我们在何时主张过什么”
这份记录保持完整。

其中每个数字背后的测量记录都在 [`benchmarks/`](benchmarks/) 中，按原样公开——
包括失败的尝试、后来证明有误的假设，以及测出后又被舍弃的数字。

```bibtex
@misc{makazhan2026exact,
  title        = {Exact Layer Streaming: LoRA Fine-Tuning of an 8B Model on a 4 GB Laptop GPU},
  author       = {Makazhan, Alpamys},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {v3},
  doi          = {10.5281/zenodo.21918325},
  url          = {https://doi.org/10.5281/zenodo.21918325}
}
```

## 许可证

[Apache-2.0](LICENSE)。Copyright © Soup 贡献者。
