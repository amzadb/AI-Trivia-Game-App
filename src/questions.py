import random
import dspy

class QuestionBank:
    def __init__(self):
        self.questions = []
        self.load_questions()

    def load_questions(self):
        self.questions = [
            {
                "question": "Which company created the open-source platform 'Android'?",
                "options": ["Google", "Microsoft", "Apple"],
                "answer": "Google"
            },
            {
                "question": "Which protocol is commonly used for communication between Microservices in a RESTful architecture?",
                "options": ["HTTP", "TCP", "UDP"],
                "answer": "HTTP"
            },
            {
                "question": "When was Python released?",
                "options": ["Feb-91", "Jan-95", "Dec-2000"],
                "answer": "Feb-91"
            },
            {
                "question": "Which model is a widely used framework for building artificial intelligence (AI) models?",
                "options": ["TensorFlow", "PyTorch", "Scikit-learn"],
                "answer": "TensorFlow"
            },
            {
                "question": "Which command is used to run a .NET Core application from the command line?",
                "options": ["dotnet run", "dotnet build", "dotnet start"],
                "answer": "dotnet run"
            },
            {
                "question": "Which cloud service provider is known for offering the largest range of cloud computing services?",
                "options": ["Amazon Web Services (AWS)", "Google Cloud Platform (GCP)", "Microsoft Azure"],
                "answer": "Amazon Web Services (AWS)"
            },
            {
                "question": "Who invented the first programmable mechanical computer, the Analytical Engine?",
                "options": ["Charles Babbage", "Alan Turing", "John von Neumann"],
                "answer": "Charles Babbage"
            },
            {
                "question": "Who is the inventor of the first computer virus?",
                "options": ["Robert Morris", "Fred Cohen", "John McAfee"],
                "answer": "Robert Morris"
            },
            {
                "question": "Who is known as the 'father of artificial intelligence'?",
                "options": ["John McCarthy", "Alan Turing", "Geoffrey Hinton"],
                "answer": "John McCarthy"
            },
            {
                "question": "What does the acronym 'SaaS' stand for in cloud computing?",
                "options": ["Software as a Service", "System as a Service", "Storage as a Service"],
                "answer": "Software as a Service"
            },
            {
                "question": "Who is known as the father of computer science?",
                "options": ["Alan Turing", "Charles Babbage", "John von Neumann"],
                "answer": "Alan Turing"
            },
            {
                "question": "What does HTML stand for?",
                "options": ["HyperText Markup Language", "HighText Machine Language", "Hyperlink and Text Markup Language"],
                "answer": "HyperText Markup Language"
            },
            {
                "question": "Which programming language is often referred to as the backbone of the web?",
                "options": ["Python", "JavaScript", "C++"],
                "answer": "JavaScript"
            },
            {
                "question": "What does CSS stand for?",
                "options": ["Cascading Style Sheets", "Creative Style System", "Computer Styling Syntax"],
                "answer": "Cascading Style Sheets"
            },
            {
                "question": "Which data structure uses LIFO (Last In, First Out) methodology?",
                "options": ["Queue", "Stack", "Linked List"],
                "answer": "Stack"
            },
            {
                "question": "Which company developed the C programming language?",
                "options": ["Apple", "Bell Labs", "Microsoft"],
                "answer": "Bell Labs"
            },
            {
                "question": "What is the time complexity of binary search?",
                "options": ["O(n)", "O(log n)", "O(n^2)"],
                "answer": "O(log n)"
            },
            {
                "question": "Which protocol is used for secure communication over the internet?",
                "options": ["HTTP", "FTP", "HTTPS"],
                "answer": "HTTPS"
            },
            {
                "question": "What is the default branch name in Git repositories?",
                "options": ["main", "master", "develop"],
                "answer": "main"
            },
            {
                "question": "Popular RPA tool for automation?",
                "options": ["UiPath", "Blue Prism", "Automation Anywhere"],
                "answer": "UiPath"
            },
            {
                "question": "First Bot Name?",
                "options": ["ELIZA", "Siri", "Alexa"],
                "answer": "ELIZA"
            },
            {
                "question": "Inventors of Siri?",
                "options": ["Dag Kittlaus, Tom Gruber, and Adam Cheyer", "Elon Musk, Jeff Bezos, and Bill Gates", "Larry Page, Sergey Brin, and Sundar Pichai"],
                "answer": "Dag Kittlaus, Tom Gruber, and Adam Cheyer"
            },
            {
                "question": "Which year was the first smartphone released?",
                "options": ["1994 (IBM Simon)", "2007 (Apple iPhone)", "2000 (BlackBerry 850)"],
                "answer": "1994 (IBM Simon)"
            },
            {
                "question": "Which company developed the first commercially successful laptop computer?",
                "options": ["Toshiba", "IBM", "Apple"],
                "answer": "Toshiba"
            },
            {
                "question": "What is the full form of Wi-Fi?",
                "options": ["Wireless Fidelity", "Wide Frequency", "Wireless Functionality"],
                "answer": "Wireless Fidelity"
            },
            {
                "question": "What is the full form of RPA?",
                "options": ["Robotic Process Automation", "Remote Process Application", "Rapid Processing Algorithm"],
                "answer": "Robotic Process Automation"
            },
            {
                "question": "In SOLID principles, what does 'S' stand for?",
                "options": ["Single Responsibility Principle (SRP)", "Scalability Principle", "Software Modularity"],
                "answer": "Single Responsibility Principle (SRP)"
            },
            {
                "question": "What is the full form of TDD?",
                "options": ["Test-Driven Development", "Technical Design Document", "Top-Down Deployment"],
                "answer": "Test-Driven Development"
            },
            {
                "question": "What is the full form of SSO?",
                "options": ["Single Sign-On", "Secure System Operation", "Software Security Optimization"],
                "answer": "Single Sign-On"
            },
            {
                "question": "What is the full form of MFA?",
                "options": ["Multi-Factor Authentication", "Mobile Framework Application", "Modular Functional Algorithm"],
                 "answer": "Multi-Factor Authentication"
            },
            {
                "question": "Which type of testing is performed to check if a new feature works correctly without breaking existing functionality?",
                "options": ["Regression Testing", "Unit Testing", "Performance Testing"],
                "answer": "Regression Testing"
            },
            {
                "question": "Which type of testing is performed to check if the software is ready for release and can be deployed?",
                "options": ["User Acceptance Testing (UAT)", "Functional Testing", "Security Testing"],
                "answer": "User Acceptance Testing (UAT)"
            },
            {
                "question": "What is a commonly used development methodology in software development?",
                "options": ["Agile", "Waterfall", "V-Model"],
                "answer": "Agile"
            },
            {
                "question": "Which is the latest stable version of Python as of 2025?",
                "options": ["Python 3.12", "Python 3.10", "Python 3.8"],
                "answer": "Python 3.12"
            },
            {
                "question": "In which year was Facebook founded by Mark Zuckerberg and his college roommates?",
                "options": ["2004", "2006", "2008"],
                "answer": "2004"
            },
            {
                "question": "Which company was founded by Jack Dorsey, Noah Glass, Biz Stone, and Evan Williams in 2006?",
                "options": ["Twitter", "Instagram", "LinkedIn"],
                "answer": "Twitter"
            },
            {
                "question": "Which company was founded by Reed Hastings and Marc Randolph in 1997?",
                "options": ["Netflix", "Amazon", "Hulu"],
                "answer": "Netflix"
            },
            {
                "question": "Who founded WhatsApp in 2009?",
                "options": ["Brian Acton and Jan Koum", "Mark Zuckerberg and Sheryl Sandberg", "Pavel Durov and Nikolai Durov"],
                "answer": "Brian Acton and Jan Koum"
            },
            {
                "question": "What do you call the smallest unit of data in computing?",
                "options": ["bit", "byte", "kilobyte"],
                "answer": "bit"
            },
            {
                "question": "What is the term for storing files online instead of locally?",
                "options": ["Cloud Storage", "External Drive", "Cache"],
                "answer": "Cloud Storage"
            },
            {
                "question": "Which company created Azure, a popular cloud platform?",
                "options": ["Microsoft", "Google", "Amazon"],
                "answer": "Microsoft"
            },
            {
                "question": "What is the term for combining development and operations?",
                "options": ["DevOps", "Agile", "Scrum"],
                "answer": "DevOps"
            },
            {
                "question": "What is the process of converting data into unreadable text?",
                "options": ["Encryption", "Decryption", "Compression"],
                "answer": "Encryption"
            },
            {
                "question": "Which protocol is used to send emails?",
                "options": ["SMTP", "HTTP", "FTP"],
                "answer": "SMTP"
            },
            {
                "question": "Which language is known as the 'mother' of all programming languages?",
                "options": ["C", "Assembly", "Java"],
                "answer": "C"
            },
            {
                "question": "Which term refers to testing a program for errors?",
                "options": ["Debugging", "Compiling", "Rendering"],
                "answer": "Debugging"
            },
            {
                "question": "Which AI technology is used to create realistic images and videos from text descriptions?",
                "options": ["DALL-E", "ChatGPT", "Stable Diffusion"],
                "answer": "DALL-E"
            },
            {
                "question": "What is the primary benefit of using RAG in AI models?",
                "options": ["Accuracy", "Speed", "Energy Efficiency"],
                "answer": "Accuracy"
            },
            {
                "question": "Which programming language is known for its simplicity and readability?",
                "options": ["C", "Python", "Java"],
                "answer": "Python"
            },
            {
                "question": "RAG models often rely on what type of data?",
                "options": ["Documents", "Images", "Audio"],
                "answer": "Documents"
            },
            {
                "question": "Amazon's virtual assistant used in Echo devices.",
                "options": ["Alexa", "Siri", "Google Assistant"],
                "answer": "Alexa"
            },
            {
                "question": "What design pattern ensures a class has only one instance?",
                "options": ["Singleton", "Factory", "Observer"],
                "answer": "Singleton"
            },
            {
                "question": "Which pattern allows an object to act as a substitute for another object?",
                "options": ["Proxy", "Adapter", "Decorator"],
                "answer": "Proxy"
            },
            {
                "question": "Which project management methodology uses a visual board to manage workflow and tasks?",
                "options": ["Kanban", "Scrum", "Waterfall"],
                "answer": "Kanban"
            },
            {
                "question": "Which project management certification is widely recognized and valued?",
                "options": ["PMP", "Scrum Master", "PRINCE2"],
                "answer": "PMP"
            },
            {
                "question": "What type of testing ensures usability across devices and browsers?",
                "options": ["Cross-browser", "Unit", "Integration"],
                "answer": "Cross-browser"
            },
            {
                "question": "What is the primary focus of UX design?",
                "options": ["Experience", "Code Efficiency", "Database Optimization"],
                "answer": "Experience"
            },
            {
                "question": "What is the term for a blueprint of an object?",
                "options": ["Class", "Object", "Method"],
                "answer": "Class"
            },
            {
                "question": "What is the ability to take many forms in OOP?",
                "options": ["Polymorphism", "Encapsulation", "Abstraction"],
                "answer": "Polymorphism"
            },
            {
                "question": "What is the term for a network security device that monitors and controls incoming and outgoing network traffic?",
                "options": ["Firewall", "Router", "Gateway"],
                "answer": "Firewall"
            },
            {
                "question": "What is the term for a weakness in a system that can be exploited?",
                "options": ["Vulnerability", "Malware", "Threat"],
                "answer": "Vulnerability"
            },
            {
                "question": "What is the term for unauthorized access to data?",
                "options": ["Breach", "Exploit", "Patch"],
                "answer": "Breach"
            },
            {
                "question": "What is Sora?",
                "options": [
                "A text-to-video AI model by OpenAI",
                "A virtual reality headset",
                "A cloud computing platform"
                ],
                "answer": "A text-to-video AI model by OpenAI"
            },
            {
                "question": "What is Sora used for?",
                "options": [
                "Creating videos from text prompts",
                "Automating software testing",
                "Managing cloud services"
                ],
                "answer": "Creating videos from text prompts"
            },
            {
                "question": "AI text-to-speech tool called Synthesia is used in one of the projects in iSpace. Which client project uses Synthesia?",
                "options": ["KornFerry", "Microsoft", "IBM"],
                "answer": "KornFerry"
            },
            {
                "question": "Who is India's first AI news anchor?",
                "options": ["Sana", "Lisa", "Evan"],
                "answer": "Sana"
            },
            {
                "question": "Can you name any three AI news anchors in India?",
                "options": [
                "Sana, Lisa, Soundarya",
                "Alexa, Siri, Google Assistant",
                "Maya, Evan, Cortana"
                ],
                "answer": "Sana, Lisa, Soundarya"
            },
            {
                "question": "What does API stand for?",
                "options": ["Application Programming Interface", "Advanced Programming Integration", "Application Programming Interchange"],
                "answer": "Application Programming Interface"
            }
            ]

    def get_random_question(self):
        return random.choice(self.questions)

    def explain(question, user_answer, correct_answer):
        prompt = (
            f"Given that the question is: {question} and the correct answer is '{correct_answer}', "
            f"please explain why my answer '{user_answer}' is incorrect. "
            f"Keep it short, within 3 sentences."
        )

        model_name = "deepseek-r1:1.5b"
        lm = dspy.LM(
            f'ollama_chat/{model_name}', api_base='http://localhost:11434', api_key='', cache=False
        )
        response_text = lm(prompt)
        if isinstance(response_text, list):
            response_text = response_text[0]
 
        explanation_start = response_text.find('<think>')
        explanation_end = response_text.find('</think>')
        if explanation_start != -1 and explanation_end != -1: 
                    # Extracting the explanation part        
            concise_explanation = response_text[explanation_start + len('<think>'):explanation_end].strip()
            return concise_explanation
        else: 
            return "No valid explanation found."