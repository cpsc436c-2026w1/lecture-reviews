### Managed Spark on EMR and Glue

**Amazon EMR.** AWS's managed service that launches a cluster of EC2 instances with Spark installed. You pay for the nodes from launch until you terminate the cluster.

**AWS Glue.** AWS's managed Spark service with a visual job editor and table definitions: you choose a job's worker type and number of workers, or let it scale them, and it starts the workers. A notebook session bills until you stop it, and its idle timeout is 48 hours by default.

**Worker type (Glue).** The size of each Glue worker, from G.1X (1 DPU: 4 vCPU, 16 GB) upward, such as G.2X at 2 DPUs. Together with the number of workers it defines a job's capacity, while the service picks the hardware underneath.

**DPU (Glue).** Glue's billing unit: 4 vCPU and 16 GB, the size of one G.1X worker, billed per second, with a 1-minute minimum, while a job runs or a session exists.

**Primary node.** The one EMR instance that runs the cluster manager and the HDFS name service. It runs no executors.

**Core node.** An EMR instance that runs executors and stores HDFS data. A role an instance plays in the cluster, not a Spark slot.

**Task node.** An optional EMR instance that runs executors and stores no HDFS data, so it can be removed or bought as spot capacity without losing HDFS data.

**HDFS.** A file system that splits files into blocks across a cluster's core nodes' disks. Its data is lost when the cluster terminates, so our inputs and outputs stay on S3.

### Instances and billing

**Instance type.** The size you pick when you launch an EC2 server: how many vCPUs and how much memory it has, how fast its network is, and whether it has its own local disk.

**Spot instance.** Spare EC2 capacity sold much cheaper than on-demand. AWS can take it back after a two-minute warning, so it suits work that can stop and restart.

**Ephemeral infrastructure.** A server or cluster created for one piece of work and deleted after it, so it bills only around that work. Our EMR clusters were launched for a run and terminated after.

**Provisioned capacity.** Compute you pay for while it is allocated to you, used or not. Unlike pay-per-use compute, its charge continues when nothing runs.

**Usage-based billing.** Charges for measured work, such as each request or each millisecond a function runs. They stop when nothing runs; stored data and logs still cost money.

**Idle test.** The question to ask of each compute charge: does it bill while nothing runs? If yes, it is provisioned capacity. Storage and logs are counted separately.

### Also used on this page

**Driver (Spark).** The program that coordinates a Spark application: it runs your code, builds the query plan and sends tasks to the executors.

**Executor (Spark).** A Spark program running on an EMR core or task node. It runs tasks and keeps their data in its memory or on the node's disk.

**Slot (Spark).** One executor core, as room to run one task on one Spark partition at a time. An executor with 4 cores runs 4 tasks at once; our EMR nodes have one per vCPU.

**Stage.** A set of tasks Spark can run before rows have to move between partitions. Every task in it runs the same steps on a different partition.
