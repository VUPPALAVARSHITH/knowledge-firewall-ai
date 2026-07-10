"""
validator.py

Knowledge Firewall AI

Validates Dataset 4 semantic chunks.
"""

from collections import Counter


class ChunkValidator:

    VALID_SECTIONS = {
        "METADATA",
        "TITLE",
        "PURPOSE",
        "SCOPE",
        "DEFINITIONS",
        "POLICY_STATEMENT",
        "RESPONSIBILITIES",
        "EXCEPTIONS",
        "COMPLIANCE",
        "REVIEW_CYCLE",
        "KEYWORDS"
    }

    def validate(self, chunks):

        errors = []

        # --------------------------------------------------
        # Duplicate IDs
        # --------------------------------------------------

        ids = [chunk.chunk_id for chunk in chunks]

        duplicates = [

            cid

            for cid, count in Counter(ids).items()

            if count > 1

        ]

        for duplicate in duplicates:

            errors.append(f"Duplicate Chunk ID : {duplicate}")

        # --------------------------------------------------
        # Validate every chunk
        # --------------------------------------------------

        for chunk in chunks:

            if not chunk.text.strip():

                errors.append(f"{chunk.chunk_id} has empty text.")

            if chunk.section not in self.VALID_SECTIONS:

                errors.append(f"{chunk.chunk_id} invalid section.")

            if not (0 <= chunk.priority <= 1):

                errors.append(f"{chunk.chunk_id} invalid priority.")

            if chunk.word_count <= 0:

                errors.append(f"{chunk.chunk_id} invalid word count.")

            if chunk.character_count <= 0:

                errors.append(f"{chunk.chunk_id} invalid character count.")

            if not chunk.policy_id:

                errors.append(f"{chunk.chunk_id} missing policy id.")

            if not chunk.department:

                errors.append(f"{chunk.chunk_id} missing department.")

            if not chunk.category:

                errors.append(f"{chunk.chunk_id} missing category.")

        return errors