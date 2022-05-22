# Mrcong-Scraper
Scrape posts url and get direct download link from mrcong.com

## Download program
To download the program you can simple run this command in your terminal 

```
git clone https://github.com/bayy420-999/Mrcong-Scraper.git
```

## Run the program 
After you finished the download, go to project directory by typing 
```
cd Mrcong-Scraper 
```
And then run `main.py` file with command below 
```
python3 main.py
```
At the first time you will prompted with 
```
Choose method to generate url (Type "1" to generate url, type "2" to use list of urls):
```
There are two ways to get list of url, first one is by generating list of url by calling `generate_urls()` function and the second one is by providing txt file which contain urls list.

If you type `1` you will be asked to input which `tag` you want to scrape and how many `page` you want to scrape 

You can get list of tags [here](https://mrcong.com/sets/)
```
Input tag that you want to scrape: xiuren 

How many page you want to scrape: 10
```
If you type `2` you will be asked to input txt file which contains list of url, you can separate each url with `space` or `new line`
```
Input txt file that contains list of urls: data.txt 
```
After you done with list of url, you can move to next step which is choosing correct regex pattern to get correct results, you will prompted with 
```
Which regex pattern to use? (Type "1" to find posts url, type "2" to find downloads url):
```
There are two patterns you can use
1. `'post\-box\-title\"\>\s+\<a\shref\=\"(.*?)\"'`
which is used to get all posts url inside class `post-box-title`
2. `'\<a\shref\=\"(.*?)\starget\=\"\_blank\"\sclass\=\"shortc\-button\smedium\s'`
which is used to get all download url inside class `shortc-button medium`



You can type `1` in terminal to use pattern 1, and type `2` to use pattern 2
