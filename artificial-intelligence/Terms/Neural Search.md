Information retrieval technology is one of the main technologies that enabled the modern Internet to exist.

These days, search technology is at the heart of a variety of applications, ranging from web page search to product recommendations.

For many years, this technology didn't see much change, until neural networks came into play.

## What is neural search?

Neural search, also known as neural information retrieval (IR), is an approach to search and information retrieval that leverages deep neural networks to improve the effectiveness of search systems.

Neural search encompasses a wide range of techniques and models, including word embeddings, transformer-based models, and deep learning architectures.

One example of a neural network model used in neural search that you may be familiar with is BERT. 

![](BERT.webp)

No, not him, ya dingus.

[BERT (Bidirectional Encoder Representations from Transformers)](BERT%20(Bidirectional%20Encoder%20Representations%20from%20Transformers).md), as in, Bidirectional Encoder Representations from Transformers - is a deep learning model that is capable of understanding the context of words in a sentence by processing text bidirectionally.

Or, if you're an SEO wizard like myself, you may think about the BERT algorithm update in 2019. Same thing, pretty much.

Historically, language models could only read text input sequentially - either left-to-right or right-to-left - but couldn't do both at the same time.

BERT is different because it is designed to read in both directions at once. This capability, enabled by the introduction of Transformers, is known as bidirectionality.

But we've all used Google in 2019 and beyond and could probably agree that it still needs some work, eh?

Let's take a step back for a second to understand where we've come from, so we may understand where we are now.... Confucious say.


### Symbolic Search

Symbolic search engines, also known as traditional or keyword-based search engines, rely on the use of symbols (such as keywords, terms, or tokens) to index and retrieve information. 

These search engines typically use rule-based algorithms, Boolean logic, and keyword matching to find relevant documents or web pages based on user queries. 

**Examples of symbolic search engines and related technologies include:**

1. Early Web Search Engines: Some of the early web search engines, such as AltaVista, Lycos, and Yahoo! Search, primarily relied on keyword matching and Boolean operators to retrieve relevant web pages. These search engines used simple algorithms to match query terms with the content of web pages.
    
2. SQL Database Search: SQL (Structured Query Language) databases allow users to perform searches using SQL queries that specify conditions based on keywords, attributes, and logical operators. These queries are symbolic in nature, as they rely on the precise matching of terms and conditions.
    
3. Boolean Search: Boolean search is a type of symbolic search that allows users to combine keywords with Boolean operators (AND, OR, NOT) to narrow or broaden search results. Many library databases, academic search engines, and job search platforms offer Boolean search functionality.
    
4. Regular Expression Search: Some search tools allow users to perform searches using regular expressions, which are symbolic patterns that describe specific text strings. Regular expression search is commonly used in text editors, programming environments, and data processing tools.

Google's search engine originally started with an emphasis on keyword matching and link analysis (PageRank), it has evolved significantly over the years to incorporate more advanced algorithms and techniques, including machine learning and natural language understanding.

It's search algorithms now use a combination of methods to understand and rank search results, such as:

1. Keyword Matching: Google still considers the presence and relevance of keywords in a query and in the content of web pages. However, this is just one of many factors that Google uses to determine search results.
    
2. Semantic Understanding: Google uses natural language processing and machine learning algorithms to understand the meaning and context of queries and web pages. This allows Google to better match queries with relevant content, even if the exact keywords are not present.
    
3. User Behavior and Personalization: Google considers user behavior data, such as click-through rates and dwell time, as well as personalization factors, such as location and search history, to provide more relevant search results to individual users.
    
4. Link Analysis: Google's PageRank algorithm, which analyzes the quality and quantity of links pointing to a web page, is one of the factors used to assess the authority and relevance of web pages.
    
5. Machine Learning Algorithms: Google has introduced [Machine Learning](Machine%20Learning.md) algorithms, such as RankBrain, to better understand complex and ambiguous queries. Additionally, BERT (Bidirectional Encoder Representations from Transformers) is used to improve the understanding of natural language in search queries.

However, Google, and other traditional keyword-based search algorithms may not take into account the real meaning of the query and documents, leading to suboptimal search results.

They are also easier to game because they were orginally built on 2 primary factors for their ranking determination: [keywords](https://devinschumacher.com/seo-keywords/) & [backlinks](https://devinschumacher.com/backlinks/).

Plus, not everything is about Google, other businesses need search capabilities too - from ecommerce brands delivering better results (*cough* Amazon *cough*) to hospitals - which may need to pull records from similar patients based on something other than keywords to better understand a diagnosis or treatment options.

Neural search aims to address more of these limitations by using neural network models to capture the semantic relationships between queries and documents, allowing for more accurate and relevant search results. 

## How does neural search work?

Neural search aims to improve information retrieval from queries by focusing on meaning rather than keywords. To achieve this, neural search typically works in two steps:

### Step 1: Encoding

A specially trained neural network encoder converts the query and the searched objects (e.g., documents, images) into a vector representation called embeddings. 

The encoder is trained so that similar objects, such as texts with the same meaning or similar images, receive embeddings that are close to each other in the vector space.

### Step 2: Information Retrieval (IR)

To find objects similar to the query, the system searches for embeddings that are nearest to the query's embedding. 

The most common way to determine the distance between two vectors is to calculate the cosine similarity, which measures the cosine of the angle between the vectors. 

The usual Euclidean distance can also be used, but cosine similarity is often preferred because it accounts for the direction of the vectors and is less sensitive to the curse of dimensionality.

## Benefits of neural search

1. Improved revelance
2. Information in context
3. Natural language understanding
4. Ease of deployment
5. Multimodal Search Capabilities
6. Handling Language Variations
7. Cross-Lingual Search
8. Continuous Learning & Improvement
9. Resilience to Spelling & Grammar Errors
10. Personalized Search Experience
11. Enhanced Recommendations & Query Suggestions
12. Scalability & Efficiency

### Semantic Understanding for Improved Relevance

Neural search engines use deep learning models and vector embeddings to understand the underlying meaning and relationships between words, phrases, and entire documents. 

By representing data as vectors in a high-dimensional space, neural search engines can capture the semantic relationships between data points. 

Similar or related items have embeddings that are close to each other in the vector space, while dissimilar or unrelated items have embeddings that are farther apart.

![](Neural%20search%20recognizes%20semantic%20words%201.png)

This semantic understanding allows neural search engines to:

-  Retrieve more relevant and accurate search results by matching queries with content that is semantically similar, even if the exact keywords are not present.
-   Understand synonyms, paraphrases, and variations in language, providing a more flexible and natural search experience for users.
-   Handle complex and ambiguous queries by interpreting the context and intent behind the user's search.

### Information in Context
Neural search engines are capable of understanding the context in which words and phrases are used. 

This allows them to consider the broader context of a query and retrieve information that is not only relevant to the specific keywords but also aligned with the overall intent and context of the query. 

As a result, users receive search results that are more meaningful and better suited to their needs.

### Natural Language Understanding
Neural search engines excel at Natural Language Understanding (NLU), allowing them to interpret queries that are phrased in everyday language. 

This makes it possible for users to interact with the search engine using conversational language, complex questions, or ambiguous queries. 

Neural search engines can interpret and respond to such queries effectively, enhancing the overall user experience.

### Ease of Deployment
With the availability of pre-trained neural network models and frameworks, deploying a neural search engine has become more accessible.

Developers can take advantage of existing models, such as BERT, and fine-tune them for specific use cases. 

We created V3CTRON for both developers and non-developers to have free access to their own personal vector database & neural search engine.

### Multimodal Search Capabilities

"Multimodal", or Modalities" refer to different types or forms of data that can be processed, analyzed, and understood by a system. 

Each modality represents a distinct way of capturing and representing information. Common modalities include:

1.  Text: Written or typed language, including documents, articles, social media posts, and search queries.
    
2.  Images: Visual data in the form of digital photographs, illustrations, diagrams, and scanned documents.
    
3.  Videos: Moving images or sequences of images, often accompanied by audio, representing dynamic visual content.
    
4.  Audio: Sound data, including speech, music, environmental sounds, and audio recordings.
    
5.  3D Data: Three-dimensional representations of objects or scenes, often used in computer graphics, virtual reality, and computer-aided design.
    
6.  Sensor Data: Data collected from sensors, such as temperature, humidity, pressure, and motion sensors, used in various applications like the Internet of Things (IoT) and wearable devices.
    
A multimodal system, like a neural search engine, is one that can handle and integrate data from multiple modalities. 

For example, a multimodal search engine might allow users to submit queries using text, images, or voice and retrieve relevant results across different types of content, such as web pages, images, videos, and audio files. 

By leveraging information from different modalities, multimodal systems can provide richer and more comprehensive insights and interactions.

This flexibility enhances the search experience and opens up new possibilities for information retrieval.

### Handling Language Variations

Neural search engines are effective at handling variations in language, including synonyms, slang, abbreviations, and different dialects. 

For example, it can recognize synonyms (e.g., "car" and "automobile"), slang (e.g., "cool" and "awesome"), abbreviations (e.g., "TV" and "television"), and different dialects or regional language variations. 

The focus here is on understanding different ways of expressing similar meanings within the same language.

By understanding the semantic meaning of words and phrases, neural search engines can recognize when different terms have similar meanings and provide relevant results even when the query language varies.

### Cross-Lingual Search

Neural search engines can be trained to understand and retrieve content in multiple languages, enabling cross-lingual search capabilities. 

This capability refers to the ability of a neural search engine to understand and retrieve content across multiple languages. 

For example, a user might submit a query in English and retrieve relevant results in French, Spanish, or Chinese. 

The focus here is on bridging the language barrier between queries and content in different languages, making information accessible to a global audience.

### Continuous Learning & Improvement

Neural search engines can continuously learn and improve over time through retraining and fine-tuning. 

As new data becomes available and user behavior patterns change, neural search engines can adapt and update their models to maintain and enhance their performance. 

This continuous learning capability ensures that the search engine remains effective and relevant in a dynamic and evolving information landscape.

### Resilience to Spelling & Grammar Errors

Neural search engines are often more robust to spelling and grammar errors in queries compared to traditional keyword-based search engines. 

By understanding the semantic meaning of words and phrases, neural search engines can often infer the user's intent even when the query contains typos or grammatical mistakes, providing relevant results despite the errors.

### Personalized Search Experience

Some neural search engines can leverage user behavior data, preferences, and search history to provide a more personalized search experience. 

By understanding individual users' preferences and interests, neural search engines can tailor search results to better meet the needs of each user, enhancing the overall search experience.

### Enhanced Recommendations & Query Suggestions

Neural search engines can provide enhanced recommendations and query suggestions by understanding the semantic relationships between queries, documents, and user behavior. 

For example, a neural search engine might suggest related queries or topics based on the user's current search, helping users explore information more effectively.

### Scalability & Efficiency

Neural search engines can efficiently handle large volumes of data by representing queries and documents as compact vector embeddings. 

This representation allows for efficient similarity-based retrieval and ranking of search results, even in large-scale information retrieval systems.

It's important to note that the specific benefits and capabilities of a neural search engine will depend on its design, implementation, and the underlying models and algorithms used. 

Additionally, while neural search offers many advantages, it may not be the best solution for all use cases, and traditional keyword-based search engines may still be preferred in certain scenarios.

## How vectors play a role in neural search

Vectors play a central role in neural search by enabling the representation and comparison of complex data in a way that captures semantic meaning. 

In neural search, data—whether it be text, images, audio, or other modalities—is transformed into numerical vector representations known as embeddings. 

These embeddings are generated using neural network models trained on large datasets. 

The process of converting data into vector embeddings is often referred to as encoding.

### Representing Data as Vectors

In neural search, each data point (e.g., a word, sentence, image, or audio clip) is represented as a point in a high-dimensional vector space. 

The position of the point in this space is determined by its vector embedding. 

The goal of the encoding process is to generate embeddings such that similar or related data points have embeddings that are close to each other in the vector space, while dissimilar or unrelated data points have embeddings that are farther apart.

For example, in the case of text data, words or sentences with similar meanings should have vector embeddings that are close together in the vector space. 

Similarly, for image data, images with similar visual content should have similar vector embeddings.

### Retrieving and Ranking Results

Once data is represented as vectors, neural search engines can efficiently retrieve and rank search results based on the similarity between the vector embeddings of the query and the items in the search index. 

Similarity is typically measured using metrics such as cosine similarity or Euclidean distance.

When a user submits a query, the neural search engine first converts the query into its vector representation using the same encoding process. 

It then compares the query's vector to the vectors of items in the search index to find the items that are most similar to the query. 

The search engine ranks the results based on their similarity scores and returns the most relevant items to the user.

## Neural search engines

A neural search engine is a search engine that uses deep learning techniques to carry out its core functions.

For any search engine there are three primary components: 

1. indexer
2. query processor
3. ranking algorithm

Unlike traditional search engines, which develop these components separately using heuristic or rule-based approaches, a neural search engine designs all three components using deep learning methodologies.

Deep learning in search engines has several advantages. 

First, it allows for the holistic training of the entire system, potentially leading to increased overall effectiveness. 

Second, the integration of all components within a single deep learning framework allows for seamless information exchange between the components, which contributes to improved performance. 

Finally, the unified deep learning framework enables the development of diverse neural search engines, such as those dedicated to image or video searches, which can be especially useful in fields where multimodal data is critical.