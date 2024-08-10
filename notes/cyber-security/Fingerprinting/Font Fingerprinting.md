# Font Fingerprinting

Font fingerprinting techniques rely on measuring the dimensions of HTML elements filled with text or single Unicode glyphs. However, font rendering in web browsers can be affected by multiple factors, leading to subtle differences in these measurements.

The Fonts Enumeration attack is a brute-force method that tries different fonts from a dictionary of known typefaces. By comparing the rendered element's size with default values, this attack can determine whether the substituted font is present on the system.

The Unicode Glyphs Measurement technique uses special Unicode characters with a large font size and default letterforms as a font-family to create fingerprints by hashing the obtained measurement results.

Give it a try: [https://browserleaks.com/fonts](https://browserleaks.com/fonts)

