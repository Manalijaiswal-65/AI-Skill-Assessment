import re
import json

def test_extraction(json_response_str):
    try:
        # Robust extraction: find the first { and last }
        match = re.search(r'\{.*\}', json_response_str, re.DOTALL)
        if not match:
            print(f"DEBUG: No JSON object found in AI response")
            return None
        
        cleaned_str = match.group(0)
        return json.loads(cleaned_str)
    except Exception as e:
        print(f"FAILED: {e}")
        return None

# Test cases
test_cases = [
    '{"skills": ["Python"], "questions": []}', # Clean JSON
    'Here is the JSON: ```json\n{"skills": ["JS"], "questions": []}\n``` Hope this helps!', # With markdown and text
    'No JSON here', # No JSON
    '{"incomplete": ', # Invalid JSON
]

for i, case in enumerate(test_cases):
    print(f"Test {i+1}:")
    result = test_extraction(case)
    if result:
        print(f"  SUCCESS: {result}")
    else:
        print(f"  FAILED as expected or error occurred.")
