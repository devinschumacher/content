# Audio Fingerprinting

---

Web Audio API is a powerful system for handling audio operations. Designed to work inside an [AudioContext](https://developer.mozilla.org/en-US/docs/Web/API/AudioContext), the Web Audio API links together audio nodes and builds an audio graph. A single AudioContext can handle multiple types of audio sources that plug into other nodes and form chains of audio processing.

A source can be an audio element, a stream, or an in-memory source generated mathematically with an Oscillator. We’ll use the Oscillator for our purposes and then connect it to other nodes for additional processing.

1. A website can embed an audio file or stream into a page that is played silently in the background.
2. The website then uses JavaScript to analyze the audio waveform and extract the unique features to create an audio fingerprint.
3. The audio fingerprint is then combined with other data points, such as the user's browser version, operating system, screen resolution, and installed fonts, to create a browser fingerprint.
4. The browser fingerprint can then be used to identify the user across multiple visits to the website, even if they have cleared their cookies or are using a different IP address.

