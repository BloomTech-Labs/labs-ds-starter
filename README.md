# Labs Data Science API Template

## Tech Stack
- Logic: Python
- API Framework: FastAPI
- Database: PostgreSQL
- ML Model: Sklearn, RandomForestClassifier


## API Structure
- API Root `/` Swagger Docs
  - DB Interface `/data/`
    - Insert Data `/data/insert/`
    - Count Data `/data/count/`
    - Seed Data `/data/seed/`
  - ML Interface `/model/`
    - Train Method `/model/train/`
    - Predict Method `/model/predict/`
