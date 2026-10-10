### Parquet

**Parquet.** A columnar file format. Rows are grouped into blocks that each store every column separately, and metadata at the end of the file says where each part is.

**Row group.** A horizontal block inside one Parquet file, holding one column chunk per column. Its size is set when the file is written, and a file can hold one or many.

**Column chunk.** The values of one field within one row group of a Parquet file. The writer can store their min and max, which lets a reader skip the whole row group.

**Footer.** The metadata at the end of a Parquet file: the schema, where each column chunk starts and, if the writer stored them, each chunk's min and max. A reader fetches it before any data.

**Projection pushdown.** Handing the reader the list of columns a query uses, so it reads only those columns from a Parquet file.

**Predicate pushdown.** Handing the reader the query's filter, so it can skip row groups whose stored min and max show that no row can match.

### Layout and files on S3

**Folder partition.** A dataset layout with one named location per value of a column, such as `day=2012-06-14/` (on S3, a prefix). A filter on that column skips the other locations without opening them.

**Compaction.** Rewriting many small files into fewer, larger ones, so a query opens fewer files. Too few files, or too few row groups, can leave cores idle.

**Prefix.** The leading part of an object's name, such as `day=2012-06-14/`. S3 lists objects by it, and the console's folders are built from it; the general-purpose buckets we use have no real folders.

**S3.** AWS's object store. You reach each object over the network by its name inside a bucket, and the data stays with no server running.

**Byte-range read.** Asking S3 for one stated part of an object instead of the whole object. Parquet libraries fetch the footer this way, then only the column chunks a query needs.

### Memory and resources

**Eager load.** Reading the whole dataset into memory before the work starts. If data and working space exceed memory, the operating system swaps to disk or stops the program.

**Storage, memory, compute and network.** The four things every data task uses, each with a capacity and a rate. Looking at a job from each in turn helps find its bottleneck, and cloud architecture often trades one for another.

**EBS volume.** A disk an EC2 instance reaches over the network, as its main disk or an extra one. Its data survives a stop, and it bills per GB-month while it exists, even when the instance is stopped.

### Also used on this page

**Instance type.** The size you pick when you launch an EC2 server: how many vCPUs and how much memory it has, how fast its network is, and whether it has its own local disk.

**Time shape of demand.** When a workload asks for its resources across a day or a week: a steady rate, a daily rhythm, a burst, or a scheduled job. With the peak rate, it decides whether provisioned or usage-based billing is cheaper.

**Amazon EMR.** AWS's managed service that launches a cluster of EC2 instances with Spark installed. You pay for the nodes from launch until you terminate the cluster.

**Primary node (EMR).** The one EMR instance that runs the cluster manager and the HDFS name service. It runs no executors.

**Core node (EMR).** An EMR instance that runs executors and stores HDFS data. A role an instance plays in the cluster, not a Spark slot.

**Task node (EMR).** An optional EMR instance that runs executors and stores no HDFS data, so it can be removed or bought as spot capacity without losing data.
