from typing import Optional, Dict, Any
from crewai_tools import SerperDevTool
from .search_config import SearchConfig

class EnhancedSearchTool(SerperDevTool):
    """Enhanced search tool with advanced Google search operators"""

    def __init__(self):
        super().__init__()
        self.config: Optional[SearchConfig] = None

    def configure(self, search_config: SearchConfig) -> 'EnhancedSearchTool':
        """Configure the search tool with search parameters"""
        self.config = search_config
        return self

    def search(self, additional_params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute search with configured parameters
        
        Args:
            additional_params: Optional additional parameters to include in the search
        
        Returns:
            Dict containing search results
        
        Raises:
            ValueError: If search configuration is not set
        """
        if not self.config:
            raise ValueError("Search configuration not set. Use configure() method first.")

        # Build the query string using the configuration
        query = str(self.config)

        # Merge with any additional parameters
        params = {}
        if additional_params:
            params.update(additional_params)

        # Execute the search using the parent class implementation
        return super().search(query, **params)

    @staticmethod
    def builder(topic: str) -> SearchConfig:
        """
        Create a new search configuration builder
        
        Args:
            topic: The main search topic/query
            
        Returns:
            SearchConfig instance for fluent configuration
        """
        return SearchConfig(topic)

    def __str__(self) -> str:
        """String representation of the tool"""
        return f"EnhancedSearchTool(config={self.config})"
