
import os
import json
from typing import List, Dict, Any, Optional, Tuple
from pathlib import Path

from models.user_session import UserSession
from models.suggestions import Suggestion, SuggestionSet


class HistoryService:
    
    def __init__(self, data_file: Optional[str] = None):
        # Default to data directory in the project root
        if data_file is None:
            data_dir = Path(__file__).parent.parent.parent / "data"
            data_dir.mkdir(exist_ok=True)
            data_file = data_dir / "session_history.json"
            
        self.data_file = Path(data_file)
        
        # Create file if it doesn't exist
        if not self.data_file.exists():
            self._save_data({"sessions": []})
    
    def add_session(self, session: UserSession, suggestions: SuggestionSet) -> None:
        data = self._load_data()
        
        # Create session entry
        session_entry = {
            "session": session.to_dict(),
            "suggestions": suggestions.to_dict()
        }
        
        # Add to start of list (most recent first)
        data["sessions"].insert(0, session_entry)
        
        # Keep only the most recent 10 sessions
        data["sessions"] = data["sessions"][:10]
        
        # Save updated data
        self._save_data(data)
    
    def get_recent_sessions(self, count: int = 3) -> List[Dict[str, Any]]:
        data = self._load_data()
        return data["sessions"][:count]
    
    def _load_data(self) -> Dict[str, List[Dict[str, Any]]]:
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            # Return empty data if file doesn't exist or is invalid
            return {"sessions": []}
    
    def _save_data(self, data: Dict[str, Any]) -> None:
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=2)