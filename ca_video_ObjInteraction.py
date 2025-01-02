'''
This is the script for Object interactions
'''

from templates.video_functions import *
from templates.video_objectAnalysis import *


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
    import random
    import json
    import pickle

    pass
# ####################### The correct path should be represented here. Represent this in configfile ######
if True:
    GCP_AUTH_FILE = "/Users/thomasjoseph/Desktop/JMJTL/Projects/Gen_ai/key1.json"

    # Set path as env var
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = GCP_AUTH_FILE

    pass


#####################################
# Function for element extraction
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


######## Asset processing steps #########################

# Load the result pickle files
# Check if the Text Tone data frame exists
if os.path.exists('optimise_output/optimise_video_interactions_df.pkl'):  # Change the paths
    print("Loading Optimise Object interaction file from disk")
    with open('optimise_output/optimise_video_interactions_df.pkl', 'rb') as f:  # Change the paths
        optimise_video_interactions_df = pickle.load(f)
        print(optimise_video_interactions_df.shape)
else:
    print("Creating new people emotions  file")
    optimise_video_interactions_df = pd.DataFrame()

# Take only the relevant part from the file
### Emotions
interaction_df = pd.DataFrame()
# Reset the index of the interaction video df
optimise_video_interactions_df = optimise_video_interactions_df.reset_index(drop=True)

for index,row in optimise_video_interactions_df.iterrows():
    max_attempts = 5
    attempt = 0
    success = False

    # Attempt to call elementExtraction_absa up to max_attempts times
    while attempt < max_attempts and not success:
        try:
            # Call the element extraction functions
            objInterText = optimise_video_interactions_df['InteractionDescription'].iloc[index]

            objInteractionAction_elements = elementExtraction_video(object_interaction_extraction_response_schema,
                                                                    object_interaction_extraction_prompt_system,
                                                                    object_interaction_extraction_prompt, objInterText)
            # Convert the elements into a dataframe
            df_interaction = extract_physical_objects_data_to_single_row(objInteractionAction_elements)
            # Consolidate into the main data frame
            interaction_df = pd.concat([interaction_df, df_interaction])


            success = True  # Set success flag to True if the call succeeds
            print(f"Successfully processed row {index}")

            # Save the consolidated dataframe
            with open('optimise_output/optimise_video_objInteraction_df.pkl', 'wb') as f:
                pickle.dump(interaction_df, f)

        except Exception as e:
            # Increment the attempt count and print the error
            attempt += 1
            print(f"Attempt {attempt} failed for row {index}. Error: {e}")

            # If max attempts reached, skip to the next iteration
            if attempt == max_attempts:
                print(f"Skipping row {index} after {max_attempts} failed attempts.")


