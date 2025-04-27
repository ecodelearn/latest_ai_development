from datetime import datetime
from typing import Optional, Dict, Any

class SearchConfig:
    """Configuration class for enhanced search functionality"""
    
    def __init__(self, topic: str):
        self.topic = topic
        self.file_type: Optional[str] = None
        self.site: Optional[str] = None
        self.in_title: Optional[str] = None
        self.in_url: Optional[str] = None
        self.in_text: Optional[str] = None
        self.date_before: Optional[str] = None
        self.date_after: Optional[str] = None
        self.exact_phrase: bool = False

    def with_file_type(self, file_type: str) -> 'SearchConfig':
        """Set file type filter"""
        self.file_type = file_type
        return self

    def with_site(self, site: str) -> 'SearchConfig':
        """Set site filter"""
        self.site = site
        return self

    def with_title(self, title: str) -> 'SearchConfig':
        """Set title search"""
        self.in_title = title
        return self

    def with_url(self, url: str) -> 'SearchConfig':
        """Set URL search"""
        self.in_url = url
        return self

    def with_text(self, text: str) -> 'SearchConfig':
        """Set text content search"""
        self.in_text = text
        return self

    def with_date_range(self, before: Optional[str] = None, after: Optional[str] = None) -> 'SearchConfig':
        """Set date range filter"""
        self.date_before = before
        self.date_after = after
        return self

    def with_exact_phrase(self, exact: bool = True) -> 'SearchConfig':
        """Set exact phrase matching"""
        self.exact_phrase = exact
        return self

    @property
    def as_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary format"""
        return {
            "topic": self.topic,
            "current_year": str(datetime.now().year)
        }

    def __str__(self) -> str:
        """String representation of search configuration"""
        parts = []
        
        if self.exact_phrase:
            parts.append(f'"{self.topic}"')
        else:
            parts.append(self.topic)
            
        if self.file_type:
            parts.append(f'filetype:{self.file_type}')
        if self.site:
            parts.append(f'site:{self.site}')
        if self.in_title:
            parts.append(f'intitle:{self.in_title}')
        if self.in_url:
            parts.append(f'inurl:{self.in_url}')
        if self.in_text:
            parts.append(f'intext:{self.in_text}')
        if self.date_before or self.date_after:
            date_parts = []
            if self.date_before:
                date_parts.append(f'before:{self.date_before}')
            if self.date_after:
                date_parts.append(f'after:{self.date_after}')
            parts.extend(date_parts)
            
        return ' '.join(parts)
