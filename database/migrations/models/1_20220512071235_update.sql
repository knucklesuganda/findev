-- upgrade --
CREATE TABLE IF NOT EXISTS "usermodel" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "email" VARCHAR(255) NOT NULL UNIQUE,
    "hashed_password" VARCHAR(1024) NOT NULL,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "is_superuser" BOOL NOT NULL  DEFAULT False,
    "is_verified" BOOL NOT NULL  DEFAULT False,
    "username" VARCHAR(100) NOT NULL
);
CREATE INDEX IF NOT EXISTS "idx_usermodel_email_7287ba" ON "usermodel" ("email");
-- downgrade --
DROP TABLE IF EXISTS "usermodel";
