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

git clone https://github.com/yashaswini-sureshh/FLIGHTPAL_ASSISTANT.git

### Create Virtual Environment

python -m venv venv

venv\Scripts\activate

## Follow the steps to exactly run the project ##
## step 1##

### Install Dependencies

pip install -r requirements.txt

## step 2##
### Configure Environment

Create a `.env` file using `.env.example`
keep the api keys for google ai key and avationstack api key
below i have mentioned my api keys use it for test purpose:

GOOGLE_API_KEY=AQ.Ab8RN6JwgXF4gdTm44HRPuB72eHo-jm_hFR84diHu4WK09O_dA
AVIATIONSTACK_API_KEY=ba00ce50721fd2a07e58af1f6551d443

## step 3##
make sure every folder contain __init__.py
so that python will understand folders as modules

## step 4 

python src\rag\document_loader.py
python src\rag\text_processing.py
python src\rag\vector_store.py 
run the above cmds to 
load to documents,
text pre_processing,
converting into embedings.

## step 5
### create database folder
python build_db.py 
run the command,it builds Build Vector Database

python src\rag\rag_pipeline.py

### Run Application

python src\rag\rag_pipeline.py
python -m src.ui.app

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
