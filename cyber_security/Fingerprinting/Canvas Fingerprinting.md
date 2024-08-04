# Canvas Fingerprinting

---

Canvas fingerprinting is a specific kind of browser fingerprinting that involves using a “digital canvas” to create a unique identifier to the way your browser has rendered content on a visited page - from fonts to colors, etc.

In HTML5, drawing operations render differently depending on the computer’s software and hardware characteristics. So, when the browser renders the page, code javascript can be run to draw a canvas, and apply different techniques to impact the render.

Anti-aliasing, hinting, and font availability can produce different results depending on your operating system, hardware, and settings Differences in GPU or [graphics drivers](https://eric-diehl.com/fingerprinting-canvas-of-browser/) can further differentiate image output. Drawing background colors and shapes on top of the text can help highlight these differences.

Then, the output from a canvas fingerprint generates a [hash code](https://github.com/artem0/canvas-fingerprinting), which can be stored to identify the user. Though the hash is unique, the same browser should create the same one each time.

