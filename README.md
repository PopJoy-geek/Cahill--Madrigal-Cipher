# Cahill--Madrigal-Cipher
Crypto, unshackled: *Dual-layer* encryption (keyboard→alphabet substitution) coupled with an *involutory* numeric cipher — f(f(x)) = x. Zero cryptography borrowed — pure logical architecture.

---

## The Genesis: No Theory, Just Design

This isn't another implementation of a classical cipher. This is the result of a first-principles thought experiment:

> *"How would I design a way to transform information if I knew nothing about existing cryptography?"*

The answer is Madrigal Cipher — a symmetric encryption algorithm built from scratch, focusing on elegant mechanics and a self-inverting structure.

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

markdown

## 🚀 Quick Start

You can instantly run and experiment with this cipher directly in your browser using GitHub Codespaces:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/PopJoy-geek/Cahill--Madrigal-Cipher)

### Example Usage

```python
# For a valid shift and number:
from madrigal import encrypt, decrypt

message = "Secret123"
key = 8

encrypted_text = encrypt(message, key)
decrypted_text = decrypt(encrypted_text, key)

print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
# Output should verify that decrypted_text == message
```

print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
# Output should verify that decrypted_text == message
```
