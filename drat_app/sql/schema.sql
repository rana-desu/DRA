-- Database schema for disaster reporting system
BEGIN TRANSACTION;

-- Authentication data table
CREATE TABLE IF NOT EXISTS AuthData (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);

-- User-reported data table
CREATE TABLE IF NOT EXISTS UserData (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER REFERENCES AuthData(id),
    location TEXT NOT NULL,
    injury TEXT NOT NULL,
    food_hours INTEGER NOT NULL CHECK(food_hours >= 0),
    water_hours INTEGER NOT NULL CHECK(water_hours >= 0),
    age_group TEXT NOT NULL CHECK(age_group IN ('child', 'adult', 'senior')),
    pregnant BOOLEAN DEFAULT 0,
    gender TEXT,
    mobile TEXT,
    reported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- News/Disaster data table
CREATE TABLE IF NOT EXISTS NewsData (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    location TEXT NOT NULL,
    disaster_type TEXT NOT NULL,
    severity INTEGER CHECK(severity BETWEEN 1 AND 5),
    reported_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    source TEXT
);

-- Master normalized data table
CREATE TABLE IF NOT EXISTS Master (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_data_id INTEGER REFERENCES UserData(id),
    news_data_id INTEGER REFERENCES NewsData(id),
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    priority_score INTEGER,
    status TEXT DEFAULT 'pending'
);

-- Log table for raw aggregations
CREATE TABLE IF NOT EXISTS Log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    log_type TEXT NOT NULL,
    record_count INTEGER NOT NULL,
    aggregated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    summary_data TEXT
);

-- Priority tracking log
CREATE TABLE IF NOT EXISTS PriorityLog (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    master_id INTEGER REFERENCES Master(id),
    priority_score INTEGER NOT NULL,
    assigned_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    assigned_to TEXT,
    status TEXT DEFAULT 'unresolved'
);

-- Indexes for better performance
CREATE INDEX IF NOT EXISTS idx_user_location ON UserData(location);
CREATE INDEX IF NOT EXISTS idx_news_location ON NewsData(location);
CREATE INDEX IF NOT EXISTS idx_master_priority ON Master(priority_score);

COMMIT;