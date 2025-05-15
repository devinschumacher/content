
## server side rendering (SSR)

When you visit a web page, a network request is sent from your browser (the client) to a web server (where the website page being requested is being hosted).

The server processes the code associated with that page (HTML, CSS, JavaScript) to render that page and then sends the rendered web page to your browser, so your browser can display it for you.

Ssubsequent page requests (ex: you click on a link to go to another page of the website, or you submit a form, etc.) are also sent to the web server to be processed & returned.

- Initial page load = fast
- Subsequent page visits = slow


## single page application (SPA)

When you visit a web page, a network request is sent from your browser (the client) to a web server (where the website page being requested is being hosted).

The server processes the code associated with that page (HTML, CSS, JavaScript) to create one large JavaScript 'bundle' for the entire application, and sends that to your browser, then your browser performs a bunch of processing of that JavaScript to render the page in your browser.

Subsequent page requests (ex: you click on a link to go to another page of the website, or you submit a form, etc.) are NOT sent to the web server to be processed & returned...they are processed by your browser.

**Note: SPAs DO make requests to servers, however:** 
1. They only make requests to fetch raw data, not the HTML/CSS/JS used in the browser
2. They only make these requests for data needed that is not already included in the initially provided application bundle

- Initial page load = slow
- Subsequent page visits = fast


## Universal Rendering (UR)

Universal rendering is the best of both worlds (SSR + SPA).
Nuxt does this by default.

 When you visit a web page, a network request is sent from your browser (the client) to a web server (where the website page being requested is being hosted).
 
The server processes the code associated with that page (HTML, CSS, JavaScript) to render that page and then sends the rendered web page to your browser, so your browser can display it for you.

While you're on the page, in the background, the server continues to process the app bundle and sends it over without you needing to wait around for it.

- Initial page visit = fast
- Subsequent page visits = fast