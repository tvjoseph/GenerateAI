'''
18-Oct-2024
This is the script for extracting creative elements from images
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
    GCP_AUTH_FILE = "/Users/thomasjoseph/Desktop/JMJTL/Projects/Gen_ai/key.json" ##### Change this path to config file or vault

    # Set path as env var
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GCP_AUTH_FILE

    pass

# Element extraction function
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

##### Object prompt configurations #########
# Extract objects from image
obj_prompt_system = (
        "You are an experienced vision agent who identifies different objects within an image."
        "For each image, identify **all** the objects. Return each object as a separate entry."
        "For each object, specify:"
        " - the type (object name)"
        " - the percentage of the area it occupies in the image"
        " - the object's attention score (a value between 0 and 100)"
        " - the object's position based on a 9-position grid, which includes:"
        " top-left, top-center, top-right, center-left, center, center-right, bottom-left, bottom-center, bottom-right."
        "If there are multiple objects, list them separately."
    )

# Output schema updated to handle multiple objects with attention score and position in a 9-grid format
obj_response_schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "subject": { "type": "string" },           # Object type
                "area": { "type": "integer" },             # Area as a percentage
                "attention_score": { "type": "number" },   # Attention score between 0 and 1
                "position": { "type": "string" },          # Position on a 9-grid (e.g., "top-left", "center")
            },
            "required": ["subject", "area", "attention_score", "position"],
        }
    }

obj_prompt = "Identify all objects within this image. For each object, identify its type, the percentage of the area it occupies, its attention score (0 to 100), and its position on a 9-position grid (top-left, center, etc.)."

################## Colour extracton prompt configs ##############
col_prompt_system = (
        "You are an experienced vision agent that identifies colors within an image."
        "For each image, identify **all** the colors. Return each color as a separate entry."
        "For each color, specify:"
        " - the Pantone color name (closest match)"
        " - the corresponding Hex code of the color"
        " - the percentage of the area the color occupies in the image."
        "If there are multiple colors, list them separately."
    )

    # Output schema updated to handle multiple colors, Pantone name, Hex code, and area
col_response_schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "pantone_color": { "type": "string" },     # Pantone color name
                "hex_code": { "type": "string" },          # Hex code of the color
                "area": { "type": "integer" },             # Area as a percentage
            },
            "required": ["pantone_color", "hex_code", "area"],
        }
    }
col_prompt = "Identify all colors in this image. For each color, identify its closest Pantone color name, Hex code, and the percentage of the area it occupies."


########## Extract people from images ###########
# people analysis
people_prompt_system = (
    "You are an experienced vision agent that identifies people within an image. "
    "For each image, identify **all** the people. Return each person as a separate entry. "
    "For each person, specify: "
    " - the person's gender (male, female, or unknown) "
    " - the person's age group (0-10, 10-20, 20-25, 25-30, 30-35, 35-50, 50-60, 60-75, 75+) "
    " - the person's emotion (e.g., happy, sad, angry, surprised, neutral, calm, fear, confused, etc.) "
    " - the percentage of the area the person occupies in the image "
    " - the person's position based on a 9-position grid, which includes: "
    " top-left, top-center, top-right, center-left, center, center-right, bottom-left, bottom-center, bottom-right "
    " - the **attention score** (a value between 0 and 100, indicating how much attention the person might attract in the image)"
    "If there are multiple people, list them separately."
)


    # Output schema updated to handle multiple people, gender, age, emotion, and area
people_response_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "subject": { "type": "string" },             # Identifies the subject as a person
            "gender": { "type": "string" },              # Gender (male, female, unknown)
            "age": { "type": "string" },                 # Age group (0-10, 10-20, 20-25, 25-30, 30-35, 35-50, 50-60, 60-75, 75+)
            "emotion": { "type": "string" },             # Emotion (happy, sad, angry, neutral, etc.)
            "area": { "type": "integer" },               # Area occupied as a percentage
            "position": { "type": "string" },            # Position in the 9-position grid
            "attention_score": { "type": "number" }      # Attention score (0 to 100)
        },
        "required": ["subject", "gender", "age", "emotion", "area", "position", "attention_score"]
    }
}


people_prompt = (
    "Identify all people in this image. "
    "For each person, identify their gender, age group, emotion, the percentage of the area they occupy, "
    "their position in the 9-position grid, and their attention score (a value between 0 and 100)."
)


#### Logo Extraction ################
logo_prompt_system = (
        "You are an experienced vision agent that identifies logos within an image."
        "For each image, identify **all** the logos. Return each logo as a separate entry."
        "For each logo, specify:"
        " - the logo's name or type"
        " - the percentage of the area it occupies in the image"
        " - the logo's attention score (a value between 0 and 100)."
        " - the Logo position based on a 9-position grid, which includes:"
        " top-left, top-center, top-right, center-left, center, center-right, bottom-left, bottom-center, bottom-right."
        "If there are multiple logos, list them separately."
    )

    # Output schema updated to handle multiple logos, area, and attention score
logo_response_schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "logo_name": { "type": "string" },          # Logo name or type
                "area": { "type": "integer" },              # Area as a percentage
                "attention_score": { "type": "number" },
                "position": { "type": "string" },            # Attention score between 0 and 1
            },
            "required": ["logo_name", "area", "attention_score","position"],
        }
    }
logo_prompt = "Identify all logos in this image. For each logo, identify its name, the percentage of the area it occupies, and its attention score (0 to 100)."

####### Text processing ##########
# Text data
txt_prompt_system = (
    "You are an experienced vision agent that identifies text within an image."
    "For each image, identify **all** the text. Return each text as a separate entry."
    "For each text, specify:"
    " - extract the text as it is"
    " - the percentage of the area it occupies in the image ( a value between 0 and 1)"
    " - text's attention score (a value between 0 and 100)."
    " - the text position based on a 9-position grid, which includes:"
    " top-left, top-center, top-right, center-left, center, center-right, bottom-left, bottom-center, bottom-right."
    "If there are multiple texts, list them separately."
)

# Output schema updated to handle multiple logos, area, and attention score
txt_response_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "text_value": { "type": "string" },          # Logo name or type
            "area": { "type": "integer" },              # Area as a percentage
            "attention_score": { "type": "number" },
            "position": { "type": "string" },            # Attention score between 0 and 1
        },
        "required": ["text_value", "area", "attention_score","position"],
    }
}

txt_prompt = "Identify all text in this image. For each text, identify the percentage of the area it occupies, and its attention score (0 to 100)."

##### Celebrity Detection #########
celebrity_prompt_system = (
    "You are an experienced vision agent that identifies celebrities within an image. "
    "For each image, identify **all** the celebrities present. Return each celebrity as a separate entry. "
    "For each celebrity, specify: "
    " - the celebrity's name (if identified) "
    " - the person's gender (male, female, or unknown) "
    " - the person's age group (0-10, 10-20, 20-25, 25-30, 30-35, 35-50, 50-60, 60-75, 75+) "
    " - the person's emotion (e.g., happy, sad, angry, surprised, neutral, calm, fear, confused, etc.) "
    " - the percentage of the area the person occupies in the image. "
    " - the person's position based on a 9-position grid, which includes: "
    " top-left, top-center, top-right, center-left, center, center-right, bottom-left, bottom-center, bottom-right. "
    " - the **attention score** (a value between 0 and 100, indicating the viewer’s likelihood of focusing on the celebrity)"
    "If there are multiple celebrities, list them separately."
)


celebrity_response_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "subject": { "type": "string" },              # Identifies the subject as a celebrity
            "celebrity_name": { "type": "string" },       # Name of the celebrity (if identifiable)
            "gender": { "type": "string" },               # Gender (male, female, unknown)
            "age": { "type": "string" },                  # Age group (0-10, 10-20, 20-25, 25-30, 30-35, 35-50, 50-60, 60-75, 75+)
            "emotion": { "type": "string" },              # Emotion (happy, sad, angry, surprised, neutral, etc.)
            "area": { "type": "integer" },                # Area occupied as a percentage
            "position": { "type": "string" },             # Position in the image grid
            "attention_score": { "type": "number" }       # Attention score (0-1)
        },
        "required": ["subject", "celebrity_name", "gender", "age", "emotion", "area", "position", "attention_score"]
    }
}

celebrity_prompt = (
    "Identify all celebrities in this image. "
    "For each celebrity, identify their name (if possible), gender, age group, emotion, "
    "the percentage of the area they occupy, their position in the 9-position grid, "
    "and the attention score (a value between 0 and 100, indicating the likelihood of the viewer focusing on the celebrity)."
)

# Read the image

########## Change this path to config file#############
picture_url = '/Users/thomasjoseph/Desktop/JMJTL/Data/Addidas/assets/453734675.jpeg'
rl_image = Image.load_from_file(picture_url)
##########################################################

# Extract objects from the image
obj_elements = elementExtraction(obj_response_schema,obj_prompt_system,obj_prompt,rl_image)

print(obj_elements , '##################')
# Extract the colour from the image
col_elements = elementExtraction(col_response_schema,col_prompt_system,col_prompt,rl_image)
print(col_elements , '##################')
# Extract the people from the image
people_elements = elementExtraction(people_response_schema,people_prompt_system,people_prompt,rl_image)
print(people_elements , '##################')
# Extract the logo from the image
logo_elements = elementExtraction(logo_response_schema,logo_prompt_system,logo_prompt,rl_image)
print(logo_elements , '##################')
# Extract the text from the image
txt_elements = elementExtraction(txt_response_schema,txt_prompt_system,txt_prompt,rl_image)
print(txt_elements , '##################')
# Celebrity extraction
celebrity_elements = elementExtraction(celebrity_response_schema,celebrity_prompt_system,celebrity_prompt,rl_image)
print(celebrity_elements , '##################')
# Get dimensions
rl_img = PIL_Image.open(picture_url)  # Open the image using PIL
# Get dimensions
width, height = rl_img.size

# Convert the files into dataframe
objects_json = json.loads(obj_elements)
colors_json = json.loads(col_elements)
people_json = json.loads(people_elements)
logos_json = json.loads(logo_elements)
texts_json = json.loads(obj_elements)
celebrities_json = json.loads(celebrity_elements)

# Convert JSON data to DataFrames
df_objects = pd.DataFrame(objects_json)
df_colors = pd.DataFrame(colors_json)
df_people = pd.DataFrame(people_json)
df_logos = pd.DataFrame(logos_json)
df_texts = pd.DataFrame(texts_json)
df_celebrities = pd.DataFrame(celebrities_json)

# Save all the files as csv
df_objects.to_csv("df_objects.csv", index=False)
df_colors.to_csv("df_colors.csv", index=False)
df_people.to_csv("df_people.csv", index=False)
df_logos.to_csv("df_logos.csv", index=False)
df_texts.to_csv("df_texts.csv", index=False)
df_celebrities.to_csv("df_celebrities.csv", index=False)

# Store the width and height
width, height







