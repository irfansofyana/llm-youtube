# llm-youtube

LLM plugin for extracting content from YouTube videos.

This plugin is inspired by Simon Willison's [llm-hacker-news](https://github.com/simonw/llm-hacker-news) and his excellent [llm](https://github.com/simonw/llm) tool.

## Installation

```bash
llm install llm-youtube
```

## Usage

Passing the video ID

example:

```bash
llm -f yt:zv72WMmVkPw 'Please summarize this video'
```

Passing the Video URL

example:

```bash
llm -f yt:https://www.youtube.com/watch\?v\=zv72WMmVkPw 'Please summarize this video'
```

We can also use a system prompt to improve the result

example:

```bash
llm -f yt:sCr_gb8rdEI --system "You are an expert at analyzing YouTube videos. Extract the key points only, ignore filler content." "What is this video about?"
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

```bash
cd llm-youtube
python -m venv venv
source venv/bin/activate
```

Now install the dependencies:

```bash
pip install -e .
```
