"""
Utilities for CLI formatting and user interaction.
"""
import os
import sys
from typing import List, Dict, Any, Optional
import datetime
from colorama import Fore, Back, Style, init

from models.user_session import UserSession
from models.suggestions import SuggestionSet
import questionary

from models.suggestions import SuggestionSet, Suggestion 
init()

TERM_WIDTH = os.get_terminal_size().columns if sys.stdout.isatty() else 80


def clear_screen() -> None:
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header() -> None:
    """Print the application header."""
    clear_screen()
    print(f"{Fore.CYAN}{Style.BRIGHT}{'=' * TERM_WIDTH}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{Style.BRIGHT}{'ModeSwitch - AI Productivity Assistant':^{TERM_WIDTH}}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{Style.BRIGHT}{'=' * TERM_WIDTH}{Style.RESET_ALL}")
    print()


def print_suggestions(session: UserSession, suggestions: SuggestionSet) -> None:
    
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}SESSION DETAILS:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Mode:{Style.RESET_ALL} {session.mode.capitalize()}")
    print(f"{Fore.YELLOW}Mood:{Style.RESET_ALL} {session.mood.capitalize()}")
    print(f"{Fore.YELLOW}Time:{Style.RESET_ALL} {session.time_of_day.capitalize()}")
    
    # Print date/time
    dt = datetime.datetime.fromisoformat(session.timestamp)
    formatted_time = dt.strftime("%A, %B %d at %I:%M %p")
    print(f"{Fore.YELLOW}Date:{Style.RESET_ALL} {formatted_time}")
    
    print(f"\n{Fore.GREEN}{Style.BRIGHT}YOUR PERSONALIZED SUGGESTIONS:{Style.RESET_ALL}")
    
    # Print each suggestion
    for i, suggestion in enumerate(suggestions.suggestions, 1):
        print(f"\n{Fore.GREEN}{Style.BRIGHT}Suggestion {i}:{Style.RESET_ALL}")
        print(f"{Fore.GREEN}Action:{Style.RESET_ALL} {suggestion.action}")
        print(f"{Fore.GREEN}App/Site:{Style.RESET_ALL} {suggestion.app_or_site}")
        print(f"{Fore.GREEN}Quote:{Style.RESET_ALL} \"{suggestion.quote}\"")
    
    print(f"\n{Fore.CYAN}{'=' * TERM_WIDTH}{Style.RESET_ALL}")

    choices = [
        questionary.Choice(
            title=f"{i+1}. {s.action} - {s.app_or_site}",
            value=i
        )
        for i, s in enumerate(suggestions.suggestions)
    ]

    selected_index = questionary.select(
        "Pick your Top Suggestion:", choices=choices
    ).ask()

    if selected_index is not None and 0 <= selected_index < len(suggestions.suggestions):
        top = suggestions.suggestions.pop(selected_index)
        suggestions.suggestions.insert(0, top)



def print_history(sessions: List[Dict[str, Any]]) -> None:
    """Print session history with nice formatting."""
    if not sessions:
        print(f"\n{Fore.YELLOW}No previous sessions found.{Style.RESET_ALL}")
        return
    
    print(f"\n{Fore.YELLOW}{Style.BRIGHT}RECENT SESSIONS:{Style.RESET_ALL}")
    
    for i, entry in enumerate(sessions, 1):
        session_data = entry["session"]
        suggestions_data = entry["suggestions"]
        
        dt = datetime.datetime.fromisoformat(session_data["timestamp"])
        formatted_time = dt.strftime("%A, %B %d at %I:%M %p")
        
        print(f"\n{Fore.CYAN}{Style.BRIGHT}Session {i} - {formatted_time}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Mode:{Style.RESET_ALL} {session_data['mode'].capitalize()}")
        print(f"{Fore.CYAN}Mood:{Style.RESET_ALL} {session_data['mood'].capitalize()}")
        
        print(f"{Fore.GREEN}{Style.BRIGHT}Top Suggestion:{Style.RESET_ALL}")
        if suggestions_data["suggestions"]:
            top_suggestion = suggestions_data["suggestions"][0]
            print(f"{Fore.GREEN}Action:{Style.RESET_ALL} {top_suggestion['action']}")
            print(f"{Fore.GREEN}App/Site:{Style.RESET_ALL} {top_suggestion['app_or_site']}")
            print(f"{Fore.GREEN}Quote:{Style.RESET_ALL} {top_suggestion['quote']}")
        else:
            print(f"{Fore.YELLOW}No suggestions available{Style.RESET_ALL}")
        
        print(f"{Fore.CYAN}{'-' * 40}{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}{'=' * TERM_WIDTH}{Style.RESET_ALL}")


def get_user_input(prompt: str, choices: List[str]) -> str:
    print(f"{prompt} (Options: {', '.join(choices)} or enter your own):")
    user_input = input("> ").strip().lower()
    
    if not user_input:
        print("Input cannot be empty. Please try again.")
        return get_user_input(prompt, choices)
    
    return user_input
