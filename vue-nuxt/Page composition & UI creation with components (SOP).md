
1. Have a starting point
2. Layouts & user interface elements
3. Relationships, the data flow, interactions and events
4. User interactivity elements (inputs, dialogs, notifications, etc.)
5. Design patterns & trade-offs

---

## 1. have a design
Have or make a design starting point (sketch/wireframe/figma design/etc.).

## 2. Layouts & user interface elements

> "How can we represent the layout and multiple elements with components?"

- Should we use columns? sections? navigation menus? islands?
- Are there dialogs or modals?

### 2.1. "slice the page"
1. Take your design file & mark sections w/ rectangles that may represent components, from the outermost down to a singular unit of interaction.
2. Repeat until you have a comfortable amount of components.

![](1.jpg)

### 2.2. extract the relationships
1. After you've identified the components, extract the relationships between them to create a hierarchy from the top-most root component.
2. Name the components

![](2.png)


## 3. Relationships, the data flow, interactions and events

> "How will these components communicate and relate to each other?"

Here we aim to understand the user's interaction with a use-case, user story, etc.

**For each component:** 
1. Decide what information it will hold (the state)
2. What will pass down to its children / need from its parent
3. What events it will trigger
4. Document it in some kind of documentation - scribbles/notes/UML (Universal Modeling Language) diagrams.

![](component-diagram.png)


## 4. User interactivity elements (inputs, dialogs, notifications, etc.)
