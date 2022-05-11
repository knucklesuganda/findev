-- upgrade --
ALTER TABLE "usermodel" ADD "username" VARCHAR(100) NOT NULL;
-- downgrade --
ALTER TABLE "usermodel" DROP COLUMN "username";
