'''
30-Oct-2024
This is the script to generate emotional descriptions from video
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




################################# Prompt Configurations ##################

# Define the prompt configurations for the video
emo_video_prompt_system = (
    "You are an experienced vision agent that analyzes advertisements and identifies the emotions they are likely to invoke in a viewer across different video segments."
    "For each 2-second segment of the video, identify **all** the emotions the segment might invoke."
    "Return each emotion as a separate entry for each segment."
    "For each segment, specify:"
    " - the timestamp of the segment (e.g., 0-2s, 2-4s, 4-6s, etc.)."
    " - the emotion (e.g., happiness, sadness, excitement, anger, surprise, calmness, etc.)"
    " - the intensity of the emotion (a value between 0 and 1 indicating how strongly the segment is likely to invoke that emotion)"
    " - a brief description of the segment in relation to the emotion (a sentence or two explaining why the segment might invoke that emotion)."
    "If the segment is likely to invoke multiple emotions, list them separately for each segment."
)

emo_video_response_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "timestamp": { "type": "string" },            # Timestamp of the video segment (e.g., "0-2s", "2-4s", etc.)
            "emotion": { "type": "string" },              # Likely invoked emotion in this segment
            "intensity": { "type": "number" },            # Intensity of invoked emotion (0 to 1)
            "description": { "type": "string" },          # Brief description of how this segment evokes the emotion
        },
        "required": ["timestamp", "emotion", "intensity", "description"],
    }
}

emo_video_prompt = (
    "Analyze this advertisement video in 2-second segments and identify all emotions each segment is likely to invoke in a viewer. "
    "For each segment, specify its timestamp, the type of emotion, the intensity (a value between 0 and 1), and provide a brief description explaining how the segment invokes this emotion."
)

#################################################################



########### Summarizing the elements accross the video ###############
def summarize_attribute_elements(json_input, response_schema, prompt_system, prompt, model_name="gemini-1.5-pro"):
    """
    Summarize extracted emotional elements across segments of a video, based on JSON input.

    Args:
        json_input (list): The JSON data containing emotional elements across video segments.
        response_schema (dict): The response schema to validate the structure of the output.
        prompt_system (str): The system-level instructions for the model.
        prompt (str): The prompt to generate the summary of emotions.
        model_name (str): Name of the generative model.

    Returns:
        dict: JSON response summarizing emotional elements across the video segments.
    """
    # Convert JSON input to string format for passing into the model
    json_str_input = json.dumps(json_input)

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

    '''
    # Query the model with JSON input as text and summarization prompt
    responses = model.generate_content(
        [Part(json_str_input, mime_type="application/json"), prompt],
        stream=False,
    )
    '''

    responses = model.generate_content(
        [json_str_input, prompt],
        stream=False,
    )

    # Parse and return the JSON part of the response
    jsonResponse = json.loads(responses.text)

    return jsonResponse



#### Emotional summary prompt configurations ################

emotion_summary_prompt_system = (
    "You are an advanced analysis agent specializing in summarizing emotional elements in video content. "
    "You will analyze the provided JSON data to identify unique text descriptions that appear throughout the video. "
    "For each unique description, you will identify the time range(s) in which it appears and summarize the emotional elements invoked by the content within those ranges. "
    "Additionally, provide an overall emotional score for each emotion, calculated as the average intensity of that emotion across all appearances of the text. "
    "Each entry should include:"
    " - the unique text description"
    " - the time slots in which this description appears (in 'HH:MM:SS - HH:MM:SS' format)"
    " - a summary of the emotional elements invoked within these time slots, listing emotions with their average intensity and any notable variations"
    " - an overall emotional score for each emotion (average intensity across all occurrences of the text)"
)
emotion_summary_response_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "description": { "type": "string" },          # Unique text description
            "time_slots": { "type": "string" },           # Time slots in 'HH:MM:SS - HH:MM:SS' format
            "emotional_summary": {                        # Summary of emotions invoked in the time slots
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "emotion": { "type": "string" },  # Emotion name
                        "average_intensity": { "type": "number" } # Average intensity of the emotion
                    },
                    "required": ["emotion", "average_intensity"]
                }
            },
            "overall_emotional_score": {                  # Overall emotional score for each emotion
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "emotion": { "type": "string" },
                        "score": { "type": "number" }
                    },
                    "required": ["emotion", "score"]
                }
            }
        },
        "required": ["description", "time_slots", "emotional_summary", "overall_emotional_score"]
    }
}
emotion_summary_prompt = (
    "Analyze the provided JSON data of emotional elements in a video. "
    "For each unique text description, perform the following steps:"
    "1. Extract the unique text description and identify the time slots in which it appears, using the format 'HH:MM:SS - HH:MM:SS' for each range."
    "2. Summarize the emotional elements invoked within these time slots by listing the unique emotions and calculating their average intensity."
    "3. Provide an overall emotional score for each emotion by averaging the intensities across all appearances of this description."
    "Return the summary in a structured JSON format with keys: 'description', 'time_slots', 'emotional_summary' (with emotions and average intensities), and 'overall_emotional_score'."
)




# Convert the summary to a df
def extract_overall_emotional_score(json_data):
    records = []
    for entry in json_data:
        description = entry['description']
        time_slots = entry['time_slots']

        # Split time slots into start and end times
        start_time, end_time = time_slots.split(' - ')
        start_seconds = start_time.split(':')[-1]
        end_seconds = end_time.split(':')[-1]

        # Extract overall_emotional_score
        for score in entry['overall_emotional_score']:
            record = {
                'Description': description,
                'StartSeconds': start_seconds,
                'EndSeconds': end_seconds,
                'OverallEmotion': score['emotion'],
                'Score': score['score']
            }
            records.append(record)

    return pd.DataFrame(records)


# Actual process for the extraction

# Define the path of the image ( This needs to be changed ). We need to provide the paths of all assets
assetPath = '/Users/thomasjoseph/Desktop/JMJTL/Data/Dell/175272552.mp4' ##### Needs to be changed ###

# Read the video file and convert to the binary format
# Convert the asset to binary format
with open(assetPath, "rb") as f:
    video_data = f.read()
# Convert the video to the required format
video1 = Part.from_data(mime_type="video/mp4",data=video_data)
# Get the emotional elements extracted
emotion_elements = elementExtraction_video(emo_video_response_schema,emo_video_prompt_system,emo_video_prompt,video1)
# Get the summary of the emotions.
emotion_summary = summarize_attribute_elements(emotion_elements, emotion_summary_response_schema, emotion_summary_prompt_system, emotion_summary_prompt)
# Convert the summary which is json format to a pandas dataframe
emotional_summary_df = extract_overall_emotional_score(emotion_summary)
