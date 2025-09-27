# JWT Security Analyser

JWT Security Analyser is an open-source Python tool designed to inspect, validate, and analyze JSON Web Tokens (JWTs) for security vulnerabilities and best practices. It helps developers, security professionals, and DevOps teams to identify weaknesses in their JWT implementation, such as insecure signing algorithms, missing claims, weak secrets, and more.

## Features

- Decode and inspect JWTs
- Detect insecure signing algorithms
- Validate standard and custom claims
- Check for token expiration and misuse
- Identify weak secrets and misconfigurations
- Command-line interface for quick analysis
- Easily extensible for custom checks

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python -m jwt_security_analyser.analyser --token <JWT_TOKEN>
```

## License

MIT License