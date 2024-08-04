# Passive OS fingerprint masking (TCP/IP Fingerprint)

It's possible to detect an operating system of a device by analyzing its network traffic. Different implementations of the TCP/IP stack in operating systems help to determine which OS generated the package.

In this context, a set of operating system-specific package parameters is called an OS fingerprint. Since this method involves observing passing traffic without sending any requests, it is called passive OS fingerprinting.

You can check this fingerprint on [browserleaks.com/ip](https://browserleaks.com/ip) under "TCP/IP Fingerprint". In Multilogin you may encounter the following results:

- A proxy server intercepts your network packages and repacks them, that's why if you use a proxy, the above test may show an OS different from your original one (for example, Linux)
- If you use Multilogin on a VM, the above test may show your original OS regardless of the OS selected in the [profile settings](https://docs.multilogin.com/l/en/article/ymlhur08ng-forbid-multi-start) (for example, if your original OS is macOS, the TCP/IP Fingerprint may show macOS even on a Windows VM with a Windows browser profile)

TCP/IP fingerprint is a connection fingerprint, and Multilogin cannot affect it in any way. Websites for the most part ignore this parameter, since mismatches between TCP/IP Fingerprint and actual OS are common in normal traffic.

They are caused by certain network devices and configurations.

Nevertheless, it's possible to mask this fingerprint on the proxy level by using services that specifically provide this type of masking solution – for example, [iproxy.online](https://multilogin.com/partners/iproxy-online/).

