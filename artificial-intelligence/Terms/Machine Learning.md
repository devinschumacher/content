Machine learning is the process where computers learn to make decisions from data without being explicitly programmed.

For example, learning to predict whether an email is spam or not spam given its content and sender.

Or learning to cluster books into different categories based on the words they contain, then assigning any new book to one of the existing clusters.

Let's a step back to understand this better.

## Exploring the Machine Learning Landscape

Traditionally, computers must have everything explicitly defined in order to perform a task.

This means every possible scenario the program may encounter must be pre-programmed by a human.

The program will only be able to execute tasks based on these pre-defined rules. If the program encounters something it hasn't been pre-programmed to deal with - it will not be able to continue operating.

There's no room for "improvisation", "learning on the job" or any "learning" at all.

### Example: 49 state capitols

Imagine a program that has been given the capitol for 49 states in the USA.

If you ask if for the capitol of a state that it was pre-programmed with, it can tell you.

- Human: What's the capitol of California?
- Computer: Sacramento.

But what if you asked it for the capitol of that 50th state it was never pre-programmed to have a response for?

- Human: What's the capitol of (that 50th state you didn't get programmed with) Hawaii?
- Computer: Error.

Without being given the response for every possible input, the machine cannot properly answer. It has no capacity to understand what you're asking if it was not pre-programmed with that scenario.

Enter: Machine Learning

## The Role of Data in Machine Learning

With ML, programs are designed to learn from data, improve over time & find solutions without each scenario pre-loaded.

They learn like humans: recognizing patterns. 

Using past info to guide future decisions when similar situations arise.

### Example: Panda Dogs  

Imagine you want to teach a computer to recognize a certain breed of dog.

With traditional programming, you'd need to write code to detect specific attributes that the machine could use to positively identify the dog.

- 4 legs
- fur
- paws
- etc.

Maybe you give it 100 images of dogs, with features labeled, and 100 images of pandas with it's labels:

- 4 legs
- fur
- paws
- black around eyes

Next time it comes across these image - it would know what it is, bc it had seen them before.

After seeing images, with explicitly labeled features you're feeling confident about the machine. So it's presented with a test... Captcha time!

Label: dog or panda:

![](panda-dog.png)

- beep boop*
1. panda
2. panda

Children see animals, and are told "dog" or "panda".

(Maybe the occasional "the cow says 'moo'", "the dog says 'ruff'" kinda thing)

But we aren't given EVERY feature and told to mentally archive animals based on thousands of possible feature combinations.

Our brains are not wired for information storage & retrieval in that way - so to make up for it we recognize patterns, make associations, and have the ability for "critical thinking".

Machines don't.

Until they are built to learn like humans do.

Machine learning attempts to let machines learn like humans learn.

By providing large sets of data ("datasets") aka "a bunch of examples of X", the ML algorithm is designed to extract associations, patterns, etc. like humans do.

The main difference is that humans learn with sensory input from: sight, smell, taste, touch, hearing.

Machines understand numbers, so their sensory input comes from converting inputs to numbers, and finding the patterns between those.

Given enough examples in the training 'data set', the machine can extract enough relationships, patterns, associations in the numbers to make accurate decisions when presented with new data it had not previously seen.

The machine can learn.

Traditional programming = recall explicitly provided previous information to make decision.

Machine learning = recall previously provided information, recognize patterns & associations, make decision on new information.

## A brief history & timeline of machine learning

- 1943: Warren McCulloch and Walter Pitts introduced the concept of artificial neurons.
- 1949: Donald Hebb published "The Organization of Behaviour," introducing Hebbian learning.
- 1950: Alan Turing proposed the Turing test in "Computing Machinery and Intelligence."
- 1952: Arthur Samuel developed a checkers-playing program, an early example of reinforcement learning.
- 1956: The Dartmouth Conference marked the birth of artificial intelligence as a field.
- 1957: Frank Rosenblatt introduced the perceptron, an early artificial neural network.
- 1967: The k-nearest neighbors algorithm was introduced for pattern classification.
- 1970: The concept of reinforcement learning was formalized by Richard Bellman.
- 1979: The Stanford Cart successfully navigated a chair-filled room autonomously.
- 1986: Geoffrey Hinton and collaborators introduced the backpropagation algorithm.
- 1992: Support vector machines were introduced by Vladimir Vapnik and Alexey Chervonenkis.
- 1995: Tin Kam Ho introduced the random decision forests (random forests) algorithm.
- 1997: IBM's Deep Blue defeated world chess champion Garry Kasparov.
- 2001: Support vector machines became popular for classification tasks.
- 2006: Geoffrey Hinton introduced the term "deep learning" and proposed deep belief networks.
- 2009: Fei-Fei Li and collaborators started the ImageNet project for visual object recognition.
- 2012: AlexNet won the ImageNet Large Scale Visual Recognition Challenge (ILSVRC).
- 2014: Facebook introduced DeepFace, a facial recognition system using deep learning.
- 2015: Microsoft's ResNet achieved superhuman performance on the ImageNet challenge.
- 2016: Google DeepMind's AlphaGo defeated world champion Go player Lee Sedol.
- 2017: AlphaGo Zero, which learned Go without human data, defeated its predecessor AlphaGo.
- 2018: OpenAI's GPT-2 language model demonstrated impressive language generation capabilities.
- 2019: BERT revolutionized natural language processing tasks.
- 2020: OpenAI introduced GPT-3, one of the largest language models ever created.
- 2021: OpenAI's DALL·E generated high-quality images from textual descriptions.
- 2022: Continued advancements in machine learning, including IoT, 5G Edge, and AutoML.

## Steps in the Machine Learning Process 

1.  Data Collection: Gathering information that we'll use to teach our computer program. This information could come from surveys, sensors, websites, or other sources.
    
2.  Data Preprocessing: Getting the collected information ready for the computer program to learn from it. This involves three main steps:
    
    1.  Data Cleaning: Fixing any mistakes or missing parts in the information, like correcting typos or filling in blanks.
    2.  Feature Engineering: Choosing the most important parts of the information that will help the program make good predictions or decisions.
    3.  Data Splitting: Dividing the information into two or more groups. One group is used to teach the program, and the other group is used to test how well it learned.
3.  Model Selection: Picking the right "recipe" or method that the computer program will use to learn from the information. Different recipes work better for different types of problems.
    
4.  Model Training: Teaching the computer program using the information we collected and the recipe we picked. The program learns to recognize patterns and make predictions based on the examples it sees.
    
5.  Model Evaluation: Checking how well the program learned by testing it with the group of information we set aside earlier. We see if the program's predictions or decisions match the correct answers.
    
6.  Model Deployment: Putting the trained program to work in the real world. For example, we might use it in a smartphone app, on a website, or as part of a larger system. The program can now make predictions or decisions based on new information it receives.


## Ethical Considerations in Machine Learning
As machine learning models become increasingly integrated into our daily lives, it's essential to consider the ethical implications of their use. 

From ensuring fairness to protecting privacy, ethical considerations play a crucial role in the responsible development and deployment of machine learning technologies.

### Bias and Fairness in Machine Learning
Machine learning models learn from data, and if the data used to train them contains biases, the models may make unfair or discriminatory decisions. 

For example, consider a job recruitment algorithm that screens resumes. If the algorithm is trained on resumes submitted over the past decade, it may inadvertently learn gender bias if it was historically more common for men to be hired for certain roles. 

As a result, the algorithm may favor male applicants, perpetuating gender inequality. 

To address this, practitioners must actively work to identify and mitigate biases in their models to ensure equitable treatment of all individuals.

### Privacy and Security Concerns
Machine learning often involves using sensitive or personal data, and it is crucial to handle this data carefully to protect people's privacy and prevent unauthorized access. 

Consider a healthcare organization that uses machine learning to predict patient outcomes. 

While this technology has the potential to improve patient care, it also raises privacy concerns. The organization must handle sensitive patient data with the utmost care, ensuring that individuals' identities are protected and that data is securely stored. 

Failure to do so could lead to data breaches and violations of patient privacy, with serious legal and ethical repercussions.

### Responsible AI and Ethical Guidelines
Responsible AI encompasses the ethical development and deployment of machine learning and artificial intelligence technologies. It involves transparency in algorithmic decision-making, accountability for AI's impact, and consideration of ethical principles. 

Imagine a machine learning model used by a bank to assess creditworthiness. 

While the model may accurately predict default risk, it may also inadvertently discriminate against certain demographic groups. 

The bank must be transparent about how the model makes decisions, ensure that it aligns with ethical guidelines, and provide recourse for individuals who believe they have been treated unfairly.

## Practical Tips for Getting Started with Machine Learning
Embarking on a journey to learn machine learning can be both exciting and challenging. 

With the right resources and a proactive approach, you can develop the skills needed to create impactful machine learning models. 

### Online Resources and Courses
Aspiring machine learning practitioners have access to a wealth of online resources. Platforms like Coursera, Udemy, and edX offer comprehensive courses taught by experts. 

Additionally, websites like Kaggle and Towards Data Science provide tutorials, articles, and practical challenges to help learners gain hands-on experience.

### Machine Learning Competitions and Datasets
Machine learning competitions are an excellent way to apply skills to real-world problems.

Kaggle and DrivenData host competitions where participants develop models to tackle challenges in fields like healthcare, finance, and environmental science. 

Publicly available datasets, such as those on the UCI Machine Learning Repository, also provide opportunities for independent exploration and learning.

### Building a Portfolio of Machine Learning Projects
A well-curated portfolio showcases a practitioner's skills and expertise. 

Beginners can start by implementing classic machine learning algorithms on standard datasets. As skills develop, practitioners can tackle more complex projects, such as building recommendation systems or image classifiers. 

Documenting the process, results, and insights in a portfolio demonstrates proficiency and creativity to potential employers and collaborators.

## The Future of Machine Learning
Machine learning is a rapidly evolving field that continues to transform industries and reshape our world. 
As we look to the future, several key trends and developments are expected to drive further innovation and unlock new possibilities in machine learning.

### Impact on the Job Market and Job Replacement
Machine learning and automation are expected to significantly impact the job market. 

According to a report by the World Economic Forum, by 2025, automation and AI are projected to create 12 million more jobs than they displace. 

However, the transition may also lead to the displacement of 85 million jobs. As a result, there will be a growing need for reskilling and upskilling workers to adapt to the changing job landscape.

### Advancements in Technology and Scientific Breakthroughs
Machine learning is driving advancements in various fields, including healthcare, finance, and natural language processing. 

For example, machine learning models have been used to accelerate drug discovery and improve medical diagnosis.

In 2020, the AI program AlphaFold, developed by DeepMind, made a breakthrough in predicting protein folding, a challenge that had remained unsolved for decades. This achievement has the potential to revolutionize drug development and our understanding of diseases.

### Growing Importance of Explainable AI
As machine learning models become more prevalent in decision-making, the need for transparency and interpretability grows. 

Explainable AI (XAI) aims to make machine learning models more understandable to humans, providing insights into how and why models make certain predictions. 

XAI will play a critical role in building trust and ensuring ethical use of AI.

### Integration of Machine Learning with Edge Computing
Edge computing brings data processing closer to the source of data generation, such as IoT devices. 

The integration of machine learning with edge computing will enable real-time analysis and decision-making, enhancing applications in areas like healthcare, manufacturing, and autonomous vehicles.

The future of machine learning holds immense potential for innovation and positive impact. By embracing new technologies and prioritizing ethical considerations, we can unlock the full potential of machine learning and shape a better future for all.
