### Triggers: what starts a function

**Request (trigger).** A call that asks a Lambda function for an answer while the caller waits for it, such as a browser going through API Gateway.

**Event (trigger).** A report that something happened, such as a new object landing in a bucket. A Lambda function processes it with no caller waiting for an answer.

**EventBridge.** The AWS service whose rules match things that happen, such as a new object in a bucket, or fire on a clock, and send each match to a target such as a Lambda function.

**API Gateway.** The AWS service that gives a function a web address, so a browser or a program can call it over HTTP. Its simplest kind waits at most 30 seconds for an answer.

### Inside a Lambda function

**Lambda function.** The unit you deploy to AWS Lambda: your code and its settings, run each time a trigger fires. One setting, memory, also sets its CPU and its price per millisecond.

**Handler.** The function in your code that Lambda calls on each invocation, taking `event` and `context`. Code outside it runs once per environment, so a client built there is reused.

**Execution environment.** The isolated space AWS sets up to run a Lambda function, with its memory and a temporary disk. AWS may reuse it for later calls and pauses it between them.

**Cold start.** The set-up before the first call in a new Lambda environment: AWS loads the code, then your code's initialisation runs, such as opening connections and importing libraries.

**Execution role.** The identity AWS takes on when it runs a Lambda function. It decides which resources the code may read or change.

### Cost models

**Provisioned capacity.** Compute you pay for while it is allocated to you, used or not. Unlike pay-per-use compute, its charge continues when nothing runs.

**Usage-based billing.** Charges for measured work, such as each request or each millisecond a function runs. They stop when nothing runs; stored data and logs still cost money.

**Idle test.** The question to ask of each compute charge: does it bill while nothing runs? If yes, it is provisioned capacity. Storage and logs are counted separately.

**Time shape of demand.** When a workload asks for its resources across a day or a week: a steady rate, a daily rhythm, a burst, or a scheduled job. With the peak rate, it decides whether provisioned or usage-based billing is cheaper.

**Ephemeral infrastructure.** A server or cluster created for one piece of work and deleted after it, so it bills only around that work. Our EMR clusters were launched for a run and terminated after.

**Instance (EC2).** A virtual machine you rent from AWS, billed per second for the time it runs. Stopping it ends the compute charge, but its EBS disk still bills.

### Also used on this page

**Serverless.** A service model where the platform runs and scales your code and you never pick or patch the computers under it. It usually bills per request and running time; stored data still costs money.

**Compaction.** Rewriting many small files into fewer, larger ones, so a query opens fewer files. Too few files, or too few row groups, can leave cores idle.

**Folder partition.** A dataset layout with one named location per value of a column, such as `day=2012-06-14/` (on S3, a prefix). A filter on that column skips the other locations without opening them.

**Prefix (S3).** The leading part of an object's name, such as `day=2012-06-14/`. S3 lists objects by it, and the console's folders are built from it; the general-purpose buckets we use have no real folders.

**Parquet.** A columnar file format. Rows are grouped into blocks that each store every column separately, and metadata at the end of the file says where each part is.
