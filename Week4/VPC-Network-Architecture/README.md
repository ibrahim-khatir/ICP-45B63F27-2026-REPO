# Production-Grade VPC Network Architecture

A multi-AZ VPC on AWS with public/private subnet isolation, per-AZ NAT gateways, and a three-tier security group model (web / app / db) using security-group-to-security-group references instead of CIDR rules.

## Architecture

- 1 VPC (`10.0.0.0/16`) across 2 Availability Zones
- Public subnets (`10.0.1.0/24`, `10.0.2.0/24`) — NAT gateways, internet-facing resources
- Private subnets (`10.0.11.0/24`, `10.0.12.0/24`) — app/db tier, no direct internet exposure
- Internet Gateway for public subnet traffic
- Route tables define public vs. private — not a subnet property, a routing decision
- Layered security groups: `sg-web` → `sg-app` → `sg-db`, each tier only trusting the one directly in front of it, by security group reference rather than IP


## Key takeaways

- Public/private subnet designation comes entirely from route table configuration (route to an IGW/NAT vs. none)
- Security-group-to-security-group references scale better than CIDR rules — no IP tracking as instances get replaced
- Per-AZ NAT gateways avoid a cross-AZ single point of failure (with a documented cost tradeoff vs. a single shared NAT)

