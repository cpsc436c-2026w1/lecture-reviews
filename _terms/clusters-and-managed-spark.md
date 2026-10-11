### Clusters and managed Spark {#terms-clusters-and-managed-spark}

**Amazon EMR.** AWS's managed service that launches a cluster of EC2 instances with Spark installed. You pay for the nodes from launch until you terminate the cluster.

**Primary node (EMR).** The one EMR instance that runs the cluster manager and the HDFS name service. It runs no executors.

**Core node (EMR).** An EMR instance that runs executors and stores HDFS data. A role an instance plays in the cluster, not a Spark slot.

**Task node (EMR).** An optional EMR instance that runs executors and stores no HDFS data, so it can be removed or bought as spot capacity without losing data.

**HDFS.** A file system that splits files into blocks across a cluster's core nodes' disks. Its data is lost when the cluster terminates, so our inputs and outputs stay on S3.

**AWS Glue.** AWS's managed Spark service with a visual job editor and table definitions: you choose a job's worker count and it starts the workers. A notebook session bills until you stop it, and its idle timeout is 48 hours by default.

**DPU.** Glue's billing unit: 4 vCPU and 16 GB, the size of one G.1X worker, billed per second, with a 1-minute minimum, while a job runs or a session exists.
