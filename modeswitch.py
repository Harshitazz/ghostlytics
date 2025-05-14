
import argparse
import datetime

from models.user_session import UserSession
from services.suggestion_service import SuggestionService
from services.history_service import HistoryService
from utils.cli_utils import print_header, print_suggestions, print_history, get_user_input

def get_current_time() -> str:
    now = datetime.datetime.now()
    if now.hour < 12:
        return "morning"
    elif now.hour < 17:
        return "afternoon"
    else:
        return "evening"

def parse_arguments():
    parser = argparse.ArgumentParser(description="ModeSwitch - AI Productivity Assistant")
    parser.add_argument("--mode", type=str, choices=["gaming", "work", "study"], 
                        help="Set your productivity mode")
    parser.add_argument("--mood", type=str, 
                        choices=["happy", "stressed", "tired", "energetic"], 
                        help="Set your current mood")
    parser.add_argument("--time", type=str, 
                        choices=["morning", "afternoon", "evening"], 
                        help="Set time of day (auto-detected if not provided)")
    parser.add_argument("--history", action="store_true", 
                        help="Show your session history")
    
    return parser.parse_args()

def main():
    print_header()
    
    args = parse_arguments()
    history_service = HistoryService()
    
    if args.history:
        sessions = history_service.get_recent_sessions(3)
        print_history(sessions)
        return
    
    mode = args.mode
    if not mode:
        mode = get_user_input(
            "Select your mode", 
            ["gaming", "work", "study"]
        )
    
    mood = args.mood
    if not mood:
        mood = get_user_input(
            "How are you feeling?", 
            ["happy", "stressed", "tired", "energetic"]
        )
    
    time_of_day = args.time or get_current_time()
    
    session = UserSession(
        mode=mode,
        mood=mood,
        time_of_day=time_of_day,
        timestamp=datetime.datetime.now().isoformat()
    )
    
    suggestion_service = SuggestionService()
    suggestions = suggestion_service.generate_suggestions(session)
    

    print_suggestions(session, suggestions)
    
    history_service.add_session(session, suggestions)

if __name__ == "__main__":
    main()