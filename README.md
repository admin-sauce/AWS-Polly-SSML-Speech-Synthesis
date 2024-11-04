# AWS Polly & SSML Speech Synthesis

This repository contains an example project for converting text into speech using **AWS Polly** and **SSML (Speech Synthesis Markup Language)**. As part of my **#30DaysCloudChallenge**, I’ve documented how to use SSML tags to customize the pronunciation, pacing, and emphasis of AWS Polly’s text-to-speech output.

## Overview

AWS Polly enables developers to add natural-sounding speech to applications. SSML takes this a step further by allowing fine control over the way Polly reads text, making it perfect for creating lifelike voices in applications.

## Features

- 📢 Text-to-speech conversion using AWS Polly
- ✨ Enhanced control over speech output with SSML tags (e.g., emphasis, spelling, and number formatting)
- 🛠️ Script to easily implement and test SSML with AWS Polly

## Getting Started

### Prerequisites

- **AWS Account** with access to the Polly service
- **AWS CLI** configured with credentials for Polly access
- **Python 3.x** with `boto3` library installed for using AWS SDK

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/aws-polly-ssml-speech-synthesis.git
   cd aws-polly-ssml-speech-synthesis
   ```
2. Install dependencies:
   ```bash
   pip install boto3
   ```

3. Configure AWS CLI for Polly:
   ```bash
   aws configure
   ```

### Usage

1. **Prepare Your SSML File**: Customize the `ssml-example.xml` file with SSML tags such as `<say-as>` and `<emphasis>` to control pronunciation. You can find examples in the `examples/ssml-text-sample.txt`.

2. **Run the Python Script**:
   Use `scripts/polly_ssml_example.py` to convert your SSML text into speech and save it as an MP3 file.
   ```bash
   python scripts/polly_ssml_example.py
   ```

3. **Test the Output**:
   The script will generate an audio file (`audio-output-sample.mp3`) for playback. Adjust SSML tags as needed to refine speech output.
