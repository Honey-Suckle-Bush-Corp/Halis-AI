# halis_logic.py
import random
from textblob import TextBlob

# --- Static Knowledge Base ---
knowledge_base = {
    "grounding": [
        "5-4-3-2-1 grounding technique: Name 5 things you can see, 4 you can touch, 3 you can hear, 2 you can smell, 1 you can taste.",
        "Deep breathing: Inhale for 4 seconds, hold for 4, exhale 4, hold 4.",
        "Notice your surroundings: What colors, textures, and objects do you see?",
        "Progressive muscle relaxation: Tense and release each muscle group slowly."
    ],
    "encouragement": [
        "You're doing your best, and that's enough.",
        "Small steps are still progress.",
        "It's okay to feel how you feel. You are valid.",
        "Remember to take breaks and care for yourself."
    ],
    "reflection": [
        "Can you describe what just happened that made you feel this way?",
        "What thoughts are running through your mind right now?",
        "If you could give advice to a friend feeling like this, what would it be?",
        "What is one thing you can do right now to support yourself?"
    ]
}

# --- Emotion Keywords ---
emotion_keywords = {
    "happy": ["happy", "joy", "excited", "content", "pleased", "grateful", "cheerful"],
    "sad": ["sad", "down", "upset", "unhappy", "depressed", "mournful", "melancholy"],
    "anxious": ["anxious", "nervous", "worried", "stressed", "overwhelmed", "tense", "uneasy"],
    "angry": ["angry", "mad", "frustrated", "annoyed", "irritated", "resentful"],
    "lonely": ["lonely", "alone", "isolated", "abandoned", "left out"],
    "calm": ["calm", "relaxed", "peaceful", "serene", "centered"],
    "confused": ["confused", "unsure", "lost", "uncertain", "puzzled", "doubtful"],
    "hopeful": ["hopeful", "optimistic", "expectant", "positive"],
    "fearful": ["fearful", "scared", "afraid", "terrified", "worried"],
    "guilty": ["guilty", "regretful", "ashamed", "remorseful"]
}

# --- Global Phrase Bank ---
global_phrase_bank = {
    "encouragement": set(knowledge_base["encouragement"]),
    "reflection": set(knowledge_base["reflection"])
}

# --- Helper Functions ---
def detect_emotion(message):
    """Detect emotion from keywords first, fallback to sentiment analysis."""
    message_lower = message.lower()
    for emotion, keywords in emotion_keywords.items():
        if any(word in message_lower for word in keywords):
            return emotion
    polarity = TextBlob(message).sentiment.polarity
    if polarity > 0.3:
        return "happy"
    elif polarity < -0.3:
        return "sad"
    else:
        return "neutral"

def learn_new_phrases(message):
    """Dynamically add non-personal phrases to the global bank."""
    words = message.split()
    if any(word.lower() in emotion_keywords["happy"] for word in words):
        global_phrase_bank["encouragement"].add(message)
    if any(word.lower() in emotion_keywords["sad"] + emotion_keywords["anxious"] for word in words):
        global_phrase_bank["reflection"].add(message)

def generate_response(message, context=None):
    """
    Generates a Halis response using session-limited context.
    """
    last_emotion = detect_emotion(message)
    learn_new_phrases(message)

    response_options = []

    if last_emotion in ["sad", "anxious", "angry", "lonely", "fearful", "guilty"]:
        response_options.append(random.choice(knowledge_base["grounding"]))
        if random.random() < 0.5:
            response_options.append(random.choice(list(global_phrase_bank["reflection"])))
    else:
        response_options.append(random.choice(list(global_phrase_bank["encouragement"])))

    if random.random() < 0.3:
        response_options.append(random.choice(list(global_phrase_bank["encouragement"])))

    final_response = " ".join(response_options)
    return final_response


