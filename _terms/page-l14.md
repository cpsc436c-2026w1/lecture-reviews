**Operational system**. Reads and changes data as users act.

**Analytical system**. Holds a read-only copy for analysis.

**Polling** (L13). The consumer asks the source for new data every *T* seconds.

**Dual write** (L13). The application writes the same change to two systems, and a transaction does not cover both.

**Outbox table** (L13). A table the application writes each event to, in the same transaction as the change.

**Event stream**. Unbounded data, made available a piece at a time (DDIA 2e ch. 12).

**Event**. A record of one thing that happened.

**Producer** (publisher, sender). The application that makes an event.

**Consumer** (subscriber, recipient). An application that processes events.

**Database trigger**. Code the database runs inside each write.

**Change stream** (L13). A table's committed changes, read after the write.

**Publish/subscribe**. Subscribers get what producers send.

**Message broker**. Holds events between producers and consumers.

**Current state**. The latest version of each item, as a table keeps it.

**Immutable event**. A change appended once, never changed.

**Partition** (AWS: shard). One slice of a stream, in order, with its own read and write limits.

**Partition key** (Kinesis). The value that picks a record's shard.

**Queue**. Each delivery goes to one consumer, which deletes it.

**Standard queue** (SQS). Delivers each message at least once, in best-effort order.

**Load balancing** (DDIA). The consumers share the messages.

**Acknowledgment**. The consumer's signal that a message is done.

**Visibility timeout**. How long a queue hides a received message.

**SQS FIFO queue**. Keeps order within a message group and drops a repeated deduplication id for 5 minutes.

**Topic** (SNS sense). Every subscriber gets its own copy.

**Topic** (DDIA, Kafka). A named stream of related events.

**Fan-out** (DDIA). Each message is delivered to every subscriber.

**Consumer group** (DDIA). The workers doing one job. Each group gets every message. One worker in the group gets each message.

**Enhanced fan-out** (AWS, Kinesis). Each registered consumer gets its own read capacity on every shard (about read capacity, a different use of "fan-out").

**Filter policy**. A subscriber's rule for which messages it gets.

**Log**. Events appended in order and kept, read or not.

**Log-based message broker** (DDIA). A broker that keeps a log.

**Offset** (log position). A consumer's position in a log.

**Retention period**. How long a log keeps each event.

**Replay**. Move the offset back and read again.

**Backpressure**. Block the producer until the consumers catch up.

**Event sourcing** (DDIA 2e ch. 3). The event log is the truth, tables are derived views.

**Source of truth** (L12's system of record). The store whose copy is right when copies disagree.

**Tombstone**. An event that marks a key as deleted.

**Timeout**. The sender stops waiting for an answer after a set time.

**Delivery guarantee**. How many times each message arrives.

**At-most-once**. Never retry, so a message may be lost.

**At-least-once**. Retry until acknowledged, so it may arrive twice.

**Effectively-once**. At-least-once, plus an effect that counts once.

**Idempotent** (L12). Applying it twice gives the same result as once.

**Request id**. An id made where the request starts.

**Conditional write** (L12). A write that succeeds only if a condition holds.

**End-to-end argument**. Only the endpoints can provide some functions completely, such as duplicate suppression with a request id from the client to the database ([DDIA 2e, ch. 13, "The end-to-end argument"](https://learning.oreilly.com/library/view/designing-data-intensive-applications/9781098119058/ch13.html)).

**Poison message**. An event the consumer always fails on.

**Dead-letter queue**. A queue where failed messages go aside.

**On-failure destination**. Where Lambda reports a batch it skips.
