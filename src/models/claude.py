"""
Claude API integration for computational self-construction experiments.
"""

import os
from typing import List, Dict, Optional
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()


class ClaudeModel:
    """
    Interface to Claude API for self-construction experiments.
    
    Uses Anthropic's official Python client to interact with Claude models.
    """
    
    def __init__(self, model: str = "claude-sonnet-4-20250514"):
        """
        Initialize Claude model.
        
        Args:
            model: Model identifier (default: claude-sonnet-4)
        """
        api_key = os.getenv('ANTHROPIC_API_KEY')
        if not api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment")
        
        self.client = Anthropic(api_key=api_key)
        self.model = model
        self.name = "claude"
    
    def query(
        self, 
        prompt: str, 
        context: Optional[List[Dict[str, str]]] = None,
        max_tokens: int = 1000
    ) -> str:
        """
        Send query to Claude and get response.
        
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
        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            messages=messages
        )
        
        return response.content[0].text