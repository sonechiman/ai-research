from google.cloud import translate


def translate_text(text):
    translate_client = translate.Client()
    target = 'ja'

    translation = translate_client.translate(
        text,
        target_language=target)
    return translation['translatedText']
