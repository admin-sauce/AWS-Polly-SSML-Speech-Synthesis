import boto3
polly_client = boto3.Session().client('polly')

def convert_ssml_to_audio(ssml_text, output_format='mp3', voice_id='Joanna'):
    response = polly_client.synthesize_speech(
        Text=ssml_text,
        OutputFormat=output_format,
        VoiceId=voice_id,
        TextType='ssml'
    )
    return response['AudioStream'].read()

if __name__ == "__main__":
    with open('ssml-example.xml', 'r') as ssml_file:
        ssml_text = ssml_file.read()

    audio_data = convert_ssml_to_audio(ssml_text)

    with open('examples/audio-output-sample.mp3', 'wb') as audio_file:
        audio_file.write(audio_data)
    print("Audio file saved as examples/audio-output-sample.mp3")
