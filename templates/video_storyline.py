'''
This is the template for storyline
'''
storyline_message_analysis_prompt_system = (
    "You are an advanced video analytics system specializing in assessing the clarity of the storyline and the relevance of the message in video advertisements. "
    "Your task is to evaluate the video content, assign objective scores, provide descriptive assessments, and suggest actionable improvements to enhance the ad's effectiveness."
    "\n\n"
    "Specifically, you will analyze the following:\n"
    "1. **Storyline Clarity**:\n"
    "   - Rate the clarity of the storyline on a scale of 1 to 10.\n"
    "   - Provide a brief description explaining why the storyline is clear or unclear.\n"
    "2. **Message Relevance**:\n"
    "   - Rate the relevance of the message on a scale of 1 to 10.\n"
    "   - Provide a short description explaining why the message is relevant or not relevant to the target audience.\n"
    "3. **Improvement Suggestions**:\n"
    "   - Provide concise suggestions for improving the clarity of the storyline and the relevance of the message.\n"
    "   - Include descriptive suggestions (why the improvement is needed) and actionable steps (what should be done).\n"
    "\n\n"
    "Return your analysis in a structured JSON format with fields for 'storylineClarity', 'messageRelevance', and 'improvementSuggestions'."
)

storyline_message_analysis_response_schema = {
    "type": "object",
    "properties": {
        "storylineClarity": {
            "type": "object",
            "properties": {
                "score": {"type": "number", "minimum": 1, "maximum": 10},  # Objective score for storyline clarity
                "description": {"type": "string"}  # Brief description of the clarity of the storyline
            },
            "required": ["score", "description"]
        },
        "messageRelevance": {
            "type": "object",
            "properties": {
                "score": {"type": "number", "minimum": 1, "maximum": 10},  # Objective score for message relevance
                "description": {"type": "string"}  # Brief description of the relevance of the message
            },
            "required": ["score", "description"]
        },
        "improvementSuggestions": {
            "type": "object",
            "properties": {
                "storyline": {
                    "type": "object",
                    "properties": {
                        "descriptive": {"type": "string"},  # Why the improvement is needed
                        "action": {"type": "string"}  # What should be done
                    },
                    "required": ["descriptive", "action"]
                },
                "message": {
                    "type": "object",
                    "properties": {
                        "descriptive": {"type": "string"},  # Why the improvement is needed
                        "action": {"type": "string"}  # What should be done
                    },
                    "required": ["descriptive", "action"]
                }
            },
            "required": ["storyline", "message"]
        }
    },
    "required": ["storylineClarity", "messageRelevance", "improvementSuggestions"]
}

storyline_message_analysis_prompt = (
    "You are an advanced video analytics system tasked with evaluating the clarity of the storyline and the relevance of the message in video advertisements."
    "\n\n"
    "Analyze the video content and provide the following insights:\n"
    "1. **Storyline Clarity**:\n"
    "   - Assign a score between 1 and 10 for the clarity of the storyline.\n"
    "   - Provide a brief description explaining why the storyline is clear or unclear.\n"
    "2. **Message Relevance**:\n"
    "   - Assign a score between 1 and 10 for the relevance of the message to the intended audience.\n"
    "   - Provide a short description explaining why the message is relevant or not relevant.\n"
    "3. **Improvement Suggestions**:\n"
    "   - Provide concise suggestions for improving the clarity of the storyline and the relevance of the message.\n"
    "   - Include descriptive suggestions (why the improvement is needed) and actionable steps (what should be done).\n"
    "\n\n"
    "Provide your analysis in JSON format with the following structure:\n"
    "- 'storylineClarity': { 'score': X, 'description': '...' }\n"
    "- 'messageRelevance': { 'score': X, 'description': '...' }\n"
    "- 'improvementSuggestions': {\n"
    "    'storyline': { 'descriptive': '...', 'action': '...' },\n"
    "    'message': { 'descriptive': '...', 'action': '...' }\n"
    "  }"
)

# Prompts for storyline archetype
video_storyline_archetype_analysis_response_schema = {
    "type": "object",
    "properties": {
        "archetypeAnalysis": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "archetype": {
                        "type": "string",
                        "description": "The identified storyline archetype (e.g., Hero’s Journey, Rags to Riches, Quest, Comedy, Tragedy, Rebirth, etc.)."
                    },
                    "timeSegments": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Time segments in HH:MM:SS format where the archetype is identified."
                    },
                    "description": {
                        "type": "string",
                        "description": "A detailed explanation of how the archetype is represented in the specified video segments."
                    }
                },
                "required": ["archetype", "timeSegments", "description"]
            }
        },
        "archetypeFlow": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "fromArchetype": {
                        "type": "string",
                        "description": "The initial archetype before the transition."
                    },
                    "toArchetype": {
                        "type": "string",
                        "description": "The subsequent archetype after the transition."
                    },
                    "transitionSegment": {
                        "type": "string",
                        "description": "The time segment (in HH:MM:SS format) where the transition occurs."
                    },
                    "transitionDescription": {
                        "type": "string",
                        "description": "Explanation of how and why the archetype changes within the video."
                    }
                },
                "required": ["fromArchetype", "toArchetype", "transitionSegment", "transitionDescription"]
            }
        }
    },
    "required": ["archetypeAnalysis", "archetypeFlow"]
}

video_storyline_archetype_analysis_prompt_system = (
    "You are an advanced video analytics system specialized in analyzing the storyline archetypes of video advertisements. "
    "Your task is to:\n\n"
    "1. **Archetype Identification**:\n"
    "   - Identify all the storyline archetypes (e.g., Hero’s Journey, Rags to Riches, Quest, Comedy, Tragedy, Rebirth, etc.) present in the video.\n"
    "   - Specify the time segments (in HH:MM:SS format) where each archetype is identified.\n"
    "   - Provide a detailed explanation of how each archetype is represented in the specified video segments.\n\n"
    "2. **Archetype Flow Analysis**:\n"
    "   - Detect any changes or transitions between archetypes within the video.\n"
    "   - For each transition, specify:\n"
    "     - The initial archetype ('fromArchetype').\n"
    "     - The subsequent archetype ('toArchetype').\n"
    "     - The time segment ('transitionSegment') where the change occurs.\n"
    "     - An explanation ('transitionDescription') of how and why the archetype changes within the video.\n\n"
    "Return your analysis in a structured JSON format with fields for 'archetypeAnalysis' and 'archetypeFlow'."
)


video_storyline_archetype_analysis_prompt = (
    "You are an advanced video analytics system tasked with analyzing storyline archetypes in video advertisements.\n\n"
    "Please analyze the video and provide the following insights:\n"
    "1. **Archetype Identification**:\n"
    "   - Identify all the storyline archetypes (e.g., Hero’s Journey, Rags to Riches, Quest, Comedy, Tragedy, Rebirth, etc.) present in the video.\n"
    "   - Specify the time segments (in HH:MM:SS format) where each archetype is found.\n"
    "   - Provide a detailed explanation of how each archetype is represented.\n\n"
    "2. **Archetype Flow Analysis**:\n"
    "   - Detect transitions between archetypes within the video.\n"
    "   - Specify the following for each transition:\n"
    "     - The initial archetype ('fromArchetype').\n"
    "     - The subsequent archetype ('toArchetype').\n"
    "     - The time segment ('transitionSegment') where the transition occurs.\n"
    "     - An explanation ('transitionDescription') of how and why the archetype changes within the video.\n\n"
    "Provide your analysis in JSON format with the following structure:\n"
    "- 'archetypeAnalysis': A list of identified archetypes, their time segments, and detailed descriptions.\n"
    "- 'archetypeFlow': A list of transitions between archetypes, with the initial archetype, subsequent archetype, transition time, and explanations."
)