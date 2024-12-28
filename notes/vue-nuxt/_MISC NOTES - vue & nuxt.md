
Solve "hydration mismatch" errors using the `<ClientOnly>` component, or make it a `MyComponent.client.vue` file. 
> ref: lesson 0016 of "Mastering Nuxt 3" course for details


## Pages v. layouts v. components & organizing your code in nuxt


How do you know when to use which one?

One way is to look at the special properties that nuxt gives to each of these types of "components". 
- pages: used to define `rounting`
- layouts: properties to be able to share code between pages
- components: lightweight with no extra behind-the-scenes functionality on them

- first, just get things to work (then get them to work well by refactoring))
- rule of 3: you want to see something happen about 3 times before you refactor/create an abstraction for it.

- components typically do one things
- layouts often do multiple things (...these are starting to sound like what i was calling "sections").


1. default to using pages
2. move common pieces to layouts
	- are there similar styling, sections, etc? pull them out to layouts
3. move smaller pieces to components
	- start by putting things in to a layout and then you can move them to a component later on 
	- are there now different / multiple layouts using the same header? you can refactor this into its own component..


  

## Application Rendering (SSR v. SPA v. Universal)

  

**SSR:**

- initial page load fast (bc only sending small amount of data)

**SPA:**

- You make initial request to visit a page...
- server processes & sends back the entire app as a javascript bundle
- when the bundle is on the browser, the browser processes and renders the app
- slow on initial page load (bc js bundle)
- past on subsequent actions (bc no roundtrips to server) *note:* SPAs do make requests to server, but mainly for raw data -- not for the HTML/CSS to render in thr browser

  

**UNIVERSAL RENDERING:**

- a mix of the best of both SSR+SPA
- fast startup initial page load w/ minimal roundtrips to server (bc initial page load sends only whats needed to render the page, and further data and "full app bundle" is fetched (and even things preloaded) in background while you are already on a rendered page).

  

**HYDRATION**:ß
nuxt/vue docs -> concepts -> hydration
  

- when first go to nuxt app it uses SSR to serve the app and then loads in the app to run on the client side. hydration is the process of going from a static html page served by the server, to a fully interactive js application.

- if you initialize "state" on the server and then want to load the state on the client... you can end up with a 'hydration mismatch' (for example if you start something with a value of "empty" and then the local storage or app or whatever hydrate and show that the state is different, there is now a mismatch between client<-->server)