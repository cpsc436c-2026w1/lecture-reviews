**System prompt**. The instructions the app sends first, with role `system`.

**User message**. The person's question, and anything we add to it, like RAG chunks.

**Tool call**. The LLM asking our app to run a tool, with arguments (the SQL).

**Tool result**. What our app sends back after running the tool, as a message with role `tool`.

**Reply**. The LLM's final answer in words.

**Output format**. A JSON schema sent with the request (strict mode).

**Structured output**. A reply that the provider returns as JSON matching a schema we give.

**Strict mode**. A strict JSON schema: the provider restricts which tokens can be generated, so a finished reply matches the schema's fields and types (constrained sampling).

**RAG** (retrieval-augmented generation). Before the call, find the documents that match the question and add them to the prompt.

**Term-based retrieval**. Score a chunk by the words it shares with the question.

**Embedding-based retrieval**. A neural network maps each chunk to a vector where texts with similar meaning land close together, and the score is how close the question's vector is.

**Hybrid search**. Term-based and embedding-based retrieval combined, as production systems often do.

**Eval** (evaluation). An automated test of a model's answers over many inputs.

**Dataset** (Inspect). Labelled samples, typically a table with `input` and `target` columns. The input is the prompt, the target is the ideal answer or grading guidance.

**Solver** (Inspect). Produces an answer for each sample. It can be a single model call or an agent using tools over many turns.

**Scorer** (Inspect). Evaluates the output, using text comparisons, model grading, or other custom schemes.

**Guardrail**. A check on what goes into or comes out of the model that blocks or changes a request.

**Trace**. The record of one question: each tool call, the SQL, the checks' verdicts, tokens, price and time.
