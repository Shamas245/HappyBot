def detect_positive_themes(text: str) -> str:
    """Detect positive themes based on specific keywords."""
    themes = {
        "creativity": ["imagine", "creative", "build", "make", "design", "create"],
        "curiosity": ["learn", "explore", "discover", "question", "wonder", "investigate"],
        "kindness": ["help", "kind", "share", "care", "support", "love"],
        "exploration": ["adventure", "journey", "explore", "travel", "discover", "seek"],
        "reflection": ["reflect", "think", "contemplate", "consider", "ponder"],
        "problem solving": ["solve", "resolve", "figure out", "troubleshoot", "challenge"],
        "bravery": ["courage", "brave", "fearless", "risk", "adventure"],
        "resilience": ["persist", "overcome", "endure", "strong", "bounce back"],
        "empathy": ["understand", "sympathize", "care", "compassion", "relate"],
        "teamwork": ["collaborate", "team", "work together", "help each other", "cooperate"]
    }

    # Lowercase the input text to make the search case-insensitive
    text = text.lower()

    # Check for the presence of keywords for each theme
    for badge, keywords in themes.items():
        if any(keyword in text for keyword in keywords):
            return badge.capitalize()

    # If no theme is detected, return None
    return None
