
from dataclasses import dataclass
from typing import List, Dict, Any, Optional
import datetime


@dataclass
class UserSession:
    mode: str  # gaming, work, or study
    mood: str  # happy, stressed, tired, or energetic
    time_of_day: str  # morning, afternoon, or evening
    timestamp: str  # ISO format timestamp
    
    def to_dict(self) -> Dict[str, str]:
        return {
            "mode": self.mode,
            "mood": self.mood,
            "time_of_day": self.time_of_day,
            "timestamp": self.timestamp
        }
        
    @classmethod
    def from_dict(cls, data: Dict[str, str]) -> 'UserSession':
        return cls(
            mode=data["mode"],
            mood=data["mood"],
            time_of_day=data["time_of_day"],
            timestamp=data["timestamp"]
        )