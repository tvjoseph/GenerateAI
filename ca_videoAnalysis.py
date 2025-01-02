'''
This script is to process videos to extract additional features for creative analytics.
The features extracted would be
1. Invoked Emotions of the video
2. Humour elements in the video
3. Relevance of the story line
4. Visual appeal of the elements
5. Audio and Sound appeal
'''
from templates.video_emotions import video_emotion_analysis_response_schema,video_emotion_analysis_prompt_system,video_emotion_analysis_prompt
from templates.video_humour import video_humor_analysis_response_schema,video_humor_analysis_prompt_system,video_humor_analysis_prompt
from templates.video_storyline import storyline_message_analysis_response_schema,storyline_message_analysis_prompt_system,storyline_message_analysis_prompt
from templates.video_visualAesthetics import color_visual_analysis_response_schema,color_visual_analysis_prompt_system,color_visual_analysis_prompt
from templates.video_AudioSound import sound_music_analysis_response_schema,sound_music_analysis_prompt_system,sound_music_analysis_prompt
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
# Check if the consolidated data frame exists
if os.path.exists('optimise_output/optimise_video_consol_df.pkl'): # Change the paths
    print("Loading Optimise consolidated file from disk")
    with open('optimise_output/optimise_video_consol_df.pkl', 'rb') as f: # Change the paths
      optimise_video_consol_df = pickle.load(f)
      print(optimise_video_consol_df.shape)
else:
    print("Creating new Consolidated file")
    optimise_video_consol_df = pd.DataFrame()

if os.path.exists('optimise_output/optimise_video_visual_df.pkl'): # Change the paths
    print("Loading Optimise visual file from disk")
    with open('optimise_output/optimise_video_visual_df.pkl', 'rb') as f: # Change the paths
      optimise_video_visual_df = pickle.load(f)
      print(optimise_video_visual_df.shape)
else:
    print("Creating new Visual file")
    optimise_video_visual_df = pd.DataFrame()

if os.path.exists('optimise_output/optimise_video_storyline_df.pkl'): # Change the paths
    print("Loading Optimise Storyline file from disk")
    with open('optimise_output/optimise_video_storyline_df.pkl', 'rb') as f: # Change the paths
      optimise_video_storyline_df = pickle.load(f)
      print(optimise_video_storyline_df.shape)
else:
    print("Creating new Storyline file")
    optimise_video_storyline_df = pd.DataFrame()

if os.path.exists('optimise_output/optimise_video_interactions_df.pkl'): # Change the paths
    print("Loading Optimise Object interaction file from disk")
    with open('optimise_output/optimise_video_interactions_df.pkl', 'rb') as f: # Change the paths
      optimise_video_interactions_df = pickle.load(f)
      print(optimise_video_interactions_df.shape)
else:
    print("Creating new Object interaction file")
    optimise_video_interactions_df = pd.DataFrame()

if os.path.exists('optimise_output/optimise_video_motions_df.pkl'): # Change the paths
    print("Loading Optimise Object motions file from disk")
    with open('optimise_output/optimise_video_motions_df.pkl', 'rb') as f: # Change the paths
      optimise_video_motions_df = pickle.load(f)
      print(optimise_video_motions_df.shape)
else:
    print("Creating new Object motions file")
    optimise_video_motions_df = pd.DataFrame()

if os.path.exists('optimise_output/optimise_video_flow_df.pkl'): # Change the paths
    print("Loading Optimise Object video flow file from disk")
    with open('optimise_output/optimise_video_flow_df.pkl', 'rb') as f: # Change the paths
      optimise_video_flow_df = pickle.load(f)
      print(optimise_video_flow_df.shape)
else:
    print("Creating new Object video flow file")
    optimise_video_flow_df = pd.DataFrame()

if os.path.exists('optimise_output/optimise_video_rarity_df.pkl'): # Change the paths
    print("Loading Optimise Object rarity/uniqueness file from disk")
    with open('optimise_output/optimise_video_rarity_df.pkl', 'rb') as f: # Change the paths
      optimise_video_rarity_df = pickle.load(f)
      print(optimise_video_rarity_df.shape)
else:
    print("Creating new Object rarity/uniqueness file")
    optimise_video_rarity_df = pd.DataFrame()

if os.path.exists('optimise_output/optimise_video_alignment_df.pkl'): # Change the paths
    print("Loading Optimise Object Alignment file from disk")
    with open('optimise_output/optimise_video_alignment_df.pkl', 'rb') as f: # Change the paths
      optimise_video_alignment_df = pickle.load(f)
      print(optimise_video_alignment_df.shape)
else:
    print("Creating new Object Alignment file")
    optimise_video_alignment_df = pd.DataFrame()







# Get the list of all the files
# Directory containing the mp4 files
directory = '/Users/thomasjoseph/Desktop/JMJTL/Data/Dell/assets-mp4' # Change this path

# Get all files in the directory
all_files = os.listdir(directory)

# Filter only mp4 files that do not contain 'heatmap' in their name
mp4_files_no_heatmap = [file for file in all_files if file.endswith('.mp4') and 'heatmap' not in file]

# Read the assets one by one
for index,mp4file in enumerate(mp4_files_no_heatmap[234:]):
    print(index,mp4file)
    #print(optimise_video_consol_df.shape,optimise_video_visual_df.shape,optimise_video_storyline_df.shape)
    print(optimise_video_alignment_df.shape, optimise_video_rarity_df.shape, optimise_video_flow_df.shape, optimise_video_motions_df.shape, optimise_video_interactions_df.shape)
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
            '''
            
            videoEmotion_elements = elementExtraction_video(video_emotion_analysis_response_schema,
                                                            video_emotion_analysis_prompt_system,
                                                            video_emotion_analysis_prompt, video1)

            videoHumour_elements = elementExtraction_video(video_humor_analysis_response_schema,
                                                           video_humor_analysis_prompt_system,
                                                           video_humor_analysis_prompt, video1)

            videoStoryline_elements = elementExtraction_video(storyline_message_analysis_response_schema,
                                                              storyline_message_analysis_prompt_system,
                                                              storyline_message_analysis_prompt, video1)

            videoVisualappeal_elements = elementExtraction_video(color_visual_analysis_response_schema,
                                                                 color_visual_analysis_prompt_system,
                                                                 color_visual_analysis_prompt, video1)

            videoAudioappeal_elements = elementExtraction_video(sound_music_analysis_response_schema,
                                                                sound_music_analysis_prompt_system,
                                                                sound_music_analysis_prompt, video1)
            '''

            objINteraction_elements = elementExtraction_video(video_object_interaction_analysis_response_schema,
                                                              video_object_interaction_analysis_prompt_system,
                                                              video_object_interaction_analysis_prompt, video1)

            objMotionPattern_elements = elementExtraction_video(video_motion_pattern_analysis_response_schema,
                                                                video_motion_pattern_analysis_prompt_system,
                                                                video_motion_pattern_analysis_prompt, video1)

            objVisualFlow_elements = elementExtraction_video(video_visual_flow_analysis_response_schema,
                                                             video_visual_flow_analysis_prompt_system,
                                                             video_visual_flow_analysis_prompt, video1)

            objRarity_elements = elementExtraction_video(video_object_rarity_analysis_response_schema,
                                                         video_object_rarity_analysis_prompt_system,
                                                         video_object_rarity_analysis_prompt, video1)

            objAlignment_elements = elementExtraction_video(video_object_alignment_analysis_response_schema,
                                                            video_object_alignment_analysis_prompt_system,
                                                            video_object_alignment_analysis_prompt, video1)


            success = True  # Set success flag to True if the call succeeds
            print(f"Successfully processed row {index}")
            '''
            
            # Convert the output into dataframes
            df_consol = extract_data_to_dataframe(videoEmotion_elements, videoHumour_elements, videoAudioappeal_elements)
            df_consol['fileName'] = mp4file
            optimise_video_consol_df = pd.concat([optimise_video_consol_df, df_consol])
            # Convert the storyline output into dataframe
            df_storyline = extract_storyline_data_to_dataframe(videoStoryline_elements)
            df_storyline['fileName'] = mp4file
            optimise_video_storyline_df = pd.concat([optimise_video_storyline_df, df_storyline])
            # Convert visual output into dataframe
            df_visual = extract_visual_data_to_dataframe(videoVisualappeal_elements)
            df_visual['fileName'] = mp4file
            optimise_video_visual_df = pd.concat([optimise_video_visual_df, df_visual])
            

            # Save the consolidated dataframe
            with open('optimise_output/optimise_video_consol_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_consol_df, f)
            with open('optimise_output/optimise_video_storyline_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_storyline_df, f)
            with open('optimise_output/optimise_video_visual_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_visual_df, f)
            '''

            # Convert the output into dataframes
            df_interactions = extract_object_interactions_data_to_dataframe(objINteraction_elements)
            df_interactions['fileName'] = mp4file
            optimise_video_interactions_df = pd.concat([optimise_video_interactions_df, df_interactions])

            df_motionPatterns = extract_motion_patterns_data_to_dataframe(objMotionPattern_elements)
            df_motionPatterns['fileName'] = mp4file
            optimise_video_motions_df = pd.concat([optimise_video_motions_df, df_motionPatterns])

            df_visualFlow = extract_visual_flow_data_to_dataframe(objVisualFlow_elements)
            df_visualFlow['fileName'] = mp4file
            optimise_video_flow_df = pd.concat([optimise_video_flow_df, df_visualFlow])

            df_uniqueness = extract_object_rarity_data_to_dataframe(objRarity_elements)
            df_uniqueness['fileName'] = mp4file
            optimise_video_rarity_df = pd.concat([optimise_video_rarity_df, df_uniqueness])

            df_ObjAlign = extract_object_alignment_data_to_dataframe(objAlignment_elements)
            df_ObjAlign['fileName'] = mp4file
            optimise_video_alignment_df = pd.concat([optimise_video_alignment_df, df_ObjAlign])

            # Save the consolidated dataframe
            with open('optimise_output/optimise_video_interactions_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_interactions_df, f)

            with open('optimise_output/optimise_video_motions_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_motions_df, f)

            with open('optimise_output/optimise_video_flow_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_flow_df, f)

            with open('optimise_output/optimise_video_rarity_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_rarity_df, f)

            with open('optimise_output/optimise_video_alignment_df.pkl', 'wb') as f:
                pickle.dump(optimise_video_alignment_df, f)

        except Exception as e:
            # Increment the attempt count and print the error
            attempt += 1
            print(f"Attempt {attempt} failed for row {index}. Error: {e}")

            # If max attempts reached, skip to the next iteration
            if attempt == max_attempts:
                print(f"Skipping row {index} after {max_attempts} failed attempts.")






