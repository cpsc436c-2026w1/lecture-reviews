| | Our app (1×) | 100× |
|---|--:|--:|
| Trip changes a day | 3.3 million | 326 million |
| Live table size | 0.38 GB | 38 GB |
| Daily partitions: one export, one Glue run | $0.06 | $4.59 |
| Rewrite every 20 min: 72 full exports and Glue runs | $4.15 | $310.76 |
| Lakehouse every 20 min: 72 incremental exports, 72 `MERGE` runs, nightly compaction | $1.29 | $22.91 |
| CDC: DynamoDB Streams to Lambda, reading the changes only | $0.65 | $6.09 |
| &nbsp;&nbsp;+ write each change to a DynamoDB table | +$2.24 | +$224.43 |
| &nbsp;&nbsp;+ write each zone's count every 30 s to a DynamoDB table | +$0.52 | +$0.52 |
| &nbsp;&nbsp;+ append each zone's count every 30 s to an Iceberg table through Athena | +$0.26 | +$0.26 |
| [&nbsp;&nbsp;+ a full copy into the lakehouse through Kinesis and Firehose]{style="color:#8a8f98"} | [L14]{style="color:#8a8f98"} | |
| [Zero-ETL integration: AWS copies the table into the lakehouse for you]{style="color:#8a8f98"} | [L14]{style="color:#8a8f98"} | |
: {tbl-colwidths="[60,20,20]"}
