'''
This script provides the templates for logo analysis
'''

### Logo placement and visibility prompt systems #####

video_logo_analysis_response_schema = {
    "type": "object",
    "properties": {
        "logoAnalysis": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "placement": {"type": "string"},  # Logo placement (e.g., "top-right corner", "center screen")
                    "visibilityDuration": {
                        "type": "number",
                        "minimum": 0,  # Duration in seconds the logo is visible
                    },
                    "keyMoments": {
                        "type": "array",
                        "items": {"type": "string"}  # Time segments in HH:MM:SS format
                    },
                    "sizeAndProminence": {
                        "type": "string"  # Description of logo size and prominence
                    },
                    "brandRecallScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for logo's impact on brand recall
                    },
                    "brandAffinityScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for logo's contribution to brand affinity
                    },
                    "viewerEngagementScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for viewer engagement influenced by logo
                    },
                    "description": {
                        "type": "string"  # Explanation of how the logo impacts metrics
                    },
                    "improvementSuggestions": {
                        "type": "string"  # Suggestions for optimizing logo placement and visibility
                    }
                },
                "required": [
                    "placement",
                    "visibilityDuration",
                    "keyMoments",
                    "sizeAndProminence",
                    "brandRecallScore",
                    "brandAffinityScore",
                    "viewerEngagementScore",
                    "description"
                ]
            }
        }
    },
    "required": ["logoAnalysis"]
}

video_logo_analysis_prompt_system = (
    "You are an advanced video analytics system specialized in evaluating logo placement and visibility in video advertisements. "
    "Your task is to assess how the placement and visibility of the logo influence brand recall, strengthen brand affinity, and enhance viewer engagement."
    "\n\n"
    "Specifically, you will:\n"
    "1. **Logo Placement and Visibility**:\n"
    "   - Identify where the logo is placed within the video (e.g., 'top-right corner', 'center screen').\n"
    "   - Calculate the total time (in seconds) the logo is visible.\n"
    "   - Highlight key moments (in HH:MM:SS format) where the logo is prominently displayed.\n"
    "   - Evaluate the size and prominence of the logo relative to other visual elements in the video.\n"
    "\n\n"
    "2. **Impact on Brand Metrics**:\n"
    "   - Assess the logo's impact on **brand recall** and provide a score between 1 and 10.\n"
    "   - Evaluate how effectively the logo strengthens **brand affinity** and provide a score between 1 and 10.\n"
    "   - Analyze how the logo contributes to **viewer engagement** and provide a score between 1 and 10.\n"
    "\n\n"
    "3. **Suggestions for Improvement**:\n"
    "   - If the logo placement or visibility can be improved, suggest actionable ways to enhance brand recall, strengthen brand affinity, and increase viewer engagement."
    "\n\n"
    "Return your analysis in a structured JSON format with fields for 'logoAnalysis'."
)

video_logo_analysis_prompt = (
    "You are an advanced video analytics system tasked with analyzing logo placement and visibility in video advertisements."
    "\n\n"
    "Analyze the video content and provide the following insights:\n"
    "1. **Logo Placement and Visibility**:\n"
    "   - Describe where the logo appears in the video (e.g., 'top-right corner', 'center screen').\n"
    "   - Calculate the total visibility duration of the logo (in seconds).\n"
    "   - Highlight the key moments (in HH:MM:SS format) when the logo is prominently displayed.\n"
    "   - Assess the size and prominence of the logo compared to other elements in the video.\n"
    "\n\n"
    "2. **Impact on Brand Metrics**:\n"
    "   - Provide a score (1–10) for how well the logo placement and visibility enhance **brand recall**.\n"
    "   - Provide a score (1–10) for how effectively the logo strengthens **brand affinity**.\n"
    "   - Provide a score (1–10) for how the logo contributes to **viewer engagement**.\n"
    "\n\n"
    "3. **Suggestions for Improvement**:\n"
    "   - Recommend actionable ways to optimize the logo's placement, visibility, and impact on branding metrics."
    "\n\n"
    "Provide your response in JSON format with the following structure:\n"
    "- 'logoAnalysis': A list of objects containing the logo's placement, visibility duration, key moments, size/prominence assessments, brand impact scores, and suggestions."
)

##### Duration of logo visibility ######
video_logo_visibility_analysis_response_schema = {
    "type": "object",
    "properties": {
        "logoVisibilityAnalysis": {
            "type": "object",
            "properties": {
                "totalVisibilityDuration": {
                    "type": "number",
                    "minimum": 0,  # Total visibility duration in seconds
                    "description": "Total duration in seconds the logo is visible in the video."
                },
                "brandRecallScore": {
                    "type": "number",
                    "minimum": 1,
                    "maximum": 10,  # Score for logo's impact on brand recall
                    "description": "Score assessing how the total visibility duration influences brand recall."
                },
                "brandAffinityScore": {
                    "type": "number",
                    "minimum": 1,
                    "maximum": 10,  # Score for logo's impact on brand affinity
                    "description": "Score evaluating how the total visibility duration strengthens brand affinity."
                },
                "viewerEngagementScore": {
                    "type": "number",
                    "minimum": 1,
                    "maximum": 10,  # Score for logo's impact on viewer engagement
                    "description": "Score assessing how the total visibility duration enhances viewer engagement."
                },
                "description": {
                    "type": "string",  # Explanation of the relationship between duration and branding metrics
                    "description": "Explanation of how the total visibility duration influences brand recall, brand affinity, and viewer engagement."
                },
                "improvementSuggestions": {
                    "type": "string",  # Suggestions for optimizing logo visibility duration
                    "description": "Suggestions for optimizing the duration of logo visibility to improve branding metrics."
                }
            },
            "required": [
                "totalVisibilityDuration",
                "brandRecallScore",
                "brandAffinityScore",
                "viewerEngagementScore",
                "description"
            ]
        }
    },
    "required": ["logoVisibilityAnalysis"]
}

video_logo_visibility_analysis_prompt_system = (
    "You are an advanced video analytics system specialized in evaluating the total visibility duration of logos in video advertisements. "
    "Your task is to assess how the total duration of logo visibility influences brand recall, strengthens brand affinity, and enhances viewer engagement."
    "\n\n"
    "Specifically, you will:\n"
    "1. **Calculate Total Visibility Duration**:\n"
    "   - Measure the total duration (in seconds) for which the logo is visible in the video.\n"
    "\n\n"
    "2. **Impact on Brand Metrics**:\n"
    "   - Provide a score (1–10) for how the total visibility duration enhances **brand recall**.\n"
    "   - Provide a score (1–10) for how effectively the total visibility duration strengthens **brand affinity**.\n"
    "   - Provide a score (1–10) for how the total visibility duration contributes to **viewer engagement**.\n"
    "\n\n"
    "3. **Suggestions for Improvement**:\n"
    "   - If the total visibility duration can be optimized, provide actionable suggestions to improve its impact on branding metrics."
    "\n\n"
    "Return your analysis in a structured JSON format with fields for 'logoVisibilityAnalysis'."
)

video_logo_visibility_analysis_prompt = (
    "You are an advanced video analytics system tasked with analyzing the total duration of logo visibility in video advertisements."
    "\n\n"
    "Analyze the video content and provide the following insights:\n"
    "1. **Total Visibility Duration**:\n"
    "   - Measure and report the total duration (in seconds) for which the logo is visible in the video.\n"
    "\n\n"
    "2. **Impact on Brand Metrics**:\n"
    "   - Provide a score (1–10) for how the total visibility duration enhances **brand recall**.\n"
    "   - Provide a score (1–10) for how effectively the total visibility duration strengthens **brand affinity**.\n"
    "   - Provide a score (1–10) for how the total visibility duration contributes to **viewer engagement**.\n"
    "\n\n"
    "3. **Suggestions for Improvement**:\n"
    "   - Provide actionable suggestions for optimizing the duration of logo visibility to improve branding metrics."
    "\n\n"
    "Provide your response in JSON format with the following structure:\n"
    "- 'logoVisibilityAnalysis': An object containing the total visibility duration, branding metric scores, explanations, and improvement suggestions."
)

### Logo size and prominance ########

video_logo_size_prominence_analysis_response_schema = {
    "type": "object",
    "properties": {
        "logoSizeProminenceAnalysis": {
            "type": "object",
            "properties": {
                "averageLogoSize": {
                    "type": "number",
                    "description": "Average size of the logo as a percentage of the video frame area."
                },
                "prominenceScore": {
                    "type": "number",
                    "minimum": 1,
                    "maximum": 10,
                    "description": "Score assessing how visually prominent the logo is throughout the video."
                },
                "brandRecallScore": {
                    "type": "number",
                    "minimum": 1,
                    "maximum": 10,
                    "description": "Score assessing how the size and prominence of the logo influence brand recall."
                },
                "brandAffinityScore": {
                    "type": "number",
                    "minimum": 1,
                    "maximum": 10,
                    "description": "Score evaluating how the size and prominence of the logo strengthen brand affinity."
                },
                "viewerEngagementScore": {
                    "type": "number",
                    "minimum": 1,
                    "maximum": 10,
                    "description": "Score assessing how the size and prominence of the logo enhance viewer engagement."
                },
                "description": {
                    "type": "string",
                    "description": "Explanation of how logo size and prominence impact brand recall, brand affinity, and viewer engagement."
                },
                "improvementSuggestions": {
                    "type": "string",
                    "description": "Suggestions for optimizing the size and prominence of the logo to improve branding metrics."
                }
            },
            "required": [
                "averageLogoSize",
                "prominenceScore",
                "brandRecallScore",
                "brandAffinityScore",
                "viewerEngagementScore",
                "description"
            ]
        }
    },
    "required": ["logoSizeProminenceAnalysis"]
}

video_logo_size_prominence_analysis_prompt_system = (
    "You are an advanced video analytics system specialized in evaluating the size and prominence of logos in video advertisements. "
    "Your task is to assess how the size and prominence of the logo influence brand recall, strengthen brand affinity, and enhance viewer engagement."
    "\n\n"
    "Specifically, you will:\n"
    "1. **Logo Size and Prominence Analysis**:\n"
    "   - Calculate the average size of the logo as a percentage of the video frame area.\n"
    "   - Assess the visual prominence of the logo and provide a prominence score (1–10).\n"
    "\n\n"
    "2. **Impact on Brand Metrics**:\n"
    "   - Provide a score (1–10) for how the logo's size and prominence enhance **brand recall**.\n"
    "   - Provide a score (1–10) for how the logo's size and prominence strengthen **brand affinity**.\n"
    "   - Provide a score (1–10) for how the logo's size and prominence contribute to **viewer engagement**.\n"
    "\n\n"
    "3. **Suggestions for Improvement**:\n"
    "   - If the logo size and prominence can be optimized, provide actionable suggestions to improve their impact on branding metrics."
    "\n\n"
    "Return your analysis in a structured JSON format with fields for 'logoSizeProminenceAnalysis'."
)

video_logo_size_prominence_analysis_prompt = (
    "You are an advanced video analytics system tasked with analyzing the size and prominence of the logo in video advertisements."
    "\n\n"
    "Analyze the video content and provide the following insights:\n"
    "1. **Logo Size and Prominence Analysis**:\n"
    "   - Calculate and report the average size of the logo as a percentage of the video frame area.\n"
    "   - Assess the visual prominence of the logo and provide a prominence score (1–10).\n"
    "\n\n"
    "2. **Impact on Brand Metrics**:\n"
    "   - Provide a score (1–10) for how the logo's size and prominence enhance **brand recall**.\n"
    "   - Provide a score (1–10) for how the logo's size and prominence strengthen **brand affinity**.\n"
    "   - Provide a score (1–10) for how the logo's size and prominence contribute to **viewer engagement**.\n"
    "\n\n"
    "3. **Suggestions for Improvement**:\n"
    "   - Provide actionable suggestions for optimizing the size and prominence of the logo to improve branding metrics."
    "\n\n"
    "Provide your response in JSON format with the following structure:\n"
    "- 'logoSizeProminenceAnalysis': An object containing the average logo size, prominence score, branding metric scores, explanations, and improvement suggestions."
)

### Logo interaction with objects and other elements

video_logo_interaction_analysis_response_schema = {
    "type": "object",
    "properties": {
        "logoInteractionAnalysis": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "interactionType": {
                        "type": "string",
                        "description": "Type of interaction (e.g., overlay, proximity, integration with objects, alignment with brand elements)."
                    },
                    "associatedElements": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of objects or brand elements interacting with the logo."
                    },
                    "timeSegments": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Time segments in HH:MM:SS format where these interactions occur."
                    },
                    "brandRecallScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10,
                        "description": "Score assessing how the interactions influence brand recall."
                    },
                    "brandAffinityScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10,
                        "description": "Score evaluating how the interactions strengthen brand affinity."
                    },
                    "viewerEngagementScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10,
                        "description": "Score assessing how the interactions enhance viewer engagement."
                    },
                    "description": {
                        "type": "string",
                        "description": "Explanation of how the interactions impact brand recall, brand affinity, and viewer engagement."
                    },
                    "improvementSuggestions": {
                        "type": "string",
                        "description": "Suggestions for optimizing interactions between the logo and other brand elements to improve branding metrics."
                    }
                },
                "required": [
                    "interactionType",
                    "associatedElements",
                    "timeSegments",
                    "brandRecallScore",
                    "brandAffinityScore",
                    "viewerEngagementScore",
                    "description"
                ]
            }
        }
    },
    "required": ["logoInteractionAnalysis"]
}

video_logo_interaction_analysis_prompt_system = (
    "You are an advanced video analytics system specialized in evaluating interactions between a brand's logo and other objects or brand elements in video advertisements. "
    "Your task is to assess how these interactions influence brand recall, strengthen brand affinity, and enhance viewer engagement."
    "\n\n"
    "Specifically, you will:\n"
    "1. **Interaction Detection**:\n"
    "   - Identify the type of interactions involving the logo (e.g., overlay, proximity, integration with objects, alignment with brand elements).\n"
    "   - List the associated objects or brand elements interacting with the logo.\n"
    "   - Specify the time segments (in HH:MM:SS format) where these interactions occur.\n"
    "\n\n"
    "2. **Impact on Brand Metrics**:\n"
    "   - Provide a score (1–10) for how the logo's interactions enhance **brand recall**.\n"
    "   - Provide a score (1–10) for how the logo's interactions strengthen **brand affinity**.\n"
    "   - Provide a score (1–10) for how the logo's interactions contribute to **viewer engagement**.\n"
    "\n\n"
    "3. **Suggestions for Improvement**:\n"
    "   - If the interactions can be optimized, provide actionable suggestions to better align them with branding goals and enhance their impact."
    "\n\n"
    "Return your analysis in a structured JSON format with fields for 'logoInteractionAnalysis'."
)

video_logo_interaction_analysis_prompt = (
    "You are an advanced video analytics system tasked with analyzing interactions between a brand's logo and other objects or brand elements in video advertisements."
    "\n\n"
    "Analyze the video content and provide the following insights:\n"
    "1. **Interaction Detection**:\n"
    "   - Identify the type of interactions involving the logo (e.g., overlay, proximity, integration with objects, alignment with brand elements).\n"
    "   - List the objects or brand elements interacting with the logo.\n"
    "   - Specify the time segments (in HH:MM:SS format) where these interactions occur.\n"
    "\n\n"
    "2. **Impact on Brand Metrics**:\n"
    "   - Provide a score (1–10) for how the logo's interactions enhance **brand recall**.\n"
    "   - Provide a score (1–10) for how the logo's interactions strengthen **brand affinity**.\n"
    "   - Provide a score (1–10) for how the logo's interactions contribute to **viewer engagement**.\n"
    "\n\n"
    "3. **Suggestions for Improvement**:\n"
    "   - Provide actionable suggestions for optimizing the interactions between the logo and other brand elements to improve branding metrics."
    "\n\n"
    "Provide your response in JSON format with the following structure:\n"
    "- 'logoInteractionAnalysis': A list of detected interactions, associated elements, time segments, branding metric scores, descriptions, and improvement suggestions."
)
