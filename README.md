# ZTA
ZTA-Prototyping

This is a early-code prototyping the NIST specs for a ZTA based security architecture. See: 

https://www.nist.gov/publications/zero-trust-architecture

and NIST 800-207: https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf

Disclaimer:
This code is NOT for production and serves as a POC sample and prototyping environment only...you have been warned :)

### Basics first
This POC is mainly be writen in Python to make prototyping easy. It is by no means ment to be performant or scalable. However some design-consideration tend into this direction. One is, besides a vertical scalability, the base-desing should also allow a horizontal scalability. Another point that adresses the potential perfomrance and definite addresses resilience of the system is the chosen database for most of the datamanagement. Details about that considaration can be found in the wiki.

### Project/POC parts
The projects main part are the components in the controlplane. Second, sole for the purpouse of this POC and some tests, are the external mocking parts, that will simulate typical external components of a ZTA, as descibed in the NIST and oterh documents.