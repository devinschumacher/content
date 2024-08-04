# README

## Project - Devin's SEO articles

- [Course outline](https://dynalist.io/d/eRXMTh6-Aj9QLfgKedIa02Ji)

1. Duplicate the `posts/templates/template.md` file and rename it to the title of your article
2. Paste the content from the `seo-articles.csv` file into your `.md` file
3. Add a return carriage in the code fences & Run the script to fix the images

### How to fix the image links in these markdown files

1. cd to the directory where the file is
2. run: `find . -type f -name '*.md' -exec sed i '' -e ':a' -e 'N' -e '$!ba' -e 's/-\n/-/g' {} +`

