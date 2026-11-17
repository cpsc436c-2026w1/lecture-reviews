**Workflow**. App code sets the possible steps and their order before a request arrives. Model calls and tools run inside those paths.

**Agent**. The model uses results from earlier steps to choose its next action or tool.

**Orchestrator-workers**. A planner model call splits the request into subtasks that depend on it. App code bounds the plan, runs a worker for each subtask and combines the results.

**Agent loop**. The model returns a tool call, app code runs it and sends the tool result back, and the model returns the next tool call or the final reply.

**Bounded agent**. An agent with limits on its actions, time or spend that the model cannot remove. Reaching a limit stops the loop.

**Approval gate**. A person approves before an action runs.

**Idempotent write**. A write that has the same effect whether it is sent once or several times. Retries use the same request key so the store can recognize the repeated write.

**Agent SDK**. A library that runs the agent loop. It sends messages and tool definitions to the model, runs tool calls and sends tool results back to the model.

**Router** (L17). A component that sends each request to one of several predefined paths, such as a cheaper model or a stronger model.

**Agent runtime**. A service that runs agent code on request. A session groups related calls to an agent.

**Container image** (L16). Our app and what it needs, in one package. [Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) runs a container as an [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) task.

**Model server**. A program that loads a model's weights and answers model calls.

**Serving a model yourself**. Running a model server for an open model in your own container instead of using a provider.
