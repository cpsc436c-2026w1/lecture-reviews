**Prompt injection**. Instructions in what the user types, or in data the model reads, that make the model do what the app did not intend.

**Direct prompt injection**. The attacker writes the instructions into the prompt itself, such as the question.

**Indirect prompt injection**. The attacker places the instructions in data the app adds from its tools or RAG, such as a retrieved chunk.

**Resource and access limits** (caps). Limits on who may use the app and how much, such as sign-in, rate rules and quotas.

**Per-key budgets**. A spending limit for each student's or team's key, kept by a model gateway.

**Model gateway**. One service between the apps and the model providers: it holds the provider key, checks each key's budget and forwards the call.

**LLM capability restrictions** (system-level defense). Limits on what the model's actions can do that hold whatever the model writes, such as read-only tools, isolation and human approval for write actions.

**Guardrail**. A check on what goes into the model (input guard) or what comes out of it (output guard).

**Post-processing**. App code that fixes simple, predictable mistakes in the model's output.

**AI as a judge**. An eval scorer that is itself a model, used when no exact check exists.

**Prefill**. The step that handles every input token of a request in one pass.

**Decode**. The step that generates the reply, one step for each output token.

**Prompt cache**. The provider keeps the processed start of a prompt that repeats, so later calls skip that part of prefill and pay less for it.

**Load balancer**. A service that receives each request and sends it to one of several tasks (push).

**Competing consumers**. Workers share the messages of one queue: each message goes to one of them, and an idle worker takes the next (pull).
