from src.firewall.verifier import ChunkVerifier
from src.firewall.knowledge_firewall import KnowledgeFirewall


class SecurityManager:
    """
    Enterprise wrapper around the Knowledge Firewall.

    This class does not implement security logic.
    It simply exposes the existing backend in a
    clean interface for dashboards and enterprise modules.
    """

    def __init__(self):

        self.verifier = ChunkVerifier()

        self.firewall = KnowledgeFirewall()

    # --------------------------------------------------

    def verify_chunk(self, chunk):

        return self.verifier.verify(chunk)

    # --------------------------------------------------

    def verify_query(

        self,

        query,

        top_k=5,

        include_suspicious=False

    ):

        return self.firewall.verify_query(

            query=query,

            top_k=top_k,

            include_suspicious=include_suspicious

        )