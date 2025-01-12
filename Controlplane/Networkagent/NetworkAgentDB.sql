CREATE TABLE "AdditionalData" (

  CONSTRAINT "OID"  REFERENCES "ObjectID" ("OID") ON DELETE CASCADE
);

CREATE TABLE "Authentication" (
  "AuthZoken" blob,
  "AuthTokenTimeStamp" DATE,
  PRIMARY KEY ("AuthZoken"),
  CONSTRAINT "OID"  REFERENCES "ObjectID" ("OID") ON DELETE CASCADE
);

CREATE TABLE "ControlplaneID" (
  "CPID" INTEGER NOT NULL ON CONFLICT ABORT,
  "ÍsLocal" integer NOT NULL ON CONFLICT ABORT DEFAULT no COLLATE BINARY,
  PRIMARY KEY ("CPID")
);

CREATE TABLE "Integrity" (
  "OSType" TEXT NOT NULL,
  "OSTypeTimeStamp" DATE NOT NULL,
  "OSBuild" TEXT NOT NULL,
  "OSBuildTimeStamp" DATE NOT NULL,
  "AVType" TEXT NOT NULL,
  "AVTypeTimeStamp" DATE NOT NULL,
  "AVBuild" TEXT NOT NULL,
  "AVBuildTimeStamp" DATE NOT NULL,
  "AVIsActive" integer NOT NULL,
  "AVIsActiveTimeStamp" DATE NOT NULL,
  "OSUpdatesPending" integer NOT NULL,
  "OSUpdatesPendingTimeStamp" DATE NOT NULL,
  "SystemIsManaged" integer NOT NULL,
  "SystemIsManagedTimeStamp" DATE NOT NULL,
  CONSTRAINT "OID"  REFERENCES "ObjectID" ("OID") ON DELETE CASCADE
);

CREATE TABLE "ObjectID" (
  "OID" INTEGER NOT NULL ON CONFLICT ABORT,
  "UpdateStamp" integer NOT NULL ON CONFLICT FAIL,
  PRIMARY KEY ("OID")
);

