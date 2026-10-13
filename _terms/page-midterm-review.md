### Compute and billing

**Instance (EC2).** A virtual machine you rent from AWS, billed per second for the time it runs. Stopping it ends the compute charge, but its EBS disk still bills.

**Instance type.** The size you pick when you launch an EC2 server: how many vCPUs and how much memory it has, how fast its network is, and whether it has its own local disk.

**Spot instance.** Spare EC2 capacity sold much cheaper than on-demand. AWS can take it back after a two-minute warning, so it suits work that can stop and restart.

**Provisioned capacity.** Compute you pay for while it is allocated to you, used or not. Unlike pay-per-use compute, its charge continues when nothing runs.

**Usage-based billing.** Charges for measured work, such as each request or each millisecond a function runs. They stop when nothing runs; stored data and logs still cost money.

**Idle test.** The question to ask of each compute charge: does it bill while nothing runs? If yes, it is provisioned capacity. Storage and logs are counted separately.

**Time shape of demand.** When a workload asks for its resources across a day or a week: a steady rate, a daily rhythm, a burst, or a scheduled job. With the peak rate, it decides whether provisioned or usage-based billing is cheaper.

**Cost granularity.** The unit a provider bills in, such as one second of instance time or one request. With per-second billing, a faster, pricier instance can come out cheaper per task.

**Ephemeral infrastructure.** A server or cluster created for one piece of work and deleted after it, so it bills only around that work. Our EMR clusters were launched for a run and terminated after.

### Storage and access

**S3.** AWS's object store. You reach each object over the network by its name inside a bucket, and the data stays with no server running.

**Bucket.** A named container in S3 that holds objects. Its name is part of every object's address.

**Object key.** The full name of one stored file inside an S3 bucket. It is only a name, unrelated to the column a group-by or a join uses.

**Prefix (S3).** The leading part of an object's name, such as `day=2012-06-14/`. S3 lists objects by it, and the console's folders are built from it; the general-purpose buckets we use have no real folders.

**EBS volume.** A disk an EC2 instance reaches over the network, as its main disk or an extra one. Its data survives a stop, and it bills per GB-month while it exists, even when the instance is stopped.

**Byte-range read.** Asking S3 for one stated part of an object instead of the whole object. Parquet libraries fetch the footer this way, then only the column chunks a query needs.

**IAM policy.** A JSON document that says which actions are allowed on which AWS resources. Attached to a role, it sets what anything using that role may do.

**Security group.** The rules that say what network traffic may reach an EC2 instance and what it may send out, by protocol, port and address. They do not decide what the instance may do with other AWS resources.

### Serverless functions

**Serverless.** A service model where the platform runs and scales your code and you never pick or patch the computers under it. It usually bills per request and running time; stored data still costs money.

**Lambda function.** The unit you deploy to AWS Lambda: your code and its settings, run each time a trigger fires. One setting, memory, also sets its CPU and its price per millisecond.

**Execution role.** The identity AWS takes on when it runs a Lambda function. It decides which resources the code may read or change.

**Execution environment.** The isolated space AWS sets up to run a Lambda function, with its memory and a temporary disk. AWS may reuse it for later calls and pauses it between them.

**Cold start.** The set-up before the first call in a new Lambda environment: AWS loads the code, then your code's initialisation runs, such as opening connections and importing libraries.

**Handler.** The function in your code that Lambda calls on each invocation, taking `event` and `context`. Code outside it runs once per environment, so a client built there is reused.

**Request (trigger).** A call that asks a Lambda function for an answer while the caller waits for it, such as a browser going through API Gateway.

**Event (trigger).** A report that something happened, such as a new object landing in a bucket. A Lambda function processes it with no caller waiting for an answer.

**EventBridge.** The AWS service whose rules match things that happen, such as a new object in a bucket, or fire on a clock, and send each match to a target such as a Lambda function.

**API Gateway.** The AWS service that gives a function a web address, so a browser or a program can call it over HTTP. Its simplest kind waits at most 30 seconds for an answer.

### Files, memory and layout

**Parquet.** A columnar file format. Rows are grouped into blocks that each store every column separately, and metadata at the end of the file says where each part is.

**Row group.** A horizontal block inside one Parquet file, holding one column chunk per column. Its size is set when the file is written, and a file can hold one or many.

**Column chunk.** The values of one field within one row group of a Parquet file. The writer can store their min and max, which lets a reader skip the whole row group.

**Footer (Parquet).** The metadata at the end of a Parquet file: the schema, where each column chunk starts and, if the writer stored them, each chunk's min and max. A reader fetches it before any data.

**Projection pushdown.** Handing the reader the list of columns a query uses, so it reads only those columns from a Parquet file.

**Predicate pushdown.** Handing the reader the query's filter, so it can skip row groups whose stored min and max show that no row can match.

**Folder partition.** A dataset layout with one named location per value of a column, such as `day=2012-06-14/` (on S3, a prefix). A filter on that column skips the other locations without opening them.

**Compaction.** Rewriting many small files into fewer, larger ones, so a query opens fewer files. Too few files, or too few row groups, can leave cores idle.

**Eager load.** Reading the whole dataset into memory before the work starts. If data and working space exceed memory, the operating system swaps to disk or stops the program.

**Storage, memory, compute and network.** The four things every data task uses, each with a capacity and a rate. Looking at a job from each in turn helps find its bottleneck, and cloud architecture often trades one for another.

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

### Clusters and managed Spark

**Amazon EMR.** AWS's managed service that launches a cluster of EC2 instances with Spark installed. You pay for the nodes from launch until you terminate the cluster.

**Primary node (EMR).** The one EMR instance that runs the cluster manager and the HDFS name service. It runs no executors.

**Core node (EMR).** An EMR instance that runs executors and stores HDFS data. A role an instance plays in the cluster, not a Spark slot.

**Task node (EMR).** An optional EMR instance that runs executors and stores no HDFS data, so it can be removed or bought as spot capacity without losing HDFS data.

**HDFS.** A file system that splits files into blocks across a cluster's core nodes' disks. Its data is lost when the cluster terminates, so our inputs and outputs stay on S3.

**AWS Glue.** AWS's managed Spark service with a visual job editor and table definitions: you choose a job's worker type and number of workers, or let it scale them, and it starts the workers. A notebook session bills until you stop it, and its idle timeout is 48 hours by default.

**Worker type (Glue).** The size of each Glue worker, from G.1X (1 DPU: 4 vCPU, 16 GB) upward, such as G.2X at 2 DPUs. Together with the number of workers it defines a job's capacity, while the service picks the hardware underneath.

**DPU (Glue).** Glue's billing unit: 4 vCPU and 16 GB, the size of one G.1X worker, billed per second, with a 1-minute minimum, while a job runs or a session exists.
