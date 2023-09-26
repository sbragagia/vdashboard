# Login details
USER="dylan"
DATABASE="formula1"
CSV_DIRECTORY="/home/dylan/Documents/Archives/Formula1/"

# List all CSV files in the specified directory
CSV_FILES=($(find "$CSV_DIRECTORY" -type f -name "*.csv"))

for file in "${CSV_FILES[@]}"; do
  # Extract the table name from the CSV filename
  table_name=$(basename "$file" .csv)

  # Import the CSV file into the corresponding table
  psql -U "$USER" -d "$DATABASE" -c "\copy $table_name FROM '$file' DELIMITER ',' CSV HEADER NULL AS '\N';"
done
