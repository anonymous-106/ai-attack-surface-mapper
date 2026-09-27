# AI Attack Surface Mapper

AI Attack Surface Mapper is a cybersecurity project designed to discover, organize, and eventually analyze the attack surface of an authorized target.

The project is being developed incrementally, beginning with a controlled foundation for target definition, scope enforcement, validation, logging, configuration, command-line interaction, testing, and documentation.

## Purpose

The goal of this project is to build a structured system that can eventually map the attack surface of an authorized target.

The project is intended for:

- Authorized security assessments
- Security research
- Educational and laboratory environments
- Understanding attack-surface discovery and mapping

The tool must only be used against targets for which explicit authorization has been obtained.

## Current Features

The current implementation contains the project's foundational components:

- Target representation
- Supported target types
- Scope definition
- Target validation
- Out-of-scope target rejection
- Empty-scope rejection
- Logging system
- Configurable log level
- Error logging
- Command-line interface
- Command-line target input
- Basic configuration management
- Automated testing with pytest
- Initial project architecture documentation

## Project Structure

```text
ai-attack-surface-mapper/
│
├── core/
│   ├── logger.py
│   ├── target.py
│   └── validator.py
│
├── models/
│   └── target.py
│
├── tests/
│   ├── test_logger.py
│   └── test_validator.py
│
├── docs/
│   └── architecture.md
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
└── .gitignore