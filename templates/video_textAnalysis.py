'''
Script for prompt configurations for text and CTA
'''

video_cta_tone_analysis_prompt_system = (
    "You are an advanced video analytics system specialized in analyzing the tone of Call-to-Actions (CTAs) in video advertisements. "
    "Your task is to categorize the tone of the CTA, evaluate the type of response it elicits from viewers, and assess its effectiveness in driving action and communicating product benefits."
    "\n\n"
    "Specifically, you will:\n"
    "1. **Tone and Response Analysis**:\n"
    "   - Identify the tone of the CTA (e.g., persuasive, emotional, urgent, informational, inspiring, etc.).\n"
    "   - Categorize the type of response elicited by the tone (e.g., curiosity, excitement, trust, motivation, etc.)."
    "\n\n"
    "2. **Effectiveness Assessment**:\n"
    "   - Assess how well the tone drives user action and provide an objective score between 1 and 10.\n"
    "   - Evaluate how effectively the tone communicates the product benefits and provide an objective score between 1 and 10."
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the tone of the CTA can be improved, provide actionable suggestions to make it more effective in driving action or communicating benefits."
    "\n\n"
    "Return your analysis in a structured JSON format with fields for 'ctaToneAnalysis'."
)
video_cta_tone_analysis_response_schema = {
    "type": "object",
    "properties": {
        "ctaToneAnalysis": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "ctaTone": {"type": "string"},  # Tone of the CTA (e.g., persuasive, emotional, etc.)
                    "responseType": {
                        "type": "string"  # Type of viewer response elicited (e.g., curiosity, trust, etc.)
                    },
                    "actionDriveScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for driving user action
                    },
                    "benefitCommunicationScore": {
                        "type": "number",
                        "minimum": 1,
                        "maximum": 10  # Score for communicating product benefits
                    },
                    "improvementSuggestions": {
                        "type": "string"  # Suggestions for improving the tone of the CTA
                    }
                },
                "required": [
                    "ctaTone",
                    "responseType",
                    "actionDriveScore",
                    "benefitCommunicationScore"
                ]
            }
        }
    },
    "required": ["ctaToneAnalysis"]
}
video_cta_tone_analysis_prompt = (
    "You are an advanced video analytics system tasked with analyzing the tone of Call-to-Actions (CTAs) in video advertisements."
    "\n\n"
    "Analyze the video content and provide the following insights:\n"
    "1. **Tone and Response Analysis**:\n"
    "   - Identify the tone of the CTA (e.g., persuasive, emotional, urgent, informational, inspiring, etc.).\n"
    "   - Describe the type of viewer response elicited by the tone (e.g., curiosity, excitement, trust, motivation, etc.)."
    "\n\n"
    "2. **Effectiveness Assessment**:\n"
    "   - Rate how effectively the tone drives user action on a scale of 1 to 10.\n"
    "   - Rate how effectively the tone communicates product benefits on a scale of 1 to 10."
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the tone of the CTA can be improved, provide actionable suggestions to make it more impactful for driving user action and communicating product benefits."
    "\n\n"
    "Provide your analysis in JSON format with the following structure:\n"
    "- 'ctaToneAnalysis': A list of tones, the types of responses elicited, scores for action-driving effectiveness, scores for benefit communication, and improvement suggestions (if any)."
)

# Product benefits

video_product_benefit_analysis_response_schema = {
    "type": "object",
    "properties": {
        "productBenefitAnalysis": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "object",
                    "properties": {
                        "benefits": {
                            "type": "array",
                            "items": {"type": "string"}  # List of product benefits conveyed through text
                        },
                        "clarityScore": {
                            "type": "number",
                            "minimum": 1,
                            "maximum": 10  # Score for clarity of product benefits in text
                        },
                        "actionDriveScore": {
                            "type": "number",
                            "minimum": 1,
                            "maximum": 10  # Score for effectiveness in driving user action
                        },
                        "improvementSuggestions": {
                            "type": "string"  # Suggestions for improving text-based communication of benefits
                        }
                    },
                    "required": ["benefits", "clarityScore", "actionDriveScore"]
                },
                "audio": {
                    "type": "object",
                    "properties": {
                        "benefits": {
                            "type": "array",
                            "items": {"type": "string"}  # List of product benefits conveyed through audio
                        },
                        "clarityScore": {
                            "type": "number",
                            "minimum": 1,
                            "maximum": 10  # Score for clarity of product benefits in audio
                        },
                        "actionDriveScore": {
                            "type": "number",
                            "minimum": 1,
                            "maximum": 10  # Score for effectiveness in driving user action
                        },
                        "improvementSuggestions": {
                            "type": "string"  # Suggestions for improving audio-based communication of benefits
                        }
                    },
                    "required": ["benefits", "clarityScore", "actionDriveScore"]
                }
            },
            "required": ["text", "audio"]
        }
    },
    "required": ["productBenefitAnalysis"]
}
video_product_benefit_analysis_prompt_system = (
    "You are an advanced video analytics system specialized in analyzing how product benefits are communicated through text and audio in video advertisements. "
    "Your task is to assess the clarity and effectiveness of product benefits presented in both textual and audio formats, and evaluate how well these representations drive user action."
    "\n\n"
    "Specifically, you will:\n"
    "1. **Text Analysis**:\n"
    "   - Identify the product benefits conveyed through text in the video.\n"
    "   - Evaluate the clarity and representation of these product benefits.\n"
    "   - Rate how effectively the text drives user action on a scale of 1 to 10."
    "\n\n"
    "2. **Audio Analysis**:\n"
    "   - Identify the product benefits conveyed through audio (e.g., voiceovers, sound cues).\n"
    "   - Evaluate the clarity and representation of these product benefits.\n"
    "   - Rate how effectively the audio drives user action on a scale of 1 to 10."
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the product benefits in text or audio can be improved, provide actionable suggestions to enhance their clarity and impact."
    "\n\n"
    "Return your analysis in a structured JSON format with fields for 'productBenefitAnalysis'."
)
video_product_benefit_analysis_prompt = (
    "You are an advanced video analytics system tasked with analyzing how product benefits are communicated through text and audio in video advertisements."
    "\n\n"
    "Analyze the video content and provide the following insights:\n"
    "1. **Text Analysis**:\n"
    "   - Identify the product benefits conveyed through text.\n"
    "   - Evaluate the clarity and representation of these product benefits.\n"
    "   - Rate how effectively the text drives user action on a scale of 1 to 10."
    "\n\n"
    "2. **Audio Analysis**:\n"
    "   - Identify the product benefits conveyed through audio (e.g., voiceovers, sound cues).\n"
    "   - Evaluate the clarity and representation of these product benefits.\n"
    "   - Rate how effectively the audio drives user action on a scale of 1 to 10."
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the product benefits in text or audio can be improved, provide actionable suggestions to enhance their clarity and impact."
    "\n\n"
    "Provide your analysis in JSON format with the following structure:\n"
    "- 'productBenefitAnalysis': A detailed analysis of product benefits in text and audio, including clarity scores, action-driving effectiveness scores, and suggestions for improvement (if any)."
)

# Product claims
video_product_claim_analysis_response_schema = {
    "type": "object",
    "properties": {
        "productClaimAnalysis": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "object",
                    "properties": {
                        "claims": {
                            "type": "array",
                            "items": {"type": "string"}  # List of product claims conveyed through text
                        },
                        "clarityScore": {
                            "type": "number",
                            "minimum": 1,
                            "maximum": 10  # Score for clarity of product claims in text
                        },
                        "credibilityScore": {
                            "type": "number",
                            "minimum": 1,
                            "maximum": 10  # Score for credibility of product claims in text
                        },
                        "actionDriveScore": {
                            "type": "number",
                            "minimum": 1,
                            "maximum": 10  # Score for effectiveness in driving user action
                        },
                        "improvementSuggestions": {
                            "type": "string"  # Suggestions for improving text-based communication of claims
                        }
                    },
                    "required": ["claims", "clarityScore", "credibilityScore", "actionDriveScore"]
                },
                "audio": {
                    "type": "object",
                    "properties": {
                        "claims": {
                            "type": "array",
                            "items": {"type": "string"}  # List of product claims conveyed through audio
                        },
                        "clarityScore": {
                            "type": "number",
                            "minimum": 1,
                            "maximum": 10  # Score for clarity of product claims in audio
                        },
                        "credibilityScore": {
                            "type": "number",
                            "minimum": 1,
                            "maximum": 10  # Score for credibility of product claims in audio
                        },
                        "actionDriveScore": {
                            "type": "number",
                            "minimum": 1,
                            "maximum": 10  # Score for effectiveness in driving user action
                        },
                        "improvementSuggestions": {
                            "type": "string"  # Suggestions for improving audio-based communication of claims
                        }
                    },
                    "required": ["claims", "clarityScore", "credibilityScore", "actionDriveScore"]
                }
            },
            "required": ["text", "audio"]
        }
    },
    "required": ["productClaimAnalysis"]
}


video_product_claim_analysis_prompt_system = (
    "You are an advanced video analytics system specialized in analyzing how product claims are communicated through text and audio in video advertisements. "
    "Your task is to assess the clarity, credibility, and effectiveness of product claims presented in both textual and audio formats, and evaluate how well these representations drive user action."
    "\n\n"
    "Specifically, you will:\n"
    "1. **Text Analysis**:\n"
    "   - Identify the product claims conveyed through text in the video.\n"
    "   - Evaluate the clarity, credibility, and representation of these claims.\n"
    "   - Rate how effectively the text drives user action on a scale of 1 to 10."
    "\n\n"
    "2. **Audio Analysis**:\n"
    "   - Identify the product claims conveyed through audio (e.g., voiceovers, sound cues).\n"
    "   - Evaluate the clarity, credibility, and representation of these claims.\n"
    "   - Rate how effectively the audio drives user action on a scale of 1 to 10."
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the product claims in text or audio can be improved, provide actionable suggestions to enhance their clarity, credibility, and impact."
    "\n\n"
    "Return your analysis in a structured JSON format with fields for 'productClaimAnalysis'."
)
video_product_claim_analysis_prompt = (
    "You are an advanced video analytics system tasked with analyzing how product claims are communicated through text and audio in video advertisements."
    "\n\n"
    "Analyze the video content and provide the following insights:\n"
    "1. **Text Analysis**:\n"
    "   - Identify the product claims conveyed through text.\n"
    "   - Evaluate the clarity, credibility, and representation of these claims.\n"
    "   - Rate how effectively the text drives user action on a scale of 1 to 10."
    "\n\n"
    "2. **Audio Analysis**:\n"
    "   - Identify the product claims conveyed through audio (e.g., voiceovers, sound cues).\n"
    "   - Evaluate the clarity, credibility, and representation of these claims.\n"
    "   - Rate how effectively the audio drives user action on a scale of 1 to 10."
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the product claims in text or audio can be improved, provide actionable suggestions to enhance their clarity, credibility, and impact."
    "\n\n"
    "Provide your analysis in JSON format with the following structure:\n"
    "- 'productClaimAnalysis': A detailed analysis of product claims in text and audio, including clarity scores, credibility scores, action-driving effectiveness scores, and suggestions for improvement (if any)."
)

# Product features
video_product_feature_analysis_response_schema = {
    "type": "object",
    "properties": {
        "productFeatureAnalysis": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "object",
                    "properties": {
                        "features": {
                            "type": "array",
                            "items": {"type": "string"}  # List of product features conveyed through text
                        },
                        "clarityScore": {
                            "type": "number",
                            "minimum": 1,
                            "maximum": 10  # Score for clarity of product features in text
                        },
                        "comprehensivenessScore": {
                            "type": "number",
                            "minimum": 1,
                            "maximum": 10  # Score for comprehensiveness of product features in text
                        },
                        "actionDriveScore": {
                            "type": "number",
                            "minimum": 1,
                            "maximum": 10  # Score for effectiveness in driving user action
                        },
                        "improvementSuggestions": {
                            "type": "string"  # Suggestions for improving text-based communication of features
                        }
                    },
                    "required": ["features", "clarityScore", "comprehensivenessScore", "actionDriveScore"]
                },
                "audio": {
                    "type": "object",
                    "properties": {
                        "features": {
                            "type": "array",
                            "items": {"type": "string"}  # List of product features conveyed through audio
                        },
                        "clarityScore": {
                            "type": "number",
                            "minimum": 1,
                            "maximum": 10  # Score for clarity of product features in audio
                        },
                        "comprehensivenessScore": {
                            "type": "number",
                            "minimum": 1,
                            "maximum": 10  # Score for comprehensiveness of product features in audio
                        },
                        "actionDriveScore": {
                            "type": "number",
                            "minimum": 1,
                            "maximum": 10  # Score for effectiveness in driving user action
                        },
                        "improvementSuggestions": {
                            "type": "string"  # Suggestions for improving audio-based communication of features
                        }
                    },
                    "required": ["features", "clarityScore", "comprehensivenessScore", "actionDriveScore"]
                }
            },
            "required": ["text", "audio"]
        }
    },
    "required": ["productFeatureAnalysis"]
}


video_product_feature_analysis_prompt_system = (
    "You are an advanced video analytics system specialized in analyzing how product features are communicated through text and audio in video advertisements. "
    "Your task is to assess the clarity, comprehensiveness, and effectiveness of product features presented in both textual and audio formats, and evaluate how well these representations drive user action."
    "\n\n"
    "Specifically, you will:\n"
    "1. **Text Analysis**:\n"
    "   - Identify the product features conveyed through text in the video.\n"
    "   - Evaluate the clarity, comprehensiveness, and representation of these features.\n"
    "   - Rate how effectively the text drives user action on a scale of 1 to 10."
    "\n\n"
    "2. **Audio Analysis**:\n"
    "   - Identify the product features conveyed through audio (e.g., voiceovers, sound cues).\n"
    "   - Evaluate the clarity, comprehensiveness, and representation of these features.\n"
    "   - Rate how effectively the audio drives user action on a scale of 1 to 10."
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the product features in text or audio can be improved, provide actionable suggestions to enhance their clarity, comprehensiveness, and impact."
    "\n\n"
    "Return your analysis in a structured JSON format with fields for 'productFeatureAnalysis'."
)

video_product_feature_analysis_prompt = (
    "You are an advanced video analytics system tasked with analyzing how product features are communicated through text and audio in video advertisements."
    "\n\n"
    "Analyze the video content and provide the following insights:\n"
    "1. **Text Analysis**:\n"
    "   - Identify the product features conveyed through text.\n"
    "   - Evaluate the clarity, comprehensiveness, and representation of these features.\n"
    "   - Rate how effectively the text drives user action on a scale of 1 to 10."
    "\n\n"
    "2. **Audio Analysis**:\n"
    "   - Identify the product features conveyed through audio (e.g., voiceovers, sound cues).\n"
    "   - Evaluate the clarity, comprehensiveness, and representation of these features.\n"
    "   - Rate how effectively the audio drives user action on a scale of 1 to 10."
    "\n\n"
    "3. **Improvement Suggestions**:\n"
    "   - If the product features in text or audio can be improved, provide actionable suggestions to enhance their clarity, comprehensiveness, and impact."
    "\n\n"
    "Provide your analysis in JSON format with the following structure:\n"
    "- 'productFeatureAnalysis': A detailed analysis of product features in text and audio, including clarity scores, comprehensiveness scores, action-driving effectiveness scores, and suggestions for improvement (if any)."
)
