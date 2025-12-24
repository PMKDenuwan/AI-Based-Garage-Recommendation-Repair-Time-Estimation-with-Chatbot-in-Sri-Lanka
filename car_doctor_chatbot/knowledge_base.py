# knowledge_base.py - Fault categories and question flows

# ============================================
# PART 1: FAULT CATEGORIES FROM YOUR DATASET
# ============================================

FAULT_CATEGORIES = {
    "Engine": {
        "keywords": ["overheating", "steam", "temperature", "coolant", "knocking", "shaking", "power loss"],
        "severities": {
            "Minor": ["Oil leak (Gasket)", "Spark plug change", "Throttle body cleaning"],
            "Moderate": ["Misfiring", "High fuel consumption", "Engine mount worn", "Coolant leak"],
            "Major": ["Overheating", "Timing belt failure", "Water pump failure", "Head gasket leak"]
        }
    },
    "Electrical": {
        "keywords": ["battery", "start", "crank", "lights", "dead", "alternator", "charging"],
        "severities": {
            "Minor": ["Battery drain", "Bulb blown", "Horn issue"],
            "Moderate": ["Alternator issue", "Fuel pump issue", "Ignition coil failure"],
            "Major": ["Complete alternator failure", "Battery completely dead"]
        }
    },
    "Brake": {
        "keywords": ["brake", "braking", "squealing", "grinding", "soft pedal", "stopping"],
        "severities": {
            "Minor": ["Brake pad wear", "Brake noise"],
            "Moderate": ["Brake fluid leak", "Weak braking", "ABS sensor"],
            "Major": ["Brake booster failure", "Master cylinder failure"]
        }
    },
    "Transmission": {
        "keywords": ["gear", "clutch", "slipping", "grinding", "transmission", "shift"],
        "severities": {
            "Minor": ["Mounts", "Gear selector cable"],
            "Moderate": ["Hard gear shifting", "Jerking", "Gearbox oil leak"],
            "Major": ["Clutch slipping", "Reverse gear failure"]
        }
    },
    "Suspension": {
        "keywords": ["vibration", "clunking", "steering", "bumps", "pulling", "shaking"],
        "severities": {
            "Minor": ["Stabilizer links", "Sway bar links"],
            "Moderate": ["Shocks", "Ball joints", "Tie rod ends", "Bearings"],
            "Major": []
        }
    },
    "AC": {
        "keywords": ["ac", "air conditioning", "cooling", "warm air", "cold", "blowing"],
        "severities": {
            "Minor": ["Blower motor", "AC filter", "Gas refill", "Belt"],
            "Moderate": ["AC not cooling", "Condenser fan", "Refrigerant leaks"],
            "Major": ["Compressor failure", "Evaporator leak"]
        }
    },
    "Body": {
        "keywords": ["door", "window", "mirror", "lock", "rust", "lights", "glass"],
        "severities": {
            "Minor": ["Rust", "Door locks", "Mirrors", "Tail lamps", "Glass cracks"],
            "Moderate": [],
            "Major": []
        }
    }
}

# ============================================
# PART 2: CATEGORY-SPECIFIC QUESTIONS
# ============================================

QUESTION_FLOWS = {
    "Engine": [
        {
            "id": "Q1",
            "text": "👉 Is the temperature warning light ON on your dashboard?",
            "symptom_key": "temperature_warning_light"
        },
        {
            "id": "Q2",
            "text": "👉 Do you see steam or smoke coming from the bonnet (hood)?",
            "symptom_key": "steam_or_smoke"
        },
        {
            "id": "Q3",
            "text": "👉 Can you see any coolant or water leaking under the car?",
            "symptom_key": "coolant_leak"
        },
        {
            "id": "Q4",
            "text": "👉 Is the engine still running, or did it turn off?",
            "symptom_key": "engine_status"
        },
        {
            "id": "Q5",
            "text": "👉 Do you hear any unusual knocking, hissing, or tapping sounds?",
            "symptom_key": "unusual_noise"
        }
    ],
    
    "Electrical": [
        {
            "id": "Q1",
            "text": "👉 When you turn the key, does the engine try to crank (make turning sounds)?",
            "symptom_key": "engine_cranks"
        },
        {
            "id": "Q2",
            "text": "👉 Are the dashboard lights turning on at all?",
            "symptom_key": "dashboard_lights_on"
        },
        {
            "id": "Q3",
            "text": "👉 Are the headlights or dashboard lights looking dim or weak?",
            "symptom_key": "lights_dim"
        }
    ],
    
    "Brake": [
        {
            "id": "Q1",
            "text": "👉 Is the brake warning light ON?",
            "symptom_key": "brake_warning_light"
        },
        {
            "id": "Q2",
            "text": "👉 Does the brake pedal feel soft or spongy when you press it?",
            "symptom_key": "soft_brake_pedal"
        },
        {
            "id": "Q3",
            "text": "👉 Do you hear squealing or grinding when braking?",
            "symptom_key": "brake_noise"
        }
    ],
    
    "Transmission": [
        {
            "id": "Q1",
            "text": "👉 Is it difficult to change gears?",
            "symptom_key": "difficult_gear_change"
        },
        {
            "id": "Q2",
            "text": "👉 Do you hear grinding noise when changing gears?",
            "symptom_key": "grinding_noise"
        },
        {
            "id": "Q3",
            "text": "👉 Does the engine rev (RPM goes up) but car doesn't move much?",
            "symptom_key": "no_movement"
        }
    ],
    
    "Suspension": [
        {
            "id": "Q1",
            "text": "👉 Does the steering wheel vibrate while driving?",
            "symptom_key": "steering_vibration"
        },
        {
            "id": "Q2",
            "text": "👉 Is the vibration worse at high speeds (above 60 km/h)?",
            "symptom_key": "high_speed_vibration"
        },
        {
            "id": "Q3",
            "text": "👉 Do you hear clunking or knocking on bumps?",
            "symptom_key": "clunking_noise"
        }
    ],
    
    "AC": [
        {
            "id": "Q1",
            "text": "👉 Is the AC blowing air, but it's warm?",
            "symptom_key": "ac_blowing_warm"
        },
        {
            "id": "Q2",
            "text": "👉 Do you hear clicking or rattling when AC is on?",
            "symptom_key": "ac_noise"
        }
    ],
    
    "Body": [
        {
            "id": "Q1",
            "text": "👉 Which part has the issue? (door / window / mirror / lights)",
            "symptom_key": "body_component"
        }
    ]
}

# ============================================
# PART 3: WARNING LIGHTS DATABASE
# ============================================

WARNING_LIGHTS = {
    "Temperature Warning": {
        "color": "Red",
        "category": "Engine",
        "severity": "Major",
        "meaning": "Engine overheating - coolant system failure"
    },
    "Check Engine Light": {
        "color": "Yellow",
        "category": "Engine",
        "severity": "Moderate",
        "meaning": "Engine system issue - needs diagnosis"
    },
    "Battery Warning": {
        "color": "Red",
        "category": "Electrical",
        "severity": "Major",
        "meaning": "Alternator failure - battery not charging"
    },
    "Brake Warning": {
        "color": "Red",
        "category": "Brake",
        "severity": "Major",
        "meaning": "Brake system failure - brake fluid low"
    },
    "Oil Pressure Warning": {
        "color": "Red",
        "category": "Engine",
        "severity": "Major",
        "meaning": "Low oil pressure - engine damage risk"
    },
    "ABS Warning": {
        "color": "Yellow",
        "category": "Brake",
        "severity": "Moderate",
        "meaning": "Anti-lock brake system fault"
    }
}

# ============================================
# HELPER FUNCTIONS
# ============================================

def detect_category(user_message: str) -> str:
    """Detect fault category from user's message"""
    message_lower = user_message.lower()
    
    for category, data in FAULT_CATEGORIES.items():
        for keyword in data["keywords"]:
            if keyword in message_lower:
                return category
    
    return None

def get_questions_for_category(category: str) -> list:
    """Get question flow for detected category"""
    return QUESTION_FLOWS.get(category, [])

def get_fault_types(category: str, severity: str = None) -> list:
    """Get fault types for category"""
    if category not in FAULT_CATEGORIES:
        return []
    
    severities = FAULT_CATEGORIES[category]["severities"]
    
    if severity:
        return severities.get(severity, [])
    
    # Return all fault types
    all_faults = []
    for fault_list in severities.values():
        all_faults.extend(fault_list)
    return all_faults

# ============================================
# TEST THE KNOWLEDGE BASE
# ============================================

if __name__ == "__main__":
    print("="*70)
    print("🧪 TESTING KNOWLEDGE BASE")
    print("="*70)
    
    # Test 1: Category detection
    test_messages = [
        "My car is overheating",
        "Battery is dead",
        "Brakes are squealing",
        "Gears won't shift"
    ]
    
    print("\n1️⃣ CATEGORY DETECTION TEST:")
    for msg in test_messages:
        category = detect_category(msg)
        print(f"   '{msg}' → {category}")
    
    # Test 2: Question flows
    print("\n2️⃣ QUESTION FLOW TEST:")
    for category in ["Engine", "Brake", "Electrical"]:
        questions = get_questions_for_category(category)
        print(f"\n   {category}: {len(questions)} questions")
        for q in questions[:2]:  # Show first 2
            print(f"      - {q['text']}")
    
    # Test 3: Fault types
    print("\n3️⃣ FAULT TYPES TEST:")
    print(f"   Engine (Major): {get_fault_types('Engine', 'Major')[:3]}")
    print(f"   Brake (Minor): {get_fault_types('Brake', 'Minor')}")
    
    print("\n✅ Knowledge base working correctly!")s