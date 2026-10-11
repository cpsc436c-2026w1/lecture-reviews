### Spark: how a job runs {#terms-spark-how-a-job-runs}

**Driver (Spark).** The program that coordinates a Spark application: it runs your code, builds the query plan and sends tasks to the executors.

**Executor (Spark).** A Spark program running on an EMR core or task node. It runs tasks and keeps their data in its memory or on the node's disk.

**Partition (Spark).** A chunk of rows that one task processes as one unit. When reading files it holds one or more splits, each a byte range of one file, planned from the file sizes and the number of slots.

**Task (Spark).** One stage's work on one chunk of rows, run in one slot: by default, one executor core.

**Slot (Spark).** One executor core, as room to run one task on one Spark partition at a time. An executor with 4 cores runs 4 tasks at once; our EMR nodes have one per vCPU.

**Stage.** A set of tasks Spark can run before rows have to move between partitions. Every task in it runs the same steps on a different partition.

**Wave.** The set of a stage's tasks that run at the same time, one per slot. 36 reading tasks on 8 slots need 5 of them.

**Transformation (Spark).** A step such as `filter` or `groupBy(...).count()` that is only recorded in the plan. No task runs until an action asks for a result.

**Action (Spark).** On a Spark DataFrame, a call such as `df.count()`, `df.collect()` or `df.write.parquet()` that makes Spark run the plan built so far. Unlike pandas, where each step runs as soon as you call it.
