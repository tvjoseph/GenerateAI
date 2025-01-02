'''
This is the script to extract Descriptions and list of everything in a segment

1) one sentence summary of the brand visually as per Gemini and
2) a list of all the things that appear in the creative assets
'''
if True:
    import os
    import sys

    #import colorama
    import datetime as dt
    import enum
    import json
    import re
    import requests
    import logging
    import pandas as pd

    from typing import List, Tuple, Optional, Dict, Any  # Dict, List, Optional, Tuple, Any

    #from vertexai.preview.vision_models import ImageGenerationModel
    import vertexai.preview.vision_models as vision_models
    import vertexai.preview.generative_models as generative_models
    from vertexai.generative_models import GenerativeModel, Part
    import base64
    from vertexai.generative_models import SafetySetting
    from vertexai.generative_models import Image
    from PIL import Image as PIL_Image
    import random
    import pickle
    import tempfile
    import os
    pass

if True:
   # Read the key
    GCP_AUTH_FILE = "/Users/thomasjoseph/Desktop/JMJTL/Projects/Gen_ai/key1.json"
    # Set path as env var
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GCP_AUTH_FILE

    pass


def elementExtraction_video(response_schema, prompt_system, prompt, target_video, model_name="gemini-1.5-pro"):
    # Define the model
    model_name = model_name
    # Define generation config
    generation_config = generative_models.GenerationConfig(
        temperature=0.9,  # Controls randomness. Range: [0.0, 1.0]
        top_p=0.8,
        top_k=10,
        candidate_count=1,
        max_output_tokens=8192,  # max number of output tokens to generate per message.
        response_schema=response_schema,
        response_mime_type="application/json",
        seed=1,
    )
    # Define the model
    model = generative_models.GenerativeModel(
        model_name=model_name,
        generation_config=generation_config,
        system_instruction=prompt_system,
        safety_settings={},  # Adjust safety settings
    )

    # Query the model for multiple objects in the image
    # response = model.generate_content([target_picture, prompt])
    responses = model.generate_content(
        [target_video, prompt],
        stream=False,
    )


    # Load the json part of the response
    jsonResponse = json.loads(responses.text)

    return jsonResponse

### Getting the prompt configurations ###########

brand_summary_prompt_system = (
    "You are a seasoned brand consultant analyzing advertisements to understand the essence of a brand. "
    "Your task is to watch the entire video advertisement and provide a one-sentence summary that captures the overall impression of the brand as presented in the video. "
    "Consider aspects such as the brand’s personality, values, tone, and positioning. "
    "In addition to the summary, provide a score for each of the following aspects on a scale from 1 to 10, reflecting how strongly each is conveyed: "
    "- Brand Personality (how distinctive and memorable the brand's personality appears)"
    "- Brand Values (how clearly the brand’s core values come through)"
    "- Brand Tone (how consistent and appropriate the tone of communication is)"
    "- Brand Positioning (how well-defined and differentiated the brand positioning is)."
)

brand_summary_response_schema = {
    "type": "object",
    "properties": {
        "brandSummary": {
            "type": "string",
            "description": "A one-sentence summary capturing the overall impression and identity of the brand in the advertisement."
        },
        "personalityScore": {
            "type": "integer",
            "description": "Score for the brand's personality (1-10).",
            "minimum": 1,
            "maximum": 10
        },
        "valuesScore": {
            "type": "integer",
            "description": "Score for the brand's values (1-10).",
            "minimum": 1,
            "maximum": 10
        },
        "toneScore": {
            "type": "integer",
            "description": "Score for the brand's tone (1-10).",
            "minimum": 1,
            "maximum": 10
        },
        "positioningScore": {
            "type": "integer",
            "description": "Score for the brand's positioning (1-10).",
            "minimum": 1,
            "maximum": 10
        }
    },
    "required": ["brandSummary", "personalityScore", "valuesScore", "toneScore", "positioningScore"]
}

brand_summary_prompt = (
    "Watch the entire video advertisement and provide a one-sentence summary that captures the overall impression of the brand. "
    "The summary should reflect the brand’s personality, values, tone, and positioning as presented in the video. "
    "Additionally, rate each of the following aspects on a scale from 1 to 10 based on how strongly they are conveyed in the video: "
    "- Brand Personality "
    "- Brand Values "
    "- Brand Tone "
    "- Brand Positioning."
)

# Prompt configurations for visual elements

visual_elements_extraction_prompt_system = (
    "You are an advanced visual analysis expert specializing in extracting detailed elements from creative video assets. "
    "Your task is to watch the entire video advertisement and provide a comprehensive list of all visible elements present throughout the video. "
    "The elements to be identified include:"
    "\n- Logos (any brand logos that appear)"
    "\n- Text (any written text or on-screen messaging)"
    "\n- Objects (any objects or products shown)"
    "\n- People (gender, age group, ethnicity)"
    "\n- Scenery (background environments such as urban, nature, etc.)"
    "\n- Celebrities (identify if any recognizable public figures appear)"
    "\n- Call-to-Action (CTA, any explicit calls to action such as 'Buy Now', 'Learn More')"
    "\n- Color Schemes (dominant colors and overall color themes)"
    "\n"
    "For each element, provide a description along with any relevant details that help in identifying and understanding its role in the video."
    "If the element appears multiple times, mention each occurrence and its timestamp (e.g., 0-2s, 2-4s, 4-6s, etc.)."
    "The output should be a structured list, with each entry providing the type of element, a description, timestamps, and additional details where applicable."
)

visual_elements_extraction_response_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "elementType": {
                "type": "string",
                "description": "The type of element (e.g., Logo, Text, Object, Person, Scenery, Celebrity, CTA, Color Scheme)."
            },
            "description": {
                "type": "string",
                "description": "A brief description of the element and any distinguishing features."
            },
            "timestamps": {
                "type": "array",
                "items": { "type": "string" },
                "description": "List of timestamps where this element appears (e.g., ['0-2s', '4-6s'])."
            },
            "additionalDetails": {
                "type": "object",
                "properties": {
                    "gender": { "type": "string", "description": "Gender of people if applicable (e.g., Male, Female, Non-binary)." },
                    "ageGroup": { "type": "string", "description": "Age group of people if applicable (e.g., Children, Young Adults, Middle-aged, Seniors)." },
                    "ethnicity": { "type": "string", "description": "Ethnicity of people if applicable." },
                    "dominantColors": {
                        "type": "array",
                        "items": { "type": "string" },
                        "description": "List of dominant colors or overall color schemes."
                    },
                    "ctaText": { "type": "string", "description": "The exact text of the Call-to-Action, if applicable." },
                    "celebrityName": { "type": "string", "description": "Name of celebrity if recognizable." }
                }
            }
        },
        "required": ["elementType", "description", "timestamps"]
    }
}


visual_elements_extraction_prompt = (
    "Watch the video advertisement carefully and extract a list of all visible elements that appear in the video. "
    "For each element, include:"
    "\n- Element type (e.g., Logo, Text, Object, Person, Scenery, Celebrity, CTA, Color Scheme)."
    "\n- A brief description of the element."
    "\n- The timestamps at which the element appears (e.g., 0-2s, 4-6s)."
    "\n- Additional details if relevant, such as:"
    "\n  - Gender, age group, and ethnicity for people appearing in the video."
    "\n  - Dominant colors and overall color scheme."
    "\n  - Specific Call-to-Action (CTA) text if applicable."
    "\n  - Name of any celebrity if they are recognizable."
    "Your goal is to provide a comprehensive list with accurate details, helping in the detailed analysis of the brand asset."
)



######## Process the asset #########
# Define the path of the image ( This needs to be changed ). We need to provide the paths of all assets
#assetPath = '/Users/thomasjoseph/Desktop/JMJTL/Data/Dell/175272552.mp4' ##### Needs to be changed ###
assetPath = '/Users/thomasjoseph/Desktop/JMJTL/Data/IC_Data/180258547.mp4'

# Read the video file and convert to the binary format
# Convert the asset to binary format
with open(assetPath, "rb") as f:
    video_data = f.read()
# Convert the video to the required format
video1 = Part.from_data(mime_type="video/mp4",data=video_data)
# Get the emotional elements extracted
brandDescription_elements = elementExtraction_video(brand_summary_response_schema,brand_summary_prompt_system,brand_summary_prompt,video1)
print(brandDescription_elements)
# Convert JSON to DataFrame
df_brandSummary = pd.DataFrame([brandDescription_elements])
print(df_brandSummary)


# Visual elements extraction
visual_elements = elementExtraction_video(visual_elements_extraction_response_schema,visual_elements_extraction_prompt_system,visual_elements_extraction_prompt,video1)
print(visual_elements)
# Convert JSON to DataFrame
df_visual = pd.json_normalize(visual_elements)
print(df_visual)





