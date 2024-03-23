# What is idempotent

In the context of software development and computer science, idempotence refers to the property of certain operations in mathematics and computer science, that can be applied multiple times without changing the result beyond the initial application.

For example, in HTTP methods, a request is considered idempotent if it can be made many times and yield the same result. GET, PUT, DELETE, HEAD, OPTIONS, and TRACE methods are idempotent, while POST is not. This means if you make the same DELETE request multiple times, the first request will delete the resource and subsequent requests will do nothing, but the result (the status of the resource) remains the same.

What is Stick Affinity?
"Stickiness" or "Stick Affinity" is a concept in load balancing, particularly in the context of AWS (Amazon Web Services).

In a load balancing scenario, incoming requests are distributed across multiple targets, such as EC2 instances. This distribution is typically done in a way that each request is independent of the others. However, in some cases, it's beneficial for the same client to be directed to the same target for each request. This is where stickiness comes into play.

When stickiness is enabled, the load balancer uses a special cookie to associate the client with a specific target. This means that all requests from the same client will be directed to the same target as long as the target is healthy and the stickiness duration has not expired. This is useful in scenarios where you have session-based applications that need to maintain state between requests.

In AWS, you can enable stickiness on both Application Load Balancers and Classic Load Balancers. However, it's important to note that this can lead to uneven distribution of requests if not managed properly.
