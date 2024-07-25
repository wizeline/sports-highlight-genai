# Example usage
# subtitles = [
#     {'start_time': 0.0, 'end_time': 2.5, 'text': 'Hello, world!'},
#     {'start_time': 3.0, 'end_time': 6.0, 'text': 'This is an example of an SRT file.'},
#     {'start_time': 7.0, 'end_time': 9.0, 'text': 'Subtitles can be created easily with Python.'}
# ]
def create_srt(subtitles, output_file):
    """
    Creates an .srt file with the given subtitles.
    
    :param subtitles: A list of dictionaries, each containing 'start_time', 'end_time', and 'text'.
    :param output_file: The path to the output .srt file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, subtitle in enumerate(subtitles, start=1):
            f.write(f"{i}\n")
            f.write(f"{format_time(subtitle['start_time'])} --> {format_time(subtitle['end_time'])}\n")
            f.write(f"{subtitle['text']}\n\n")


def format_time(seconds):
    """
    Converts time in seconds to the SRT time format (hh:mm:ss,ms).
    
    :param seconds: Time in seconds.
    :return: Time in SRT format.
    """
    milliseconds = int((seconds % 1) * 1000)
    seconds = int(seconds)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"