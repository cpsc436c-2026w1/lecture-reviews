### Spark: how a job runs

**Driver.** The program that coordinates a Spark application: it runs your code, builds the query plan and sends tasks to the executors.

**Executor.** A Spark program running on an EMR core or task node. It runs tasks and keeps their data in its memory or on the node's disk.

**Partition.** A chunk of rows that one task processes as one unit. When reading files it holds one or more splits, each a byte range of one file, planned from the file sizes and the number of slots.

**Task.** One stage's work on one chunk of rows, run in one slot: by default, one executor core.

**Slot.** One executor core, as room to run one task on one Spark partition at a time. An executor with 4 cores runs 4 tasks at once; our EMR nodes have one per vCPU.

**Stage.** A set of tasks Spark can run before rows have to move between partitions. Every task in it runs the same steps on a different partition.

**Wave.** The set of a stage's tasks that run at the same time, one per slot. 36 reading tasks on 8 slots need 5 of them.

**Transformation.** A step such as `filter` or `groupBy(...).count()` that is only recorded in the plan. No task runs until an action asks for a result.

**Action.** On a Spark DataFrame, a call such as `df.count()`, `df.collect()` or `df.write.parquet()` that makes Spark run the plan built so far. Unlike pandas, where each step runs as soon as you call it.

### Spark: shuffles and slow stages

**Narrow transformation.** A step each task does on its own partition, so no rows move between partitions: `filter`, `select`, `withColumn`.

**Wide transformation.** A step that needs rows from other partitions, such as `groupBy`, `orderBy`, a window or most joins. Spark adds a shuffle before it.

**Shuffle (Exchange).** Moving rows between partitions for the next stage: each task writes its rows to its node's disk, and the next stage's tasks read them, often from other nodes.

**Window query.** A step that computes a value over a group of rows and puts it on each row, such as each trip's payment-type average next to the trip. Every row goes into an `Exchange`.

**Hot key.** One join, window or sort value with far more rows than the others. All its rows go to one task, which runs long after the rest of its stage; more nodes do not help.

**Spill.** Writing to the node's disk when the rows a task sorts, groups or shuffles do not fit in its share of executor memory. The result is correct but slower.

### The EMR cluster

**Amazon EMR.** AWS's managed service that launches a cluster of EC2 instances with Spark installed. You pay for the nodes from launch until you terminate the cluster.

**Primary node.** The one EMR instance that runs the cluster manager and the HDFS name service. It runs no executors.

**Core node.** An EMR instance that runs executors and stores HDFS data. A role an instance plays in the cluster, not a Spark slot.

**Task node.** An optional EMR instance that runs executors and stores no HDFS data, so it can be removed or bought as spot capacity without losing data.

**HDFS.** A file system that splits files into blocks across a cluster's core nodes' disks. Its data is lost when the cluster terminates, so our inputs and outputs stay on S3.

### Also used on this page

**Parquet.** A columnar file format. Rows are grouped into blocks that each store every column separately, and metadata at the end of the file says where each part is.

**Instance type.** The size you pick when you launch an EC2 server: how many vCPUs and how much memory it has, how fast its network is, and whether it has its own local disk.

**S3.** AWS's object store. You reach each object over the network by its name inside a bucket, and the data stays with no server running.
