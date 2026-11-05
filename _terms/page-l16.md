**Prompt injection**. Instructions in what the user types, or in data the model reads, that make the model do what the app did not intend.

**Direct prompt injection**. The attacker writes the instructions into the prompt itself, such as the question.

**Indirect prompt injection**. The attacker places the instructions in data the app adds, such as a tool result or a chunk added through RAG.

**Resource and access limits** (caps). Limits on who may use the app and how much, such as sign-in, rate rules and quotas.

**Per-key budgets**. A spending limit for each key, kept by a model gateway.

**Model gateway**. A service between apps and model providers. It can hold the provider key, check each key's budget and forward the calls.

**LLM capability restrictions** (system-level defense). Limits on the actions the model can take, whatever it writes. Examples: read-only tools, isolation and human approval for write actions.

**Guardrails**. Checks on what goes into the model and what comes out of it. An input guard checks the input; an output guard checks the output.

**Post-processing**. App code that fixes simple, predictable mistakes in the model's output.

**AI as a judge**. A model used as an eval scorer, often when no exact check exists.

**Prefill**. The step that handles every input token of a request in one pass.

**Decode**. The step that generates the reply, one step for each output token.

**Prompt cache** (also context cache or prefix cache). The provider keeps the processed start of a prompt that repeats, so later calls reuse that work instead of repeating that part of prefill. Providers that offer it charge less for the cached part.

**Load balancer**. A service that receives requests and sends each one to one of several destinations (push). In our app, the destinations are tasks.

**Competing consumers**. Workers pull messages from one shared queue. One worker handles a message at a time, and an idle worker pulls the next one (pull).
