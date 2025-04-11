import pytest
from unittest.mock import patch
from llm_youtube import youtube_fragment_loader

@pytest.fixture
def mock_transcript_data():
    return [
        {"text": "This is the first line of the transcript.", "duration": 2.5, "start": 0.0},
        {"text": "This is the second line.", "duration": 1.8, "start": 2.5},
        {"text": "And this is the third line of the transcript.", "duration": 3.0, "start": 4.3}
    ]

def test_youtube_fragment_loader(mock_transcript_data):
    video_id = "dQw4w9WgXcQ"
    url = f"https://www.youtube.com/watch?v={video_id}"
    
    # Mock the YouTubeTranscriptApi.get_transcript method
    with patch('llm_youtube.YouTubeTranscriptApi.get_transcript') as mock_get_transcript:
        # Configure the mock to return our test data
        mock_get_transcript.return_value = mock_transcript_data
        
        # Call the function we want to test
        fragment = youtube_fragment_loader(url)
        
        # Assert that the mock was called with the correct video ID
        mock_get_transcript.assert_called_once_with(video_id)
        
        # Assert that the fragment has the expected properties
        assert fragment.source == url
        assert str(fragment) == "This is the first line of the transcript. This is the second line. And this is the third line of the transcript."

def test_youtube_fragment_loader_with_direct_id(mock_transcript_data):
    video_id = "dQw4w9WgXcQ"
    
    # Mock the YouTubeTranscriptApi.get_transcript method
    with patch('llm_youtube.YouTubeTranscriptApi.get_transcript') as mock_get_transcript:
        # Configure the mock to return our test data
        mock_get_transcript.return_value = mock_transcript_data
        
        # Call the function with just the video ID
        fragment = youtube_fragment_loader(video_id)
        
        # Assert that the mock was called with the correct video ID
        mock_get_transcript.assert_called_once_with(video_id)
        
        # Assert that the fragment has the expected properties
        assert fragment.source == f"https://www.youtube.com/watch?v={video_id}"
        assert str(fragment) == "This is the first line of the transcript. This is the second line. And this is the third line of the transcript."