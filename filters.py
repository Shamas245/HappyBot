from better_profanity import profanity

# Load default profanity list
profanity.load_censor_words()

# Topics that are unsafe for children or teens
UNSAFE_TOPICS = {
    "violence", "bomb", "weapon", "drugs", "sex", 
    "self-harm", "alcohol", "suicide", "murder", "terrorism",
    "abuse", "bullying", "rape", "pedophilia", "hate speech",
    "racism", "discrimination", "extremism", "pedophilia", "exploitation",
    "human trafficking", "pornography", "illegal substances", "death",
    "torture", "assault", "war", "genocide", "bullying",
    "harassment", "sexual harassment", "incest", "domestic violence",
    "kidnapping", "gangs", "hate crimes", "disfigurement",
    "sadism", "masochism", "cannibalism", "slavery", "necrophilia",
    "terrorist groups", "anarchy", "anarchism", "political violence", "extreme political views",
    "cult", "religious extremism", "sacrifice", "mutilation", "beheadings",
    "school shootings", "mass shootings", "child labor", "child abuse", "child neglect",
    "toxic substances", "chemical warfare", "nuclear weapons", "biological warfare", "war crimes",
    "trafficking", "illegal weapons", "cruelty to animals", "animal abuse", "poaching",
    "execution", "massacre", "poisoning", "drug trafficking", "sex trafficking"
}


def input_is_safe(user_input: str) -> bool:
    """Check if the user input is appropriate for children/teens."""
    user_input_lower = user_input.lower()

    if profanity.contains_profanity(user_input):
        return False

    return not any(topic in user_input_lower for topic in UNSAFE_TOPICS)

def output_is_safe(response: str) -> bool:
    """Check if the chatbot output is appropriate (same logic as input)."""
    return input_is_safe(response)
