# gemini_integration.py - Add Gemini API to make responses natural

import google.generativeai as genai
from chatbot_core import DiagnosticChatbot

# ============================================
# STEP 1: CONFIGURE GEMINI
# ============================================

GEMINI_API_KEY = "AIzaSyAxPz6oJY0DpuNXWbfQbxblq-dhSBOC8dA"  # ← PUT YOUR KEY HERE
genai.configure(api_key=GEMINI_API_KEY)

# Create model
model = genai.GenerativeModel('gemini-1.5-flash')

# ============================================
# STEP 2: CREATE ENHANCED CHATBOT
# ============================================

class GeminiChatbot(DiagnosticChatbot):
    """
    Enhanced chatbot that uses Gemini to make responses more natural
    """
    
    def __init__(self):
        super().__init__()
        self.gemini_model = model
    
    def _make_response_natural(self, question_text: str) -> str:
        """
        Use Gemini to make the question sound more natural and empathetic
        
        Input: "Is the engine still running?"
        Output: "Got it 👍 Now, important question - is the engine still running, or did it turn off?"
        """
        
        prompt = f"""You are a friendly, empathetic car mechanic assistant.

Take this technical question and make it sound natural and caring, like a friend helping.

Technical question: "{question_text}"

Rules:
1. Keep it short (1-2 sentences max)
2. Use 👉 emoji for the question
3. Sound empathetic if it's a serious issue
4. Don't add extra questions
5. Keep the core question unchanged

Respond with ONLY the improved question, nothing else."""

        try:
            response = self.gemini_model.generate_content(prompt)
            improved = response.text.strip()
            
            # Remove quotes if Gemini added them
            improved = improved.strip('"').strip("'")
            
            return improved
        except Exception as e:
            print(f"⚠️  Gemini error: {e}")
            # Fallback to original question
            return question_text
    
    def _ask_next_question(self) -> dict:
        """Override to use Gemini for natural responses"""
        # Get the base response
        result = super()._ask_next_question()
        
        # Make it natural with Gemini (optional - only if you want)
        # For now, we'll skip this to keep it fast
        # Uncomment below to enable:
        
        # if result['stage'] == 'questioning':
        #     natural_message = self._make_response_natural(result['bot_message'])
        #     result['bot_message'] = natural_message
        
        return result

# ============================================
# STEP 3: TEST WITH GEMINI
# ============================================

def test_natural_responses():
    """Test Gemini's natural language improvements"""
    print("="*70)
    print("🧪 TESTING GEMINI NATURAL RESPONSES")
    print("="*70)
    
    bot = GeminiChatbot()
    
    technical_questions = [
        "Is the temperature warning light ON?",
        "Do you see steam or smoke?",
        "Is the engine still running?"
    ]
    
    print("\nMaking questions more natural with Gemini...\n")
    
    for q in technical_questions:
        natural_q = bot._make_response_natural(q)
        print(f"Before: {q}")
        print(f"After:  {natural_q}")
        print()
    
    print("✅ Gemini integration working!")

# ============================================
# STEP 4: FULL CONVERSATION TEST
# ============================================

def test_full_conversation():
    """Test complete conversation with Gemini"""
    print("="*70)
    print("🚗 FULL CONVERSATION TEST")
    print("="*70)
    
    bot = GeminiChatbot()
    
    # Start
    greeting = bot.start_conversation("Kavindu")
    print(f"\n🤖: {greeting}")
    
    # Conversation
    messages = [
        "My Suzuki Alto is overheating near Dondra",
        "Yes, the temperature light is red",
        "Yes, I see steam coming out",
        "Yes, there's coolant leaking",
        "The engine stopped"
    ]
    
    for msg in messages:
        print(f"\n👤: {msg}")
        
        result = bot.process_message(msg)
        print(f"\n🤖: {result['bot_message']}")
        
        if result['stage'] == 'diagnosis_complete':
            print("\n" + "="*70)
            print("✅ DIAGNOSIS COMPLETE")
            print("="*70)
            
            diagnosis = result['diagnosis']
            print(f"\n📋 {diagnosis['fault_category']}: {diagnosis['fault_type']}")
            print(f"⚠️  Severity: {diagnosis['severity']}")
            print(f"🚗 Drivable: {'No' if not diagnosis['is_safe_to_drive'] else 'Yes'}")
            
            break

# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("\nSelect test:")
    print("1. Test natural responses")
    print("2. Test full conversation")
    
    choice = input("\nChoice (1-2): ").strip()
    
    if choice == "1":
        test_natural_responses()
    elif choice == "2":
        test_full_conversation()
    else:
        print("Invalid choice")