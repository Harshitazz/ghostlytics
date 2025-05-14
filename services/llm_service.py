
import os
from typing import Dict, List, Any, Optional
import json

from config import get_groq_api_key, LLM_MODEL, LLM_TEMPERATURE, LLM_MAX_TOKENS

try:
    from langchain_groq import ChatGroq
    from langchain.schema import HumanMessage, SystemMessage
except ImportError:
    print("Required libraries not found. Please install with 'pip install langchain-groq langchain'.")
    exit(1)


class LLMService:
    
    def __init__(self):
        self.groq_api_key = get_groq_api_key()
        
        # Initialize Groq client
        self.llm = ChatGroq(
            model_name=LLM_MODEL,
            api_key=self.groq_api_key,
            temperature=LLM_TEMPERATURE,
            max_tokens=LLM_MAX_TOKENS
        )
    
    def generate_suggestions(self, context: Dict[str, Any]) -> Dict[str, Any]:
        prompt = self._create_prompt(context)
        
        messages = [
            SystemMessage(content="""You are a helpful productivity assistant.
You provide personalized suggestions based on a user's mode (gaming, work, or study),
mood (happy, stressed, tired, energetic), and time of day.
Always provide exactly 3 suggestions, each with an action, app/site, and motivational quote."""),
            HumanMessage(content=prompt)
        ]
        
        response = self.llm.invoke(messages)
        
        try:
            return self._parse_response(response.content)
        except Exception as e:
            print(f"Error parsing LLM response: {e}")
            return 
    
    def _create_prompt(self, context: Dict[str, Any]) -> str:
        """Create a prompt for the LLM based on user context."""
        return f"""
Based on the following user context, provide 3 personalized productivity suggestions:
- Mode: {context['mode']}
- Mood: {context['mood']}
- Time of Day: {context['time_of_day']}

For each suggestion, provide:
1. An action the user should take
2. An app or website they should use
3. A motivational quote or piece of advice

Format your response as JSON with the following structure:
{{
  "suggestions": [
    {{
      "action": "...",
      "app_or_site": "...",
      "quote": "..."
    }},
    ...
  ]
}}
"""
    
    def _parse_response(self, response_text: str) -> Dict[str, Any]:
        """Parse the LLM response into structured suggestions."""
        # Extract JSON from the response
        try:
            json_start = response_text.find('{')
            json_end = response_text.rfind('}') + 1
            
            if json_start == -1 or json_end == 0:
                raise ValueError("No JSON found in response")
            
            json_str = response_text[json_start:json_end]
            data = json.loads(json_str)
            
            if "suggestions" not in data or not isinstance(data["suggestions"], list):
                raise ValueError("Invalid response structure")
            
            return data
        except Exception as e:
            raise ValueError(f"Failed to parse LLM response: {e}")
    
 