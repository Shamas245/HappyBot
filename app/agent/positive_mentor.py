import os
from dotenv import load_dotenv


load_dotenv()


def load_gemini():
    gemini_key = os.environ.get('GEMINI_KEY')
    return gemini_key

import requests
from fastapi import FastAPI, Query

app = FastAPI()
load_gemini()


FORBIDDEN_WORDS = {
    "Safety & Harm": {
        "Violence & Abuse": [
            "kill", "killing", "murdered", "murder",
            "hurt", "hurting", "harm", "harming", "injure", "injuring", "injury",
            "hit", "punch", "kick", "slap", "beat", "beating",
            "fight", "fighting", "attack", "attacking", "assault", "assaulted", "assault",
            "bully", "bullying",
            "abuse", "abusive", "mistreat", "mistreatment",
            "torture", "tortured", "torment",
            "weapon", "weapons", "gun", "guns", "knife", "knives", "bomb", "bombs",
            "shoot", "shooting", "stab", "stabbing", "explosion", "explode",
            "threat", "threaten", "threatened",
            "strangle", "strangle"
        ],
        "Suicide & Self-Harm": [
            "suicide", "suicidal", "self-harm", "self-injure", "cut", "cutting", "burn", "burning", "kill myself",
            "end my life", "I want to die",
            "pills", "overdose",
            "razor", "blade"
        ],
        "Dangerous Activities": [
            "drugs", "drug", "marijuana", "cocaine", "heroin", "ecstasy", "meth", "opioids", "vape", "vaping",
            "smoke", "smoking",
            "alcohol", "beer", "wine", "liquor", "drunk", "drinking", "intoxicated",
            "gamble", "gambling",
            "dare", "dares",
            "trespass", "trespassing",
            "run away", "running away"
        ],
        "Grooming and Exploitation": [
            "groom", "grooming",
            "pedophile", "pedophilia",
            "exploit", "exploitation",
            "child abuse", "child pornography",
            "age play"
        ]
    },
    "Inappropriate Content": {
        "Sexually Explicit": [
            "sex", "sexual", "porn", "pornography", "erotic", "nude", "naked",
            "intercourse", "masturbate", "orgasm", "penis", "vagina", "breasts",
            "rape", "raping",
            "prostitute", "prostitution"
        ],
        "Hate Speech": [
            "hate", "hatred", "racist", "racism", "sexist", "sexism",
            "homophobic", "homophobia", "transphobic", "transphobia",
            "nazi", "fascist",
            "ethnic slur", "racial slur"
        ],
        "Profanity": [
            "fuck", "shit", "damn", "ass", "bitch", "bastard",
            "piss", "cunt", "cock", "dick", "slut",
            "motherfucker"
        ]
    }
}

safety_harm = FORBIDDEN_WORDS['Safety & Harm']
violence_abuse = safety_harm['Violence & Abuse']
suic_selfharm = safety_harm['Suicide & Self-Harm']
dang_act = safety_harm['Dangerous Activities']
groom_exp = safety_harm['Grooming and Exploitation']
inappr_content = FORBIDDEN_WORDS['Inappropriate Content']
sex_explicit = inappr_content['Sexually Explicit']
hate_speech = inappr_content['Hate Speech']
profanity = inappr_content['Profanity']

words = violence_abuse + suic_selfharm + dang_act + groom_exp + sex_explicit + hate_speech + profanity

@app.get('/chat')
def ask(prompt: str, options: str = Query('system', enum=['assistant', 'user'])):
    updated_system_message = 'The Child-Safe AI Mentor is a secure, educational AI platform crafted for children, teens, \
                       and adults. It ensures responsible AI usage by offering age-specific interactions, content \
                       filtering, and parental control features.'
    response = requests.post(
        "https://api.aimlapi.com/v1/chat/completions",
        headers={
            "Content-Type": "application/json",

            # Insert your AIML API Key instead of <YOUR_AIMLAPI_KEY>:
            "Authorization": f"Bearer {load_gemini()}",
            "Content-Type": "application/json"
        },
        json={
            "model": "qwen-max",
            "messages": [
                {
                    "role": f"{options}",
                    # Insert your question for the model here, instead of Hello:
                    "content": f"{updated_system_message}"
                }
            ]
        }
    )

    data = response.json()

    if prompt in words:
        return 'Forbidden content.'
    else:
        return data
