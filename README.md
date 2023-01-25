# Twitter Content Filter
Twitter Content Filter is a tool for flagging and filtering out bad content from Twitter using hashtags and a CSV file of keywords to compare against. The tool is written in Python and uses the tweepy and pandas libraries to access the Twitter API and read/write CSV files.

## Getting Started
To use this tool, you will need to set up a developer account on Twitter, create an app, and obtain the necessary API keys and tokens. You will also need to have Python and the tweepy and pandas libraries installed on your computer.

## Usage
1. First, we will need to import the necessary libraries for reading and manipulating the CSV file and for accessing and parsing tweets. These libraries include pandas, tweepy, and re.

2. Next, we will need to set up our API credentials for accessing tweets using tweepy. This includes creating a developer account on Twitter, creating an app, and obtaining the necessary API keys and tokens.

3. We will then use pandas to read in our CSV file and create a dataframe from it. We will then use the pandas `str.contains()` method to search for any hashtags in the tweets that match words in the CSV file.

4. If we find a match, we will not add it to the CSV file. If we do not find a match, we will use the pandas `append()` method to add the new hashtag to the CSV file.

5. We will then use the tweepy library to search for tweets containing the hashtag and use the re library to extract the hashtags from the tweets.

6. Finally, we will save the updated CSV file using the pandas `to_csv()` method.

## Use case 
1. Create a CSV file called hashtags.csv with the list of keywords that you want to filter out.
2. Run the script by typing `python twitter_content_filter.py` in your command line.
3. The script will search for tweets containing the hashtag you specified in the script and extract the hashtags from those tweets.
4. It will then compare the hashtags in those tweets to the keywords in the CSV file and filter out any tweets that match keywords on the list.
5. The filtered tweets will be saved to a new CSV file called `filtered_hashtags.csv`

## Note
This tool is intended to be used as a starting point for filtering out bad content on Twitter and may require additional modification to suit your specific use case.

## Use case
### Schools:
This  tool can be used on a network level to filter out bad content in schools to protect students. Here's how:

1. First, install the tool on a server within the school's network. This will allow the tool to filter out bad content on all devices connected to the network.
2. Create a list of keywords in a CSV file that are relevant to the school's policies and the type of content that should be blocked.
3. Configure the tool to run on a regular schedule (e.g. every hour) to check for new tweets containing the specified hashtag.
4. If the tool finds a tweet that contains a keyword from the CSV file, it will block access to the tweet on all devices connected to the network.
5. To prevent students from circumventing the filter, the school can also use a content filtering software on the network level.
6. Additionally, the school can use a VPN or a proxy service to block access to certain websites. This will provide an extra layer of security to ensure that students are not able to access bad content.

It's important to note that this tool can only filter out tweets containing the hashtag specified in the script, and it will not block access to websites or other social media platforms.

Additionally, using this tool is not a substitute for education and proactive measures to protect students. It's important to educate students on internet safety and to provide guidance on how to use the internet responsibly.

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
Thank you to the tweepy and pandas libraries for making it easy to access the Twitter API and manipulate CSV files in Python.

The above code is just an example and may require additional modification to suit your specific use case.

Feel free to modify and use the code as you wish, but please give credit where it's due.

If you have any questions or issues, please do not hesitate to contact me.
