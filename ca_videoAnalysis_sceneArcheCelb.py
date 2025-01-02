'''
This script contains the analysis for Video story archtype, celebrity identification and People identification
'''

from templates.video_functions import *
from templates.video_storyline import *
from templates.video_people import *
from templates.video_Making import *

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
# Check if the video scene data frame exists
if os.path.exists('optimise_output/optimise_video_scene_df.pkl'):  # Change the paths
    print("Loading Optimise Video scene file from disk")
    with open('optimise_output/optimise_video_scene_df.pkl', 'rb') as f:  # Change the paths
        optimise_video_scene_df = pickle.load(f)
        print(optimise_video_scene_df.shape)
else:
    print("Creating Video scene  file")
    optimise_video_scene_df = pd.DataFrame()

if os.path.exists('optimise_output/optimise_video_storyArchtype_df.pkl'):  # Change the paths
    print("Loading Optimise story archetype file from disk")
    with open('optimise_output/optimise_video_storyArchtype_df.pkl', 'rb') as f:  # Change the paths
        optimise_video_storyArchtype_df = pickle.load(f)
        print(optimise_video_storyArchtype_df.shape)
else:
    print("Creating Optimise story archetype file")
    optimise_video_storyArchtype_df = pd.DataFrame()

if os.path.exists('optimise_output/optimise_video_celebrityIdentify_df.pkl'):  # Change the paths
    print("Loading Optimise Celebrity identification file from disk")
    with open('optimise_output/optimise_video_celebrityIdentify_df.pkl', 'rb') as f:  # Change the paths
        optimise_video_celebrityIdentify_df = pickle.load(f)
        print(optimise_video_celebrityIdentify_df.shape)
else:
    print("Creating Celebrity identification  file")
    optimise_video_celebrityIdentify_df = pd.DataFrame()

if os.path.exists('optimise_output/optimise_video_actorCelebPeople_df.pkl'):  # Change the paths
    print("Loading Optimise  actor celeb file from disk")
    with open('optimise_output/optimise_video_actorCelebPeople_df.pkl', 'rb') as f:  # Change the paths
        optimise_video_actorCelebPeople_df = pickle.load(f)
        print(optimise_video_actorCelebPeople_df.shape)
else:
    print("Creating new actor celeb file")
    optimise_video_actorCelebPeople_df = pd.DataFrame()

# Get the list of all the files
# Directory containing the mp4 files
directory = '/Users/thomasjoseph/Desktop/JMJTL/Data/Dell/assets-mp4'  # Change this path

# Get all files in the directory
all_files = os.listdir(directory)

# Filter only mp4 files that do not contain 'heatmap' in their name
mp4_files_no_heatmap = [file for file in all_files if file.endswith('.mp4') and 'heatmap' not in file]

# Read the assets one by one
for index, mp4file in enumerate(mp4_files_no_heatmap[758:]):
    print(index, mp4file)
    print(optimise_video_scene_df.shape, optimise_video_storyArchtype_df.shape, optimise_video_celebrityIdentify_df.shape,
          optimise_video_actorCelebPeople_df.shape)
    # Get the asset path
    assetPath = directory + '/' + mp4file
    # Read the asset
    # Convert the asset to binary format
    with open(assetPath, "rb") as f:
        video_data = f.read()
    # Convert the video to the required format
    video1 = Part.from_data(mime_type="video/mp4", data=video_data)
    # Initialize the number of attempts
    max_attempts = 5
    attempt = 0
    success = False

    # Attempt to call elementExtraction_absa up to max_attempts times
    while attempt < max_attempts and not success:
        try:
            # Call the element extraction functions

            archetype_elements = elementExtraction_video(video_storyline_archetype_analysis_response_schema,
                                                              video_storyline_archetype_analysis_prompt_system,
                                                              video_storyline_archetype_analysis_prompt, video1)

            celebrity_elements = elementExtraction_video(video_celebrity_identification_response_schema,
                                                         video_celebrity_identification_prompt_system,
                                                         video_celebrity_identification_prompt, video1)

            scene_elements = elementExtraction_video(video_scene_analysis_response_schema,
                                                     video_scene_analysis_prompt_system,
                                                     video_scene_analysis_prompt, video1)

            Peoplecelebrity_elements = elementExtraction_video(video_Peoplecelebrity_identification_response_schema,
                                                               video_Peoplecelebrity_identification_prompt_system,
                                                               video_Peoplecelebrity_identification_prompt, video1)

            success = True  # Set success flag to True if the call succeeds
            print(f"Successfully processed row {index}")


            # Convert the output into dataframes
            df_archtype = extract_archetype_data_to_dataframe(archetype_elements)
            df_archtype['fileName'] = mp4file
            optimise_video_storyArchtype_df = pd.concat([optimise_video_storyArchtype_df, df_archtype])

            df_sceneAnalysis = extract_scene_data_to_dataframe(scene_elements)
            df_sceneAnalysis['fileName'] = mp4file
            optimise_video_scene_df = pd.concat([optimise_video_scene_df, df_sceneAnalysis])

            df_celebrity = extract_celebrity_data_to_dataframe(celebrity_elements)
            df_celebrity['fileName'] = mp4file
            optimise_video_celebrityIdentify_df = pd.concat([optimise_video_celebrityIdentify_df, df_celebrity])

            df_peopleIdentification = extract_person_identification_data_to_dataframe(Peoplecelebrity_elements)
            df_peopleIdentification['fileName'] = mp4file
            optimise_video_actorCelebPeople_df = pd.concat([optimise_video_actorCelebPeople_df, df_peopleIdentification])

            # Save the consolidated dataframe
            with open('optimise_output/optimise_video_storyArchtype_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_storyArchtype_df, f)

            with open('optimise_output/optimise_video_scene_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_scene_df, f)

            with open('optimise_output/optimise_video_celebrityIdentify_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_celebrityIdentify_df, f)

            with open('optimise_output/optimise_video_actorCelebPeople_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_actorCelebPeople_df, f)

        except Exception as e:
            # Increment the attempt count and print the error
            attempt += 1
            print(f"Attempt {attempt} failed for row {index}. Error: {e}")

            # If max attempts reached, skip to the next iteration
            if attempt == max_attempts:
                print(f"Skipping row {index} after {max_attempts} failed attempts.")