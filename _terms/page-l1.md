### Memory and resources

**Storage, memory, compute and network.** The four things every data task uses, each with a capacity and a rate. Looking at a job from each in turn helps find its bottleneck, and cloud architecture often trades one for another.

**Eager load.** Reading the whole dataset into memory before the work starts. If data and working space exceed memory, the operating system swaps to disk or stops the program.

### Parquet

**Parquet.** A columnar file format. Rows are grouped into blocks that each store every column separately, and metadata at the end of the file says where each part is.

**Row group.** A horizontal block inside one Parquet file, holding one column chunk per column. Its size is set when the file is written, and a file can hold one or many.

**Column chunk.** The values of one field within one row group of a Parquet file. The writer can store their min and max, which lets a reader skip the whole row group.

**Footer.** The metadata at the end of a Parquet file: the schema, where each column chunk starts and, if the writer stored them, each chunk's min and max. A reader fetches it before any data.

**Projection pushdown.** Handing the reader the list of columns a query uses, so it reads only those columns from a Parquet file.

**Predicate pushdown.** Handing the reader the query's filter, so it can skip row groups whose stored min and max show that no row can match.

### Files on S3

**S3.** AWS's object store. You reach each object over the network by its name inside a bucket, and the data stays with no server running.

**Byte-range read.** Asking S3 for one stated part of an object instead of the whole object. Parquet libraries fetch the footer this way, then only the column chunks a query needs.

### Also used on this page

**Instance (EC2).** A virtual machine you rent from AWS, billed per second for the time it runs. Stopping it ends the compute charge, but its EBS disk still bills.

**Instance type.** The size you pick when you launch an EC2 server: how many vCPUs and how much memory it has, how fast its network is, and whether it has its own local disk.

**Cost granularity.** The unit a provider bills in, such as one second of instance time or one request. With per-second billing, a faster, pricier instance can come out cheaper per task.
