# Cahill--Madrigal-Cipher 🔐
Crypto, unshackled: *Dual-layer* encryption (keyboard→alphabet substitution) coupled with an *involutory* numeric cipher — f(f(x)) = x. Zero cryptography borrowed — pure logical architecture.

---

## 🧠 The Genesis: No Theory, Just Design

This isn't another implementation of a classical cipher. This is the result of a first-principles thought experiment:

> *"How would I design a way to transform information if I knew nothing about existing cryptography?"*

The answer is Cahill——Madrigal-Cipher — a symmetric encryption algorithm built from scratch, focusing on elegant mechanics and a self-inverting structure.

## ✨ Core Concepts

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

## 🚀 Live Demo & Output

### Quick Run
1. **Click** the [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/PopJoy-geek/Cahill--Madrigal-Cipher) button above
2. **Wait** for the environment to start (2-3 minutes)
3. **Run** in the terminal:
   ```bash
   python3 "Cahill - Madrigal - Cipher.py"
   ```

### What You'll See
Here's the exact output from running the demo with `custom_key = 7`:

```
Custom encrypted message: Crf mpn yjjq r sjckjl?
Custom decrypted message: Can you keep a secret?

Custom encrypted message: Mjjl gj rl 41.6068 tjvkjjjs N, 892.3391 tjvkjjs W rl 5qg.
Custom decrypted message: Meet me at 48.6061 degrees N, 129.3328 degrees W at 5pm.

Custom encrypted message: %Kw@f! Ac&t#gm29  
Custom decrypted message: %Kh@n! Ac&d#my92

Custom encrypted message: Coqwjks lkrfsupkg gjssrvjs oflp rf nfkjcpvfoarezj upkg lp sjcnkj ofupkgrlopf ukpg nfrnlwpkoajt rccjss...
Custom decrypted message: Ciphers transform messages into an unrecognizable form to secure information...
```

### Key Features Demonstrated
- **Text Encryption**: Letters are transformed through dual-layer substitution (keyboard → alphabet mapping)
- **Coordinate Encryption**: Numbers use a **self-inverse transformation** where `encrypt(encrypt(number)) == number` always holds
- **Password Protection**: Complex passwords with symbols remain fully recoverable
- **Paragraph Encryption**: Handles large blocks of text while preserving all formatting
- **Symmetric Design**: Separate but complementary `encrypt()` and `decrypt()` functions maintain perfect reversibility

### Technical Insight
The cipher employs two distinct mechanisms:
- **Letters**: Dual-layer substitution with symmetric encryption/decryption
- **Numbers**: Pure self-inverse transformation - the same operation encrypts and decrypts

### 🎛️ Customize Your Experience
Modify the encryption key in `Cahill - Madrigal - Cipher.py`:
```python
custom_key = 7  # ← Change this value to any number (1-8 recommended)
```

**Try different keys and observe how the encryption changes while decryption always recovers the original text perfectly!**

### 💡 Pro Tips
- The cipher preserves spaces, punctuation, and capitalization
- Numbers and coordinates undergo special involutory transformation
- Perfect for learning cryptography concepts through hands-on experimentation


