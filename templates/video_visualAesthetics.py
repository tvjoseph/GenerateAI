'''
Template for visual and Aesthetics appeal
'''

color_visual_analysis_prompt_system = (
    "You are an advanced video analytics system specializing in analyzing the use of color and visuals in video advertisements. "
    "Your task is to evaluate the emotional and aesthetic impact of colors and visuals used in the ad."
    "\n\n"
    "Specifically, you will analyze the following:\n"
    "1. **Color Analysis**:\n"
    "   - Identify the primary colors used in the ad.\n"
    "   - For each color, determine the emotional appeal it conveys (e.g., excitement, calmness, trust, warmth, etc.).\n"
    "   - Assign an objective score between 1 and 10 for the emotional appeal of each color.\n"
    "   - Assign an objective score between 1 and 10 for the aesthetic and visual appeal of each color.\n"
    "   - Provide a brief explanation for the emotional and aesthetic impact of each color.\n"
    "\n"
    "2. **Visual Appeal**:\n"
    "   - Assess the overall use of visuals, such as imagery, animations, and graphics.\n"
    "   - Assign an objective score between 1 and 10 for the overall visual appeal of the ad.\n"
    "   - Provide a brief description of how visuals contribute to the emotional and aesthetic experience.\n"
    "\n\n"
    "Return your analysis in a structured JSON format with fields for 'colors' and 'visuals'."
)

color_visual_analysis_response_schema = {
    "type": "object",
    "properties": {
        "colors": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "color": {"type": "string"},  # The identified color (e.g., red, blue, etc.)
                    "emotionalAppeal": {"type": "string"},  # Emotional appeal of the color (e.g., excitement, trust)
                    "emotionScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Objective score for emotional appeal
                    },
                    "aestheticScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Objective score for aesthetic appeal
                    },
                    "description": {"type": "string"}  # Explanation of the emotional and aesthetic impact
                },
                "required": ["color", "emotionalAppeal", "emotionScore", "aestheticScore", "description"]
            }
        },
        "visuals": {
            "type": "object",
            "properties": {
                "overallScore": {
                    "type": "number",
                    "minimum": 1,
                    "maximum": 10  # Objective score for overall visual appeal
                },
                "description": {"type": "string"}  # Brief description of visual impact
            },
            "required": ["overallScore", "description"]
        }
    },
    "required": ["colors", "visuals"]
}

color_visual_analysis_prompt = (
    "You are an advanced video analytics system tasked with analyzing the use of color and visuals in video advertisements."
    "\n\n"
    "Analyze the video content and provide the following insights:\n"
    "1. **Color Analysis**:\n"
    "   - Identify the primary colors used in the ad.\n"
    "   - For each color, describe its emotional appeal (e.g., excitement, calmness, trust, warmth, etc.).\n"
    "   - Assign an objective score between 1 and 10 for the emotional appeal of each color.\n"
    "   - Assign an objective score between 1 and 10 for the aesthetic and visual appeal of each color.\n"
    "   - Provide a short explanation of the emotional and aesthetic impact of each color.\n"
    "\n"
    "2. **Visual Appeal**:\n"
    "   - Assess the overall use of visuals, such as imagery, animations, and graphics.\n"
    "   - Assign an objective score between 1 and 10 for the overall visual appeal.\n"
    "   - Provide a brief description of how visuals contribute to the emotional and aesthetic experience.\n"
    "\n\n"
    "Provide your analysis in JSON format with the following structure:\n"
    "- 'colors': A list of objects, each with fields for 'color', 'emotionalAppeal', 'emotionScore', 'aestheticScore', and 'description'.\n"
    "- 'visuals': An object with fields for 'overallScore' and 'description'."
)