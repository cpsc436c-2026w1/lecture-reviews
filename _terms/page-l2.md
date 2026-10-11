### EC2 instances

**Instance.** A virtual machine you rent from AWS, billed per second for the time it runs. Stopping it ends the compute charge, but its EBS disk still bills.

**Instance type.** The size you pick when you launch an EC2 server: how many vCPUs and how much memory it has, how fast its network is, and whether it has its own local disk.

**EBS volume.** A disk an EC2 instance reaches over the network, as its main disk or an extra one. Its data survives a stop, and it bills per GB-month while it exists, even when the instance is stopped.

**Security group.** The rules that say what network traffic may reach an EC2 instance and what it may send out, by protocol, port and address. They do not decide what the instance may do with other AWS resources.

**IAM policy.** A JSON document that says which actions are allowed on which AWS resources. Attached to a role, it sets what anything using that role may do.

### S3

**S3.** AWS's object store. You reach each object over the network by its name inside a bucket, and the data stays with no server running.

**Bucket.** A named container in S3 that holds objects. Its name is part of every object's address.

**Object key.** The full name of one stored file inside an S3 bucket. It is only a name, unrelated to the column a group-by or a join uses.

**Prefix.** The leading part of an object's name, such as `day=2012-06-14/`. S3 lists objects by it, and the console's folders are built from it; the general-purpose buckets we use have no real folders.

### Lambda functions

**Lambda function.** The unit you deploy to AWS Lambda: your code and its settings, run each time a trigger fires. One setting, memory, also sets its CPU and its price per millisecond.

**Execution role.** The identity AWS takes on when it runs a Lambda function. It decides which resources the code may read or change.

**Execution environment.** The isolated space AWS sets up to run a Lambda function, with its memory and a temporary disk. AWS may reuse it for later calls and pauses it between them.

**Cold start.** The set-up before the first call in a new Lambda environment: AWS loads the code, then your code's initialisation runs, such as opening connections and importing libraries.

**Handler.** The function in your code that Lambda calls on each invocation, taking `event` and `context`. Code outside it runs once per environment, so a client built there is reused.

### Billing

**Time shape of demand.** When a workload asks for its resources across a day or a week: a steady rate, a daily rhythm, a burst, or a scheduled job. With the peak rate, it decides whether provisioned or usage-based billing is cheaper.

**Provisioned capacity.** Compute you pay for while it is allocated to you, used or not. Unlike pay-per-use compute, its charge continues when nothing runs.

**Usage-based billing.** Charges for measured work, such as each request or each millisecond a function runs. They stop when nothing runs; stored data and logs still cost money.

**Idle test.** The question to ask of each compute charge: does it bill while nothing runs? If yes, it is provisioned capacity. Storage and logs are counted separately.
