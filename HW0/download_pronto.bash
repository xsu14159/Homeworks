mkdir pronto
cd pronto
echo "there is some data inside" > README.txt
curl -O https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
mkdir data
cd data
unzip open_data_year_one.zip
head *.csv

