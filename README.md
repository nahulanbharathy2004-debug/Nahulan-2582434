# Nahulan-2582434
AI-Based Smart Classroom Doubt Assistant
# AI-Based Smart Classroom Doubt Assistant

An offline, privacy-first classroom assistant engineered for university students and educators. The application provides instant, multi-modal doubt resolution by coupling a local Large Language Model (LLM) for conceptual explanations with a local Image Generation Model for educational diagrams and visual concept representations.

---

## Problem Statement
In large university classrooms and self-paced study environments:
* Students hesitate to interrupt lectures or lack access to 24/7 personalized academic support.
* Text-only explanations frequently fail to convey complex spatial, structural, and scientific concepts.
* Utilizing proprietary cloud AI tools introduces recurring subscription costs, internet bandwidth dependency, and potential privacy risks with academic material.

**Solution:** The **Smart Classroom Doubt Assistant** runs 100% locally on workstation hardware. It breaks down complex academic questions into structured step-by-step pedagogical explanations while concurrently synthesizing visual educational aids.

---

##  Key Features
* **Zero Cloud Dependency:** Runs completely on local hardware via local inference servers (Ollama & Stable Diffusion WebUI API).
* **Multi-Modal Conceptual Answers:** Delivers both structured theoretical explanations and synthesized visual concept representations in a single workflow.
* **Dual-Prompt Processing Pipeline:** The local LLM answers the student query and formulates an optimized technical diffusion prompt tailored for educational imagery.
* **Session Export:** Automatically saves generated summaries, diagrams, and session notes to the local `outputs/` directory.

---

## System Architecture 
```text
+-------------------------------------------------------------+
|                     Streamlit Web UI                        |
|   (Accepts Student Query & Academic Subject Selection)      |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|               Local LLM Server (Ollama / Llama 3)           |
|  - Generates Step-by-Step Conceptual Answer                 |
|  - Formulates Targeted Visual Prompt for Diagram            |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|        Local Diffusion API (Stable Diffusion WebUI)         |
|  - Generates Visual Illustration / Scientific Concept Art   |
+------------------------------+------------------------------+
                               |
                               v
+-------------------------------------------------------------+
|                 Display & Output Storage                    |
|      - Streamlit UI displays Text + Image side-by-side      |
|      - Image and Transcript saved to outputs/               |
+-------------------------------------------------------------+
```

---

##  Repository Structure

```text
Nahulan-2582434/
│
├── README.md              # Project documentation and setup guide
├── LICENSE                # Open-source MIT License
├── .gitignore             # Git exclusion rules
├── requirements.txt       # Python environment dependencies
├── app.py                 # Primary Streamlit application
├── src/
│   ├── __init__.py
│   ├── llm_engine.py      # Ollama API integration client
│   └── visual_engine.py   # Stable Diffusion API integration client
├── docs/
│   ├── architecture.png   # System architecture diagram
│   ├── workflow.png       # Pipeline workflow diagram
│   └── screenshots/       # Application UI screenshots
├── models/                # Local model configurations
├── data/                  # Sample academic doubt prompts
├── outputs/               # Generated session notes and diagrams
└── demo/
    └── demo.mp4           # Video demonstration of local workflow
```
## Installation & Usage
---
### 1. Prerequisites
* **Python**: `3.10` or higher
* **Ollama**: Installed and running locally ([Download Ollama](https://ollama.com/))
* **Stable Diffusion WebUI (AUTOMATIC1111)**: Installed with `--api` flag enabled

### 2. Model Preparation
Pull the preferred local LLM via terminal:
```bash
ollama run llama3
# Linux/macOS
./webui.sh --api --listen

# Windows
webui-user.bat --api
```
* **Dual-Prompt Pipeline:** Seamlessly translates user queries into conceptual explanations and targeted visual prompts concurrently.
* **100% Offline & Local:** Operates with zero external API dependencies using local LLM and image diffusion backends.
---

##  Technology Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Frontend UI** | Streamlit | Web interface and interactive user controls |
| **Text Generation** | Ollama (`llama3`) | Core reasoning and conceptual doubt resolution |
| **Image Generation** | Stable Diffusion WebUI API | Visual diagram and concept illustration |
| **Language** | Python 3.10+ | Core orchestration and API integration |

---

## Session Outputs

All processed queries automatically generate local records in the `outputs/` folder:
* **Session Notes:** Formatted markdown/text files containing subject context and detailed explanations.
* **Concept Diagrams:** High-resolution PNG diagrams illustrating the core mechanism of the query.

---

##  License & Acknowledgments

* **License:** Distributed under the MIT License.
* **Author:** NAHULAN BHARATHY K (Register No: 2582434)
* **Context-Aware Responses:** Tailors explanations based on selected academic subject domains.
* **Automatic Session Export:** Automatically archives generated text explanations and diagram assets into the local `outputs/` directory.
