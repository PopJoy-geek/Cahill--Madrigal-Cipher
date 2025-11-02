# Cahill--Madrigal-Cipher
Crypto, unshackled: *Dual-layer* encryption (keyboard→alphabet substitution) coupled with an *involutory* numeric cipher — f(f(x)) = x. Zero cryptography borrowed — pure logical architecture.

---

## The Genesis: No Theory, Just Design

This isn't another implementation of a classical cipher. This is the result of a first-principles thought experiment:

> *"How would I design a way to transform information if I knew nothing about existing cryptography?"*

The answer is Cahill——Madrigal-Cipher — a symmetric encryption algorithm built from scratch, focusing on elegant mechanics and a self-inverting structure.

## Core Concepts

### 1. Dual-Layer Letter Encryption
Letters undergo a two-stage substitution:
1.  **Layout Mapping:** A letter is located on the QWERTY keyboard (`alphabet1`).
2.  **Alphabet Shift:** Its positional index is shifted and used to fetch a substitute from a standard alphabet (`alphabet2`).

This creates a unique substitution layer that is both intuitive and non-trivial to break.

### 2. Involutory Numeric Cipher (The Beautiful Part)
The number encryption has a mathematically elegant property: **it is its own inverse.**


```python
# For a valid shift and number:
encrypted_num = cipher(original_num, shift)
decrypted_num = cipher(encrypted_num, shift) # == original_num!
```

## 🚀 Quick Start

You can instantly run and experiment with this cipher directly in your browser using GitHub Codespaces:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/PopJoy-geek/Cahill--Madrigal-Cipher)

### Example Usage

```python
# Import from the renamed file  
from cahill_madrigal_cipher import encrypt, decrypt

# Example 1: Secret Message with Coordinates
message = "Can you keep a secret? Meet me at 48.6061 degrees N, 129.3328 degrees W at 5pm."
key = 7

encrypted_text = encrypt(message, key)
decrypted_text = decrypt(encrypted_text, key)

print("=== Secret Coordinate Message ===")
print(f"Original: {message}")
print(f"Encrypted: {encrypted_text}")  
print(f"Decrypted: {decrypted_text}")
print(f"Success: {decrypted_text == message}\n")

# Example 2: Simple Verification
test_message = "Hello World 123"
test_encrypted = encrypt(test_message, key)
test_decrypted = decrypt(test_encrypted, key)

print("=== Basic Function Test ===")
print(f"Test Original: {test_message}")
print(f"Test Encrypted: {test_encrypted}")
print(f"Test Decrypted: {test_decrypted}")
print(f"Test Success: {test_decrypted == test_message}")
```
