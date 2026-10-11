### Serverless functions {#terms-serverless-functions}

**Serverless.** A service model where the platform runs and scales your code and you never pick or patch the computers under it. It usually bills per request and running time; stored data still costs money.

**Lambda function.** The unit you deploy to AWS Lambda: your code and its settings, run each time a trigger fires. One setting, memory, also sets its CPU and its price per millisecond.

**Execution role.** The identity AWS takes on when it runs a Lambda function. It decides which resources the code may read or change.

**Execution environment.** The isolated space AWS sets up to run a Lambda function, with its memory and a temporary disk. AWS may reuse it for later calls and pauses it between them.

**Cold start.** The set-up before the first call in a new Lambda environment: AWS loads the code, then your code's initialisation runs, such as opening connections and importing libraries.

**Handler.** The function in your code that Lambda calls on each invocation, taking `event` and `context`. Code outside it runs once per environment, so a client built there is reused.

**Request (trigger).** A call that asks a Lambda function for an answer while the caller waits for it, such as a browser going through API Gateway.

**Event (trigger).** A report that something happened, such as a new object landing in a bucket. A Lambda function processes it with no caller waiting for an answer.

**EventBridge.** The AWS service whose rules match things that happen, such as a new object in a bucket, or fire on a clock, and send each match to a target such as a Lambda function.

**API Gateway.** The AWS service that gives a function a web address, so a browser or a program can call it over HTTP. Its simplest kind waits at most 30 seconds for an answer.
