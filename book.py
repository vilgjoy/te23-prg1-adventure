format = [
    {
        "id": 1,
        "title": "String title for page",
        "text": "String text for page",
        "options": [
            {"text": "Option 1 with next page id", "next_id": 2},
            {"text": "Option 2 with next page id", "next_id": 3},
        ],
    },
]
BOOK = [
    {
        "id": 1,
        "title": "The Beginning",
        "text": "You are a young adventurer who has just set out on a journey to explore the world. You have heard tales of great treasures and ancient artifacts hidden in the far corners of the land, and you are determined to find them. As you travel through the dense forest, you come across a fork in the road. Do you take the left path or the right path?",
        "options": [
            {"text": "Take the left path", "next_id": 2},
            {"text": "Take the right path", "next_id": 3},
        ],
    },
    {
        "id": 2,
        "title": "The Left Path",
        "text": "You decide to take the left path. As you walk along the winding trail, you hear a rustling in the bushes. Suddenly, a bandit jumps out and demands that you hand over all of your gold. Do you give him your gold or try to fight him?",
        "options": [
            {"text": "Give him your gold", "next_id": 4},
            {"text": "Fight him", "next_id": 5},
        ],
    },
    {
        "id": 3,
        "title": "The Right Path",
        "text": "You choose to take the right path. As you make your way down the trail, you come across a small village. The villagers are friendly and offer you a place to rest for the night. Do you stay in the village or continue on your journey?",
        "options": [
            {"text": "Stay in the village", "next_id": 6},
            {"text": "Continue on your journey", "next_id": 7},
        ],
    },
    {
        "id": 4,
        "title": "The Bandit",
        "text": "You decide to give the bandit your gold. He takes it and runs off into the forest. You continue on your journey, but you can't help but feel like you've been taken advantage of. You arrive at a crossroads. Do you go left or right?",
        "options": [
            {"text": "Go left", "next_id": 8},
            {"text": "Go right", "next_id": 9},
        ],
    },
    {
        "id": 5,
        "title": "The Fight",
        "text": "You decide to fight the bandit. You draw your sword and prepare to defend yourself. The bandit is no match for your skills, and you quickly defeat him. You continue on your journey, feeling proud of your victory. You arrive at a crossroads. Do you go left or right?",
        "options": [
            {"text": "Go left", "next_id": 8},
            {"text": "Go right", "next_id": 9},
        ],
        "loot": "Bandit's Slippers",
    },
    {
        "id": 6,
        "title": "The Village",
        "text": "You decide to stay in the village for the night. The villagers welcome you with open arms and offer you a warm meal and a soft bed to sleep in. You wake up the next morning feeling refreshed and ready to continue your journey. As you leave the village, the villagers give you a small gift to help you on your way. Do you accept the gift or politely decline?",
        "options": [
            {"text": "Accept the gift", "next_id": 10},
            {"text": "Decline the gift", "next_id": 11},
        ],
    },
]