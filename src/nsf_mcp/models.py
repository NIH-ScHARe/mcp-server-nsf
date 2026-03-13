"""
Data models used across the project.

These are simple Python representations of NSF awards.

Having a model layer helps keep data structured and
makes downstream processing (embeddings, analytics)
cleaner.
"""

from dataclasses import dataclass


@dataclass
class Award:
    """
    Representation of an NSF award.
    """

    title: str
    abstract: str
    institution: str
    funding: float

    @classmethod
    def from_api(cls, data: dict):
        """
        Convert raw NSF API JSON into an Award object.
        """

        return cls(
            title=data.get("title", ""),
            abstract=data.get("abstractText", ""),
            institution=data.get("awardeeName", ""),
            funding=float(data.get("fundsObligatedAmt", 0)),
        )
