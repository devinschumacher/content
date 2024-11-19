# [**WebRTC**](https://browserleaks.com/webrtc)

WebRTC stands for "Web Real-Time Communications," and it is a set of open-source technologies and standards that enable real-time communication (voice, video, and data) directly between web browsers without requiring any plugins or additional software installations.

WebRTC is built into modern web browsers, including Chrome, Firefox, and Safari, and it uses a combination of JavaScript APIs, HTML, and signaling protocols to establish peer-to-peer connections between browsers.

This allows users to communicate in real-time without needing to install any additional software or plugins.

WebRTC is often used for applications such as video conferencing, voice calling, file sharing, and online gaming.

It supports a range of audio and video codecs, as well as security protocols such as DTLS-SRTP to ensure that all communications are secure and private.

> WebGL is a JavaScript API used to render 3D graphics within a web browser by utilizing the device's GPU. This makes it possible for websites to gather detailed information about a user's graphics card, which can be used to create a unique browser fingerprint.

## How WebRTC can be used to track you

Since WebRTC establishes a connection through a UDP protocol, it is not routed through proxy servers that you may use in a browser. Websites may exploit this fact to reveal your real public and local IP addresses even if you are using a proxy. The same plugin can also be used to reveal your local IP addresses or track your media devices.

### What WebRTC plugin leaks

- Public IP address(es)
- Local IP address(es)
- Media device numbers and hashes (covered on the [Media devices page](https://docs.multilogin.com/l/en/article/dznduwe2jz-media-devices))

