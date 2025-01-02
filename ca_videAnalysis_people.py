from templates.video_functions import *
from templates.video_people import *

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
if os.path.exists('optimise_output/optimise_video_peopleEmotions_df.pkl'):  # Change the paths
    print("Loading Optimise people emotions file from disk")
    with open('optimise_output/optimise_video_peopleEmotions_df.pkl', 'rb') as f:  # Change the paths
        optimise_video_peopleEmotions_df = pickle.load(f)
        print(optimise_video_peopleEmotions_df.shape)
else:
    print("Creating new people emotions  file")
    optimise_video_peopleEmotions_df = pd.DataFrame()

if os.path.exists('optimise_output/optimise_video_peopleGesture_df.pkl'):  # Change the paths
    print("Loading Optimise People gestures file from disk")
    with open('optimise_output/optimise_video_peopleGesture_df.pkl', 'rb') as f:  # Change the paths
        optimise_video_peopleGesture_df = pickle.load(f)
        print(optimise_video_peopleGesture_df.shape)
else:
    print("Creating Optimise People gestures file")
    optimise_video_peopleGesture_df = pd.DataFrame()

if os.path.exists('optimise_output/optimise_video_peopleObjInter_df.pkl'):  # Change the paths
    print("Loading Optimise People object interaction file from disk")
    with open('optimise_output/optimise_video_peopleObjInter_df.pkl', 'rb') as f:  # Change the paths
        optimise_video_peopleObjInter_df = pickle.load(f)
        print(optimise_video_peopleObjInter_df.shape)
else:
    print("Creating People object interaction")
    optimise_video_peopleObjInter_df = pd.DataFrame()

if os.path.exists('optimise_output/optimise_video_peopleDemographics_df.pkl'):  # Change the paths
    print("Loading Optimise  People demographics file from disk")
    with open('optimise_output/optimise_video_peopleDemographics_df.pkl', 'rb') as f:  # Change the paths
        optimise_video_peopleDemographics_df = pickle.load(f)
        print(optimise_video_peopleDemographics_df.shape)
else:
    print("Creating new People demographics file")
    optimise_video_peopleDemographics_df = pd.DataFrame()


if os.path.exists('optimise_output/optimise_video_peoplePeopleInter_df.pkl'):  # Change the paths
    print("Loading Optimise  People People interaction file from disk")
    with open('optimise_output/optimise_video_peoplePeopleInter_df.pkl', 'rb') as f:  # Change the paths
        optimise_video_peoplePeopleInter_df = pickle.load(f)
        print(optimise_video_peoplePeopleInter_df.shape)
else:
    print("Creating new People People interaction file")
    optimise_video_peoplePeopleInter_df = pd.DataFrame()


# Get the list of all the files
# Directory containing the mp4 files
directory = '/Users/thomasjoseph/Desktop/JMJTL/Data/Dell/assets-mp4'  # Change this path

# Get all files in the directory
all_files = os.listdir(directory)

# Filter only mp4 files that do not contain 'heatmap' in their name
mp4_files_no_heatmap = [file for file in all_files if file.endswith('.mp4') and 'heatmap' not in file]

# Read the assets one by one
for index, mp4file in enumerate(mp4_files_no_heatmap[0:]):
    print(index, mp4file)
    print(optimise_video_peopleEmotions_df.shape, optimise_video_peopleGesture_df.shape, optimise_video_peopleObjInter_df.shape,
          optimise_video_peopleDemographics_df.shape,optimise_video_peoplePeopleInter_df.shape)
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

            peopleEmotions_elements = elementExtraction_video(video_human_emotion_analysis_response_schema,
                                                              video_human_emotion_analysis_prompt_system,
                                                              video_human_emotion_analysis_prompt, video1)

            peopleGestures_elements = elementExtraction_video(video_human_gesture_analysis_response_schema,
                                                              video_human_gesture_analysis_prompt_system,
                                                              video_human_gesture_analysis_prompt, video1)

            peopleObjInteraction_elements = elementExtraction_video(video_human_object_interaction_response_schema,
                                                                    video_human_object_interaction_prompt_system,
                                                                    video_human_object_interaction_prompt, video1)

            peopleDemographics_elements = elementExtraction_video(video_demographics_analysis_response_schema,
                                                                  video_demographics_analysis_prompt_system,
                                                                  video_demographics_analysis_prompt, video1)

            peoplePeopleInter_elements = elementExtraction_video(video_people_interaction_analysis_response_schema,
                                                                 video_people_interaction_analysis_prompt_system,
                                                                 video_people_interaction_analysis_prompt, video1)


            success = True  # Set success flag to True if the call succeeds
            print(f"Successfully processed row {index}")


            # Convert the output into dataframes
            df_peopleEmotions = extract_human_emotion_data_to_dataframe(peopleEmotions_elements)
            df_peopleEmotions['fileName'] = mp4file
            optimise_video_peopleEmotions_df = pd.concat([optimise_video_peopleEmotions_df, df_peopleEmotions])

            df_peopleGestures = extract_human_gesture_data_to_dataframe(peopleGestures_elements)
            df_peopleGestures['fileName'] = mp4file
            optimise_video_peopleGesture_df = pd.concat([optimise_video_peopleGesture_df, df_peopleGestures])

            df_peopleObjInter = extract_human_object_interactions_data_to_dataframe(peopleObjInteraction_elements)
            df_peopleObjInter['fileName'] = mp4file
            optimise_video_peopleObjInter_df = pd.concat([optimise_video_peopleObjInter_df, df_peopleObjInter])

            df_demographics = extract_demographics_data_to_dataframe(peopleDemographics_elements)
            df_demographics['fileName'] = mp4file
            optimise_video_peopleDemographics_df = pd.concat([optimise_video_peopleDemographics_df, df_demographics])

            df_peoplePeopleInter = extract_people_interaction_data_to_dataframe(peoplePeopleInter_elements)
            df_peoplePeopleInter['fileName'] = mp4file
            optimise_video_peoplePeopleInter_df = pd.concat([optimise_video_peoplePeopleInter_df, df_peoplePeopleInter])

            # Save the consolidated dataframe
            with open('optimise_output/optimise_video_peopleEmotions_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_peopleEmotions_df, f)

            with open('optimise_output/optimise_video_peopleGesture_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_peopleGesture_df, f)

            with open('optimise_output/optimise_video_peopleObjInter_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_peopleObjInter_df, f)

            with open('optimise_output/optimise_video_peopleDemographics_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_peopleDemographics_df, f)

            with open('optimise_output/optimise_video_peoplePeopleInter_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_peoplePeopleInter_df, f)

        except Exception as e:
            # Increment the attempt count and print the error
            attempt += 1
            print(f"Attempt {attempt} failed for row {index}. Error: {e}")

            # If max attempts reached, skip to the next iteration
            if attempt == max_attempts:
                print(f"Skipping row {index} after {max_attempts} failed attempts.")