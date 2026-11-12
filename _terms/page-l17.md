**Workflow**. App code sets the possible steps and their order before a request arrives. Model calls and tools run inside those paths.

**Agent**. The model uses results from earlier steps to choose its next action or tool.

**Bounded agent**. An agent with limits on its actions, time or spend that the model cannot remove.

**Augmented LLM**. A model given information, tools or memory beyond what it learned in training. The book calls preparing this context construction.

**Inverted index**. For each term, the list of documents where it appears.

**Vector index**. Vectors organized so a search can quickly find the ones closest to a query's vector.

**Prompt chain**. Two or more model calls in an order set by app code, where an earlier output feeds a later call.

**Answer cache**. A store of replies that the app reuses when a later request matches the cache key.

**Parallel calls**. Independent calls, to models or to other services, run at the same time. App code collects their results.

**Router**. A component that sends each request to one of several predefined paths: a cheaper model, a stronger model, a stock reply, a clarifying question or a person.

**Evaluator-optimizer**. One step produces a result. Another evaluates it against criteria. App code accepts the result or asks for a revision within a set limit.

**Orchestrator-workers**. A planner model call splits the request into subtasks that depend on it. App code runs a worker for each subtask, and a merge call combines their replies.
