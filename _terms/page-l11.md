### D1 catalog and table format

**CTAS** (`CREATE TABLE ... AS SELECT`). Writes a query's result as a new table.

**`ALTER TABLE ... ADD COLUMNS`**. A schema change, written as a new metadata file with no new snapshot.

**Metadata tables** (`"t$partitions"`, `"t$files"`, `"t$snapshots"`, `"t$history"`). Read-only tables Athena makes from an Iceberg table's metadata, one row per partition, data file or snapshot.

**Snapshot operation**. What `$snapshots` records for each snapshot: `append` (files added), `overwrite` (rows deleted or changed), `replace` (files rewritten, rows unchanged).

**Field id**. The number Iceberg gives a column when it is added. `column_sizes` in `$files` is keyed by it.

### D2 layout

**Partition spec**. A source column and a transform, such as `months(pickup_datetime)`; Iceberg derives each file's partition value from it.

**Sort order** (`WRITE ORDERED BY`). The order Iceberg asks writers to sort rows in within each file, so each row group covers a narrow range.

**Row-group size** (`write.parquet.row-group-size-bytes`). The size at which the Parquet writer starts a new row group.

**Projection pushdown**. The engine hands the reader the query's columns, so the others are never read.

### D3 query engine

**DPU-seconds**. What a Glue run is billed for, DPUs × seconds of run time with a 1-minute minimum, at the DPU-hour price.

**Data scanned limit**. A per-query limit on an Athena workgroup. A query that passes it is cancelled and billed for the Data scanned before it stopped.

### D4 corrections

**Delete file**. A file that lists rows removed from a data file. Readers skip those rows, and the data file stays as written.

**`MERGE`**. One statement that updates the rows whose key matches a source row and inserts the rest.

### D5 upkeep

**`OPTIMIZE ... REWRITE DATA USING BIN_PACK`**. Compaction in Athena: rewrites small files into larger ones, recorded as a `replace` snapshot.

**`VACUUM`**. Expires snapshots older than the table's age property, then deletes the files no remaining snapshot lists. Expired snapshots cannot be read.

**Table property**. A setting kept in the table's metadata file, such as `vacuum_max_snapshot_age_seconds`.

### D6 object storage

**Storage class**. S3's price tier for an object: lower monthly price, a fee per GB read and a minimum duration.

**Lifecycle rule**. An S3 bucket rule that moves or deletes the objects under a prefix a set number of days after they were written.

### Appendix

**`UNLOAD`**. Runs a query and writes its result as files to an empty S3 location, with no table.
