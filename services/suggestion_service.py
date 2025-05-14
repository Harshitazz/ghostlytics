
from typing import Dict, List, Any

from models.user_session import UserSession
from models.suggestions import Suggestion, SuggestionSet
from services.llm_service import LLMService


class SuggestionService:
    
    def __init__(self):
        self.llm_service = LLMService()
    
    def generate_suggestions(self, session: UserSession) -> SuggestionSet:
        
        context = {
            "mode": session.mode,
            "mood": session.mood,
            "time_of_day": session.time_of_day
        }
        
        llm_result = self.llm_service.generate_suggestions(context)
        
        suggestions = []
        for item in llm_result["suggestions"]:
            suggestion = Suggestion(
                action=item["action"],
                app_or_site=item["app_or_site"],
                quote=item["quote"]
            )
            suggestions.append(suggestion)
        
        while len(suggestions) < 3:
            suggestions.append(Suggestion(
                action="Take a moment to reflect",
                app_or_site="Mindfulness app",
                quote="The present moment is the only moment available to us."
            ))
        
        return SuggestionSet(suggestions=suggestions[:3])