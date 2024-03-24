# What is idempotent

In the context of software development and computer science, idempotence refers to the property of certain operations in mathematics and computer science, that can be applied multiple times without changing the result beyond the initial application.

For example, in HTTP methods, a request is considered idempotent if it can be made many times and yield the same result. GET, PUT, DELETE, HEAD, OPTIONS, and TRACE methods are idempotent, while POST is not. This means if you make the same DELETE request multiple times, the first request will delete the resource and subsequent requests will do nothing, but the result (the status of the resource) remains the same.

# What is Stick Affinity?

"Stickiness" or "Stick Affinity" is a concept in load balancing, particularly in the context of AWS (Amazon Web Services).

In a load balancing scenario, incoming requests are distributed across multiple targets, such as EC2 instances. This distribution is typically done in a way that each request is independent of the others. However, in some cases, it's beneficial for the same client to be directed to the same target for each request. This is where stickiness comes into play.

When stickiness is enabled, the load balancer uses a special cookie to associate the client with a specific target. This means that all requests from the same client will be directed to the same target as long as the target is healthy and the stickiness duration has not expired. This is useful in scenarios where you have session-based applications that need to maintain state between requests.

In AWS, you can enable stickiness on both Application Load Balancers and Classic Load Balancers. However, it's important to note that this can lead to uneven distribution of requests if not managed properly.

## Concepts of A records, CNAME records, and Alias records

A records, CNAME records, and Alias records are commonly used in DNS configurations:

1. **A Record (Address Record)**:
    - An A record maps a domain name to its corresponding IPv4 address. For example, if you have a website with the domain name `example.com`, an A record would link `example.com` to its IP address, such as `192.0.2.1`.
    - When a user types `example.com` into their browser, the DNS system uses the A record to find the website's IP address and connect the user to the website's server.
    - Example: `example.com IN A 192.0.2.1`.

2. **CNAME Record (Canonical Name Record)**:
    - A CNAME record maps an alias name to a true or canonical domain name. This is used when you want to alias one domain name to another.
    - For example, if you have `www.example.com` and you want it to point to `example.com`, you can use a CNAME record for `www` pointing to `example.com`.
    - It's important to note that CNAME records should not be used for the root domain (e.g., `example.com`) because they can interfere with other record types required for the root domain.
    - Example: `www.example.com IN CNAME example.com`.

3. **Alias Record**:
    - Alias records are a feature specific to certain DNS services, including Amazon Route 53, and they're not part of the standard set of DNS records. Alias records function somewhat like CNAME records but can be used at the root domain level.
    - With an Alias record, you can point your root domain (e.g., `example.com`) or subdomain (e.g., `www.example.com`) to an AWS resource like an Amazon CloudFront distribution, an Elastic Load Balancer, an S3 bucket, or another Route 53 record in the same hosted zone.
    - One key benefit of Alias records is that they can be evaluated internally within the DNS service, potentially offering better performance and avoiding the additional DNS lookup that CNAME records require.
    - Example: An Alias record in Route 53 could point `example.com` directly to an AWS resource like a CloudFront distribution.

In summary, A records are used for mapping domain names to IPv4 addresses, CNAME records are used for pointing one domain name to another, and Alias records are a Route 53-specific feature that allows for more flexible domain name mappings, especially useful for AWS resources and at the root domain level.

## CIDR (Classless Inter-Domain Routing)

CIDR stands for Classless Inter-Domain Routing. It's a method for allocating IP addresses and routing Internet Protocol packets. CIDR is used to create unique identifiers for networks and individual devices while also making the routing process more efficient and scalable. Here's a breakdown of its key aspects:

1. **IP Addressing Without Classful Constraints**: Before CIDR, IP addresses were categorized into classes (A, B, C, D, and E) based on the size of the network. CIDR allows for a more flexible allocation of IP addresses by removing these class constraints, thereby reducing the wastage of IP addresses.

2. **Notation**: CIDR notation is a compact representation of an IP address and its associated routing prefix. It's written as an IP address, followed by a slash, and then a number (for example, `192.168.0.0/24`). The number after the slash represents the number of bits in the subnet mask. In this example, `192.168.0.0` is the IP address, and `24` indicates that the first 24 bits of the IP address are the network part, leaving the remaining bits for host addresses within that network.

3. **Subnetting**: CIDR allows for flexible subnetting, which is the division of an IP network into smaller network segments or subnets. This is crucial for efficient network management and security. The subnet mask (represented by the number following the slash in CIDR notation) determines the network boundary and the size of the network.

4. **Efficient Routing**: With CIDR, routers use the IP address and its CIDR prefix to make routing decisions. CIDR aggregates routes into a smaller number of routing table entries through a process called route aggregation or route summarization. This efficiency reduces the size of routing tables and improves the speed and efficiency of routing on the internet.

5. **IP Address Conservation**: By allowing networks to be divided into variable-sized blocks, CIDR helps in conserving the available IP address space. This is particularly important given the limited number of available IPv4 addresses.

6. **Supernetting**: This is a process related to CIDR that involves combining multiple network segments or subnets into a larger network block. It's essentially the opposite of subnetting and is used for further reducing the number of routing table entries.

CIDR was introduced as a solution to the rapid exhaustion of IPv4 addresses and the scaling issues associated with the older classful network design. It's an essential concept in networking that plays a crucial role in IP addressing and routing in modern networks.