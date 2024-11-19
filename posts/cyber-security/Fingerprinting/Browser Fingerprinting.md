# Browser Fingerprinting

# Browser Fingerprinting

---

- **Types of Browser Fingerprinting:**

   [Canvas Fingerprinting](https://www.notion.so/Canvas-Fingerprinting-824fb07d9ef1440e9868e7f89e7d45ac)

   [Audio Fingerprinting](https://www.notion.so/Audio-Fingerprinting-cdd3512dbf714878a507c4781705c88d)

   [Font Fingerprinting](https://www.notion.so/Font-Fingerprinting-cf1c55ba022e4ec0a1a88bb0c93e4f13)

   [IP Address Fingerprints](https://www.notion.so/IP-Address-Fingerprints-22f5d4518880487c959a41ff79541ec1)

   [WebRTC Leak](https://browserleaks.com/webrtc)s

---

Browsers have a lot of information that might seem trivial but can be used to create a fingerprint to identify people with high accuracy.

This is known as a [browser fingerprint](https://fingerprint.com/blog/browser-fingerprinting-techniques/?utm_source=blog&utm_medium=website&utm_campaign=blog), and statistics show that if you put this information together, your browser fingerprint will only match [1 in 286,777](https://pixelprivacy.com/resources/browser-fingerprinting/) others.

[Browser fingerprinting](https://fingerprint.com/blog/browser-fingerprinting-techniques/?utm_source=blog&utm_medium=website&utm_campaign=blog) works by reading browser attributes and combining them into a single identifier removing the need for cookies or asking for permission. This identifier is stateless and works well in normal and incognito modes to identify users uniquely and their associate sessions regardless of anonymizing tactics like incognito browsing, VPNs, and cookie blockers.

Fingerprinting takes in data from the browser to help build a unique profile for each user on your site. By capturing the following specifics, fingerprinting software can identify suspicious traffic without an IP address or cookie

In addition, unlike third-party cookies which can be cleared or blocked by the browser. you cannot alter your browser fingerprint.

## Here’s a list of things data points that can be used to create a unique profile of you online:

1. Installed fonts
2. Audio fingerprinting
3. WebGL fingerprinting (graphics card and driver information)
4. Battery level (on mobile devices)
5. Mouse movements and clicks
6. Browser plugins and their versions
7. User agent string
8. HTTP headers
9. Cookies and local storage
10. Network information (IP address, MAC address, ISP, etc.)
11. Installed applications and their versions
12. Canvas fingerprinting (browser rendering of a 2D image)
13. Touchscreen capabilities (on mobile devices)
14. Device orientation (on mobile devices)
15. Device motion (on mobile devices)
16. Media devices (camera and microphone)
17. Time spent on page
18. Navigation history
19. WebGL renderer
20. Browser language
21. Installed browser themes
22. Time zone offset
23. Browser and device colors
24. TCP/IP fingerprinting
25. CSS media queries
26. Web storage features and limits
27. IndexedDB support
28. Battery charging status (on mobile devices)
29. System fonts
30. Installed language packs
31. Use of private browsing mode
32. User account status (e.g. logged in or not)
33. Do Not Track header
34. Audio and video codecs supported
35. System locale
36. Network speed and connectivity
37. Hardware vendor ID
38. WebGL capabilities (extensions and features)
39. Device memory and storage
40. Browser history
41. User agent HTTP header customization
42. Use of a VPN or proxy
43. Browser fingerprinting resistance (such as the use of anti-fingerprinting add-ons)
44. Operating system architecture
45. CPU class and clock speed
46. Number of CPU cores
47. Hardware acceleration capabilities
48. Flash version
49. Java version
50. Silverlight version
51. Device type (laptop, tablet, phone, etc.)
52. Screen orientation
53. Network latency and jitter
54. Active browser tab and its URL
55. Installed applications (e.g. Adobe Acrobat Reader, Microsoft Office)
56. Browser tab order and navigation history
57. Use of touch events (on mobile devices)
58. Pointer events (on touchscreens)
59. WebRTC fingerprinting
60. Geolocation support
61. Time since last system reboot
62. Use of a second monitor or display
63. GPU vendor and model
64. Use of CSS filters and animations
65. Device camera resolution (on mobile devices)
66. Battery health (on mobile devices)
67. Use of device sensors (such as accelerometers or gyroscopes)
68. SSL/TLS settings and features.
69. WebGL shader language version
70. WebGL vendor
71. WebGL renderer string
72. WebGL driver strings
73. WebGL max texture size
74. WebGL max cube map texture size
75. WebGL max render buffer size
76. WebGL max vertex attribs
77. WebGL max texture image units
78. WebGL max draw buffers
79. WebGL compressed texture formats
80. WebGL antialiasing support
81. WebGL stencil buffer support
82. WebGL depth buffer support
83. WebGL multiple render targets support
84. WebGL float texture support
85. WebGL half float texture support
86. WebGL standard derivatives support
87. WebGL float fragment shader support
88. WebGL depth texture support
89. WebGL instanced arrays support
90. WebGL OES texture float support
91. WebGL OES texture half float support
92. WebGL OES texture half float linear support
93. WebGL OES standard derivatives support
94. WebGL OES vertex array object support
95. WebGL OES element index uint support
96. WebGL OES texture float linear support
97. WebGL ANGLE instanced arrays support
98. WebGL ANGLE depth texture support
99. WebGL ANGLE OES texture half float support
100. WebGL ANGLE OES texture half float linear support
101. WebGL ANGLE OES standard derivatives support
102. WebGL ANGLE OES vertex array object support
103. WebGL ANGLE OES element index uint support
104. WebGL ANGLE OES texture float linear support
105. WebGL extensions
106. System disk drives and sizes
107. Screen orientation (portrait or landscape)
108. Screen size and pixel density
109. System and device time and date
110. Installed browser themes and skins
111. Open database sizes
112. Installed browser toolbars and add-ons
113. Installed browser and system fonts
114. Maximum HTTP request header size
115. Maximum HTTP response header size
116. Installed printer types
117. Installed network adapters and their configurations
118. Installed network services and their configurations
119. Installed email clients and their configurations
120. Installed PDF readers and their configurations
121. Installed multimedia codecs and their configurations
122. Installed font rendering libraries and their configurations
123. Installed image libraries and their configurations
124. Installed video capture devices and their configurations
125. Installed audio capture devices and their configurations
126. Available language support for speech recognition
127. Available language support for text-to-speech
128. Device battery status and level (on mobile devices)
129. Device accelerometer readings (on mobile devices)
130. Device gyroscope readings (on mobile devices)
131. Device magnetometer readings (on mobile devices)
132. Device compass readings (on mobile devices)
133. Device light sensor readings (on mobile devices)
134. Device proximity sensor readings (on mobile devices)
135. Device ambient temperature readings (on mobile devices)
136. Device barometer readings (on mobile devices)
137. Device GPS location data (on mobile devices)
138. Device altitude readings (on mobile devices)
139. Device speed readings (on mobile devices)
140. Device step counter readings (on mobile devices)
141. Device heart rate sensor readings (on mobile devices)
142. Available Wi-Fi networks and their configurations (on mobile devices)
143. Bluetooth device information (on mobile devices)
144. Device display information (on mobile devices)
145. Device volume and mute settings (on mobile devices)
146. Device ringer mode (on mobile devices)
147. Device network operator and signal strength (on mobile devices)
148. Device SIM card information (on mobile devices)
149. Available NFC

[**Fingerprint**](https://fingerprint.com/) **is 99.5% accurate** at identifying returning users and assigning them a unique visitorID. You can use this ID to associate fraud patterns with specific visitors and block them as needed.

