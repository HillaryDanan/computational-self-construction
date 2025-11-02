"""
GPT API integration for computational self-construction experiments.
"""

import os
from typing import List, Dict, Optional
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


class GPTModel:
    """
    Interface to GPT API for self-construction experiments.
    
    Uses OpenAI's official Python client to interact with GPT models.
    """
    
    def __init__(self, model: str = "gpt-4o"):
        """
        Initialize GPT model.
        
        Args:
            model: Model identifier (default: gpt-4o)
        """
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment")
        
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.name = "gpt"
    
    def query(
        self, 
        prompt: str, 
        context: Optional[List[Dict[str, str]]] = None,
        max_tokens: int = 1000
    ) -> str:
        """
        Send query to GPT and get response.
        
        Args:
            prompt: Query text
            context: Previous conversation history (for memory conditions)
            max_tokens: Maximum response length
            
        Returns:
            Model response text
        """
        # Build messages from context if provided
        messages = []
        
        if context:
            for exchange in context:
                messages.append({
                    "role": "user",
                    "content": exchange['query']
                })
                messages.append({
                    "role": "assistant",
                    "content": exchange['response']
                })
        
        # Add current query
        messages.append({
            "role": "user",
            "content": prompt
        })
        
        # Get response
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            max_tokens=max_tokens
        )
        
        return response.choices[0].message.content