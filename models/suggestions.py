
from dataclasses import dataclass
from typing import List, Dict, Any, Optional


@dataclass
class Suggestion:
    action: str  # What the user should do
    app_or_site: str  # App or site to use
    quote: str  # Motivational quote or advice
    
    def to_dict(self) -> Dict[str, str]:
        """Convert suggestion to dictionary for storage."""
        return {
            "action": self.action,
            "app_or_site": self.app_or_site,
            "quote": self.quote
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> 'Suggestion':
        """Create a suggestion from a dictionary."""
        return cls(
            action=data["action"],
            app_or_site=data["app_or_site"],
            quote=data["quote"]
        )


@dataclass
class SuggestionSet:
    """A set of suggestions for a user session."""
    suggestions: List[Suggestion]
    
    def to_dict(self) -> Dict[str, List[Dict[str, str]]]:
        """Convert suggestion set to dictionary for storage."""
        return {
            "suggestions": [s.to_dict() for s in self.suggestions]
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, List[Dict[str, str]]]) -> 'SuggestionSet':
        """Create a suggestion set from a dictionary."""
        return cls(
            suggestions=[Suggestion.from_dict(s) for s in data["suggestions"]]
        )