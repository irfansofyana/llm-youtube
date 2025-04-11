import llm
from youtube_transcript_api import YouTubeTranscriptApi
import re

@llm.hookimpl
def register_fragment_loaders(register):
    register("youtube", youtube_fragment_loader)

def youtube_fragment_loader(input):
    """
    Load a YouTube transcript as a fragment.

    Format: youtube:VIDEO_ID or youtube:https://www.youtube.com/watch?v=VIDEO_ID
    """
    try:
        # Extract video ID if it's a full URL
        if input.startswith("https://"):
            video_id = extract_video_id(input)
        else:
            video_id = input

        if not video_id:
            raise ValueError(f"Could not extract YouTube video ID from: {input}")

        transcript = fetch_transcript(video_id)
        source = f"youtube:{video_id}"

        return llm.Fragment(transcript, source)
    except Exception as ex:
        raise ValueError(f"Fragment 'youtube:{input}' could not be loaded: {str(ex)}")

def extract_video_id(url):
    """Extract YouTube video ID from a URL."""
    patterns = [
        r'(?:youtube\.com\/watch\?v=|youtu\.be\/)([^&\?\/]+)',
        r'youtube\.com\/embed\/([^\/\?]+)',
        r'youtube\.com\/v\/([^\/\?]+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None

def fetch_transcript(video_id):
    """Fetch transcript from YouTube API."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry["text"] for entry in transcript])
    except Exception as ex:
        raise ValueError(f"Failed to fetch transcript for video ID '{video_id}': {str(ex)}")
    