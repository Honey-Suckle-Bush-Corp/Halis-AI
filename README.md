# Halis

<b> Halis </b> is an open-source conversational AI designed to support **mental health resilience**. Built using [Rasa](https://rasa.com/), Halis offers non-clinical companionship for individuals navigating challenging moments, providing encouragement, clarity, and a gentle reminder that they're not alone.

---

## Vision
Halis was created to reflect the belief that healing isn’t linear, and people need nonjudgmental tools that support emotional awareness — not just crisis intervention. Inspired by the best of AI and the warmth of human connection.

---

## Purpose
Halis is <b> not a therapist </b> — it’s a steady digital companion that listens, reflects, and empowers users to better understand their emotions and stay grounded. It can:

- Offer daily emotional check-ins
- Provide affirmations and grounding exercises
- Suggest coping strategies
- Help articulate feelings for therapy support
- Gently recommend professional resources if needed

---

## Project Structure
Halis/
├── data/ # NLU training data
├── domain.yml # Bot personality and actions
├── models/ # Trained Rasa models
├── rasa/ # Core Rasa logic and config
├── results/ # Logs and exported interactions
├── tests/ # End-to-end test cases
├── actions/ # Custom Python actions
├── .gitignore # Ignore unnecessary files
└── README.md # This file

---

## Getting Started
### Prerequisites
- Python 3.10+
- Rasa Open Source (`pip install rasa`)
- Optional: [Poetry](https://python-poetry.org/) or `venv` for environment management

### Quick Start
#### Navigate to the project root
<i> cd Halis </i>

#### Create a virtual environment (optional but recommended)
<i>python -m venv venv '.\venv\Scripts\activate' # Windows</i>

<i>source venv/bin/activate # Mac/Linux</i>

#### Install dependencies
<i>pip install rasa</i>

#### Train the model
<i>rasa train</i>

#### Run the bot (in terminal)
<i>rasa shell</i>

---

## Disclaimer
Halis is not a substitute for professional therapy or medical care. If you or someone you know is in crisis, please seek immediate help through a licensed professional or hotline.

---

## Contributing
Pull requests, ideas, and feedback are welcome! If you’d like to collaborate, start a conversation or open an issue.

---

## Created with love by Honey Suckle Bush
In memory of Dawn, whose compassion continues to guide this mission.
