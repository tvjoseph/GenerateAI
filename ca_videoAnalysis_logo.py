'''
Script for analying Logo in video's
'''

from templates.video_functions import *
from templates.video_Logo import *

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
# Check if the Logo visibility data frame exists
if os.path.exists('optimise_output/optimise_video_logoVisibility_df.pkl'):  # Change the paths
    print("Loading Optimise Logo visibility file from disk")
    with open('optimise_output/optimise_video_logoVisibility_df.pkl', 'rb') as f:  # Change the paths
        optimise_video_logoVisibility_df = pickle.load(f)
        print(optimise_video_logoVisibility_df.shape)
else:
    print("Creating Logo visibility  file")
    optimise_video_logoVisibility_df = pd.DataFrame()

if os.path.exists('optimise_output/optimise_video_logoDuration_df.pkl'):  # Change the paths
    print("Loading Optimise Logo duration file from disk")
    with open('optimise_output/optimise_video_logoDuration_df.pkl', 'rb') as f:  # Change the paths
        optimise_video_logoDuration_df = pickle.load(f)
        print(optimise_video_logoDuration_df.shape)
else:
    print("Creating Optimise Logo duration file")
    optimise_video_logoDuration_df = pd.DataFrame()

if os.path.exists('optimise_output/optimise_video_logoSize_df.pkl'):  # Change the paths
    print("Loading Optimise Logo Size file from disk")
    with open('optimise_output/optimise_video_logoSize_df.pkl', 'rb') as f:  # Change the paths
        optimise_video_logoSize_df = pickle.load(f)
        print(optimise_video_logoSize_df.shape)
else:
    print("Creating Logo Size file")
    optimise_video_logoSize_df = pd.DataFrame()

if os.path.exists('optimise_output/optimise_video_logoInteractions_df.pkl'):  # Change the paths
    print("Loading Optimise  Logo interactions file from disk")
    with open('optimise_output/optimise_video_logoInteractions_df.pkl', 'rb') as f:  # Change the paths
        optimise_video_logoInteractions_df = pickle.load(f)
        print(optimise_video_logoInteractions_df.shape)
else:
    print("Creating new Logo interactions file")
    optimise_video_logoInteractions_df = pd.DataFrame()

# Get the list of all the files
# Directory containing the mp4 files
directory = '/Users/thomasjoseph/Desktop/JMJTL/Data/Dell/assets-mp4'  # Change this path

# Get all files in the directory
all_files = os.listdir(directory)

# Filter only mp4 files that do not contain 'heatmap' in their name
mp4_files_no_heatmap = [file for file in all_files if file.endswith('.mp4') and 'heatmap' not in file]

# Read the assets one by one
for index, mp4file in enumerate(mp4_files_no_heatmap[554:]):
    print(index, mp4file)
    print(optimise_video_logoVisibility_df.shape, optimise_video_logoDuration_df.shape, optimise_video_logoSize_df.shape,
          optimise_video_logoInteractions_df.shape)
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

            logoVisibility_elements = elementExtraction_video(video_logo_analysis_response_schema,
                                                              video_logo_analysis_prompt_system,
                                                              video_logo_analysis_prompt, video1)

            logoDuration_elements = elementExtraction_video(video_logo_visibility_analysis_response_schema,
                                                            video_logo_visibility_analysis_prompt_system,
                                                            video_logo_visibility_analysis_prompt, video1)

            logoSizeProminance_elements = elementExtraction_video(video_logo_size_prominence_analysis_response_schema,
                                                                  video_logo_size_prominence_analysis_prompt_system,
                                                                  video_logo_size_prominence_analysis_prompt, video1)

            logoInteraction_elements = elementExtraction_video(video_logo_interaction_analysis_response_schema,
                                                               video_logo_interaction_analysis_prompt_system,
                                                               video_logo_interaction_analysis_prompt, video1)

            success = True  # Set success flag to True if the call succeeds
            print(f"Successfully processed row {index}")


            # Convert the output into dataframes
            df_logoVisibility = extract_logo_analysis_data_to_dataframe(logoVisibility_elements)
            df_logoVisibility['fileName'] = mp4file
            optimise_video_logoVisibility_df = pd.concat([optimise_video_logoVisibility_df, df_logoVisibility])

            df_logoDuration = extract_logo_visibility_data_to_dataframe(logoDuration_elements)
            df_logoDuration['fileName'] = mp4file
            optimise_video_logoDuration_df = pd.concat([optimise_video_logoDuration_df, df_logoDuration])

            df_logoProminance = extract_logo_size_prominence_data_to_dataframe(logoSizeProminance_elements)
            df_logoProminance['fileName'] = mp4file
            optimise_video_logoSize_df = pd.concat([optimise_video_logoSize_df, df_logoProminance])

            df_logoInteractions = extract_logo_interaction_data_to_dataframe(logoInteraction_elements)
            df_logoInteractions['fileName'] = mp4file
            optimise_video_logoInteractions_df = pd.concat([optimise_video_logoInteractions_df, df_logoInteractions])

            # Save the consolidated dataframe
            with open('optimise_output/optimise_video_logoVisibility_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_logoVisibility_df, f)

            with open('optimise_output/optimise_video_logoDuration_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_logoDuration_df, f)

            with open('optimise_output/optimise_video_logoSize_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_logoSize_df, f)

            with open('optimise_output/optimise_video_logoInteractions_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_logoInteractions_df, f)

        except Exception as e:
            # Increment the attempt count and print the error
            attempt += 1
            print(f"Attempt {attempt} failed for row {index}. Error: {e}")

            # If max attempts reached, skip to the next iteration
            if attempt == max_attempts:
                print(f"Skipping row {index} after {max_attempts} failed attempts.")

