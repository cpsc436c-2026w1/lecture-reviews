**System of record**. The store with the authoritative copy; other copies are derived from it.

**Operational system (OLTP), analytical system (OLAP), point query**. Many small reads and writes by key, in milliseconds; scans and aggregates over many records; one record fetched by its key.

**Row-oriented, column-oriented**. One record's values stored together; one column's values stored together.

**Item, partition key, sort key**. DynamoDB's record; the key part that picks its storage partition; the optional part that orders items sharing a partition key.

**`GetItem`, `Query`, `Scan`**. One item by key; the items of one partition key; every item.

**Read request unit / write request unit**. One strong read (or two eventual) of up to 4 KB; one write of up to 1 KB.

**Export, federated query, derived copy**. A copy of the store's items written to S3 (all, or those changed in a time window); a query that reads the store through a connector; a result computed elsewhere and written back.

**Partial failure, timeout, netsplit**. Some parts fail; giving up waiting; nodes that cannot reach each other.

**Replication, sharding**. The same data on several nodes; a different slice on each node.

**Replica, leader, follower**. A copy on another node; in single-leader replication, the one that takes writes; the ones that copy from it.

**Region, Availability Zone (AZ)**. A geographic area; one or more isolated data centres (buildings of nodes) in a Region, with their own power and network.

**Synchronous, asynchronous, majority (quorum)**. "done" after the required followers have it; after the leader's own commit; after more than half have it.

**Replication lag, eventual consistency, read-after-write**. A follower behind the leader; agreement if writes stop, no deadline; your reads show your writes.

**Linearizability**. Behaves as one copy, in real-time order; "strong consistency" is a vague name for it.

**Eventually / strongly consistent read**. Any replica, may be old, 0.5 units per 4 KB; the leader, the latest value including every write finished before the read, 1 unit per 4 KB.

**CAP, PACELC**. During a netsplit, linearizable or a non-error answer from every working node; else, latency or consistency.

**Lost update, compare-and-set, conditional write, optimistic concurrency**. The second write replaces the first; write only if unchanged; DynamoDB's form; check at the end, retry if changed.

**Transaction, ACID, BASE**. A group that succeeds or fails whole; atomicity, consistency, isolation, durability; mostly "not ACID".

**Serializability**. The outcome of concurrent transactions equals running them one at a time.

**Timeliness, integrity, idempotent**. Shows the latest; nothing lost or duplicated; twice has the effect of once.
