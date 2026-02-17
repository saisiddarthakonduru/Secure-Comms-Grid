🔐 Secure Comms Grid

Blockchain & Cybersecurity Prototype – End-to-End Encryption with Digital Signatures

Secure Comms Grid is a cybersecurity prototype that simulates a military-grade secure email infrastructure using public key cryptography, blockchain-based identity registration, end-to-end encryption (E2EE), and digital signatures.

This project demonstrates how secure communication systems can ensure confidentiality, integrity, authentication, and non-repudiation.

🚀 Features

🔑 Key Generation

Generates encryption and signing key pairs

Password-protected private keys

⛓ Blockchain-Based Public Key Register

Simulated immutable ledger for public key storage

✉ Encrypt & Sign Messages

End-to-end encrypted transmission

Digital signature creation

🔓 Decrypt & Verify

Signature verification

Message integrity validation

🛡 Security Concepts Demonstrated

Asymmetric cryptography (RSA/ECC)

Hashing

Digital signatures

Blockchain ledger simulation

🏗 System Workflow

User Registration

Generate public/private keys

Register public key on blockchain ledger

Send Message

Encrypt message using recipient’s public key

Sign using sender’s private key

Receive Message

Decrypt using recipient’s private key

Verify signature using sender’s public key

🛠 Tech Stack

Python (Flask)

HTML5 / CSS3

JavaScript

Cryptography Libraries (RSA / hashing)

Simulated Blockchain (Python-based ledger)

📂 Project Structure
Secure-Comms-Grid/
│
├── app.py
├── blockchain.py
├── crypto_utils.py
├── templates/
│   └── index.html
├── static/
│   └── styles.css
└── README.md

⚙ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/secure-comms-grid.git
cd secure-comms-grid

2️⃣ Create Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py


Open in browser:

http://127.0.0.1:5000

🎯 Learning Objectives

Understand end-to-end encryption workflow

Learn digital signature implementation

Explore blockchain for identity verification

Implement secure key handling mechanisms

Build a cybersecurity prototype using Flask

🔒 Security Note

⚠ This is a prototype for educational purposes only.
It is not intended for real-world military or production deployment.
