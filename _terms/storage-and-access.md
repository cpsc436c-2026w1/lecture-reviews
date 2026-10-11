### Storage and access {#terms-storage-and-access}

**S3.** AWS's object store. You reach each object over the network by its name inside a bucket, and the data stays with no server running.

**Bucket.** A named container in S3 that holds objects. Its name is part of every object's address.

**Object key.** The full name of one stored file inside an S3 bucket. It is only a name, unrelated to the column a group-by or a join uses.

**Prefix (S3).** The leading part of an object's name, such as `day=2012-06-14/`. S3 lists objects by it, and the console's folders are built from it; the general-purpose buckets we use have no real folders.

**EBS volume.** A disk an EC2 instance reaches over the network, as its main disk or an extra one. Its data survives a stop, and it bills per GB-month while it exists, even when the instance is stopped.

**Byte-range read.** Asking S3 for one stated part of an object instead of the whole object. Parquet libraries fetch the footer this way, then only the column chunks a query needs.

**IAM policy.** A JSON document that says which actions are allowed on which AWS resources. Attached to a role, it sets what anything using that role may do.

**Security group.** The rules that say what network traffic may reach an EC2 instance and what it may send out, by protocol, port and address. They do not decide what the instance may do with other AWS resources.
