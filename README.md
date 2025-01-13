# ZTA

The existing approaches to system and networking seurity, based on perimeter security and/or defence in depth mechanisms is about to changen in favor of a so called Zero Trust Architecture (ZTA).

One of the leading publications is the NIST SP 800-207 document for which a summary is given below:

## Summary of NIST SP 800-207: Zero Trust Architecture (ZTA)

NIST SP 800-207 outlines a framework for implementing Zero Trust Architecture (ZTA) to enhance cybersecurity. Zero Trust is a security model based on the principle of "never trust, always verify." It assumes that threats can come from inside and outside the network and emphasizes strict access controls, continuous verification, and minimal trust levels.

#### Key Principles of ZTA:

* Continuous Verification: Authentication and authorization are performed continuously, not just at the point of entry.
* Least Privilege Access: Access is granted only to resources explicitly needed.
* Assume Breach: Operate under the assumption that an adversary is already in the environment.
* Resource Protection: Resources are segmented and accessed independently based on policies.

#### Components of Zero Trust Architecture (ZTA)

NIST SP 800-207 identifies seven primary components that define a Zero Trust Architecture:

1. Policy Decision Point (PDP)

The brain of the ZTA that makes access decisions based on policies and context.
It consists of:
* Policy Engine: Evaluates policies to grant or deny access.
* Policy Administrator: Implements policies by configuring enforcement points.

2. Policy Enforcement Point (PEP)

Enforces access decisions made by the PDP.
It acts as the gatekeeper, allowing or denying access to resources based on PDP instructions.

3. Enterprise Resources

The assets or systems that require protection (e.g., databases, applications, cloud resources, or devices).
Resources are secured and accessed based on strict policies.

4. Subject

Any entity (user, device, or application) attempting to access enterprise resources.
Authentication and authorization processes focus on verifying the subject's identity and context.

5. Resource Access Policies

Define the rules for accessing resources.
Policies can be based on:
* User identity: Role, group membership.
* Device state: Compliance, patch status.
* Contextual factors: Time, location, behavioral patterns.

6. Continuous Diagnostics and Mitigation (CDM)

Provides real-time monitoring and visibility into the network's security posture.
Ensures that policies remain effective and that any anomalies or threats are quickly identified and mitigated.

7. Threat Intelligence

Provides data on emerging threats and vulnerabilities.
Helps the system adapt policies and responses dynamically to evolving risks.

#### Supporting Elements in ZTA

To achieve full implementation, ZTA incorporates additional components and strategies, including:

* Identity and Access Management (IAM): Ensures robust authentication and authorization for subjects.
* Network Segmentation: Divides the network into smaller zones to limit lateral movement.
* Data Security: Protects data at rest, in motion, and in use with encryption and other controls.
* Logging and Analytics: Collects and analyzes logs for auditing, compliance, and threat detection.
* Secure Access Service Edge (SASE): Combines networking and security functions into a unified cloud-delivered service to support ZTA in distributed environments.

#### Benefits of ZTA

* Reduced Attack Surface: Minimizes exposure to threats by limiting access.
* Improved Incident Response: Facilitates faster detection and mitigation of breaches.
* Enhanced Compliance: Meets regulatory and data privacy requirements more effectively.
* Adaptability: Responds dynamically to changing security landscapes.

This comprehensive framework enables organizations to transition from traditional perimeter-based security to a more robust, adaptable, and secure zero-trust model.

See: 

https://www.nist.gov/publications/zero-trust-architecture

and 

NIST 800-207: 
https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf

NIST 800-207A ZTA Model for Access Controll in Cloud-Native Applicaitons: 
https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207A.pdf

NIST 1800-35: Implementing a Zero Trust Architecture
https://csrc.nist.gov/pubs/sp/1800/35/ipd

BSI Positiopnspapier Zero Trust 2023
https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/TechnischeLeitlinien/Zero-Trust/Zero-Trust_04072023.pdf

Zero Trust Implementation in the Emerging Technologies Era: Survey
https://arxiv.org/abs/2401.09575

Zero Trust: Applications, Challenges, and Opportunities
https://arxiv.org/abs/2401.09575

## OSS related sofwarepackages for ZTA

#### Pomerium
An identity-aware reverse proxy that provides secure access to internal applications without the need for a corporate VPN. It integrates with various identity providers and enforces context-aware access policies, ensuring that only authorized users can access specific resources.
https://www.pomerium.com/blog/open-source-zero-trust-software-solutions

#### OpenZiti
A comprehensive set of open-source tools designed to integrate zero trust principles directly into applications, enabling the creation of zero trust overlay networks with smart routing capabilities. OpenZiti provides SDKs for various programming languages, allowing developers to embed zero trust networking directly into their applications.
https://openziti.io

#### Tailscale
Built on WireGuard, Tailscale creates a secure mesh network between devices, simplifying the implementation of Zero Trust principles. It manages firewall rules and NAT traversal, allowing devices to communicate securely without exposing them to the public internet.
https://www.pomerium.com/blog/open-source-zero-trust-software-solutions

#### Pritunl Zero
An open-source BeyondCorp server that offers zero trust security for privileged access to SSH and web applications. It provides single sign-on compatibility with major providers like OneLogin, Okta, Google, Azure, and Auth0, and allows access via any web browser without the need for VPN clients.
https://research.aimultiple.com/ztna-open-source

#### Teleport
An open-source tool for providing zero trust access to servers and cloud applications using SSH, Kubernetes, and HTTPS. It can eliminate the need for VPNs by providing a single gateway to access computing infrastructure via a built-in proxy.
https://en.wikipedia.org/wiki/Teleport_%28software%29


## Commercial sofwarepackes for ZTA

### Partially addressing ZTA design considerations:

#### Axiomatics

Axiomatics specializes in dynamic authorization solutions, providing fine-grained, policy-based access control essential for Zero Trust strategies. Their offerings include:

* Centralized Policy Management: Axiomatics offers a central, dynamic Zero Trust policy engine that removes the burden of coding and managing authorization functionality individually for each application.
* Scalability: Designed to handle complex enterprise environments, Axiomatics' solutions can scale to meet the needs of large organizations, ensuring consistent policy enforcement across diverse applications and systems.
https://axiomatics.com/

#### Keycloak

Keycloak is an open-source Identity and Access Management (IAM) solution that supports Zero Trust principles through:

* Single Sign-On (SSO): Provides centralized authentication, reducing the risk of credential misuse.
* Fine-Grained Authorization: Supports role-based and attribute-based access control, allowing for detailed policy enforcement.
* Integration Capabilities: Can be integrated into various platforms to enhance security measures in line with Zero Trust models.
https://www.keycloak.org/

### Vendor specific Zero Trus Solutions

#### Zscaler Zero Trust Exchange
A cloud-native platform that provides secure access to applications and services based on Zero Trust principles, ensuring that no user or device is trusted by default.

#### Microsoft Zero Trust Solutions
Microsoft offers a comprehensive Zero Trust framework that integrates identity, endpoints, applications, and data, providing end-to-end security across the enterprise.

#### Palo Alto Networks Zero Trust Architecture
Provides a structured approach to implementing Zero Trust, redefining how security is enforced across the organization by ensuring that no user, device, or system is trusted by default.

#### Fortinet Zero Trust Architecture
Offers a comprehensive Zero Trust architecture encompassing users, applications, and infrastructure, enhancing an organization's security posture by ensuring continuous monitoring and verification.

#### Check Point Software Zero Trust Architecture
Provides a Zero Trust security architecture designed to reduce cybersecurity risk by eliminating implicit trust within an organization’s IT infrastructure. 

As a drawback all vendorspecific implementations only work well within the vendors own ecosystem. This implies benefits and drawbacks, depending if one is or is not already within the respective ecosystm.


---
Disclaimer:
This code is NOT for production and serves as a POC sample and prototyping environment only...you have been warned :)
--- 
### ZTA-Prototyping

As you see, none of the mentioned existing packages are open, vendor-independend or do implement the entire stack, proposed by NIST. So with this said, this is an approach to prototype the entire NIST stack as a POC, for testing and educational purpouses.

#### Current status
This is a early-code prototyping sketch for  the NIST SP 800-207 specs for a ZTA based security architecture. 

#### Basics first
This POC is mainly be writen in Python to make prototyping easy. It is by no means ment to be performant or scalable. However some design-consideration tend into this direction. One is, besides a vertical scalability, the base-desing should also allow a horizontal scalability. Another point that adresses the potential perfomrance and definite addresses resilience of the system is the chosen database for most of the datamanagement. Details about that considaration can be found in the wiki.

#### Project/POC parts
The projects main part are the components in the controlplane. Second, sole for the purpouse of this POC and some tests, are the external mocking parts, that will simulate typical external components of a ZTA, as descibed in the NIST and other documents.

For more details, please refere to the wiki :).