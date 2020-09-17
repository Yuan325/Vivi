#project ID: vivi-ysjylu
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/Yuan/Desktop/Files/tensorflow/Vivi/Vivi-fb0a374c6045.json"

def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    import dialogflow_v2 as dialogflow
    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    for text in texts:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        response = session_client.detect_intent(
            session=session, query_input=query_input)

        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))

def detect_intent_with_texttospeech_response(project_id, session_id, texts,
                                             language_code):
    """Returns the result of detect intent with texts as inputs and includes
    the response in an audio format.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    import simpleaudio as sa
    import dialogflow_v2 as dialogflow
    #import pyaudio
    session_client = dialogflow.SessionsClient()

    session_path = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session_path))

    for text in texts:
        text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

        query_input = dialogflow.types.QueryInput(text=text_input)

        # Set the query parameters with sentiment analysis
        output_audio_config = dialogflow.types.OutputAudioConfig(
            audio_encoding=dialogflow.enums.OutputAudioEncoding
            .OUTPUT_AUDIO_ENCODING_LINEAR_16)

        response = session_client.detect_intent(
            session=session_path, query_input=query_input,
            output_audio_config=output_audio_config)

        print('=' * 20)
        print('Query text: {}'.format(response.query_result.query_text))
        print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
        print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))
        
        action = response.query_result.action
        parameter = response.query_result.parameters.fields

        #https://realpython.com/playing-and-recording-sound-python/#pyaudio
        # The response's audio_content is binary.
        with open('output.wav', 'wb') as out:
            out.write(response.output_audio)
            print('Audio content written to file "output.wav"')
        play_obj = sa.WaveObject.from_wave_file('output.wav').play()
        play_obj.wait_done()

        return action, parameter
