'''
22-Oct-2024
This is the script for extracting Invoked emotions from images
'''

if True:
    import os
    import sys

    # import colorama
    import datetime as dt
    import enum
    import json
    import re
    import requests
    import logging
    import pandas as pd

    from typing import List, Tuple, Optional, Dict, Any  # Dict, List, Optional, Tuple, Any

    # from vertexai.preview.vision_models import ImageGenerationModel
    import vertexai.preview.vision_models as vision_models
    import vertexai.preview.generative_models as generative_models
    from vertexai.generative_models import GenerationConfig, GenerativeModel, Image, Part
    import vertexai
    from PIL import Image as PIL_Image

    pass

# Read the GCP API Key
if True:
    GCP_AUTH_FILE = "/Users/thomasjoseph/Desktop/JMJTL/Projects/Gen_ai/key1.json" ##### Change this path to config file or vault

    # Set path as env var
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GCP_AUTH_FILE

    pass

# Function to extract emotions
def elementExtraction(response_schema, prompt_system, prompt, target_picture, model_name="gemini-1.5-pro"):
    # Define the model
    model_name = model_name
    # Define generation config
    generation_config = generative_models.GenerationConfig(
        temperature=0.6,  # Controls randomness. Range: [0.0, 1.0]
        top_p=0.8,
        top_k=10,
        candidate_count=1,
        max_output_tokens=1024,  # max number of output tokens to generate per message.
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
    response = model.generate_content([target_picture, prompt])

    return response.text




# Extract Emotions from image
# Updated system prompt to describe the advertisement in terms of invoked emotions
emo_ad_prompt_system = (
    "You are an experienced vision agent that analyzes advertisements and identifies the emotions they are likely to invoke in a viewer."
    "For each image (advertisement), identify **all** the emotions the advertisement might invoke."
    "Return each emotion as a separate entry."
    "For each emotion, specify:"
    " - the emotion (e.g., happiness, sadness, excitement, anger, surprise, calmness, etc.)"
    " - the intensity of the emotion (a value between 0 and 1 indicating how strongly the ad is likely to invoke that emotion)"
    " - a brief description of the advertisement in relation to the emotion (a sentence or two explaining why the ad might invoke that emotion)."
    "If the ad is likely to invoke multiple emotions, list them separately."
)


# Response schema updated to handle multiple emotions, intensity, and a small description
emo_ad_response_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "emotion": { "type": "string" },              # Likely invoked emotion
            "intensity": { "type": "number" },            # Intensity of invoked emotion (0 to 1)
            "description": { "type": "string" },          # Brief description of how the ad evokes this emotion
        },
        "required": ["emotion", "intensity", "description"],
    }
}


# Updated prompt to query the model for likely invoked emotions in the advertisement
emo_ad_prompt = (
    "Analyze this advertisement and identify all emotions it is likely to invoke in a viewer. "
    "For each emotion, specify its type, the intensity (a value between 0 and 1), and provide a brief description explaining how the ad invokes this emotion."
)

### Prompt systems for DEI
# Updated system prompt to analyze DEI elements in an advertisement
dei_ad_prompt_system = (
    "You are an experienced vision agent that analyzes advertisements and evaluates their representation of diversity, inclusivity, and ethnicity (DEI)."
    "For each image (advertisement), identify **all** DEI-related elements."
    "For each DEI element, specify:"
    " - the diversity aspect represented (e.g., racial diversity, gender diversity, age diversity, etc.)"
    " - the inclusivity element (e.g., representation of marginalized groups, equality in roles, etc.)"
    " - the ethnic representation (e.g., specific ethnic groups represented)"
    " - the intensity of each element (a value between 0 and 1 indicating how strongly the ad represents that DEI aspect)"
    " - a brief description of how the advertisement reflects diversity, inclusivity, and ethnic representation."
    "If the ad showcases multiple DEI aspects, list them separately."
)
# Response schema updated to handle multiple DEI aspects, intensity, and a brief description
dei_ad_response_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "diversity_aspect": { "type": "string" },      # The type of diversity represented (e.g., racial, gender, age)
            "inclusivity_element": { "type": "string" },   # Inclusivity element (e.g., marginalized group representation)
            "ethnic_representation": { "type": "string" }, # Ethnic group represented
            "intensity": { "type": "number" },             # Intensity of DEI element (0 to 1)
            "description": { "type": "string" },           # Description of how the ad reflects DEI elements
        },
        "required": ["diversity_aspect", "inclusivity_element", "ethnic_representation", "intensity", "description"],
    }
}
# Updated prompt to query the model for DEI-related elements in the advertisement
dei_ad_prompt = (
    "Analyze this advertisement and identify all diversity, inclusivity, and ethnicity (DEI) elements it represents."
    "For each DEI element, specify the diversity aspect (e.g., racial, gender, age), the inclusivity element, the ethnic representation, the intensity (a value between 0 and 1), and provide a brief description of how the ad reflects DEI."
)

#### Extract Humour from images #######
# Updated system prompt to analyze humor elements in an advertisement
humor_ad_prompt_system = (
    "You are an experienced vision agent that analyzes advertisements and identifies the humor elements they are likely to invoke in a viewer."
    "For each image (advertisement), identify if the advertisement invokes humor."
    "If humor is present, return the following information as a separate entry:"
    " - the type of humor (e.g., slapstick, irony, puns, sarcasm, absurdity, etc.)"
    " - the intensity of the humor (a value between 0 and 1 indicating how strong the humorous element is)"
    " - a brief description explaining why the advertisement invokes humor and how it is conveyed."
    "If the ad invokes different types of humor, list them separately."
)

# Response schema updated to handle multiple humor types, intensity, and a brief description
humor_ad_response_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "humor_type": { "type": "string" },            # Type of humor (e.g., irony, sarcasm, etc.)
            "intensity": { "type": "number" },             # Intensity of humor (0 to 1)
            "description": { "type": "string" },           # Description of how humor is conveyed
        },
        "required": ["humor_type", "intensity", "description"],
    }
}
# Updated prompt to query the model for humor elements in the advertisement
humor_ad_prompt = (
    "Analyze this advertisement and identify any humorous elements it is likely to invoke in a viewer."
    "For each humorous element, specify the type of humor, its intensity (a value between 0 and 1), and provide a brief description of how the advertisement conveys humor."
)

# Read the image

########## Change this path to config file#############
picture_url = '/Users/thomasjoseph/Desktop/JMJTL/Data/Addidas/assets/453734675.jpeg'
rl_image = Image.load_from_file(picture_url)
##########################################################

## Extract emotions #####
emotion_elements = elementExtraction(emo_ad_response_schema,emo_ad_prompt_system,emo_ad_prompt,rl_image,model_name = "gemini-1.5-pro")
print(emotion_elements)

#### Extract DEI ######
dei_elements = elementExtraction(dei_ad_response_schema, dei_ad_prompt_system, dei_ad_prompt, rl_image, model_name="gemini-1.5-pro")
print(dei_elements)

### Extract Humour elements ####
humour_elements = elementExtraction(humor_ad_response_schema,humor_ad_prompt_system,humor_ad_prompt,rl_image,model_name = "gemini-1.5-pro")
print(humour_elements)

# Convert the elements into json and a dataframe
emotions_json = json.loads(emotion_elements)
DEI_json = json.loads(dei_elements)
humour_json = json.loads(humour_elements)

# Convert JSON data to DataFrames
df_emotions = pd.DataFrame(emotions_json)
df_DEI = pd.DataFrame(DEI_json)
df_humour = pd.DataFrame(humour_json)

# Save the df to csv files
df_emotions.to_csv("df_emotions.csv", index=False)
df_DEI.to_csv("df_DEI.csv", index=False)
df_humour.to_csv("df_humour.csv", index=False)

print(df_emotions)
print(df_DEI)
print(df_humour)



