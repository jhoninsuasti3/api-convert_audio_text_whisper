import whisper
from pydub import AudioSegment

def tranform_format_audio_to_mp3(input_path):
    """Convierte un archivo OGG a MP3 usando pydub."""
    output_path_audio = 'media/{input_path}.mp3'
    try:
        # Convertir el archivo OGG a MP3
        audio = AudioSegment.from_ogg(input_path)
        audio.export(output_path, format="mp3")
        print("Conversión completada.")
    except Exception as e:
        print("Error to convert audio mp3")

    return "Test"

def convert_audio_to_text(input_audio):
    model = whisper.load_model("base")
    result = model.transcribe(input_audio)
    print("Audio transcrito")
    return(result["text"])


def main(ogg_file, mp3_file):
    # Convertir OGG a MP3
    file = input("Ingrese el nombre del archivo: ")
    tranform_format_audio_to_mp3(file)
    convert_audio_to_text()

if __name__ == "__main__":
    main()    
    




