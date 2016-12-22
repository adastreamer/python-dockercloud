from __future__ import absolute_import

from .base import Mutable

class Swarm(Mutable):
    subsystem = "infra"
    endpoint = "/swarm"

    def save(self):
        raise AttributeError("'save' is not supported in 'Swarm'")