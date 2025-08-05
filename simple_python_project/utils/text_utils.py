"""
Text Processing Utilities
Simple text manipulation functions
"""


class TextProcessor:
    """A class for basic text processing operations."""
    
    def reverse_text(self, text: str) -> str:
        """Reverse the given text."""
        return text[::-1]
    
    def count_words(self, text: str) -> int:
        """Count the number of words in the text."""
        return len(text.split())
    
    def to_uppercase(self, text: str) -> str:
        """Convert text to uppercase."""
        return text.upper()
    
    def to_lowercase(self, text: str) -> str:
        """Convert text to lowercase."""
        return text.lower()
    
    def remove_spaces(self, text: str) -> str:
        """Remove all spaces from the text."""
        return text.replace(" ", "")
    
    def is_palindrome(self, text: str) -> bool:
        """Check if the text is a palindrome."""
        cleaned = self.remove_spaces(text.lower())
        return cleaned == cleaned[::-1]