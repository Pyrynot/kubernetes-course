#!/bin/bash

POSTGRES_POD_NAME=$(kubectl get pods --selector=app=your-postgres-app -o jsonpath='{.items[0].metadata.name}')
POSTGRES_USER="your_postgres_user"
DATABASE_NAME="your_database_name"
BACKUP_FILE="/backup/db_backup_$(date +%Y%m%d%H%M).sql"

if [ -z "$POSTGRES_POD_NAME" ]; then
  echo "Error: Could not find a PostgreSQL pod with the label 'app=your-postgres-app'."
  exit 1
fi

kubectl exec $POSTGRES_POD_NAME -- bash -c "pg_dump -U $POSTGRES_USER $DATABASE_NAME" > $BACKUP_FILE

if [ $? -ne 0 ]; then
  echo "Error: Failed to create database backup."
  exit 1
fi

gsutil cp $BACKUP_FILE gs://backup_bucket_kek/

if [ $? -ne 0 ]; then
  echo "Error: Failed to upload backup to Google Cloud Storage."
  exit 1
fi

rm $BACKUP_FILE

echo "Backup completed and uploaded successfully to GCS."
