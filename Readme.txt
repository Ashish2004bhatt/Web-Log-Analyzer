web-log-analyzer/
│
├── data/
│   ├── raw_logs/               # Raw Apache/Nginx logs
│   ├── processed/              # Cleaned + normalized logs
│   ├── features/               # Feature engineered data
│   └── models/                 # Saved ML & DL models
│
├── config/
│   ├── settings.yaml           # Global config
│   ├── logging.conf            # Logging configuration
│   └── model_config.yaml       # ML/DL model configs
│
├── ingestion/
│   ├── batch_ingestion.py      # Batch log loading
│   ├── realtime_ingestion.py   # Tail-F style streaming
│   └── ingestion_utils.py      # Helper functions
│
├── parser/
│   ├── apache_parser.py        # Apache log regex parser
│   ├── nginx_parser.py         # Nginx parser
│   ├── auto_parser.py          # Auto-detect parser
│   └── parsing_utils.py
│
├── preprocessing/
│   ├── cleaner.py              # Missing values, noise removal
│   ├── geoip_enrichment.py     # GeoIP lookup
│   ├── user_agent_parser.py    # Browser, OS extraction
│   ├── sessionizer.py          # User session formation
│   └── preprocess_pipeline.py  # Full preprocessing pipeline
│
├── feature_engineering/
│   ├── feature_extractor.py    # Basic + advanced features
│   ├── url_tokenizer.py        # URL path tokenization
│   ├── time_series_features.py # Rolling statistics
│   ├── vectorizer.py           # TF-IDF/Word2Vec for URLs
│   └── feature_pipeline.py     # Unified feature pipeline
│
├── ml_models/
│   ├── train_ml.py             # Train RF, XGB, SVM
│   ├── ml_predictor.py         # ML prediction module
│   └── model_utils.py          # Saving/loading ML models
│
├── dl_models/
│   ├── lstm_model.py           # LSTM for sequences
│   ├── autoencoder.py          # Reconstruction anomaly detection
│   ├── cnn_url_model.py        # CNN for URL patterns
│   └── train_dl.py             # Unified DL training script
│
├── anomaly_detection/
│   ├── anomaly_rules.py        # Frequency, error-rate rules
│   ├── hybrid_detector.py      # ML + DL hybrid anomaly engine
│   └── alerting.py             # Email/SMS/Webhook alerts
│
├── api/
│   ├── main.py                 # FastAPI entrypoint
│   ├── predict_routes.py       # /predict endpoint
│   ├── preprocessing_wrapper.py# Wrap preprocessing + model
│   └── security.py             # API security (JWT, rate-limit)
│
├── dashboard/
│   ├── app.py                  # Streamlit dashboard
│   ├── pages/
│   │   ├── 1_real_time.py      # Real-time log feed
│   │   ├── 2_traffic_insights.py
│   │   ├── 3_error_analysis.py
│   │   ├── 4_anomaly_heatmap.py
│   │   └── 5_model_performance.py
│   └── assets/                 # CSS, images
│
├── utils/
│   ├── logger.py               # Unified logging system
│   ├── helpers.py              # Common helpers
│   ├── validators.py           # Input validation
│   └── file_utils.py
│
├── deployment/
│   ├── Dockerfile_api          # API Docker
│   ├── Dockerfile_dashboard    # Dashboard Docker
│   ├── docker-compose.yml      # Multi-container setup
│   ├── requirements.txt
│   └── gpu_setup.md
│
├── tests/
│   ├── test_ingestion.py
│   ├── test_parser.py
│   ├── test_preprocessing.py
│   ├── test_ml.py
│   └── test_dl.py
│
├── notebooks/
│   ├── EDA.ipynb               # Exploratory Data Analysis
│   ├── FeatureTesting.ipynb
│   └── ModelTraining.ipynb
│
├── scripts/
│   ├── run_pipeline.py         # Entire pipeline runner
│   ├── train_all_models.py
│   └── generate_reports.py
│
├── .env.example
├── README.md
└── requirements.txt
