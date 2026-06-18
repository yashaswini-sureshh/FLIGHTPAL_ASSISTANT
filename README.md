# FlightPal ✈️

FlightPal is an AI-powered Travel Assistant that helps users with:

* Flight Status Tracking
* Weather Information
* Airline Policy Questions
* Travel Information Retrieval
* RAG-based Question Answering
* MCP Tool Integration

## Features

* Flight Status API
* Weather API
* Airline Policy RAG
* LangChain Agent
* MCP Server Support

## Installation

### Clone Repository

git clone https://github.com/kishore-ravada/FlightPal.git

### Create Virtual Environment

python -m venv venv

venv\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Configure Environment

Create a `.env` file using `.env.example`

### Build Vector Database

python build_db.py

### Run Application

python src/ui/app.py

## Project Structure

src/
├── agent/
├── api/
├── mcp/
├── rag/
├── router/
├── tools/
└── ui/

## Future Improvements

* Airport Maps
* Voice Assistant
* More Airlines
* Flight Booking Integration
