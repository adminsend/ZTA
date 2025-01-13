#!/usr/bin/python
#-*- coding: utf-8 -*-

class SOADirectory:
    """
    Service Registry

    Holds lists of all active instances of the ZTA Controlplane and does the houskeeping e.g. cheking if an instance is still alive.

    Holds ony ephemeral data.
    """
    def __init__(self):
        self.PIPList = None
        self.PAPList = None
        self.PDPList = None
        self.PEPProxyList = None

    def Housekeeping(self, ):
        pass

    def getPIPs(self, ):
        pass

    def getPDPs(self, ):
        pass

    def getPEPProxies(self, ):
        pass

