'''
Template for people related analysis
'''

# Emotions

video_human_emotion_analysis_response_schema = {
    "type": "object",
    "properties": {
        "humanEmotionAnalysis": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "emotion": {"type": "string"},  # Detected emotion (e.g., happiness, sadness, etc.)
                    "timeSegments": {
                        "type": "array",
                        "items": {"type": "string"}  # Time segments in HH:MM:SS format
                    },
                    "engagementScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for viewer engagement
                    },
                    "alignmentScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for alignment with brand values
                    },
                    "narrativeEnhancementScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for narrative enhancement
                    },
                    "description": {
                        "type": "string"  # Description of how the emotion impacts engagement, alignment, and narrative
                    },
                    "improvementSuggestions": {
                        "type": "string"  # Suggestions for better utilization of human emotions
                    }
                },
                "required": [
                    "emotion",
                    "timeSegments",
                    "engagementScore",
                    "alignmentScore",
                    "narrativeEnhancementScore",
                    "description"
                ]
            }
        }
    },
    "required": ["humanEmotionAnalysis"]
}


video_human_emotion_analysis_prompt_system = (
    "You are an advanced video analytics system specialized in analyzing the emotions depicted by human faces in video advertisements. "
    "Your task is to assess how these emotions contribute to viewer engagement, align with the brand's values, and enhance the overall narrative of the advertisement."
    "\n\n"
    "Specifically, you will:\n"
    "1. **Emotion Detection**:\n"
    "   - Identify the emotions depicted by human faces in the video ad (e.g., happiness, sadness, excitement, anger, etc.).\n"
    "   - Specify the time segments (in HH:MM:SS format) where each emotion is prominently displayed.\n"
    "\n\n"
    "2. **Engagement, Alignment, and Narrative Enhancement**:\n"
    "   - Assess how these emotions make the ad engaging for viewers and provide a score between 1 and 10.\n"
    "   - Evaluate how well these emotions align with the brand's values and give a score between 1 and 10.\n"
    "   - Determine how the emotions contribute to enhancing the ad's narrative and provide a score between 1 and 10.\n"
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the emotions depicted can be improved, suggest actionable ways to better utilize human emotions for engagement, alignment, and narrative enhancement."
    "\n\n"
    "Return your analysis in a structured JSON format with fields for 'humanEmotionAnalysis'."
)

video_human_emotion_analysis_prompt = (
    "You are an advanced video analytics system tasked with analyzing the emotions depicted by human faces in video advertisements."
    "\n\n"
    "Analyze the video content and provide the following insights:\n"
    "1. **Emotion Detection**:\n"
    "   - Identify the emotions displayed by human faces in the video ad (e.g., happiness, sadness, excitement, anger, etc.).\n"
    "   - Specify the time segments (in HH:MM:SS format) where each emotion is prominently displayed.\n"
    "\n\n"
    "2. **Engagement, Alignment, and Narrative Enhancement**:\n"
    "   - Assess how these emotions make the ad engaging for viewers and provide a score between 1 and 10.\n"
    "   - Evaluate how well these emotions align with the brand's values and give a score between 1 and 10.\n"
    "   - Determine how the emotions contribute to enhancing the ad's narrative and provide a score between 1 and 10.\n"
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the emotions depicted can be improved, suggest actionable ways to better utilize human emotions for engagement, alignment, and narrative enhancement."
    "\n\n"
    "Provide your analysis in JSON format with the following structure:\n"
    "- 'humanEmotionAnalysis': A list of detected emotions, their time segments, engagement scores, alignment scores, narrative enhancement scores, descriptions, and improvement suggestions."
)

# Gestures and body language

video_human_gesture_analysis_response_schema = {
    "type": "object",
    "properties": {
        "humanGestureAnalysis": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "gesture": {"type": "string"},  # Detected gesture or body language (e.g., pointing, open hands, etc.)
                    "timeSegments": {
                        "type": "array",
                        "items": {"type": "string"}  # Time segments in HH:MM:SS format
                    },
                    "engagementScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for viewer engagement
                    },
                    "alignmentScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for alignment with brand values
                    },
                    "narrativeEnhancementScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for narrative enhancement
                    },
                    "description": {
                        "type": "string"  # Description of how the gesture impacts engagement, alignment, and narrative
                    },
                    "improvementSuggestions": {
                        "type": "string"  # Suggestions for better utilization of gestures and body language
                    }
                },
                "required": [
                    "gesture",
                    "timeSegments",
                    "engagementScore",
                    "alignmentScore",
                    "narrativeEnhancementScore",
                    "description"
                ]
            }
        }
    },
    "required": ["humanGestureAnalysis"]
}


video_human_gesture_analysis_prompt_system = (
    "You are an advanced video analytics system specialized in analyzing the gestures and body language of humans in video advertisements. "
    "Your task is to assess how these gestures and body language contribute to viewer engagement, align with the brand's values, and enhance the overall narrative of the advertisement."
    "\n\n"
    "Specifically, you will:\n"
    "1. **Gesture and Body Language Detection**:\n"
    "   - Identify prominent gestures and body language exhibited by humans in the ad (e.g., confident posture, open hand gestures, pointing, facial expressions paired with gestures, etc.).\n"
    "   - Specify the time segments (in HH:MM:SS format) where these gestures and body language are observed.\n"
    "\n\n"
    "2. **Engagement, Alignment, and Narrative Enhancement**:\n"
    "   - Assess how these gestures and body language make the ad engaging for viewers and provide a score between 1 and 10.\n"
    "   - Evaluate how well these gestures and body language align with the brand's values and give a score between 1 and 10.\n"
    "   - Determine how these gestures and body language contribute to enhancing the ad's narrative and provide a score between 1 and 10.\n"
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the gestures and body language can be improved, suggest actionable ways to better utilize human gestures and body language for engagement, alignment, and narrative enhancement."
    "\n\n"
    "Return your analysis in a structured JSON format with fields for 'humanGestureAnalysis'."
)

video_human_gesture_analysis_prompt = (
    "You are an advanced video analytics system tasked with analyzing the gestures and body language of humans in video advertisements."
    "\n\n"
    "Analyze the video content and provide the following insights:\n"
    "1. **Gesture and Body Language Detection**:\n"
    "   - Identify prominent gestures and body language exhibited by humans in the ad (e.g., confident posture, open hand gestures, pointing, facial expressions paired with gestures, etc.).\n"
    "   - Specify the time segments (in HH:MM:SS format) where these gestures and body language are observed.\n"
    "\n\n"
    "2. **Engagement, Alignment, and Narrative Enhancement**:\n"
    "   - Assess how these gestures and body language make the ad engaging for viewers and provide a score between 1 and 10.\n"
    "   - Evaluate how well these gestures and body language align with the brand's values and give a score between 1 and 10.\n"
    "   - Determine how these gestures and body language contribute to enhancing the ad's narrative and provide a score between 1 and 10.\n"
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the gestures and body language can be improved, suggest actionable ways to better utilize human gestures and body language for engagement, alignment, and narrative enhancement."
    "\n\n"
    "Provide your analysis in JSON format with the following structure:\n"
    "- 'humanGestureAnalysis': A list of detected gestures, their time segments, engagement scores, alignment scores, narrative enhancement scores, descriptions, and improvement suggestions."
)

# Interactions of humans and objects


video_human_object_interaction_prompt_system = (
    "You are an advanced video analytics system specialized in analyzing human interactions with objects in video advertisements. "
    "Your task is to assess how these interactions contribute to viewer engagement, align with the brand's values, and enhance the overall narrative of the advertisement."
    "\n\n"
    "Specifically, you will:\n"
    "1. **Interaction Detection**:\n"
    "   - Identify key interactions between humans and objects in the video ad (e.g., holding a product, using a tool, interacting with brand elements like logos or packaging).\n"
    "   - Specify the time segments (in HH:MM:SS format) where these interactions occur.\n"
    "\n\n"
    "2. **Engagement, Alignment, and Narrative Enhancement**:\n"
    "   - Assess how these human-object interactions make the ad engaging for viewers and provide a score between 1 and 10.\n"
    "   - Evaluate how well these interactions align with the brand's values and give a score between 1 and 10.\n"
    "   - Determine how these interactions contribute to enhancing the ad's narrative and provide a score between 1 and 10.\n"
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the human-object interactions can be improved, suggest actionable ways to make them more impactful in terms of engagement, alignment, and narrative enhancement."
    "\n\n"
    "Return your analysis in a structured JSON format with fields for 'humanObjectInteractions'."
)

video_human_object_interaction_response_schema = {
    "type": "object",
    "properties": {
        "humanObjectInteractions": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "interaction": {
                        "type": "string"  # Description of the interaction between human and object
                    },
                    "timeSegments": {
                        "type": "array",
                        "items": {"type": "string"}  # Time segments in HH:MM:SS format
                    },
                    "engagementScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for viewer engagement
                    },
                    "alignmentScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for alignment with brand values
                    },
                    "narrativeEnhancementScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for narrative enhancement
                    },
                    "description": {
                        "type": "string"  # How the interaction impacts engagement, alignment, and narrative
                    },
                    "improvementSuggestions": {
                        "type": "string"  # Suggestions for better utilization of human-object interactions
                    }
                },
                "required": [
                    "interaction",
                    "timeSegments",
                    "engagementScore",
                    "alignmentScore",
                    "narrativeEnhancementScore",
                    "description"
                ]
            }
        }
    },
    "required": ["humanObjectInteractions"]
}

video_human_object_interaction_prompt = (
    "You are an advanced video analytics system tasked with analyzing human interactions with objects in video advertisements."
    "\n\n"
    "Analyze the video content and provide the following insights:\n"
    "1. **Interaction Detection**:\n"
    "   - Identify key interactions between humans and objects in the video ad (e.g., holding a product, using a tool, interacting with brand elements like logos or packaging).\n"
    "   - Specify the time segments (in HH:MM:SS format) where these interactions occur.\n"
    "\n\n"
    "2. **Engagement, Alignment, and Narrative Enhancement**:\n"
    "   - Assess how these human-object interactions make the ad engaging for viewers and provide a score between 1 and 10.\n"
    "   - Evaluate how well these interactions align with the brand's values and give a score between 1 and 10.\n"
    "   - Determine how these interactions contribute to enhancing the ad's narrative and provide a score between 1 and 10.\n"
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the human-object interactions can be improved, suggest actionable ways to make them more impactful in terms of engagement, alignment, and narrative enhancement."
    "\n\n"
    "Provide your analysis in JSON format with the following structure:\n"
    "- 'humanObjectInteractions': A list of detected interactions, their time segments, engagement scores, alignment scores, narrative enhancement scores, descriptions, and improvement suggestions."
)

# Demographics profile

video_demographics_analysis_response_schema = {
    "type": "object",
    "properties": {
        "demographicsAnalysis": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "demographic": {
                        "type": "object",
                        "properties": {
                            "gender": {"type": "string"},  # e.g., Male, Female, Non-Binary
                            "ageRange": {"type": "string"}  # e.g., Child, Young Adult, Adult, Senior
                        },
                        "required": ["gender", "ageRange"]
                    },
                    "timeSegments": {
                        "type": "array",
                        "items": {"type": "string"}  # Time segments in HH:MM:SS format
                    },
                    "engagementScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for viewer engagement
                    },
                    "alignmentScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for alignment with brand values
                    },
                    "narrativeEnhancementScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for narrative enhancement
                    },
                    "description": {
                        "type": "string"  # How the demographics impact engagement, alignment, and narrative
                    },
                    "improvementSuggestions": {
                        "type": "string"  # Suggestions for better utilization of demographics
                    }
                },
                "required": [
                    "demographic",
                    "timeSegments",
                    "engagementScore",
                    "alignmentScore",
                    "narrativeEnhancementScore",
                    "description"
                ]
            }
        }
    },
    "required": ["demographicsAnalysis"]
}


video_demographics_analysis_prompt_system = (
    "You are an advanced video analytics system specializing in analyzing the demographics of people (such as gender and age) depicted in video advertisements. "
    "Your task is to assess how these demographics align with the brand's values, enhance the narrative of the advertisement, and engage the viewers."
    "\n\n"
    "Specifically, you will:\n"
    "1. **Demographic Detection**:\n"
    "   - Identify the gender and approximate age range (e.g., child, young adult, adult, senior) of individuals depicted in the video.\n"
    "   - Specify the time segments (in HH:MM:SS format) where these individuals appear.\n"
    "\n\n"
    "2. **Engagement, Alignment, and Narrative Enhancement**:\n"
    "   - Assess how these demographics contribute to engaging viewers and provide a score between 1 and 10.\n"
    "   - Evaluate how well these demographics align with the brand's values and give a score between 1 and 10.\n"
    "   - Determine how these demographics enhance the ad's narrative and provide a score between 1 and 10.\n"
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the demographics used in the ad can be improved, suggest actionable ways to better align them with the brand's values, enhance the narrative, and engage the audience."
    "\n\n"
    "Return your analysis in a structured JSON format with fields for 'demographicsAnalysis'."
)

video_demographics_analysis_prompt = (
    "You are an advanced video analytics system tasked with analyzing the demographics of people (such as gender and age) depicted in video advertisements."
    "\n\n"
    "Analyze the video content and provide the following insights:\n"
    "1. **Demographic Detection**:\n"
    "   - Identify the gender and approximate age range (e.g., child, young adult, adult, senior) of individuals depicted in the video.\n"
    "   - Specify the time segments (in HH:MM:SS format) where these individuals appear.\n"
    "\n\n"
    "2. **Engagement, Alignment, and Narrative Enhancement**:\n"
    "   - Assess how these demographics contribute to engaging viewers and provide a score between 1 and 10.\n"
    "   - Evaluate how well these demographics align with the brand's values and give a score between 1 and 10.\n"
    "   - Determine how these demographics enhance the ad's narrative and provide a score between 1 and 10.\n"
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the demographics used in the ad can be improved, suggest actionable ways to better align them with the brand's values, enhance the narrative, and engage the audience."
    "\n\n"
    "Provide your analysis in JSON format with the following structure:\n"
    "- 'demographicsAnalysis': A list of detected demographics, their time segments, engagement scores, alignment scores, narrative enhancement scores, descriptions, and improvement suggestions."
)

# People to people interaction

video_people_interaction_analysis_response_schema = {
    "type": "object",
    "properties": {
        "peopleInteractionAnalysis": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "interactionType": {
                        "type": "string"  # e.g., Collaboration, Conflict, Celebration, Conversation
                    },
                    "timeSegments": {
                        "type": "array",
                        "items": {"type": "string"}  # Time segments in HH:MM:SS format
                    },
                    "engagementScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for viewer engagement
                    },
                    "alignmentScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for alignment with brand values
                    },
                    "narrativeEnhancementScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for narrative enhancement
                    },
                    "description": {
                        "type": "string"  # Explanation of how interactions impact engagement, alignment, and narrative
                    },
                    "improvementSuggestions": {
                        "type": "string"  # Suggestions for better utilization of interactions
                    }
                },
                "required": [
                    "interactionType",
                    "timeSegments",
                    "engagementScore",
                    "alignmentScore",
                    "narrativeEnhancementScore",
                    "description"
                ]
            }
        }
    },
    "required": ["peopleInteractionAnalysis"]
}

video_people_interaction_analysis_prompt_system = (
    "You are an advanced video analytics system specializing in analyzing interactions between people depicted in video advertisements. "
    "Your task is to assess how these people-to-people interactions align with the brand's values, enhance the narrative of the advertisement, and engage viewers."
    "\n\n"
    "Specifically, you will:\n"
    "1. **Interaction Detection**:\n"
    "   - Identify the nature of interactions between people in the video (e.g., collaboration, conflict, celebration, etc.).\n"
    "   - Specify the time segments (in HH:MM:SS format) where these interactions occur.\n"
    "\n\n"
    "2. **Engagement, Alignment, and Narrative Enhancement**:\n"
    "   - Assess how these interactions contribute to engaging viewers and provide a score between 1 and 10.\n"
    "   - Evaluate how well these interactions align with the brand's values and give a score between 1 and 10.\n"
    "   - Determine how these interactions enhance the ad's narrative and provide a score between 1 and 10.\n"
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the interactions can be improved, suggest actionable ways to better align them with the brand's values, enhance the narrative, and engage the audience."
    "\n\n"
    "Return your analysis in a structured JSON format with fields for 'peopleInteractionAnalysis'."
)

video_people_interaction_analysis_prompt = (
    "You are an advanced video analytics system tasked with analyzing interactions between people depicted in video advertisements."
    "\n\n"
    "Analyze the video content and provide the following insights:\n"
    "1. **Interaction Detection**:\n"
    "   - Identify the nature of interactions between people in the video (e.g., collaboration, conflict, celebration, conversation, etc.).\n"
    "   - Specify the time segments (in HH:MM:SS format) where these interactions occur.\n"
    "\n\n"
    "2. **Engagement, Alignment, and Narrative Enhancement**:\n"
    "   - Assess how these interactions contribute to engaging viewers and provide a score between 1 and 10.\n"
    "   - Evaluate how well these interactions align with the brand's values and give a score between 1 and 10.\n"
    "   - Determine how these interactions enhance the ad's narrative and provide a score between 1 and 10.\n"
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the interactions can be improved, suggest actionable ways to better align them with the brand's values, enhance the narrative, and engage the audience."
    "\n\n"
    "Provide your analysis in JSON format with the following structure:\n"
    "- 'peopleInteractionAnalysis': A list of detected interactions, their time segments, engagement scores, alignment scores, narrative enhancement scores, descriptions, and improvement suggestions."
)

# Prompt configuration for celebrity identification

video_celebrity_identification_response_schema = {
    "type": "object",
    "properties": {
        "celebrityIdentification": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "celebrityName": {
                        "type": "string",
                        "description": "Name of the identified celebrity."
                    },
                    "timeSegments": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Time segments in HH:MM:SS format where the celebrity appears."
                    },
                    "description": {
                        "type": "string",
                        "description": "A brief description of the celebrity's role or presence in the ad."
                    }
                },
                "required": ["celebrityName", "timeSegments", "description"]
            }
        }
    },
    "required": ["celebrityIdentification"]
}
video_celebrity_identification_prompt_system = (
    "You are an advanced video analytics system specialized in identifying celebrities in video advertisements. Your task is to:\n\n"
    "1. **Celebrity Identification**:\n"
    "   - Identify all the celebrities appearing in the video ad.\n"
    "   - For each celebrity, specify the time segments (in HH:MM:SS format) where they appear.\n"
    "   - Provide a brief description of their role or presence in the ad.\n\n"
    "Return your analysis in a structured JSON format with the field 'celebrityIdentification'."
)

video_celebrity_identification_prompt = (
    "You are an advanced video analytics system tasked with identifying celebrities in video advertisements.\n\n"
    "Please analyze the video and provide the following insights:\n"
    "- Identify all celebrities appearing in the video.\n"
    "- Specify the time segments (in HH:MM:SS format) where each celebrity is found.\n"
    "- Provide a brief description of their role or presence in the ad.\n\n"
    "Provide your analysis in JSON format with the following structure:\n"
    "- 'celebrityIdentification': A list of identified celebrities, their time segments, and descriptions."
)

# Prompt configuration for number of people/Actors/Celebrity name identification
# New people / celebrity identification
video_Peoplecelebrity_identification_response_schema = {
    "type": "object",
    "properties": {
        "personIdentification": {
            "type": "object",
            "properties": {
                "totalPeople": {
                    "type": "integer",
                    "description": "Total number of unique people appearing in the video ad."
                },
                "celebrities": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "celebrityName": {
                                "type": "string",
                                "description": "Name of the identified celebrity."
                            },
                            "roleDescription": {
                                "type": "string",
                                "description": "A brief description of the celebrity's role or presence in the ad."
                            }
                        },
                        "required": ["celebrityName", "roleDescription"]
                    },
                    "description": "A list of all identified celebrities, their names, and their roles in the ad."
                },
                "actors": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "description": "Names or descriptions of actors (non-celebrities) appearing in the video."
                    },
                    "description": "A list of actors or non-celebrity individuals in the ad."
                }
            },
            "required": ["totalPeople", "celebrities", "actors"]
        }
    },
    "required": ["personIdentification"]
}

video_Peoplecelebrity_identification_prompt_system = (
    "You are an advanced video analytics system specialized in identifying people in video advertisements. "
    "Your task is to:\n\n"
    "1. **Person Count and Identification**:\n"
    "   - Count the total number of unique people appearing in the video ad.\n"
    "   - Identify whether each person is a celebrity or an actor.\n"
    "   - For celebrities, provide their name and a brief description of their role or presence in the ad.\n"
    "   - For actors (non-celebrities), provide their names or a brief description.\n\n"
    "Return your analysis in a structured JSON format with the field 'personIdentification', "
    "including 'totalPeople', 'celebrities', and 'actors'."
)
video_Peoplecelebrity_identification_prompt = (
    "You are an advanced video analytics system tasked with identifying people in video advertisements.\n\n"
    "Please analyze the video and provide the following insights:\n"
    "- Count the total number of unique people appearing in the ad.\n"
    "- Identify whether each person is a celebrity or an actor.\n"
    "- For celebrities, provide their name and a brief description of their role or presence in the ad.\n"
    "- For actors (non-celebrities), provide their names or a brief description.\n\n"
    "Provide your analysis in JSON format with the following structure:\n"
    "- 'personIdentification':\n"
    "  - 'totalPeople': Total number of unique people in the ad.\n"
    "  - 'celebrities': A list of identified celebrities, their names, and role descriptions.\n"
    "  - 'actors': A list of actors (non-celebrities) with names or descriptions."
)
