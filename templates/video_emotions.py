'''
Template for video emotions
'''
video_emotion_analysis_prompt_system = (
    "You are an advanced video analytics system specialized in analyzing videos to identify emotions invoked in viewers while watching video advertisements. "
    "Your task is to assess the emotional responses evoked by the ad and provide detailed insights into the types of emotions, their associated time segments, intensity (on a scale of 1 to 10), and a short description for each."
    "\n\n"
    "Specifically, you will analyze the following:\n"
    "1. **Emotion Identification**:\n"
    "   - Identify the emotions evoked in viewers while watching the video ad (e.g., happiness, sadness, excitement, nostalgia, etc.).\n"
    "   - Specify the exact time segments during which these emotions are likely invoked (in HH:MM:SS format).\n"
    "   - Rate the intensity of each emotion on a scale of 1 to 10 (1 being the least intense and 10 being the most intense).\n"
    "   - Provide a brief description for each emotion, explaining what might be causing it (e.g., a heartwarming scene, energetic music, or impactful messaging).\n"
    "\n"
    "Return your analysis in a structured JSON format with fields for 'emotionalResponses'."
)


video_emotion_analysis_response_schema = {
    "type": "object",
    "properties": {
        "emotionalResponses": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "emotion": {"type": "string"},  # Type of emotion (e.g., happiness, sadness)
                    "timeSegments": {
                        "type": "array",
                        "items": {"type": "string"}  # Time segments in HH:MM:SS format
                    },
                    "intensity": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Intensity scale
                    },
                    "description": {"type": "string"}  # Brief description of the emotion and its cause
                },
                "required": ["emotion", "timeSegments", "intensity", "description"]
            }
        }
    },
    "required": ["emotionalResponses"]
}

video_emotion_analysis_prompt = (
    "You are an advanced video analytics system tasked with identifying the emotional responses evoked while watching a video advertisement."
    "\n\n"
    "Analyze the video content and provide the following insights:\n"
    "1. **Emotion Identification**:\n"
    "   - List the emotions evoked in viewers while watching the ad (e.g., happiness, sadness, excitement, nostalgia, etc.).\n"
    "   - Specify the exact time segments (in HH:MM:SS format) during which these emotions are likely invoked.\n"
    "   - Rate the intensity of each emotion on a scale of 1 to 10 (1 being the least intense and 10 being the most intense).\n"
    "   - Provide a short description explaining what aspects of the video (e.g., visuals, music, messaging) might be causing each emotion."
    "\n\n"
    "Provide your analysis in JSON format with the following structure:\n"
    "- 'emotionalResponses': A list of identified emotions, the corresponding time segments, intensity, and a description of their causes."
)

### Emotion context extraction
context_extraction_response_schema = {
    "type": "object",
    "properties": {
        "contextAnalysis": {
            "type": "array",
            "items": {
                "type": "string",
                "description": "A 2-3 word phrase that represents the key context of the provided text."
            }
        }
    },
    "required": ["contextAnalysis"]
}


context_extraction_prompt_system = (
    "You are an advanced text analysis system specialized in extracting key contexts from written content. "
    "Your task is to:\n\n"
    "1. **Context Extraction**:\n"
    "   - Analyze the provided text and identify all key contexts.\n"
    "   - Provide each context as a concise 2-3 word phrase.\n"
    "   - Ensure the contexts are specific, relevant, and directly tied to the content of the text.\n"
    "   - Avoid overly generic terms or overly long descriptions.\n\n"
    "Return your analysis in a structured JSON format containing the field 'contextAnalysis'."
)


context_extraction_prompt = (
    "You are an advanced text analysis system tasked with extracting key contexts from written content.\n\n"
    "Please analyze the provided text and complete the following task:\n"
    "- Extract all key contexts from the text and provide each as a concise 2-3 word phrase.\n\n"
    "Return the results in a structured JSON format with the following structure:\n"
    "- 'contextAnalysis': A list of 2-3 word phrases representing the key contexts.\n\n"
    "Input Text:\n\n{text}"
)