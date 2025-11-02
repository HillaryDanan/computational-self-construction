"""
Memory persistence implementations for maintaining context across queries.
"""

from typing import List, Dict, Any, Optional


class MemoryManager:
    """
    Manages conversation history for memory persistence conditions.
    
    In conditions with memory_persistence=True, this maintains context.
    In baseline condition, context is cleared between queries.
    """
    
    def __init__(self, persist: bool = True):
        """
        Args:
            persist: If True, maintains context. If False, clears after each query.
        """
        self.persist = persist
        self.history: List[Dict[str, str]] = []
        self.query_count = 0
    
    def add_exchange(self, query: str, response: str) -> None:
        """
        Add a query-response pair to history.
        
        Args:
            query: User query text
            response: Model response text
        """
        self.query_count += 1
        
        if self.persist:
            self.history.append({
                'query_number': self.query_count,
                'query': query,
                'response': response
            })
    
    def get_context(self) -> List[Dict[str, str]]:
        """
        Retrieve conversation history.
        
        Returns:
            List of query-response exchanges (empty if not persisting)
        """
        if self.persist:
            return self.history
        return []
    
    def clear(self) -> None:
        """Clear all history."""
        self.history = []
        self.query_count = 0
    
    def get_summary_stats(self) -> Dict[str, Any]:
        """Get statistics about memory."""
        return {
            'total_queries': self.query_count,
            'stored_exchanges': len(self.history),
            'persistence_enabled': self.persist
        }