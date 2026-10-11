### Compute and billing {#terms-compute-and-billing}

**Instance (EC2).** A virtual machine you rent from AWS, billed per second for the time it runs. Stopping it ends the compute charge, but its EBS disk still bills.

**Instance type.** The size you pick when you launch an EC2 server: how many vCPUs and how much memory it has, how fast its network is, and whether it has its own local disk.

**Spot instance.** Spare EC2 capacity sold much cheaper than on-demand. AWS can take it back after a two-minute warning, so it suits work that can stop and restart.

**Provisioned capacity.** Compute you pay for while it is allocated to you, used or not. Unlike pay-per-use compute, its charge continues when nothing runs.

**Usage-based billing.** Charges for measured work, such as each request or each millisecond a function runs. They stop when nothing runs; stored data and logs still cost money.

**Idle test.** The question to ask of each compute charge: does it bill while nothing runs? If yes, it is provisioned capacity. Storage and logs are counted separately.

**Time shape of demand.** When a workload asks for its resources across a day or a week: a steady rate, a daily rhythm, a burst, or a scheduled job. With the peak rate, it decides whether provisioned or usage-based billing is cheaper.

**Cost granularity.** The unit a provider bills in, such as one second of instance time or one request. With per-second billing, a faster, pricier instance can come out cheaper per task.

**Ephemeral infrastructure.** A server or cluster created for one piece of work and deleted after it, so it bills only around that work. Our EMR clusters were launched for a run and terminated after.
