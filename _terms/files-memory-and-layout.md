### Files, memory and layout {#terms-files-memory-and-layout}

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
