'''
This script give the templates for video making related aspects

'''

video_scene_analysis_response_schema = {
    "type": "object",
    "properties": {
        "sceneAnalysis": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "sceneAspect": {
                        "type": "string",
                        "description": "The specific scene aspect analyzed (e.g., Hand Cuts, Soft Transitions, Camera Changes, Pan Swipes, Zooms, Depth of Field Changes, Tracking Shots, Movement of Camera)."
                    },
                    "score": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10,
                        "description": "The score on a scale of 1-10 evaluating the quality or effectiveness of this scene aspect."
                    },
                    "description": {
                        "type": "string",
                        "description": "Detailed explanation of the impact of this scene aspect on the video ad's overall storytelling and engagement."
                    }
                },
                "required": ["sceneAspect", "score", "description"]
            }
        },
        "overallAssessment": {
            "type": "object",
            "properties": {
                "storytellingScore": {
                    "type": "number",
                    "minimum": 1,
                    "maximum": 10,
                    "description": "Score evaluating how effectively the scene aspects aid in storytelling."
                },
                "engagementScore": {
                    "type": "number",
                    "minimum": 1,
                    "maximum": 10,
                    "description": "Score evaluating how well the scene aspects enhance viewer engagement."
                },
                "summaryDescription": {
                    "type": "string",
                    "description": "A summary of how these scene aspects collectively contribute to storytelling and engagement."
                }
            },
            "required": ["storytellingScore", "engagementScore", "summaryDescription"]
        }
    },
    "required": ["sceneAnalysis", "overallAssessment"]
}
video_scene_analysis_prompt_system = (
    "You are an advanced video analytics system specialized in evaluating scene design in video advertisements. "
    "Your task is to:\n\n"
    "1. **Scene Aspect Evaluation**:\n"
    "   - Analyze the following scene aspects: Hand Cuts, Soft Transitions, Camera Changes, Pan Swipes, Zooms, Depth of Field Changes, Tracking Shots, and Movement of Camera.\n"
    "   - Assign a score (1-10) to each scene aspect based on its quality and effectiveness.\n"
    "   - Provide a detailed explanation of the impact of each scene aspect on the video ad's appeal, storytelling, and engagement.\n\n"
    "2. **Overall Assessment**:\n"
    "   - Evaluate how these scene aspects collectively enhance storytelling and viewer engagement.\n"
    "   - Assign a score (1-10) for storytelling effectiveness and another score (1-10) for viewer engagement.\n"
    "   - Provide a summary description explaining how these aspects enhance the ad's effectiveness in terms of storytelling and engagement.\n\n"
    "Return your analysis in a structured JSON format with fields for 'sceneAnalysis' and 'overallAssessment'."
)
video_scene_analysis_prompt = (
    "You are an advanced video analytics system tasked with analyzing the scene design and its impact in video advertisements.\n\n"
    "Analyze the video ad and provide the following insights:\n"
    "1. **Scene Aspect Evaluation**:\n"
    "   - Evaluate the following scene aspects: Hand Cuts, Soft Transitions, Camera Changes, Pan Swipes, Zooms, Depth of Field Changes, Tracking Shots, and Movement of Camera.\n"
    "   - Assign a score between 1 and 10 for each scene aspect based on its quality and effectiveness.\n"
    "   - Provide a detailed explanation of the impact of each aspect on the ad's storytelling and engagement.\n\n"
    "2. **Overall Assessment**:\n"
    "   - Assess how these scene aspects collectively enhance storytelling and viewer engagement.\n"
    "   - Provide a score between 1 and 10 for storytelling effectiveness.\n"
    "   - Provide a score between 1 and 10 for viewer engagement.\n"
    "   - Summarize how these elements enhance the ad's overall effectiveness in terms of storytelling and engagement.\n\n"
    "Return your analysis in JSON format with the following structure:\n"
    "- 'sceneAnalysis': A list of scene aspects with their scores and detailed impact descriptions.\n"
    "- 'overallAssessment': Scores for storytelling and engagement, along with a summary description."
)
