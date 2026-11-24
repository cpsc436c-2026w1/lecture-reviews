### Recap of the GenAI block

**Approval gate** (L18). A check that must pass before an action runs: a person approves, tests pass, or an eval score reaches a set threshold.

**Idempotent write** (L18). A write that has the same effect whether it is sent once or several times. Retries use the same request key so the store can recognize the repeated write.

**Model gateway** (L16). A service between apps and model providers. It can hold the provider key, check each key's budget and forward the calls.

### Stream processing patterns

**Stream processor**. A program that reads events from a stream (a log, such as Apache Kafka or Kinesis, or a queue) and runs computations on them.

**Event routing**. A rule matches each event's content and sends it to targets; nothing is kept between events. On AWS: EventBridge rules.

**FaaS on the stream**. The platform reads a batch of records and calls your function with it. On AWS: Lambda with an event source mapping.

**Micro-batch engine**. A stream engine that runs a query over each small batch of new events and keeps windows, joins and state, checkpointed. Open source: Spark Structured Streaming.

**Record-at-a-time engine**. A stream engine that processes each event as it arrives, with state and timers for each key, checkpointed. Open source: Apache Flink, Kafka Streams.

### Windows and late updates

**Event**. A record that says something happened, such as one price update.

**Window**. The time range that one count covers, such as 09:10:00 up to 09:15:00.

**Tumbling window**. Windows of a fixed length, side by side; each record falls into exactly one.

**Event time**. When the thing happened, by the source's clock.

**Stream-entry time**. When the record entered the stream, such as DynamoDB Streams. Lambda's own tumbling windows group records by this time.

**Processing time**. When the function handles the record, which can be much later if it falls behind.

**Shard** (L14). One part of a stream. Lambda reads each shard separately and keeps a window's state for each shard.

**Watermark**. A cutoff in event time: the newest event time seen so far minus a close delay. A window is final when the watermark reaches or passes its end.

**Late record**. A record whose event-time window is already final when it arrives. The job either drops it and counts the drop, or updates the stored count and counts a correction.

### Lakehouse for streams: data lake, Iceberg and Hudi

**Data lake** (L11). Raw files in object storage, read by engines that list the folders; a folder of files has no commit, no record of its schema and no history.

**Iceberg table** (L11). A table with a table format: each write is a commit, snapshots record each version, and manifests list its data files.

**Delete file** (L11). A small file that lists which rows of a data file are deleted. Readers skip those rows until compaction rewrites the data file.

**Apache Hudi**. A table format for the lake, like Iceberg (L11), built to change rows by key in files on S3.

**Commit**. One write to the table that lands whole or not at all.

**Record key**. The column that names a row.

**Upsert**. Insert a row whose key is new, and replace the row whose key exists. An **append** inserts every row, a copy too.

**File group**. The rows of a set of keys: a base file in Parquet and, in a merge-on-read table, its log files.

**Copy-on-write**. A table type in which a commit writes a new base file for every file group with a changed key.

**Merge-on-read**. A table type in which a commit appends the updates to a log file in each file group it touches.

**Compaction**. A later job that merges a file group's log files into a new base file.

**Snapshot query**. The latest completed state: base files merged with log files.

**Read-optimized query**. Base files only: faster, and missing the updates still in log files.

**Incremental query**. The rows changed since a commit, one per key, in its latest state.

### Queues and agents over a stream

**Batching window**. How long Lambda gathers messages from a queue before it calls the function (`MaximumBatchingWindowInSeconds`, 0 to 300 s, default 0).

**Event source mapping** (L14). The Lambda resource that reads a queue or a stream and calls the function with batches of records.

**Context package**. What a pipeline hands an agent when a condition is met: the details of what it found, relevant history and related signals.

**Bounded agent** (L18). An agent with limits on its actions, time or spend that the model cannot remove.
