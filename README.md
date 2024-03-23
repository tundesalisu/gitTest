# What is idempotent

In the context of software development and computer science, idempotence refers to the property of certain operations in mathematics and computer science, that can be applied multiple times without changing the result beyond the initial application.

For example, in HTTP methods, a request is considered idempotent if it can be made many times and yield the same result. GET, PUT, DELETE, HEAD, OPTIONS, and TRACE methods are idempotent, while POST is not. This means if you make the same DELETE request multiple times, the first request will delete the resource and subsequent requests will do nothing, but the result (the status of the resource) remains the same.
