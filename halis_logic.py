# halis_logic.py
import random
from textblob import TextBlob

# --- Static Knowledge Base (Curated from mental health resources) ---
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

# --- Session-Limited Context (anonymous, in RAM only) ---
session_context = {}

# --- Emotion Keywords (expanded, nuanced) ---
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

# --- Global Phrase Bank for Dynamic Growth ---
global_phrase_bank = {
    "encouragement": set(knowledge_base["encouragement"]),
    "reflection": set(knowledge_base["reflection"])
}

# --- Helper Functions ---

def detect_emotion(message):
    """Detect emotion from keywords first, then fallback to sentiment analysis."""
    message_lower = message.lower()
    for emotion, keywords in emotion_keywords.items():
        if any(word in message_lower for word in keywords):
            return emotion
    # Fallback to sentiment polarity
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
    # Simple rule: if a message contains positive keywords, add a new encouragement
    if any(word.lower() in emotion_keywords["happy"] for word in words):
        global_phrase_bank["encouragement"].add(message)
    # If message contains reflective keywords, add to reflection
    if any(word.lower() in emotion_keywords["sad"] + emotion_keywords["anxious"] for word in words):
        global_phrase_bank["reflection"].add(message)

def generate_response(message, user_id="default_user"):
    """
    Generate Halis response:
    - Detect nuanced emotion
    - Use session-limited context
    - Use grounding, encouragement, reflection techniques
    - Dynamically grow language patterns safely
    """
    # --- Detect emotion ---
    emotion = detect_emotion(message)
    
    # --- Update session memory (RAM only, per session) ---
    if user_id not in session_context:
        session_context[user_id] = {"last_emotion": emotion, "last_messages": []}
    session_context[user_id]["last_emotion"] = emotion
    session_context[user_id]["last_messages"].append(message)
    context = session_context[user_id]["last_messages"][-3:]  # last 3 messages for context
    
    # --- Learn new phrases (anonymous) ---
    learn_new_phrases(message)
    
    # --- Generate response ---
    response_options = []
    
    # Respond to detected emotion
    if emotion in ["sad", "anxious", "angry", "lonely", "fearful", "guilty"]:
        response_options.append(random.choice(knowledge_base["grounding"]))
        # Add reflection or encouragement from global phrase bank
        if random.random() < 0.5:
            response_options.append(random.choice(list(global_phrase_bank["reflection"])))
    elif emotion in ["happy", "hopeful", "calm"]:
        response_options.append(random.choice(list(global_phrase_bank["encouragement"])))
    else:
        # Neutral or confused
        response_options.append(random.choice(list(global_phrase_bank["reflection"])))
    
    # Occasionally add extra encouragement
    if random.random() < 0.3:
        response_options.append(random.choice(list(global_phrase_bank["encouragement"])))
    
    # Combine options into final response
    final_response = " ".join(response_options)
    return final_response

