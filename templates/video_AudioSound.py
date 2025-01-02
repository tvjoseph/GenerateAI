'''
This is the prompt template for audio and sound analysis
'''
sound_music_analysis_prompt_system = (
    "You are an advanced video analytics system specializing in evaluating the effectiveness of sound, voiceovers, and music in video advertisements. "
    "Your task is to assess the type of sound/music, its emotional impact, its relevance to the ad, and its overall contribution to creating emotional and brand impact."
    "\n\n"
    "Specifically, you will analyze the following:\n"
    "1. **Sound/Music Analysis**:\n"
    "   - Identify the type of sound/music used in the ad (e.g., background music, jingles, sound effects, voiceovers, etc.).\n"
    "   - Describe the emotional impact of the sound/music (e.g., excitement, calmness, nostalgia, tension, joy, etc.).\n"
    "   - Assign an objective score between 1 and 10 for the emotional impact of the sound/music.\n"
    "   - Evaluate the relevance of the sound/music to the ad's storyline, message, and branding.\n"
    "   - Assign an objective score between 1 and 10 for the relevance of the sound/music.\n"
    "   - Provide a brief explanation of how the sound/music contributes to the emotional and brand impact of the ad.\n"
    "\n\n"
    "Return your analysis in a structured JSON format with fields for 'soundMusicElements'."
)

sound_music_analysis_response_schema = {
    "type": "object",
    "properties": {
        "soundMusicElements": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "type": {"type": "string"},  # Type of sound/music (e.g., background music, voiceovers)
                    "emotionalImpact": {"type": "string"},  # Emotional impact of the sound/music
                    "emotionScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Objective score for emotional impact
                    },
                    "relevanceScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Objective score for relevance
                    },
                    "description": {"type": "string"}  # Brief explanation of its emotional and brand impact
                },
                "required": ["type", "emotionalImpact", "emotionScore", "relevanceScore", "description"]
            }
        }
    },
    "required": ["soundMusicElements"]
}

sound_music_analysis_prompt = (
    "You are an advanced video analytics system tasked with analyzing the effectiveness of sound, voiceovers, and music in video advertisements."
    "\n\n"
    "Analyze the video content and provide the following insights:\n"
    "1. **Sound/Music Analysis**:\n"
    "   - Identify the type of sound/music used in the ad (e.g., background music, jingles, sound effects, voiceovers, etc.).\n"
    "   - Describe the emotional impact of the sound/music (e.g., excitement, calmness, nostalgia, tension, joy, etc.).\n"
    "   - Assign an objective score between 1 and 10 for the emotional impact of the sound/music.\n"
    "   - Evaluate the relevance of the sound/music to the ad's storyline, message, and branding.\n"
    "   - Assign an objective score between 1 and 10 for the relevance of the sound/music.\n"
    "   - Provide a short explanation of how the sound/music contributes to the emotional and brand impact of the ad.\n"
    "\n\n"
    "Provide your analysis in JSON format with the following structure:\n"
    "- 'soundMusicElements': A list of objects, each with fields for 'type', 'emotionalImpact', 'emotionScore', 'relevanceScore', and 'description'."
)