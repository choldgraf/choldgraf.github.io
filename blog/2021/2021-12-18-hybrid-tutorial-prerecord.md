---
tags: teaching
redirect: 2021-12-18-tutorials-pre-record
date: 2021-12-17
---

# Serving in two roles at once via pre-recorded tutorials

At AGU 2021 this year I was asked to give [a short tutorial introduction to Jupyter Book](https://www.youtube.com/watch?v=lZ2FHTkyaMU).
The tutorial was 30 minutes long, and the session was fully remote.

This posed a few challenges:

- Tutorials almost **always** go over time - particularly if you're taking questions from attendees.
- It is tricky to go back and forth between lecture-style talking and going through steps yourself to make sure that you're not out-pacing the attendees.
- My time working with [the Carpentries](https://carpentries.org/) taught me that having helpers in a tutorial is extremely useful to keep things on track.

So, I decided to try an expriment this time: I'd pre-record my tutorial via Zoom, and then attend the session as a helper. The rest of this post is about my experience!

```{admonition} If you'd like to check out the tutorial

Here's a video of the tutorial in case you're interested!

<iframe width="560" height="315" src="https://www.youtube.com/embed/lZ2FHTkyaMU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

```

## An experiment: record myself ahead of time

Here's what I did:

### Before the session

1. Opened two windows on my screen on top of each other: one window was a Google Slides window with my presentation, the other was a JupyterLab window that I used to demonstrate all of the steps.

   Here's how it looked:

   ```{figure} https://user-images.githubusercontent.com/1839645/146656769-95e0e430-15ac-4b5e-a0ee-7e77e8f7b9ed.png

   My two-window setup in recording the tutorial.

2. In my slides, I included several prompts with explicit text for people to type into their own terminals and text files. I followed the instructions in these slides and typed them into the JupyterLab window myself.

   ```{figure} https://user-images.githubusercontent.com/1839645/146656866-0236e791-9a16-4c60-aa0b-e1ea99e46dd5.png
   Instructions on the top, real-time results on the bottom.
   ```

3. I used Zoom to record myself as I clicked through the slides on the top, and followed along on the bottom as if I were a participant myself.
4. I split the recording into roughly **5 minute sections**.
   I'd stop the recording briefly for each section, take a quick breather, and then move on to recording the next. This ensured that I had a moment to collect myself and if I messed up a section, I'd only have to re-record 5 minutes instead of 30.
5. After the recording, I stitched together each of the sections and did a simple fade-out / fade-in using the built-in [Windows Video Editor](https://support.microsoft.com/en-us/windows/create-films-with-video-editor-94e651f8-a5be-ae03-3c50-e49f013d47f6).

### During the session

During the tutorial, I played the pre-recorded video as the "presenter", but spent my time answering questions and addressing issues via the chat box.
Attendees would watch the pre-recorded video, and speak with me in the chat if anything came up.
This meant that I could address questions in real-time but without breaking up the flow of the tutorial.
If there was a really important question that was worth discussing as a group, I could have stopped the video to bring it up with everyone.

## Thoughts

In all, this worked really nicely!
The biggest downside is that it took a bit of extra time to pre-record the video before the talk itself.
However, I believe I might have actually *saved* time, because pre-recording the talk meant that I didn't feel the need to tinker with my slides in the hours leading up to the talk.

Here are some of the benefits that I noticed:

- I could serve as presenter and assistant in one talk - two roles with one person!
- It gave me more control over the talk length and pacing, because I *knew* how much total time was there.
- By recording it ahead of time, I was "done" with the talk much earlier than I normally am (usually I'm stressing about slides until a few moments before the talk)
- It also meant I had less anxiety before the event itself.

I'll give this another shot the next time I'm giving a remote tutorial (or maybe an in-person tutorial by myself).
In the meantime, I wanted to write up these thoughts while they were fresh in case this might work for somebody else.
