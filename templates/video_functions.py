'''
This script contains all the functions for processing the output json files
'''
import pandas as pd



# Function to extract data and convert to DataFrame for emotions , humour and sound
def extract_data_to_dataframe(emotion_json, humor_json, sound_music_json):
    records = []

    # Extract emotion data
    for element in emotion_json['emotionalResponses']:
        for segment in element['timeSegments']:
            record = {
                'Aspect': 'Emotion',
                'Description': element['description'],
                'Detail': element['emotion'],
                'Intensity': element['intensity'],
                'TimeSegment': segment
            }
            records.append(record)

    # Extract humor data
    for element in humor_json['humorElements']:
        for segment in element['timeSegments']:
            record = {
                'Aspect': 'Humor',
                'Description': element['description'],
                'Detail': element['humorType'],
                'Intensity': element['intensity'],
                'TimeSegment': segment
            }
            records.append(record)

    # Extract sound/music data
    for element in sound_music_json['soundMusicElements']:
        record = {
            'Aspect': 'Sound/Music',
            'Description': element['description'],
            'Detail': element['type'],
            'Intensity': element['emotionScore'],
            'TimeSegment': None
        }
        records.append(record)

    return pd.DataFrame(records)

# Function to extract visual data

def extract_visual_data_to_dataframe(visual_appeal_json):
    records = []

    # Extract color data
    for element in visual_appeal_json['colors']:
        # Split emotional appeals into individual categories
        emotional_appeals = element['emotionalAppeal'].split(', ')
        for appeal in emotional_appeals:
            record = {
                'Aspect': 'Visual Appeal',
                'Description': element['description'],
                'Color': element['color'],
                'AestheticScore': element['aestheticScore'],
                'EmotionScore': element['emotionScore'],
                'EmotionalAppeal': appeal
            }
            records.append(record)

    # Extract overall visuals data
    record = {
        'Aspect': 'Overall Visuals',
        'Description': visual_appeal_json['visuals']['description'],
        'OverallScore': visual_appeal_json['visuals']['overallScore']
    }
    records.append(record)

    return pd.DataFrame(records)

# Function to extract storyline data
def extract_storyline_data_to_dataframe(storyline_json):
    records = []

    # Extract improvement suggestions
    for key, value in storyline_json['improvementSuggestions'].items():
        record = {
            'Aspect': 'Improvement Suggestion',
            'Element': key.capitalize(),
            'Action': value['action'],
            'Description': value['descriptive']
        }
        records.append(record)

    # Extract message relevance
    record = {
        'Aspect': 'Message Relevance',
        'Element': 'Relevance',
        'Description': storyline_json['messageRelevance']['description'],
        'Score': storyline_json['messageRelevance']['score']
    }
    records.append(record)

    # Extract storyline clarity
    record = {
        'Aspect': 'Storyline Clarity',
        'Element': 'Clarity',
        'Description': storyline_json['storylineClarity']['description'],
        'Score': storyline_json['storylineClarity']['score']
    }
    records.append(record)

    return pd.DataFrame(records)

# Function to extract data and convert to DataFrame
def extract_object_alignment_data_to_dataframe(object_alignment_json):
    records = []

    # Extract data for each object
    for element in object_alignment_json['objectAlignmentAnalysis']:
        record = {
            'ObjectName': element['objectName'],
            'AlignmentDescription': element['alignmentDescription'],
            'BrandIdentityScore': element['brandIdentityScore'],
            'StorytellingScore': element['storytellingScore'],
            'ViewerEngagementScore': element['viewerEngagementScore'],
            'ImprovementSuggestions': element['improvementSuggestions']
        }
        records.append(record)

    return pd.DataFrame(records)

# Function to extract data and convert to DataFrame
def extract_object_rarity_data_to_dataframe(object_rarity_json):
    records = []

    # Extract data for each object
    for element in object_rarity_json['objectRarityAnalysis']:
        record = {
            'ObjectName': element['objectName'],
            'BrandIdentityScore': element['brandIdentityScore'],
            'BrandRelevance': element['brandRelevance'],
            'RarityDescription': element['rarityDescription'],
            'StorytellingScore': element['storytellingScore'],
            'ViewerEngagementScore': element['viewerEngagementScore'],
            'ImprovementSuggestions': element['improvementSuggestions']
        }
        records.append(record)

    return pd.DataFrame(records)

# Function to extract data and convert to DataFrame
def extract_visual_flow_data_to_dataframe(visual_flow_json):
    records = []

    # Extract data for each visual flow element
    for element in visual_flow_json['visualFlow']:
        for segment in element['timeSegments']:
            record = {
                'ObjectName': element['objectName'],
                'BrandIdentityScore': element['brandIdentityScore'],
                'OrderOfAppearance': ', '.join(element['orderOfAppearance']),
                'StorytellingScore': element['storytellingScore'],
                'ViewerEngagementScore': element['viewerEngagementScore'],
                'StartTime': segment['startTime'],
                'EndTime': segment['endTime'],
                'ImprovementSuggestions': element.get('improvementSuggestions', '')
            }
            records.append(record)

    return pd.DataFrame(records)

# Function to extract data and convert to DataFrame
def extract_motion_patterns_data_to_dataframe(motion_patterns_json):
    records = []

    # Extract data for each motion pattern
    for element in motion_patterns_json['motionPatterns']:
        for segment in element['timeSegments']:
            record = {
                'BrandIdentityScore': element['brandIdentityScore'],
                'Direction': element['direction'],
                'MotionDescription': element['motionDescription'],
                'Speed': element['speed'],
                'StorytellingScore': element['storytellingScore'],
                'ViewerEngagementScore': element['viewerEngagementScore'],
                'StartTime': segment.split('-')[0],
                'EndTime': segment.split('-')[1],
                'ImprovementSuggestions': element.get('improvementSuggestions', '')
            }
            records.append(record)

    return pd.DataFrame(records)

# Function to extract data and convert to DataFrame
def extract_object_interactions_data_to_dataframe(object_interactions_json):
    records = []

    # Extract data for each object interaction
    for element in object_interactions_json['objectInteractions']:
        for segment in element['timeSegments']:
            record = {
                'BrandIdentityScore': element['brandIdentityScore'],
                'InteractionDescription': element['interactionDescription'],
                'StorytellingScore': element['storytellingScore'],
                'ViewerEngagementScore': element['viewerEngagementScore'],
                'StartTime': segment.split('-')[0],
                'EndTime': segment.split('-')[1],
                'ImprovementSuggestions': element.get('improvementSuggestions', '')
            }
            records.append(record)

    return pd.DataFrame(records)

########### Text Functions ################
# Function to extract data and convert to DataFrame
def extract_product_feature_data_to_dataframe(product_feature_json):
    records = []

    # Extract data for each feature type
    for feature_type, details in product_feature_json['productFeatureAnalysis'].items():
        record = {
            'FeatureType': feature_type.capitalize(),
            'ActionDriveScore': details['actionDriveScore'],
            'ClarityScore': details['clarityScore'],
            'ComprehensivenessScore': details['comprehensivenessScore'],
            'Features': ', '.join(details['features']),
            'ImprovementSuggestions': details['improvementSuggestions']
        }
        records.append(record)

    return pd.DataFrame(records)

# Function to extract data and convert to DataFrame
def extract_product_claim_data_to_dataframe(product_claim_json):
    records = []

    # Extract data for each claim type
    for claim_type, details in product_claim_json['productClaimAnalysis'].items():
        record = {
            'ClaimType': claim_type.capitalize(),
            'ActionDriveScore': details['actionDriveScore'],
            'ClarityScore': details['clarityScore'],
            'CredibilityScore': details['credibilityScore'],
            'Claims': ', '.join(details['claims']),
            'ImprovementSuggestions': details['improvementSuggestions']
        }
        records.append(record)

    return pd.DataFrame(records)

def extract_product_benefit_data_to_dataframe(product_benefit_json):
    records = []

    # Extract data for each benefit type
    for benefit_type, details in product_benefit_json['productBenefitAnalysis'].items():
        record = {
            'BenefitType': benefit_type.capitalize(),
            'ActionDriveScore': details['actionDriveScore'],
            'ClarityScore': details['clarityScore'],
            'Benefits': ', '.join(details['benefits']),
            'ImprovementSuggestions': details['improvementSuggestions']
        }
        records.append(record)

    return pd.DataFrame(records)

# Function to extract data and convert to DataFrame
def extract_cta_tone_data_to_dataframe(cta_tone_json):
    records = []

    # Extract data for each CTA tone analysis
    for element in cta_tone_json['ctaToneAnalysis']:
        record = {
            'CTATone': element['ctaTone'],
            'ResponseType': element['responseType'],
            'ActionDriveScore': element['actionDriveScore'],
            'BenefitCommunicationScore': element['benefitCommunicationScore'],
            'ImprovementSuggestions': element['improvementSuggestions']
        }
        records.append(record)

    return pd.DataFrame(records)

## People functions



# Function to extract data and convert to DataFrame
def extract_human_emotion_data_to_dataframe(human_emotion_json):
    records = []

    # Extract data for each human emotion analysis
    for element in human_emotion_json['humanEmotionAnalysis']:
        for segment in element['timeSegments']:
            record = {
                'AlignmentScore': element['alignmentScore'],
                'Description': element['description'],
                'Emotion': element['emotion'],
                'EngagementScore': element['engagementScore'],
                'NarrativeEnhancementScore': element['narrativeEnhancementScore'],
                'StartTime': segment.split('-')[0],
                'EndTime': segment.split('-')[1],
                'ImprovementSuggestions': element.get('improvementSuggestions', '')
            }
            records.append(record)

    return pd.DataFrame(records)
# Function to extract data and convert to DataFrame
def extract_human_gesture_data_to_dataframe(human_gesture_json):
    records = []

    # Extract data for each human gesture analysis
    for element in human_gesture_json['humanGestureAnalysis']:
        for segment in element['timeSegments']:
            record = {
                'AlignmentScore': element['alignmentScore'],
                'Description': element['description'],
                'Gesture': element['gesture'],
                'EngagementScore': element['engagementScore'],
                'NarrativeEnhancementScore': element['narrativeEnhancementScore'],
                'StartTime': segment.split('-')[0],
                'EndTime': segment.split('-')[1],
                'ImprovementSuggestions': element.get('improvementSuggestions', '')
            }
            records.append(record)

    return pd.DataFrame(records)

# Function to extract data and convert to DataFrame
def extract_human_object_interactions_data_to_dataframe(human_object_interactions_json):
    records = []

    # Extract data for each human-object interaction analysis
    for element in human_object_interactions_json['humanObjectInteractions']:
        for segment in element['timeSegments']:
            record = {
                'AlignmentScore': element['alignmentScore'],
                'Description': element['description'],
                'Interaction': element['interaction'],
                'EngagementScore': element['engagementScore'],
                'NarrativeEnhancementScore': element['narrativeEnhancementScore'],
                'StartTime': segment.split('-')[0],
                'EndTime': segment.split('-')[1],
                'ImprovementSuggestions': element.get('improvementSuggestions', '')
            }
            records.append(record)

    return pd.DataFrame(records)


# Function to extract data and convert to DataFrame
def extract_demographics_data_to_dataframe(demographics_analysis_json):
    records = []

    # Extract data for each demographics analysis
    for element in demographics_analysis_json['demographicsAnalysis']:
        for segment in element['timeSegments']:
            record = {
                'AlignmentScore': element['alignmentScore'],
                'AgeRange': element['demographic']['ageRange'],
                'Gender': element['demographic']['gender'],
                'Description': element['description'],
                'EngagementScore': element['engagementScore'],
                'NarrativeEnhancementScore': element['narrativeEnhancementScore'],
                'StartTime': segment.split('-')[0],
                'EndTime': segment.split('-')[1],
                'ImprovementSuggestions': element.get('improvementSuggestions', '')
            }
            records.append(record)

    return pd.DataFrame(records)

# Function to extract data and convert to DataFrame
def extract_people_interaction_data_to_dataframe(people_interaction_json):
    records = []

    # Extract data for each people interaction analysis
    for element in people_interaction_json['peopleInteractionAnalysis']:
        for segment in element['timeSegments']:
            record = {
                'AlignmentScore': element['alignmentScore'],
                'Description': element['description'],
                'InteractionType': element['interactionType'],
                'EngagementScore': element['engagementScore'],
                'NarrativeEnhancementScore': element['narrativeEnhancementScore'],
                'StartTime': segment.split('-')[0],
                'EndTime': segment.split('-')[1],
                'ImprovementSuggestions': element.get('improvementSuggestions', '')
            }
            records.append(record)

    return pd.DataFrame(records)

# logo Functions ####



# Function to extract data and convert to DataFrame
def extract_logo_analysis_data_to_dataframe(logo_analysis_json):
    records = []

    # Extract data for each logo analysis
    for element in logo_analysis_json['logoAnalysis']:
        record = {
            'BrandAffinityScore': element['brandAffinityScore'],
            'BrandRecallScore': element['brandRecallScore'],
            'Description': element['description'],
            'KeyMoments': ', '.join(element['keyMoments']),
            'Placement': element['placement'],
            'SizeAndProminence': element['sizeAndProminence'],
            'ViewerEngagementScore': element['viewerEngagementScore'],
            'VisibilityDuration': element['visibilityDuration'],
            'ImprovementSuggestions': element.get('improvementSuggestions', '')
        }
        records.append(record)

    return pd.DataFrame(records)

# Function to extract data and convert to DataFrame
def extract_logo_visibility_data_to_dataframe(logo_visibility_json):
    records = []

    # Extract data for logo visibility analysis
    element = logo_visibility_json['logoVisibilityAnalysis']
    record = {
        'BrandAffinityScore': element['brandAffinityScore'],
        'BrandRecallScore': element['brandRecallScore'],
        'Description': element['description'],
        'TotalVisibilityDuration': element['totalVisibilityDuration'],
        'ViewerEngagementScore': element['viewerEngagementScore'],
        'ImprovementSuggestions': element.get('improvementSuggestions', '')
    }
    records.append(record)

    return pd.DataFrame(records)

# Function to extract data and convert to DataFrame
def extract_logo_size_prominence_data_to_dataframe(logo_size_prominence_json):
    records = []

    # Extract data for logo size and prominence analysis
    element = logo_size_prominence_json['logoSizeProminenceAnalysis']
    record = {
        'AverageLogoSize': element['averageLogoSize'],
        'BrandAffinityScore': element['brandAffinityScore'],
        'BrandRecallScore': element['brandRecallScore'],
        'Description': element['description'],
        'ProminenceScore': element['prominenceScore'],
        'ViewerEngagementScore': element['viewerEngagementScore'],
        'ImprovementSuggestions': element.get('improvementSuggestions', '')
    }
    records.append(record)

    return pd.DataFrame(records)

# Function to extract data and convert to DataFrame
def extract_logo_interaction_data_to_dataframe(logo_interaction_json):
    records = []

    # Extract data for each logo interaction analysis
    for element in logo_interaction_json['logoInteractionAnalysis']:
        for segment in element['timeSegments']:
            record = {
                'AssociatedElements': ', '.join(element['associatedElements']),
                'BrandAffinityScore': element['brandAffinityScore'],
                'BrandRecallScore': element['brandRecallScore'],
                'Description': element['description'],
                'InteractionType': element['interactionType'],
                'StartTime': segment.split('-')[0],
                'EndTime': segment.split('-')[1],
                'ViewerEngagementScore': element['viewerEngagementScore'],
                'ImprovementSuggestions': element.get('improvementSuggestions', '')
            }
            records.append(record)

    return pd.DataFrame(records)

# Scene df function

# Function to extract data and convert to DataFrame
def extract_scene_data_to_dataframe(scene_json):
    records = []

    # Extract overall assessment
    overall_record = {
        'Aspect': 'Overall Assessment',
        'EngagementScore': scene_json['overallAssessment']['engagementScore'],
        'StorytellingScore': scene_json['overallAssessment']['storytellingScore'],
        'Description': scene_json['overallAssessment']['summaryDescription']
    }
    records.append(overall_record)

    # Extract data for each scene analysis
    for element in scene_json['sceneAnalysis']:
        record = {
            'Aspect': element['sceneAspect'],
            'Description': element['description'],
            'Score': element['score']
        }
        records.append(record)

    return pd.DataFrame(records)

# Function to extract story archetype and flow
# Function to extract data and convert to DataFrame
def extract_archetype_data_to_dataframe(archetype_json):
    records = []

    # Extract data for each archetype analysis
    for element in archetype_json['archetypeAnalysis']:
        for segment in element['timeSegments']:
            record = {
                'Type': 'Archetype Analysis',
                'Archetype': element['archetype'],
                'Description': element['description'],
                'StartTime': segment.split('-')[0],
                'EndTime': segment.split('-')[1]
            }
            records.append(record)

    # Extract data for each archetype flow
    for element in archetype_json['archetypeFlow']:
        record = {
            'Type': 'Archetype Flow',
            'FromArchetype': element['fromArchetype'],
            'ToArchetype': element['toArchetype'],
            'TransitionDescription': element['transitionDescription'],
            'TransitionSegment': element['transitionSegment']
        }
        records.append(record)

    return pd.DataFrame(records)

# Function to extract data and convert to DataFrame for celebrity and people
def extract_celebrity_data_to_dataframe(celebrity_json):
    records = []

    # Check if 'celebrityIdentification' exists and has data
    if 'celebrityIdentification' in celebrity_json and celebrity_json['celebrityIdentification']:
        # Extract data for each celebrity identification
        for element in celebrity_json['celebrityIdentification']:
            for segment in element.get('timeSegments', []):
                record = {
                    'CelebrityName': element.get('celebrityName', ''),
                    'Description': element.get('description', ''),
                    'StartTime': segment.split('-')[0] if '-' in segment else '',
                    'EndTime': segment.split('-')[1] if '-' in segment else ''
                }
                records.append(record)

    # Return a DataFrame, empty if no records exist
    return pd.DataFrame(records, columns=['CelebrityName', 'Description', 'StartTime', 'EndTime'])

# Function for actor people identification
# Function to extract data and convert to DataFrame
def extract_person_identification_data_to_dataframe(person_identification_json):
    records = []

    # Extract actors
    for actor in person_identification_json['personIdentification']['actors']:
        record = {
            'Type': 'Actor',
            'Description': actor
        }
        records.append(record)

    # Extract celebrities
    for celebrity in person_identification_json['personIdentification']['celebrities']:
        record = {
            'Type': 'Celebrity',
            'Description': celebrity
        }
        records.append(record)

    # Add total people count
    total_people_record = {
        'Type': 'Total People',
        'Description': person_identification_json['personIdentification']['totalPeople']
    }
    records.append(total_people_record)

    return pd.DataFrame(records)

# Emotion context extraction function
# Function to extract data and convert to DataFrame
def extract_context_analysis_data_to_dataframe(context_analysis_json):
    records = []

    # Extract data for each context analysis
    for context in context_analysis_json['contextAnalysis']:
        '''
        record = {
            'Context': context
        }
        '''
        records.append(context)

    return ', '.join(records)

# Object interaction dataframe
# Function to extract data and convert to a single-row DataFrame
def extract_physical_objects_data_to_single_row(physical_objects_json):
    # Extract all physical objects
    objects = []
    activity = []
    for objs in physical_objects_json['allPhysicalObjects']:
        objects.append(objs['object'])
        activity.append(objs['activity'])

        all_physical_objects = ', '.join(objects)
        all_physical_activity = ', '.join(activity)

    # Extract object interactions
    object_interactions = [
        {
            'Interaction': interaction['interaction'],
            'ObjectPair': ', '.join(interaction['objectPair'])
        }
        for interaction in physical_objects_json['objectInteractions']
    ]

    # Convert object interactions to a string representation
    object_interactions_str = '; '.join(
        [f"{item['Interaction']} (Objects: {item['ObjectPair']})" for item in object_interactions]
    )

    # Create a single-row DataFrame
    row_data = {
        'AllPhysicalObjects': all_physical_objects,
        'Activities': all_physical_activity,
        'ObjectInteractions': object_interactions_str
    }

    return pd.DataFrame([row_data])