# Aegis OSINT Project

**Status**: Early development — transparent public research

---

## Purpose
This project explores transparency and accountability through open data sources (e.g., SEC EDGAR, CourtListener, OpenCorporates, and others).  
The goal is to build a public-facing OSINT framework that:

- Increases access to company, legal, and civic data for research and journalism  
- Provides reproducible tools for investigative analysis  
- Documents methods openly for verification and collaboration  
- Serves as a foundation for broader OSINT exploration beyond corporate data  

---

## Current Progress
- Repository established for open publication of scripts, notebooks, and methods  
- Working demo against **SEC EDGAR** (U.S. corporate filings, no token required)  
- Demo against **CourtListener** (court opinions, requires proper User-Agent)  
- Initial OpenCorporates integration (requires API token for full access)  

---

## Planned Next Steps
- Extend queries to regional datasets and sector-specific corpora  
- Add data cleaning, enrichment, and visualization pipelines  
- Expand scope to non-corporate datasets (e.g., NGOs, political contributions, sanctions lists)  
- Publish reproducible reports on findings for public review  

---

## Civic/NGO Alignment
This is a **non-commercial project** aligned with civic transparency, academic research, and investigative reporting.  
All outputs are published openly for public benefit.  

---

## Usage

Clone the repository:
```bash
git clone https://github.com/TraceFantome/aegis-osint.git
cd aegis-osint
Create and activate a virtual environment:
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
