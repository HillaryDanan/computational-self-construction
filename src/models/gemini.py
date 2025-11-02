"""
Gemini API integration for computational self-construction experiments.
"""

import os
from typing import List, Dict, Optional
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


class GeminiModel:
    """
    Interface to Gemini API for self-construction experiments.
    
    Uses Google's generativeai library to interact with Gemini models.
    """
    
    def __init__(self, model: str = "gemini-2.5-flash"):
        """
        Initialize Gemini model.
        
        Args:
            model: Model identifier (default: gemini-2.5-flash)
        """
        api_key = os.getenv('GOOGLE_API_KEY')
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model)
        self.name = "gemini"
        self.model_name = model
        print(f"[DEBUG] Initialized Gemini with model: {model}")
    
    def query(
        self, 
        prompt: str, 
        context: Optional[List[Dict[str, str]]] = None,
        max_tokens: int = 1000
    ) -> str:
        """
        Send query to Gemini and get response.
        
        Args:
            prompt: Query text
            context: Previous conversation history (for memory conditions)
                     Format: [{'query': 'user msg', 'response': 'model msg'}, ...]
            max_tokens: Maximum response length
            
        Returns:
            Model response text
        """
        # Gemini handles context differently - build full conversation
        if context:
            # Convert context to Gemini chat history format
            history = []
            for exchange in context:
                history.append({
                    "role": "user",
                    "parts": [exchange['query']]
                })
                history.append({
                    "role": "model",
                    "parts": [exchange['response']]
                })
            
            # Start chat with history
            chat = self.model.start_chat(history=history)
            response = chat.send_message(prompt)
        else:
            # No context, single query
            response = self.model.generate_content(prompt)
        
        return response.text