SKILLS = [

    # =========================
    # Programming Languages
    # =========================
    "python", "java", "c", "c++", "c#", "javascript", "typescript",
    "go", "golang", "rust", "kotlin", "swift", "php", "ruby",
    "scala", "r", "matlab", "bash", "shell scripting",

    # =========================
    # Web Development (Frontend)
    # =========================
    "html", "css", "javascript", "react", "reactjs", "angular",
    "vue", "vuejs", "next.js", "nuxt.js", "bootstrap", "tailwind css",
    "material ui", "redux", "webpack", "vite",

    # =========================
    # Web Development (Backend)
    # =========================
    "node.js", "express.js", "django", "flask", "fastapi",
    "spring", "spring boot", "hibernate",
    "laravel", "codeigniter", "ruby on rails",
    "rest api", "graphql", "microservices"," Restful api"

    # =========================
    # Databases & Storage
    # =========================
    "mysql", "postgresql", "sqlite", "oracle",
    "mongodb", "cassandra", "redis", "dynamodb",
    "firebase", "elasticsearch", "neo4j",

    # =========================
    # Data Science & Analytics
    # =========================
    "data analysis", "data analytics", "data visualization",
    "pandas", "numpy", "scipy", "matplotlib", "seaborn",
    "power bi", "tableau", "excel",
    "statistics", "probability",

    # =========================
    # Machine Learning
    # =========================
    "machine learning", "supervised learning", "unsupervised learning",
    "linear regression", "logistic regression",
    "decision trees", "random forest",
    "xgboost", "lightgbm",
    "clustering", "k-means", "svm",
    "feature engineering", "model evaluation",

    # =========================
    # Deep Learning & AI
    # =========================
    "deep learning", "neural networks", "cnn", "rnn", "lstm",
    "transformers", "attention mechanism",
    "tensorflow", "keras", "pytorch",
    "computer vision", "image processing",
    "natural language processing", "nlp",
    "bert", "gpt",

    # =========================
    # Cloud Computing
    # =========================
    "cloud computing",
    "aws", "amazon web services",
    "ec2", "s3", "lambda", "iam", "cloudwatch",
    "azure", "microsoft azure",
    "google cloud", "gcp",
    "firebase",
    "serverless architecture",

    # =========================
    # DevOps & CI/CD
    # =========================
    "devops", "ci/cd",
    "docker", "kubernetes", "helm",
    "jenkins", "github actions", "gitlab ci",
    "terraform", "ansible",
    "nginx", "apache",
    "linux", "unix",

    # =========================
    # Cybersecurity
    # =========================
    "cybersecurity", "information security",
    "network security", "application security",
    "ethical hacking", "penetration testing",
    "vulnerability assessment",
    "malware analysis",
    "siem", "soc",
    "firewalls", "ids", "ips",
    "cryptography", "encryption",
    "owasp", "owasp top 10",

    # =========================
    # Blockchain & Web3
    # =========================
    "blockchain", "distributed ledger",
    "bitcoin", "ethereum",
    "smart contracts",
    "solidity", "web3.js", "ethers.js",
    "defi", "nft",
    "hyperledger",

    # =========================
    # Mobile App Development
    # =========================
    "android", "android development",
    "ios", "ios development",
    "flutter", "react native",
    "kotlin", "swift",
    "mobile application development",

    # =========================
    # Software Engineering Concepts
    # =========================
    "data structures", "algorithms",
    "object oriented programming", "oops",
    "design patterns",
    "system design",
    "software development lifecycle", "sdlc",
    "agile", "scrum",
    "unit testing", "integration testing",
    "test driven development", "tdd",

    # =========================
    # Version Control & Tools
    # =========================
    "git", "github", "gitlab", "bitbucket",
    "jira", "confluence",
    "postman", "swagger",
    "vs code", "intellij", "pycharm",

    # =========================
    # Operating Systems & Networking
    # =========================
    "operating systems",
    "computer networks",
    "tcp/ip", "http", "https",
    "dns", "load balancing",

    # =========================
    # Big Data & Distributed Systems
    # =========================
    "big data", "hadoop", "spark",
    "kafka", "flink",
    "hive", "pig",

    # =========================
    # QA & Testing
    # =========================
    "software testing",
    "manual testing", "automation testing",
    "selenium", "cypress",
    "pytest", "junit",

    # =========================
    # Soft Skills (Optional)
    # =========================
    "problem solving", "critical thinking",
    "communication", "teamwork",
    "leadership", "time management"
]


def extract_skills(text):
    text = text.lower()
    found_skills = set()

    for skill in SKILLS:
        if skill.lower() in text:
            found_skills.add(skill)

    return list(found_skills)
