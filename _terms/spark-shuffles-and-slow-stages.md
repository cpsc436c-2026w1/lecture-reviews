### Spark: shuffles and slow stages {#terms-spark-shuffles-and-slow-stages}

**Narrow transformation.** A step each task does on its own partition, so no rows move between partitions: `filter`, `select`, `withColumn`.

**Wide transformation.** A step that needs rows from other partitions, such as `groupBy`, `orderBy`, a window or most joins. Spark adds a shuffle before it.

**Shuffle (Exchange).** Moving rows between partitions for the next stage: each task writes its rows to its node's disk, and the next stage's tasks read them, often from other nodes.

**Window query.** A step that computes a value over a group of rows and puts it on each row, such as each trip's payment-type average next to the trip. Every row goes into an `Exchange`.

**Hot key.** One join, window or sort value with far more rows than the others. All its rows go to one task, which runs long after the rest of its stage; more nodes do not help.

**Spill.** Writing to the node's disk when the rows a task sorts, groups or shuffles do not fit in its share of executor memory. The result is correct but slower.
