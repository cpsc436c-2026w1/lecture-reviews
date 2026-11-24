### Recap of L18

**Orchestrator-workers**. A planner model call splits the request into subtasks that depend on it. App code bounds the plan, runs a worker for each subtask and combines the results.

**Agent loop**. The model returns a tool call, app code runs it and sends the tool result back, and the model returns the next tool call or the final reply.

**Bounded agent**. An agent with limits on its actions, time or spend that the model cannot remove. Reaching a limit stops the loop.

**Runbook first**. App code checks the causes seen before, with no model call. The agent runs only when the data does not settle the alarm, and app code checks the cause it names.

**Model gateway** (L16). A service between apps and model providers. It can hold the provider key, check each key's budget and forward the calls.

### Feedback IDs and requirements

**Feedback 1 issue**. The GitHub issue `staff-feedback` in your repository, where staff listed constraints (RF) and requests (RQ) about your proposal.

**Constraint** (RF010 …). A property of your system from your Feedback 1 issue. One that a test can check gets a rule; one that no test can check ends with `Read at Checkpoint 2: …` and what staff will read.

**Request** (RQ010 …). Something staff ask your team to do or answer. A request that starts with `Fix:` is corrected in `docs/proposal.md`; any other request gets a `Reply:` that says what you will do, and its answer is due at Checkpoint 2.

**Stakeholder input**. The section of `docs/requirements.md` with one line for each RF and RQ ID of your Feedback 1 issue, with its wording and your `Reply:`.

**Job story**. Each job story from your proposal that you plan to implement, as a heading with its ID (JS01 …) in `docs/requirements.md`.

**EARS** (Easy Approach to Requirements Syntax). One sentence of the same shape for every requirement: a keyword says when it applies, and `THE SYSTEM SHALL` says what the system then does. No keyword: always; `WHEN <trigger>`; `WHILE <state>`; `IF <problem> THEN`; `WHERE <feature>`.

**Traceability**. Each ID is defined once in `docs/`, and every other place that uses it names it: a tag in `features/`, a cell in `docs/design.md`.

### Data and examples

**Event**. A record that says something happened.

**Delivery**. One arrival of an event at the system. `received_time` is when it arrived; `event_time` is when it happened.

**Event format**. One line for each kind of event in `docs/design.md`, section `Data`, naming the fields that your examples' tables use.

**Injected fault**. A problem added to the test data on purpose, with an exact count, and recorded so the test knows the right answer. The system is not told which events are faulty.

**Simulated data set** (SIM01 …). A named set of generated test events or rows, for an example that needs more events than a small table holds. At Checkpoint 1 it is one bullet of words in `docs/design.md`, section `Data`.

**Example**. Test data and an expected answer: `Given` the data, `When` something happens, `Then` an answer known before the system runs.

**Eval in words**. An entry under `Evals` in `docs/requirements.md` for a requirement on a model's answers: the cases, what counts as correct, the runs, when it passes, and the model in use.

### Feature files and behave

**Gherkin**. The plain-text format that uses `Feature`, `Rule`, `Example`, `Given`, `When` and `Then`.

**behave**. A Python tool that reads Gherkin feature files and runs them.

**Feature file**. Plain text in `features/`, named for what the user gets.

**Rule**. A group of scenarios that show one requirement, with the requirement's ID as its tag.

**Tag**. A label such as `@R020` on the line above a feature, a rule or a scenario. It applies to everything under it.

**Step function**. Python code in `features/steps/` that behave calls for a step with matching text.

**Background**. Steps that run before every scenario of the feature.

**Scenario Outline**. Steps with `<placeholders>`, run once for each row of its `Examples:` table.

**Dry run**. behave reads the feature files and matches each step with step code, without running it.

**Undefined step**. A step without step code. behave prints a snippet for it: the empty step function to write later.

**Pull request**. A proposed change for review. The Checkpoint 1 hand-in is a merged pull request with the tag `cp1` on the merged commit.
