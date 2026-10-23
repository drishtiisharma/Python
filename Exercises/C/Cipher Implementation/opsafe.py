import oqs

with oqs.KeyEncapsulation("ML-KEM-768") as kem:

    public_key = kem.generate_keypair()
    private_key = kem.export_secret_key()

    print("Public key:", public_key.hex())
    print("Private key:", private_key.hex())