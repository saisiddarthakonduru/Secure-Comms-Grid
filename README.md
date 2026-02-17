# Secure Comms Grid - Military E2EE Communication System

## Project Structure
- **app.py** - Flask backend server
- **templates/index.html** - Web interface (client-side crypto)
- **requirements.txt** - Python dependencies

## Setup & Running

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the Application
```bash
python app.py
```

The server will start at `http://localhost:5000`

### 3. Open in Browser
Navigate to `http://localhost:5000` in your web browser to access the Secure Comms Grid interface.

## Features
- **RSA-OAEP Encryption** - End-to-End encrypted messaging
- **ECDSA Digital Signatures** - Message authentication and integrity verification
- **Key Management** - Password-protected key storage
- **Simulated Blockchain Registry** - Decentralized public key storage

## Usage
1. **Generate & Register Keys** - Create encryption and signing key pairs with a password
2. **Encrypt & Sign** - Send encrypted messages with digital signatures
3. **Decrypt & Verify** - Receive and authenticate messages from others

All cryptographic operations happen client-side in the browser using the Web Crypto API.
