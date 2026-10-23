### 1. System Preparation and Dependency Installation

The first step ensures your Ubuntu system has all necessary tools to compile C code and manage Python environments.

`sudo apt update` refreshes the package list.
`sudo apt install -y git cmake build-essential ninja-build python3 python3-venv python3-pip` installs:
*   **git**: To download the source code.
*   **cmake & ninja-build**: Build systems to compile the C library efficiently.
*   **build-essential**: Contains GCC (compiler) and Make.
*   **python3-venv & pip**: For creating isolated Python environments.

```bash
sudo apt update
sudo apt install -y git cmake build-essential ninja-build python3 python3-venv python3-pip
```

Verification commands confirm the tools are installed correctly.

```bash
git --version
cmake --version
gcc --version
python3 --version
```

### 2. Source Code Acquisition

You create a directory for source code and clone the `liboqs` repository. This library contains implementations of post-quantum cryptographic algorithms.

```bash
mkdir -p ~/src
cd ~/src
git clone https://github.com/open-quantum-safe/liboqs.git
```

The directory structure separates source code (`~/src`) from your actual project work (`~/projects`).

### 3. Compiling the Native Library

`liboqs` is written in C. You must compile it into a shared library (`.so` file) that Python can later access.

`cd ~/src/liboqs` moves into the source directory.

The `cmake` command configures the build:
*   `-S .`: Source directory is current folder.
*   `-B build`: Output goes to `build` folder.
*   `-GNinja`: Uses Ninja builder for speed.
*   `-DCMAKE_INSTALL_PREFIX=/usr/local`: Installs libraries to standard system paths.
*   `-DBUILD_SHARED_LIBS=ON`: Creates a shared library (required for dynamic linking).

```bash
cmake -S . -B build -GNinja \
  -DCMAKE_INSTALL_PREFIX=/usr/local \
  -DBUILD_SHARED_LIBS=ON
```

`cmake --build build --parallel` compiles the code using all available CPU cores.

```bash
cmake --build build --parallel
```

### 4. System-Wide Installation

`sudo cmake --install build` copies the compiled library files to `/usr/local/lib` and headers to `/usr/local/include`.

```bash
sudo cmake --install build
```

`sudo ldconfig` updates the dynamic linker cache. This allows the system to find `liboqs.so` when programs request it.

```bash
sudo ldconfig
```

`ldconfig -p | grep liboqs` verifies the library is registered and accessible.

```bash
ldconfig -p | grep liboqs
```

### 5. Python Environment Setup

You create an isolated Python environment to avoid conflicts with system packages.

`mkdir -p ~/projects/cipher` creates your project folder. `cd ~/projects/cipher` enters it.

`python3 -m venv .venv` creates a virtual environment named `.venv`. `source .venv/bin/activate` activates it, ensuring subsequent pip installs go into this isolated environment.

```bash
mkdir -p ~/projects/cipher
cd ~/projects/cipher
python3 -m venv .venv
source .venv/bin/activate
```

`python -m pip install --upgrade pip` updates pip. `python -m pip install liboqs-python` installs the Python bindings for liboqs. This package uses `cffi` or `ctypes` internally to call the native C library you compiled earlier.

```bash
python -m pip install --upgrade pip
python -m pip install liboqs-python
```

### 6. Verification of Installation

This command tests if Python can import the library and locate the underlying C functions.

```bash
python -c "import oqs; print(oqs.file); print(oqs.KeyEncapsulation)"
```

If successful, it prints the path to the module and confirms the `KeyEncapsulation` class is available.

### 7. Cipher Implementation: Key Generation

The script `opsafe.py` demonstrates Key Encapsulation Mechanism (KEM) using ML-KEM-768 (formerly Kyber-768).

`import oqs` imports the library.

`with oqs.KeyEncapsulation("ML-KEM-768") as kem:` initializes the KEM object. The `with` statement ensures proper cleanup of resources.

`kem.generate_keypair()` generates a public key and a secret key. In KEM, the "secret key" is used for decapsulation.

`kem.export_secret_key()` retrieves the private key bytes.

`.hex()` converts binary data to a hexadecimal string for readable output.

```python
import oqs

with oqs.KeyEncapsulation("ML-KEM-768") as kem:
    public_key = kem.generate_keypair()
    private_key = kem.export_secret_key()

    print("Public key:", public_key.hex())
    print("Private key:", private_key.hex())
```

Run the script with:

```bash
python opsafe.py
```

### 8. Next Steps: Encapsulation and Decapsulation

The file `step2_secret.py` (not shown in your snippet but implied) would typically demonstrate:
1.  **Encapsulation**: Using the public key to generate a shared secret and a ciphertext.
2.  **Decapsulation**: Using the private key and ciphertext to recover the same shared secret.

This shared secret is then used as the key for symmetric encryption like AES-GCM to encrypt actual messages.**