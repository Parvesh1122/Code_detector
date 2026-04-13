🔍 Code Plagiarism Detector

A robust Code Plagiarism Detection System that analyzes multiple source code files and detects similarity using algorithmic approaches such as Longest Common Subsequence (LCS) and string matching techniques. The system focuses on logical similarity rather than superficial formatting changes.

📄 Overview

This project is designed to help identify copied or highly similar code across multiple files. It preprocesses input code to remove noise (comments, spaces, formatting) and then applies algorithmic comparison techniques to compute similarity scores.

It is particularly useful in:

Academic environments for assignment evaluation
Detecting code reuse or duplication
Learning core concepts of DAA (Design and Analysis of Algorithms)
🚀 Key Features
📂 Upload and compare multiple code files
🔍 Detect logical similarity between programs
📊 Generate percentage-based similarity scores
🧹 Preprocess code (remove comments, whitespace, formatting)
⚡ Efficient comparison using Dynamic Programming (LCS)
🌐 Simple and responsive web interface
📑 Extensible for advanced detection techniques
🛠️ Tech Stack
Component	Technology
Frontend	HTML, CSS, Bootstrap
Backend	Python (Flask)
Algorithms	LCS, String Matching
File Handling	Python File I/O
Version Control	Git & GitHub
⚙️ System Workflow
User uploads one or more code files.
Files are preprocessed:
Comments removed
Extra spaces eliminated
Code normalized
Each file pair is compared.
LCS algorithm computes similarity.
Similarity score is calculated and displayed.
🧠 Core Algorithm

The system uses Longest Common Subsequence (LCS) to measure similarity.

Similarity (%) = (LCS Length / Max Length of Two Files) × 100
Why LCS?
Detects structural similarity
Ignores variable name changes
More robust than direct string matching
📦 Installation & Setup
Step 1: Clone Repository
git clone https://github.com/your-username/code-plagiarism-detector.git
Step 2: Navigate to Project
cd code-plagiarism-detector
Step 3: Install Dependencies
pip install -r requirements.txt
Step 4: Run Application
python app.py
Step 5: Open in Browser
http://localhost:5000
📂 Project Structure
code-plagiarism-detector/
│── static/              # CSS, JS files
│── templates/           # HTML pages
│── uploads/             # Uploaded code files
│── algorithms/
│     └── lcs.py         # LCS algorithm implementation
│── utils.py             # Preprocessing logic
│── app.py               # Flask application
│── requirements.txt
│── README.md
📊 Example Output
File 1	File 2	Similarity
a.py	b.py	82%
a.py	c.py	45%
📌 Applications
🎓 Academic plagiarism detection
🏫 University project evaluation
💻 Code similarity analysis
🔍 Research in string algorithms
🔮 Future Enhancements
🔍 Abstract Syntax Tree (AST) based detection
🤖 Machine Learning-based similarity scoring
📊 Graphical visualization of results
📑 Highlight plagiarized lines
🌐 Multi-language support
🔐 User authentication system
⚠️ Limitations
LCS is computationally expensive for very large files
Cannot fully detect logical plagiarism with major code restructuring
Language-dependent preprocessing may be required
🤝 Contributing

Contributions are welcome. Please fork the repository and submit a pull request.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Parvesh Kumar
