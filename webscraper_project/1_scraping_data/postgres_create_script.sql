CREATE SCHEMA IF NOT EXISTS webscr authorization rick;
CREATE TABLE webscr.vacature
    (
    vacature_key INT PRIMARY KEY NOT NULL
,   titel VARCHAR(150) NOT NULL
,   bedrijf VARCHAR(50) NOT NULL
,   plaats VARCHAR(50)
,   land VARCHAR(50)
,   thuiswerken INT NOT NULL
,   min_jaarsalaris DECIMAL(7, 2)
,   max_jaarsalaris DECIMAL(7, 2)
,   gem_jaarsalaris DECIMAL(7, 2)
,   jaarsalaris_bruto INT
,   uren_per_week INT
,   vacature_beschrijving TEXT
,   vacature_rating decimal(1, 1)
,   load_date DATE DEFAULT CURRENT_DATE
    )
