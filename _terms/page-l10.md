### Lake and lakehouse

**Data lake.** Raw files in object storage, read by engines that list the folders; a folder of files has no commit, no record of its schema and no history.

**Lakehouse.** A lake whose tables have a table format and a catalog, so readers see whole commits.

**Query engine.** Parses SQL, plans it and runs it: Spark SQL, Trino, DuckDB, Athena.

**Catalog.** Lists tables and points to each table's current metadata file: the Glue Data Catalog.

**Table format.** Metadata files that say which data files are the table now, with the schema and the snapshots: Iceberg.

**Object storage.** Keeps files as objects in buckets: S3. Which files form a table is recorded in the metadata above it.

**Storage format (file format).** Encodes rows in one data file, with a footer: Parquet.

### Iceberg's levels

**Catalog entry.** The table's name and the path of its current metadata file.

**Metadata file.** The schema, the partition spec (how files are grouped, for example by month) and the snapshots; each snapshot names a manifest list.

**Manifest.** Lists data files, each with its partition value, row count, and minimum and maximum per column.

**Data file.** A file that contains rows of a table: a Parquet file.

**Commit.** Writing new metadata files, then switching the catalog entry to the new one in one step; readers see the old snapshot or the new one, never half.

**Snapshot.** One version of the table: the data files that were the table after one commit.

### What the table format fixes

**Iceberg partitioning.** The table is partitioned by a value Iceberg derives from a column, for example the month of `pickup_datetime`, and each data file's partition value is kept in the manifests. Because the value is derived (hidden partitioning), a filter on the column itself skips files, with no folder partition column to name. Separately, the manifests keep each file's minimum and maximum per column, which also let an engine skip files.

**Delete file.** A small file that lists which rows of a data file are deleted. Readers skip those rows, and the data file itself is not changed.

**Compaction.** Rewriting many small data files into fewer larger ones (`OPTIMIZE`).

**Time travel.** Reading the table as it was at an earlier snapshot, as long as that snapshot has not been expired.

### Not layers of a lakehouse

**Cluster manager.** Starts an engine's processes on a cluster's nodes, for example YARN starting Spark's executors on EMR (L5).

**Connector.** In Trino, how the engine reads one source, such as the Glue Data Catalog or a database (L10).

**`_SUCCESS` file.** An empty file Spark writes when a job finishes writing a folder; readers of the folder do not check it by default.

**Folder partition column.** A column whose value is a folder name, such as `month=2024-03`; a data lake skips folders only when a query names it.
