Job Hunter Script for parsing Job Descriptions on Websites. 

//Current Steps:
1. Created a SQL Database where I manually copy-pasted a job description from a website 
2. Created a script "job.py" to view the contents of this database (DB Name: jobdb, it's on sqlite3)

//Possible Next Steps:
1. Create a NoSql version of the database so I can better parse and analyse the content
2. Create a WordCloud Spitter that can spit the top keywords?
3. Create a table to tabulate the differences between a job posting and my resume - refer to the attached document "Job Posting Analysis.pdf" file for details on a strategy. 



//My failied attempt at Google Cloud Platform Cloud Talent Solutions:
1. Set up Google Cloud Platform using steps from here: https://cloud.google.com/talent-solution/job-search/docs/before-you-begin
2. Download Key file, add it to Git Ignore since this is a private key. 
3. Add Path to Google: export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/key-file.json"