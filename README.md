# Labs Data Science API Template

## Tech Stack
- Logic: Python
- API Framework: FastAPI
- Database: PostgreSQL
- ML Model: Sklearn, RandomForestClassifier
- Visualizations: Plotly

## API Structure
- API Root `/` Swagger Docs
  - DB Interface `/data/` GET
    - Count Training Data Rows `/data/count/` GET
    - Insert Training Data `/data/insert/` POST
      - feature_1: int
      - feature_2: int
      - feature_3: int
      - target: string
    - Seed Training Data `/data/seed/` POST
      - num: int
  - ML Interface `/model/` GET
    - Train Method `/model/train/` GET
    - Predict Method `/model/predict/` POST
      - feature_1: int
      - feature_2: int
      - feature_3: int
  - Visualizations
    - Class by Feature `/vis/class-by-feature/` POST
      - feature_id: int
    - Class by Percentage `/vis/class-by-percent/` POST
